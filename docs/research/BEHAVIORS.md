# Behaviours — Gaststätte template → V1 implementation

Observed on https://gaststatte.framer.website/ (Framer, breakpoints 809 / 1199 px) and how each is reproduced in `assets/js/main.js` / `styles.css`.

| Template behaviour | Trigger | V1 implementation |
|---|---|---|
| Nav transparent over hero, solid white after | scroll past hero | `IntersectionObserver` on `.hero` (rootMargin = nav height) toggles `.nav.is-solid` |
| "Menu" button opens full-screen overlay with staggered links | click | `body.menu-open`, links translate/fade with per-child delay, Esc / Close / link click closes, scroll locked |
| Hero: image parallax, giant name clipped at the bottom edge | scroll | `[data-parallax]` translateY (−10 % of offset), `.giant-clip` (height .62em, overflow hidden) |
| Coloured block: statement revealed word by word | scroll progress | `.reveal-words` split into `<span class="w">`, count of `.on` words = progress between 88 % and 38 % of viewport |
| Experience: text rows with a sticky image that switches | scroll (desktop) | `.sticky` panel `position: sticky`, `IntersectionObserver` (rootMargin −38 % / −48 %) sets `.row.is-active` and the visible `<img>`; mobile shows one image per row |
| Full-bleed photo blocks with glass CTA | scroll | `.block` with parallax media, gradient overlay, `.btn--glass` (blur 12 px) |
| Photo revealed by two "shutters" with a word on each side | scroll progress | `.shutter` CSS var `--p` (0 → 1 between 85 % and 25 % of viewport) drives `translateX` of two panels + word opacity |
| Giant ticker | time | CSS `@keyframes marquee` on a duplicated track (32 s), paused for `prefers-reduced-motion` |
| Menu tabs with sliding highlight, content swap | click | `role=tablist`, `.tabs__glider` translateX, panels `hidden`, arrow-key navigation |
| Elements fade/slide into view, staggered groups | scroll | `.rv` + `.rv-group` (delay 0.09 s per child), `.rv-media` image scale-in; initial hidden state only when `html.js` |
| Gallery counter "03 / 15" (from nammos.com) | horizontal scroll | scroll-snap strip, counter updated on `scroll` |
| Newsletter / contact forms | submit | front-end only: thank-you state; contact form opens a pre-filled mailto |
| Reduced motion | media query | all transitions/animations disabled, shutters open, words visible |

Responsive: single column ≤ 999 px (gutter 20 px), two-column grids and sticky panels ≥ 1000 px (gutter 40 px). Hero and blocks use `100svh` / `92svh`; mobile art direction via `<picture>` (4:5 or 3:4 crops) vs desktop 16:9.
