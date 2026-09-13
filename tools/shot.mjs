// Full-page screenshot via CDP: node shot.mjs <url> <out.png> <width> <height> [scrollFirst=1]
import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';
const [url, out, W = '390', H = '844', scrollFirst = '1', extraJs = ''] = process.argv.slice(2);
const port = 9300 + Math.floor(Math.random() * 500);
const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
  '--headless=new', '--disable-gpu', '--no-sandbox', '--hide-scrollbars', `--remote-debugging-port=${port}`,
  `--user-data-dir=/tmp/chprof_${port}`, `--window-size=${W},${H}`, 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
let wsUrl;
for (let i = 0; i < 50; i++) { try { const r = await fetch(`http://127.0.0.1:${port}/json/version`); wsUrl = (await r.json()).webSocketDebuggerUrl; break; } catch { await sleep(200); } }
const ws = new WebSocket(wsUrl); await new Promise(r => ws.onopen = r);
let id = 0; const pending = new Map();
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); } };
const send = (method, params = {}, sessionId) => new Promise(r => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });
const { result: { targetId } } = await send('Target.createTarget', { url: 'about:blank' });
const { result: { sessionId } } = await send('Target.attachToTarget', { targetId, flatten: true });
const s = (m, p) => send(m, p, sessionId);
await s('Page.enable'); await s('Runtime.enable');
await s('Emulation.setDeviceMetricsOverride', { width: +W, height: +H, deviceScaleFactor: 1, mobile: +W < 800 });
if (+W < 800) await s('Emulation.setUserAgentOverride', { userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' });
await s('Page.navigate', { url }); await sleep(4000);
if (scrollFirst === '1') {
  await s('Runtime.evaluate', { expression: `(async()=>{const h=document.documentElement.scrollHeight;for(let y=0;y<h;y+=300){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60));}window.scrollTo(0,0);})()`, awaitPromise: true });
  await sleep(1500);
}
if (extraJs) { await s('Runtime.evaluate', { expression: extraJs, awaitPromise: true }); await sleep(800); }
const { result: { result: { value: dims } } } = await s('Runtime.evaluate', { expression: 'JSON.stringify({h:document.documentElement.scrollHeight,w:document.documentElement.scrollWidth})', returnByValue: true });
const { h } = JSON.parse(dims);
await s('Emulation.setDeviceMetricsOverride', { width: +W, height: Math.min(h, 20000), deviceScaleFactor: 1, mobile: +W < 800 });
await sleep(800);
const { result: { data } } = await s('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true });
writeFileSync(out, Buffer.from(data, 'base64'));
console.log('saved', out, 'height', h);
ws.close(); chrome.kill();
