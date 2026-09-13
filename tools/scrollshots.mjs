// Viewport screenshots while scrolling: node scrollshots.mjs <url> <outPrefix> <width> <height> [maxShots]
import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';
const [url, prefix, W = '390', H = '844', maxShots = '40'] = process.argv.slice(2);
const port = 9300 + Math.floor(Math.random() * 500);
const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', ['--headless=new', '--disable-gpu', '--no-sandbox', '--hide-scrollbars', `--remote-debugging-port=${port}`, `--user-data-dir=/tmp/chprof_${port}`, `--window-size=${W},${H}`, 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
let wsUrl; for (let i = 0; i < 50; i++) { try { const r = await fetch(`http://127.0.0.1:${port}/json/version`); wsUrl = (await r.json()).webSocketDebuggerUrl; break; } catch { await sleep(200); } }
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
await s('Page.navigate', { url }); await sleep(4500);
const ev = async (expr) => { const r = await s('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true }); return r.result?.result?.value; };
const total = await ev('document.documentElement.scrollHeight');
const step = Math.round(+H * 0.9); let n = 0;
for (let y = 0; y < total && n < +maxShots; y += step, n++) {
  await ev(`window.scrollTo(0,${y})`); await sleep(700);
  const { result: { data } } = await s('Page.captureScreenshot', { format: 'jpeg', quality: 70 });
  writeFileSync(`${prefix}_${String(n).padStart(2, '0')}.jpg`, Buffer.from(data, 'base64'));
}
console.log('total', total, 'shots', n);
ws.close(); chrome.kill();
