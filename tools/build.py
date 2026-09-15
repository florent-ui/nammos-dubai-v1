# -*- coding: utf-8 -*-
"""Build the Nammos Dubai V1 static site + the Framer kit from tools/content.py.
Usage: python tools/build.py
Outputs: index.html, menus.html, private-celebrations.html, contact.html, docs/framer-kit.md, dist-artifact/*
"""
import html as _html, os, re, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
from content import SITE, NAV, ANCHORS, HOME, MENUS_PAGE, CELEB_PAGE, CONTACT_PAGE, NOTES  # noqa: E402

IMG = ROOT / 'assets' / 'img'
SITE_URL = 'https://florent-ui.github.io/nammos-dubai-v1/'  # URL publique GitHub Pages (aperçus de lien)
e = lambda s: _html.escape(str(s), quote=False)
ea = lambda s: _html.escape(str(s), quote=True)

# ---------------------------------------------------------------- assets
def svg_inline(name, cls='', label=None):
    s = (IMG / name).read_text()
    s = re.sub(r'\s(width|height)="[^"]*"', '', s, count=2)
    s = re.sub(r'fill="(#000|#000000|black)"', 'fill="currentColor"', s)
    s = re.sub(r'stroke="(#000|#000000|black)"', 'stroke="currentColor"', s)
    attrs = f' class="{cls}"' if cls else ''
    attrs += f' role="img" aria-label="{ea(label)}"' if label else ' aria-hidden="true" focusable="false"'
    return s.replace('<svg', f'<svg{attrs}', 1).strip()

LOGO = svg_inline('nammos_world_logo_black.svg', label='Nammos')
ARROW = svg_inline('arrow_button.svg', cls='arrow')

_dims = {}
def dims(name):
    if name not in _dims:
        with Image.open(IMG / name) as im: _dims[name] = im.size
    return _dims[name]

def variants(slot):
    out = {}
    for f in IMG.glob(f'{slot}-*.webp'):
        m = re.match(rf'{re.escape(slot)}-(?:(m|d)-)?(\d+)\.webp$', f.name)
        if m: out.setdefault(m.group(1) or '', []).append((int(m.group(2)), f.name))
    if not out: raise SystemExit(f'no image for slot {slot}')
    return {k: sorted(v) for k, v in out.items()}

def pic(slot, alt, sizes='100vw', eager=False):
    v = variants(slot)
    attrs = ' fetchpriority="high" decoding="async"' if eager else ' loading="lazy" decoding="async"'
    srcset = lambda lst: ', '.join(f'assets/img/{n} {w}w' for w, n in lst)
    if 'm' in v and 'd' in v:
        _, mn = v['m'][0]; W, H = dims(mn)
        return (f'<picture><source media="(min-width: 800px)" srcset="{srcset(v["d"])}" sizes="100vw">'
                f'<img src="assets/img/{mn}" srcset="{srcset(v["m"])}" sizes="100vw" width="{W}" height="{H}" alt="{ea(alt)}"{attrs}></picture>')
    lst = v.get('') or v.get('m') or v.get('d'); _, n0 = lst[0]; W, H = dims(n0)
    return f'<img src="assets/img/{n0}" srcset="{srcset(lst)}" sizes="{sizes}" width="{W}" height="{H}" alt="{ea(alt)}"{attrs}>'

def media(slot, alt, cls='', sizes='100vw', eager=False):
    return f'<div class="media rv-media {cls}">{pic(slot, alt, sizes, eager)}</div>'

# ---------------------------------------------------------------- shared parts
RES = SITE['reservations_url']
def btn(label, href, cls='btn', external=None, icon=True):
    ext = external if external is not None else href.startswith('http')
    target = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="{cls}" href="{ea(href)}"{target}>{e(label)}{ARROW if icon else ""}</a>'

def nav(page):
    links = ANCHORS if page == 'home' else [(l, h) for l, h in NAV if l != 'Home']
    desk = ''.join(f'<a href="{ea(h)}"{" target=_blank rel=noopener" if h.startswith("http") else ""}>{e(l)}</a>' for l, h in links)
    over = ''.join(f'<a href="{ea(h)}"{" target=_blank rel=noopener" if h.startswith("http") else ""}>{e(l)}</a>' for l, h in NAV)
    socials = ''.join(f'<a href="{ea(u)}" target="_blank" rel="noopener">{e(n)}</a>' for n, u in SITE['socials'])
    return f'''
<header class="nav" id="top">
  <a class="nav__logo" href="index.html" aria-label="Nammos — home">{LOGO}</a>
  <p class="nav__center label">Nammos Dubai</p>
  <div class="nav__right">
    <nav class="nav__links label" aria-label="Sections">{desk}</nav>
    <a class="btn btn--small nav__res" href="{ea(RES)}" target="_blank" rel="noopener">Reservations</a>
    <button class="btn btn--small" type="button" data-menu-open aria-expanded="false" aria-controls="menu">Menu</button>
  </div>
</header>
<div class="overlay" id="menu">
  <div class="overlay__bar"><a href="index.html" aria-label="Nammos — home">{LOGO}</a><button class="btn btn--small btn--light" type="button" data-menu-close>Close</button></div>
  <nav class="overlay__links" aria-label="Main menu">{over}</nav>
  <div class="overlay__foot">
    <a class="btn btn--light" href="{ea(RES)}" target="_blank" rel="noopener">Reservations{ARROW}</a>
    <div class="overlay__socials label">{socials}</div>
    <p class="overlay__meta label">{e(SITE["address"][0])} · {e(SITE["address"][1])}</p>
  </div>
</div>'''

def footer():
    f = HOME['footer']
    navl = ''.join(f'<a href="{ea(h)}"{" target=_blank rel=noopener" if h.startswith("http") else ""}>{e(l)}</a>' for l, h in NAV)
    soc = ''.join(f'<a href="{ea(u)}" target="_blank" rel="noopener">{e(n)}</a>' for n, u in SITE['socials'])
    world = ''.join(f'<a href="{ea(u)}"{" target=_blank rel=noopener" if u.startswith("http") else ""}>{e(n)}</a>' for n, u in SITE['world'])
    legal = ' · '.join(f'<a href="{ea(u)}" target="_blank" rel="noopener">{e(n)}</a>' for n, u in SITE['legal'])
    return f'''
<footer class="footer" id="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand rv-group">
        <a href="index.html" aria-label="Nammos">{LOGO}</a>
        {media(f["image"], f["alt"], "footer__media", "150px")}
        <p class="lead rv">{e(f["text"])}</p>
        {btn(f["cta"], RES, "btn btn--solid rv")}
      </div>
      <div class="footer__col rv">
        <p class="label">Navigation</p>
        <nav class="footer__nav" aria-label="Footer">{navl}</nav>
        <div class="footer__socials">{soc}</div>
      </div>
      <div class="footer__col rv">
        <p class="label">{e(f["newsletter"])}</p>
        <form class="form" data-fake data-thanks="{ea(f["thanks"])}">
          <div class="field"><label for="nl-email">Email</label><input id="nl-email" name="email" type="email" required autocomplete="email" placeholder="name@email.com"></div>
          <div class="field"><label for="nl-name">Name</label><input id="nl-name" name="name" type="text" autocomplete="name" placeholder="Jane Smith"></div>
          <button class="btn btn--solid" type="submit">{e(f["subscribe"])}</button>
        </form>
      </div>
    </div>
    <div class="footer__world label"><span class="label--muted">Nammos World</span>{world}</div>
  </div>
  <div class="giant-clip footer__giant"><div class="giant container">Nammos</div></div>
  <div class="footer__bottom">
    <span>{e(SITE["copyright"])}</span>
    <span>{legal}</span>
    <span>{e(SITE["address"][0])}, {e(SITE["address"][1])}</span>
  </div>
</footer>'''

def hero_page(h):
    return f'''
<section class="hero hero--page">
  <div class="hero__media" data-parallax>{pic(h["image"], h["alt"], eager=True)}</div>
  <div class="hero__top rv-group">
    <p class="label rv">{e(h["label"])}</p>
    <h1 class="hero__title rv">{e(h["title"])}</h1>
    <p class="hero__text text rv">{e(h["text"])}</p>
  </div>
  <div class="hero__bottom"></div>
</section>'''

def contact_details(dark=False):
    hours = ''.join(f'<li>{e(k)} <span>{e(v)}</span></li>' for k, v in SITE['hours'])
    return f'''
      <div><p class="label">Opening Hours</p><ul>{hours}</ul></div>
      <div><p class="label">Phone</p><p><a href="tel:{SITE["phone_raw"]}">{e(SITE["phone"])}</a></p></div>
      <div><p class="label">Address</p><p><a href="{ea(SITE["map_url"])}" target="_blank" rel="noopener">{e(SITE["address"][0])}<br>{e(SITE["address"][1])}</a></p></div>
      <div><p class="label">Email</p><p><a href="mailto:{SITE["email_reservations"]}">{e(SITE["email_reservations"])}</a><br><a href="mailto:{SITE["email_events"]}">{e(SITE["email_events"])}</a></p></div>'''

# ---------------------------------------------------------------- pages
def page_home():
    H = HOME; h = H['hero']; a = H['about']; x = H['experience']; b1 = H['block1']; mt = H['menu_teaser']; ct = H['celeb_teaser']
    sh = H['shutter']; m = H['menu']; be = H['beach']; b2 = H['block2']; ce = H['celebrate']; nw = H['news']; co = H['contact']
    rows = ''.join(f'''
        <article class="row" data-index="{i}">
          {media(r["image"], r["alt"], "row__media", "(min-width: 1000px) 42vw, 100vw")}
          <p class="label label--muted">{e(r["label"])}</p>
          <div class="row__body"><h3 class="row__title">{e(r["title"])}</h3><p class="text">{e(r["text"])}</p></div>
        </article>''' for i, r in enumerate(x['rows']))
    sticky = ''.join(pic(r['image'], r['alt'], '42vw') for r in x['rows'])
    pairs = lambda ps: ''.join(f'<div class="pair rv"><p class="label">{e(k)}</p><p class="text">{e(v)}</p></div>' for k, v in ps)
    tabs = ''.join(f'<button class="tab" role="tab" type="button" id="tab-{i}" aria-controls="panel-{i}" aria-selected="{"true" if i == 0 else "false"}">{e(t)}</button>' for i, (t, _) in enumerate(m['tabs']))
    panels = ''.join(f'<div class="panel" role="tabpanel" id="panel-{i}" aria-labelledby="tab-{i}"{"" if i == 0 else " hidden"}>' + ''.join(
        f'<div class="dish"><h3 class="dish__name">{e(n)}</h3><p class="dish__price">{e(p)}</p>' + (f'<p class="dish__desc">{e(d)}</p>' if d else '') + '</div>' for n, d, p in dishes) + '</div>'
        for i, (_, dishes) in enumerate(m['tabs']))
    gallery = ''.join(f'<div class="media gallery__item">{pic(f"gallery-{i:02d}", f"{be["gallery_alt"]} {i}", "(min-width: 1000px) 320px, 74vw")}</div>' for i in range(1, 16))
    items = ''.join(f'<article class="item rv"><p class="label">{e(k)}</p><h3 class="item__title">{e(t)}</h3><p class="text">{e(d)}</p></article>' for k, t, d in ce['items'])
    cards = ''.join(f'''
        <article class="card rv">
          {media(img, alt, "card__media", "(min-width: 800px) 50vw, 100vw")}
          <p class="label">{e(date)}</p>
          <h3 class="card__title">{e(title)}</h3>
          <p class="text">{e(teaser)}</p>
          <a class="link" href="{ea(url)}" target="_blank" rel="noopener">More{ARROW}</a>
        </article>''' for date, title, teaser, url, img, alt in nw['items'])
    body = f'''
{nav('home')}
<main>
<section class="hero">
  <div class="hero__media" data-parallax>{pic(h["image"], h["alt"], eager=True)}</div>
  <div class="hero__top rv-group">
    <p class="label rv">{e(h["label"])}</p>
    <h1 class="statement rv">{e(h["statement"])}</h1>
    {btn(h["cta"], RES, "btn btn--glass rv")}
  </div>
  <div class="hero__bottom">
    <p class="hero__text text rv">{e(h["text"])}</p>
    <div class="giant-clip hero__giant" aria-hidden="true"><div class="giant">{e(h["giant"])}</div></div>
  </div>
</section>

<section class="about" id="about">
  <div class="about__mark">{LOGO}</div>
  <div class="about__inner">
    <p class="label rv">{e(a["label"])}</p>
    <p class="statement reveal-words">{e(a["text"])}</p>
    <p class="label label--muted about__line rv">{e(a["line"])}</p>
  </div>
</section>

<section class="experience" id="experience">
  <div class="container">
    <div class="experience__head rv-group">
      <p class="label label--muted rv">{e(x["label"])}</p>
      <h2 class="title rv">{e(x["title"])}</h2>
    </div>
    <div class="experience__grid">
      <div class="rows">{rows}</div>
      <div class="media sticky" aria-hidden="true">{sticky}</div>
    </div>
  </div>
</section>

<section class="block">
  <div class="block__media" data-parallax>{pic(b1["image"], b1["alt"])}</div>
  <div class="block__body rv-group">
    <h2 class="statement rv">{e(b1["statement"])}</h2>
    <p class="text rv">{e(b1["text"])}</p>
    {btn(b1["cta"], RES, "btn btn--glass rv")}
  </div>
</section>

<section class="teaser" id="menus">
  <div class="container teaser__grid">
    {media(mt["image"], mt["alt"], "teaser__media", "(min-width: 1000px) 50vw, 100vw")}
    <div class="teaser__body rv-group">
      <p class="label label--muted rv">{e(mt["label"])}</p>
      <h2 class="statement rv">{e(mt["statement"])}</h2>
      {pairs(mt["pairs"])}
      {btn(mt["cta"][0], mt["cta"][1], "btn btn--solid rv")}
    </div>
  </div>
</section>

<section class="teaser teaser--flip">
  <div class="container teaser__grid">
    <div class="teaser__body rv-group">
      <p class="label label--muted rv">{e(ct["label"])}</p>
      <h2 class="statement rv">{e(ct["statement"])}</h2>
      {pairs(ct["pairs"])}
      {btn(ct["cta"][0], ct["cta"][1], "btn btn--solid rv")}
    </div>
    {media(ct["image"], ct["alt"], "teaser__media teaser__media--tall", "(min-width: 1000px) 50vw, 100vw")}
  </div>
</section>

<section class="shutter" aria-label="{ea(sh["left"])} {ea(sh["right"])}">
  <div class="shutter__media">{pic(sh["image"], sh["alt"])}</div>
  <div class="shutter__panel shutter__panel--l"></div>
  <div class="shutter__panel shutter__panel--r"></div>
  <p class="shutter__word shutter__word--l">{e(sh["left"])}</p>
  <p class="shutter__word shutter__word--r">{e(sh["right"])}</p>
</section>

<div class="ticker" aria-hidden="true"><div class="ticker__track">{''.join(f'<div class="ticker__item">{e(H["ticker"])}<span class="ticker__dot"></span></div>' for _ in range(4))}</div></div>

<section class="menu" id="menu">
  <div class="container">
    <div class="menu__head rv-group">
      <div><p class="label label--muted rv">{e(m["label"])}</p><h2 class="statement rv" style="margin-top:14px">{e(m["statement"])}</h2></div>
      <p class="text rv">{e(m["text"])}</p>
    </div>
    <div class="menu__grid">
      <div class="media menu__side">{pic(m["image"], m["alt"], "36vw")}</div>
      <div class="rv">
        <div class="tabs" role="tablist" aria-label="Menu"><div class="tabs__glider"></div>{tabs}</div>
        {panels}
        <p class="menu__note">{e(m["note"])}</p>
        <div class="menu__cta">{btn("See the full menus", "menus.html", "btn btn--solid")}</div>
      </div>
    </div>
  </div>
</section>

<section class="beach" id="beach">
  <div class="container beach__grid">
    {media(be["image"], be["alt"], "beach__media", "(min-width: 1000px) 50vw, 100vw")}
    <div class="beach__body rv-group">
      <p class="label label--muted rv">{e(be["label"])}</p>
      <h2 class="statement rv">{e(be["statement"])}</h2>
      <p class="text rv">{e(be["text"])}</p>
    </div>
  </div>
  <div class="gallery" data-counter="#gallery-counter" aria-label="Gallery">{gallery}</div>
  <div class="gallery__foot"><p class="label label--muted">Nammos Dubai</p><p class="gallery__counter" id="gallery-counter" aria-live="polite">01 / 15</p></div>
</section>

<section class="block">
  <div class="block__media" data-parallax>{pic(b2["image"], b2["alt"])}</div>
  <div class="block__body rv-group">
    <h2 class="statement rv">{e(b2["statement"])}</h2>
    <p class="text rv">{e(b2["text"])}</p>
    {btn(b2["cta"][0], b2["cta"][1], "btn btn--glass rv")}
  </div>
</section>

<section class="celebrate" id="celebrations">
  <div class="container">
    <div class="celebrate__head">
      {media(ce["image"], ce["alt"], "celebrate__media", "(min-width: 1000px) 38vw, 100vw")}
      <div class="celebrate__body rv-group">
        <p class="label label--muted rv">{e(ce["label"])}</p>
        <h2 class="title rv">{e(ce["title"])}</h2>
      </div>
    </div>
    <div class="items">{items}</div>
    <div class="quote rv">
      <p class="quote__mark" aria-hidden="true">“</p>
      <p>{e(ce["quote"])}</p>
      <div class="quote__contact">
        <p class="label label--muted">{e(ce["contact_line"])}</p>
        <a href="mailto:{SITE["email_events"]}">{e(SITE["email_events"])}</a>
        <a href="tel:{SITE["phone_raw"]}">{e(SITE["phone"])}</a>
      </div>
    </div>
  </div>
</section>

<section class="news">
  <div class="container">
    <div class="news__head rv"><p class="label label--muted">{e(nw["label"])}</p><a class="link" href="{ea(nw["more"][1])}" target="_blank" rel="noopener">{e(nw["more"][0])}{ARROW}</a></div>
    <div class="cards">{cards}</div>
  </div>
</section>

<section class="contact" id="contact">
  <div class="contact__media" data-parallax>{pic(co["image"], co["alt"])}</div>
  <div class="contact__card rv-group">
    <p class="label rv">{e(co["label"])}</p>
    <h2 class="statement rv">{e(co["statement"])}</h2>
    <div class="contact__grid rv">{contact_details()}</div>
    <div class="contact__actions rv">
      {btn(co["cta"], RES, "btn btn--light")}
      {btn("Find us", SITE["map_url"], "btn btn--light")}
    </div>
  </div>
</section>
</main>
{footer()}'''
    return render(H['meta_title'], H['meta_desc'], body, og=True)

def page_menus():
    P = MENUS_PAGE; it = P['intro']
    slug = lambda s: re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    chips = ''.join(f'<a class="chip label" href="#{slug(c)}">{e(c)}</a>' for c, _, _ in P['categories'])
    cats = ''.join(f'''
    <section class="menu-cat" id="{slug(c)}">
      <div class="menu-cat__head rv"><h2 class="menu-cat__title">{e(c)}</h2>{f'<p class="menu-cat__sub">{e(sub)}</p>' if sub else ''}</div>
      {''.join(f'<div class="dish"><h3 class="dish__name">{e(n)}</h3><p class="dish__price">{e(p)}</p>' + (f'<p class="dish__desc">{e(d)}</p>' if d else '') + '</div>' for n, d, p in dishes)}
    </section>''' for c, sub, dishes in P['categories'])
    gal = ''.join(media(s, a, '', '(min-width: 1000px) 50vw, 100vw') for s, a in P['gallery'])
    body = f'''
{nav('menus')}
<main>
{hero_page(P['hero'])}
<section class="teaser">
  <div class="container teaser__grid">
    {media(it["image"], it["alt"], "teaser__media", "(min-width: 1000px) 50vw, 100vw")}
    <div class="teaser__body rv-group">
      <p class="label label--muted rv">{e(it["label"])}</p>
      <h2 class="statement rv">{e(it["title"])}</h2>
      <p class="text rv">{e(it["text"])}</p>
      <p class="lead rv">{e(it["line"])}</p>
      {btn("Reservations", RES, "btn btn--solid rv")}
    </div>
  </div>
</section>
<nav class="chips" aria-label="Menu categories">{chips}</nav>
<div class="container">
  {cats}
  <p class="menu__note" style="margin-top:40px">{e(P["note"])}</p>
  <p class="menu__note">{e(P["reference"])}</p>
  <div class="menu-page__gallery">{gal}</div>
  <div class="section-head"><h2 class="statement rv">Be in the heart of summer</h2><div class="rv">{btn("Reservations", RES, "btn btn--solid")}</div></div>
</div>
</main>
{footer()}'''
    return render(P['meta_title'], P['meta_desc'], body)

def page_celebrations():
    P = CELEB_PAGE
    feats = ''.join(f'''
<section class="feature{" feature--flip" if i % 2 else ""}">
  <div class="container feature__grid">
    {media(img, alt, "feature__media", "(min-width: 1000px) 50vw, 100vw")}
    <div class="feature__body rv-group">
      <p class="label label--muted rv">{e(k)}</p>
      <h2 class="feature__title rv">{e(t)}</h2>
      <p class="text rv">{e(d)}</p>
      {btn("Enquire", "mailto:" + SITE["email_events"], "btn btn--solid rv", external=False)}
    </div>
  </div>
</section>''' for i, (k, t, d, img, alt) in enumerate(P['features']))
    body = f'''
{nav('celebrations')}
<main>
{hero_page(P['hero'])}
<div class="container section-head rv"><h2 class="title">{e(P["statement"])}</h2></div>
{feats}
<section class="celebrate">
  <div class="container">
    <div class="celebrate__head">
      {media(P["image"], P["alt"], "celebrate__media", "(min-width: 1000px) 38vw, 100vw")}
      <div class="quote rv" style="margin-top:0">
        <p class="quote__mark" aria-hidden="true">“</p>
        <p>{e(P["quote"])}</p>
        <div class="quote__contact">
          <p class="label label--muted">{e(P["contact_line"])}</p>
          <a href="mailto:{SITE["email_events"]}">{e(SITE["email_events"])}</a>
          <a href="tel:{SITE["phone_raw"]}">{e(SITE["phone"])}</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
{footer()}'''
    return render(P['meta_title'], P['meta_desc'], body)

def page_contact():
    P = CONTACT_PAGE; f = P['form']
    fields = ''.join(f'<div class="field"><label for="f-{n}">{e(l)}</label><input id="f-{n}" name="{n}" type="{t}"{" required" if "*" in l else ""}></div>' for n, l, t in f['fields'])
    body = f'''
{nav('contact')}
<main>
{hero_page(P['hero'])}
<div class="container">
  <section class="details rv-group">
    <div class="details__block rv"><p class="label">Nammos Dubai</p><p>{e(SITE["address"][0])}<br>{e(SITE["address"][1])}</p></div>
    <div class="details__block rv"><p class="label">Phone</p><p><a href="tel:{SITE["phone_raw"]}">{e(SITE["phone"])}</a></p></div>
    <div class="details__block rv"><p class="label">Email</p><p><a href="mailto:{SITE["email_reservations"]}">{e(SITE["email_reservations"])}</a><br><a href="mailto:{SITE["email_events"]}">{e(SITE["email_events"])}</a></p></div>
    <div class="details__block rv"><p class="label">Opening Hours</p><ul>{''.join(f'<li>{e(k)}: {e(v)}</li>' for k, v in SITE["hours"])}</ul></div>
    <div class="details__actions rv">{btn(P["book"], RES, "btn btn--solid")}{btn(P["find_us"], SITE["map_url"], "btn")}</div>
  </section>
  <section class="contact-page__grid">
    <div class="rv-group">
      <p class="label label--muted rv">{e(f["label"])}</p>
      <h2 class="statement rv" style="margin:14px 0 16px">{e(f["title"])}</h2>
      <p class="text rv" style="margin-bottom:24px">{e(f["text"])}</p>
      <form class="form rv" data-mailto="{SITE["email_reservations"]}">
        {fields}
        <div class="field"><label for="f-message">{e(f["message"])}</label><textarea id="f-message" name="message"></textarea></div>
        <label class="check"><input type="checkbox" name="consent" required> {e(f["consent"])}</label>
        <button class="btn btn--solid" type="submit">{e(f["submit"])}{ARROW}</button>
      </form>
    </div>
    {media(P["image"], P["alt"], "contact-page__media", "(min-width: 1000px) 420px, 100vw")}
  </section>
</div>
</main>
{footer()}'''
    return render(P['meta_title'], P['meta_desc'], body)

# ---------------------------------------------------------------- render
def render(title, desc, body, og=False):
    head = f'''<title>{e(title)}</title>
<meta name="description" content="{ea(desc)}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{SITE_URL}__PAGE__">
<meta property="og:type" content="website"><meta property="og:site_name" content="Nammos Dubai"><meta property="og:url" content="{SITE_URL}__PAGE__">
<meta property="og:title" content="{ea(title)}"><meta property="og:description" content="{ea(desc)}">
<meta property="og:image" content="{SITE_URL}assets/img/og-1200.jpg"><meta property="og:image:secure_url" content="{SITE_URL}assets/img/og-1200.jpg"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Nammos Dubai, Four Seasons Resort Jumeirah">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{ea(title)}"><meta name="twitter:description" content="{ea(desc)}"><meta name="twitter:image" content="{SITE_URL}assets/img/og-1200.jpg">
<link rel="icon" href="assets/img/favicon-32x32.png" sizes="32x32">
<link rel="preload" href="assets/fonts/SaolDisplay-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/SangBleuOGSans-Medium.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/styles.css">'''
    full = f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="theme-color" content="#000000">\n{head}\n</head>\n<body>{body}\n<script src="assets/js/main.js" defer></script>\n</body>\n</html>\n'
    artifact = f'{head}\n<style>body{{margin:0;font-size:14px}}</style>{body}\n<script src="assets/js/main.js" defer></script>\n'
    return full, artifact

# ---------------------------------------------------------------- framer kit
def kit():
    H = HOME
    L = []
    L.append('# Nammos Dubai — Framer kit (template Gaststätte)\n')
    L.append('Tout le contenu ci-dessous est prêt à coller dans la template remixée. Les textes sont ceux de nammos.com/dubai. Les images sont déjà recadrées dans `assets/img/` (WebP). Les polices sont dans `assets/fonts/`.\n')
    L.append('## 1. Réglages globaux dans Framer\n')
    L.append('**Polices (Site settings → Fonts → Custom)** : uploader `SaolDisplay-Regular.woff2`, `SaolDisplay-LightItalic.woff2`, `SangBleuOGSans-Medium.woff2`, `HelveticaNeueLTPro-Roman.woff2`. Licence à confirmer avec Nammos (polices commerciales, fichiers récupérés depuis leur site).\n')
    L.append('**Styles de texte de la template → styles Nammos**\n')
    L.append('| Style Framer (template) | Desktop / Tablet / Phone | Remplacer par |\n|---|---|---|')
    L.append('| Heading 1 (Aboreto) | 360 / 250 / 150 px, lh .8, ls -5% | Saol Display Regular, majuscules, 354 / 250 / 96 px, lh .8, ls -2% |')
    L.append('| Heading 2 (Aboreto) | 44 / 36 / 28 px, lh 1.2 | Saol Display Regular, 44 / 36 / 30 px, lh 1.08 |')
    L.append('| Heading 3 (Zalando Sans) | 36 / 30 / 24 px | SangBleu OG Sans Medium, 20 / 20 / 20 px |')
    L.append('| Heading 4 (Zalando Sans) | 20 / 18 / 16 px | SangBleu OG Sans Medium, 11 px, majuscules, ls 14% |')
    L.append('| Paragraph (Zalando Sans) | 14 px, lh 1.4 | Helvetica Neue LT Pro Roman, 14 / 15 px, lh 1.6 |')
    L.append('| Small labels (Zalando 12 px) | 12 px | SangBleu OG Sans Medium 11 px, majuscules, ls 14%, couleur #6f6c68 |')
    L.append('| Buttons (Zalando 16 px) | 16 px | SangBleu OG Sans Medium 11 px, majuscules, ls 16% |')
    L.append('| Dish names (Heading 2) | 44 / 36 / 28 px | Saol Display 32 / 28 / 24 px |\n')
    L.append('**Couleurs (Assets → Color styles)**\n')
    L.append('| Token template | Valeur | Nammos |\n|---|---|---|')
    L.append('| Text (#0e0005) | noir chaud | `#000000` |')
    L.append('| Cream (#ebeadf) | crème | `#f4f4f2` |')
    L.append('| Sage (#7d9482) — blocs colorés | vert | `#f4f4f2` pour le bloc “About”, `#000000` (84 %) pour la carte Contact |')
    L.append('| Muted (#908482) | gris | `#6f6c68` |')
    L.append('| Tabs bg (#f1e8e6) | rose pâle | `#ededed` |')
    L.append('| Accent (hover) | — | `#08c6d2` (aqua Nammos, utilisé sur nammos.com) |\n')
    L.append('**Boutons** : rayon 0 (angles droits), bordure 1 px, texte majuscules 11 px espacé. Variante “glass” sur photo : fond blanc 12 %, bordure blanche 70 %, flou 12 px.\n')
    L.append('**Liens** : Réservations → ' + SITE['reservations_url'] + ' · Carte → ' + SITE['map_url'] + '\n')
    L.append('## 2. Page d’accueil — section par section\n')
    def best(slot):
        v = variants(slot); parts = []
        for k, lab in (('m', 'mobile'), ('d', 'desktop'), ('', '')):
            if k in v:
                _, n = v[k][-1]; parts.append(f'`assets/img/{n}`' + (f' ({lab})' if lab else ''))
        return ', '.join(parts)
    def sec(name, layer, fields, images):
        L.append(f'### {name}\n')
        L.append(f'*Calque Framer : `{layer}`*\n')
        for k, v in fields:
            L.append(f'- **{k}** : {v}')
        for slot, note in images:
            L.append(f'- **Image** : {best(slot)} — {note}')
        L.append('')
    h = H['hero']
    sec('Navigation', 'Desktop - Transparent / Phone - Close', [('Logo', 'nammos_world_logo_black.svg'), ('Texte centre', 'Nammos Dubai'), ('Liens desktop', ' / '.join(l for l, _ in ANCHORS)), ('Bouton', 'Menu'), ('Overlay', ' / '.join(l for l, _ in NAV) + ' + Reservations + réseaux')], [])
    sec('Hero', 'Section - Hero', [('Label', h['label']), ('Titre (Heading 2)', h['statement']), ('Bouton glass', h['cta'] + ' → SevenRooms'), ('Paragraphe', h['text']), ('Mot géant (Heading 1)', 'NAMMOS')], [('hero', 'mobile 4:5 ou 3:4 / desktop 16:9')])
    a = H['about']
    sec('About (bloc crème, texte révélé au scroll)', 'Section - About', [('Label', a['label']), ('Texte (Heading 2, centré)', a['text']), ('Ligne basse', a['line']), ('Filigrane', 'logo Nammos à 6 % d’opacité')], [])
    x = H['experience']
    sec('Experience (3 lignes, image sticky)', 'Section -  experience', [('Label', x['label']), ('Titre', x['title'])] + [(f'Ligne {i+1}', f'{r["label"]} — **{r["title"]}** — {r["text"]}') for i, r in enumerate(x['rows'])], [(r['image'], f'ligne {i+1}, 6:7') for i, r in enumerate(x['rows'])])
    b = H['block1']
    sec('Bloc photo plein écran 1', 'Section - Block', [('Titre', b['statement']), ('Texte', b['text']), ('Bouton glass', b['cta'])], [('block1', 'mobile 4:5 ou 3:4 / desktop 16:9')])
    mt = H['menu_teaser']
    sec('Menu teaser', 'Section - Menu - quote', [('Label', mt['label']), ('Titre', mt['statement'])] + [(k, v) for k, v in mt['pairs']] + [('Bouton', f'{mt["cta"][0]} → page Menus')], [('menu-teaser', '3:2')])
    ct = H['celeb_teaser']
    sec('Private Celebrations teaser', 'Section - Philosophy - quote', [('Label', ct['label']), ('Titre', ct['statement'])] + [(k, v) for k, v in ct['pairs']] + [('Bouton', f'{ct["cta"][0]} → page Private Celebrations')], [('celeb-teaser', '4:5')])
    sh = H['shutter']
    sec('Photo “volets” (scroll)', 'Section - Our menu › left shutter / right shutter', [('Mot gauche', sh['left']), ('Mot droite', sh['right'])], [('shutter', 'mobile 4:5 ou 3:4 / desktop 16:9')])
    sec('Ticker', 'Section - Our menu › Ticker wrapper', [('Texte défilant (Heading 1)', H['ticker'] + ' (texte réel du bandeau nammos.com/dubai)'), ('Séparateur', 'point aqua #08c6d2')], [])
    m = H['menu']
    sec('Menu à onglets', 'Section - Our menu › tabs - container / menu - tabs', [('Label', m['label']), ('Titre', m['statement']), ('Texte', m['text']), ('Note', m['note'])] + [(f'Onglet “{t}”', ' · '.join(f'{n} ({d}) — {p}' if d else f'{n} — {p}' for n, d, p in dishes)) for t, dishes in m['tabs']], [('menu-side', 'image sticky 4:5 (desktop)')])
    be = H['beach']
    sec('Beach Life + galerie', 'Nature Retreat', [('Label', be['label']), ('Titre', be['statement']), ('Texte', be['text']), ('Galerie', '15 photos gallery-01…15 (4:5), défilement horizontal avec compteur 01 / 15 comme sur nammos.com')], [('beach-main', '3:2')])
    b2 = H['block2']
    sec('Bloc photo plein écran 2', 'Section - Block (2)', [('Titre', b2['statement']), ('Texte', b2['text']), ('Bouton glass', b2['cta'][0])], [('block2', 'mobile 4:5 ou 3:4 / desktop 16:9')])
    ce = H['celebrate']
    sec('Celebrate the Nammos Way (grille 4 items + citation)', 'Our philosophy', [('Label', ce['label']), ('Titre', ce['title'])] + [(f'Item {i+1}', f'{k} — **{t}** — {d}') for i, (k, t, d) in enumerate(ce['items'])] + [('Citation', ce['quote']), ('Contact', f'{ce["contact_line"]} {SITE["email_events"]} / {SITE["phone"]}')], [('celebrate-main', '4:5')])
    nw = H['news']
    sec('Latest News (2 cartes)', 'ajout — dupliquer un bloc “Philosophy - quote”', [(f'Carte {i+1}', f'{d} — **{t}** — {tz} → {u}') for i, (d, t, tz, u, _, _) in enumerate(nw['items'])], [(img, '3:2') for _, _, _, _, img, _ in nw['items']])
    co = H['contact']
    sec('Contact & Reservations (carte sur photo)', 'Contact & Location', [('Label', co['label']), ('Titre', co['statement']), ('Horaires', ' · '.join(f'{k} {v}' for k, v in SITE['hours'])), ('Téléphone', SITE['phone']), ('Adresse', ', '.join(SITE['address'])), ('E-mails', f'{SITE["email_reservations"]} / {SITE["email_events"]}'), ('Boutons', f'{co["cta"]} → SevenRooms · Find us → Google Maps')], [('contact-bg', 'mobile 4:5 ou 3:4 / desktop 16:9')])
    f = H['footer']
    sec('Footer', 'Footer', [('Texte', f['text']), ('Bouton', f['cta']), ('Navigation', ' / '.join(l for l, _ in NAV)), ('Réseaux', ' / '.join(n for n, _ in SITE['socials'])), ('Newsletter', 'Email + Name + Subscribe'), ('Nammos World', ' / '.join(n for n, _ in SITE['world'])), ('Mot géant', 'NAMMOS'), ('Bas de page', f'{SITE["copyright"]} · Terms Of Service · Privacy policy')], [('footer', '1:1')])
    L.append('## 3. Pages secondaires\n')
    L.append('- **Menus** (`menus.html`) : hero + intro “Signature Flavours” + carte complète par catégorie (' + ', '.join(c for c, _, _ in MENUS_PAGE['categories']) + '). Source : carte Nammos Dubai 2022 — à remplacer par les menus actuels fournis par Nammos.')
    L.append('- **Private Celebrations** (`private-celebrations.html`) : hero + 3 blocs Weddings / Parties & Private Events / Corporate Events + citation + contact events@nammos.ae.')
    L.append('- **Contact** (`contact.html`) : hero + coordonnées + horaires + formulaire (Name, Surname, Phone, Email, Subject, Message, consentement).\n')
    L.append('## 4. Notes / à valider avec Nammos\n')
    for n in NOTES: L.append(f'- {n}')
    L.append('')
    return '\n'.join(L)

# ---------------------------------------------------------------- main
if __name__ == '__main__':
    pages = {'index.html': page_home(), 'menus.html': page_menus(), 'private-celebrations.html': page_celebrations(), 'contact.html': page_contact()}
    dist = ROOT / 'dist-artifact'; dist.mkdir(exist_ok=True)
    for name, (full, art) in pages.items():
        page = '' if name == 'index.html' else name
        full = full.replace('__PAGE__', page); art = art.replace('__PAGE__', page)
        (ROOT / name).write_text(full, encoding='utf-8')
        (dist / name).write_text(art if name == 'index.html' else full, encoding='utf-8')
    (ROOT / 'docs' / 'framer-kit.md').write_text(kit(), encoding='utf-8')
    print('built', ', '.join(pages), '+ docs/framer-kit.md')
