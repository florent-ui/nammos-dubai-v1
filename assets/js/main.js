/* Nammos Dubai V1 — interactions (no dependencies) */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add('js');

  /* Nav: transparent over the hero, solid afterwards */
  const nav = $('.nav');
  const hero = $('.hero');
  if (nav && hero && 'IntersectionObserver' in window) {
    new IntersectionObserver(([e]) => nav.classList.toggle('is-solid', !e.isIntersecting), {
      rootMargin: `-${nav.offsetHeight}px 0px 0px 0px`, threshold: 0,
    }).observe(hero);
  } else if (nav) nav.classList.add('is-solid');

  /* Menu overlay */
  const setMenu = (open) => {
    document.body.classList.toggle('menu-open', open);
    document.documentElement.style.overflow = open ? 'hidden' : '';
    $$('[data-menu-open]').forEach(b => b.setAttribute('aria-expanded', String(open)));
    if (open) $('.overlay__links a')?.focus({ preventScroll: true });
  };
  $$('[data-menu-open]').forEach(b => b.addEventListener('click', () => setMenu(true)));
  $$('[data-menu-close]').forEach(b => b.addEventListener('click', () => setMenu(false)));
  $$('.overlay a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });

  /* Reveal on scroll */
  $$('.rv-group').forEach(g => $$('.rv', g).forEach((el, i) => el.style.setProperty('--d', `${Math.min(i, 6) * 0.09}s`)));
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    }), { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    $$('.rv, .rv-media').forEach(el => io.observe(el));
  } else $$('.rv, .rv-media').forEach(el => el.classList.add('is-in'));

  /* Word-by-word statement */
  $$('.reveal-words').forEach(el => {
    el.innerHTML = el.textContent.trim().split(/\s+/).map(w => `<span class="w">${w}</span>`).join(' ');
  });

  /* Experience: sticky image switches with the active row (desktop) */
  const rows = $$('.row[data-index]');
  const stickyImgs = $$('.sticky img');
  if (rows.length && stickyImgs.length) {
    const setActive = i => {
      stickyImgs.forEach((im, j) => im.classList.toggle('on', j === i));
      rows.forEach((r, j) => r.classList.toggle('is-active', j === i));
    };
    setActive(0);
    const ro = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) setActive(+e.target.dataset.index); }),
      { rootMargin: '-38% 0px -48% 0px', threshold: 0 });
    rows.forEach(r => ro.observe(r));
  }

  /* Menu tabs */
  $$('.tabs').forEach(tabs => {
    const btns = $$('.tab', tabs);
    const glider = $('.tabs__glider', tabs);
    const panels = btns.map(b => document.getElementById(b.getAttribute('aria-controls')));
    const select = i => {
      btns.forEach((b, j) => { b.setAttribute('aria-selected', String(j === i)); b.tabIndex = j === i ? 0 : -1; });
      panels.forEach((p, j) => { if (p) p.hidden = j !== i; });
      if (glider) glider.style.transform = `translateX(${i * 100}%)`;
    };
    btns.forEach((b, i) => {
      b.addEventListener('click', () => select(i));
      b.addEventListener('keydown', e => {
        if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
          const n = (i + (e.key === 'ArrowRight' ? 1 : -1) + btns.length) % btns.length; select(n); btns[n].focus();
        }
      });
    });
    select(0);
  });

  /* Gallery counter */
  $$('.gallery').forEach(g => {
    const items = $$('.gallery__item', g);
    const out = g.dataset.counter ? $(g.dataset.counter) : null;
    if (!items.length || !out) return;
    const update = () => {
      const step = items[0].offsetWidth + parseFloat(getComputedStyle(g).columnGap || 12);
      const i = Math.min(items.length - 1, Math.round(g.scrollLeft / step));
      out.textContent = `${String(i + 1).padStart(2, '0')} / ${String(items.length).padStart(2, '0')}`;
    };
    g.addEventListener('scroll', update, { passive: true });
    update();
  });

  /* Menu page: active chip follows the category in view */
  const cats = $$('.menu-cat[id]');
  const chips = $$('.chip');
  if (cats.length && chips.length) {
    const co = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) chips.forEach(c => c.classList.toggle('on', c.getAttribute('href') === `#${e.target.id}`));
    }), { rootMargin: '-30% 0px -60% 0px', threshold: 0 });
    cats.forEach(c => co.observe(c));
  }

  /* Front-end only forms */
  $$('form[data-fake]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    f.innerHTML = `<p class="lead">${f.dataset.thanks || 'Thank you.'}</p>`;
  }));
  $$('form[data-mailto]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    const d = new FormData(f);
    const body = Array.from(d.entries()).filter(([k]) => k !== 'consent').map(([k, v]) => `${k}: ${v}`).join('\n');
    location.href = `mailto:${f.dataset.mailto}?subject=${encodeURIComponent(d.get('subject') || 'Contact from nammos.com/dubai')}&body=${encodeURIComponent(body)}`;
  }));

  /* Scroll-driven: parallax, word reveal, shutters */
  const px = $$('[data-parallax]');
  const words = $$('.reveal-words');
  const shutters = $$('.shutter');
  let ticking = false;
  const frame = () => {
    ticking = false;
    const vh = innerHeight;
    if (!reduce) px.forEach(el => {
      const r = el.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      const c = r.top + r.height / 2 - vh / 2;
      el.style.transform = `translate3d(0, ${(c * -0.1).toFixed(1)}px, 0)`;
    });
    words.forEach(el => {
      const r = el.getBoundingClientRect();
      const start = vh * 0.88, end = vh * 0.38;
      const p = Math.min(1, Math.max(0, (start - r.top) / (start - end + r.height * 0.6)));
      const ws = el.children; const n = Math.round(p * ws.length);
      for (let i = 0; i < ws.length; i++) ws[i].classList.toggle('on', i < n);
    });
    if (!reduce) shutters.forEach(s => {
      const r = s.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, (vh * 0.85 - r.top) / (vh * 0.6)));
      s.style.setProperty('--p', p.toFixed(3));
    });
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);
  frame();
})();
