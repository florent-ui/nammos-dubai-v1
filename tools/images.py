"""Image pipeline: crop Nammos source photos to the slots used by the site and export WebP at mobile-first widths.
Usage: python tools/images.py <source_dir>
"""
import os, sys
from PIL import Image, ImageOps
SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img')
os.makedirs(OUT, exist_ok=True)
M45 = ('m', (4, 5), [780, 1170]); D169 = ('d', (16, 9), [1440, 1920]); M916 = ('m', (3, 4), [780, 1170])
SLOTS = {
    'hero':            ('nammos-dubai-slider-1.jpg',                 [M45, D169], (0.5, 0.55)),
    'row-taste':       ('01_taste_nammos_dubai_0.jpg',               [('', (6, 7), [600, 900, 1200])], (0.5, 0.5)),
    'row-sun':         ('nammos-dubai-2.jpg',                        [('', (6, 7), [600, 900, 1200])], (0.5, 0.5)),
    'row-sunset':      ('nammos-sun-sets-dubai.jpg',                 [('', (6, 7), [600, 720])], (0.5, 0.5)),
    'block1':          ('nammos-dubai-3.jpg',                        [M916, D169], (0.5, 0.5)),
    'menu-teaser':     ('nammos-dubai-menu-slider.jpg',              [('', (3, 2), [780, 1200, 1600])], (0.5, 0.5)),
    'celeb-teaser':    ('nammos-dubai-private-events_01_0_1.jpg',    [('', (4, 5), [780, 1200])], (0.5, 0.5)),
    'shutter':         ('nammos_dubai-private-events-001_fresh_fish.jpg', [M45, D169], (0.5, 0.5)),
    'menu-side':       ('nammos_dubai_small_01.jpg',                 [('', (4, 5), [600, 900])], (0.5, 0.5)),
    'beach-main':      ('nammos_dubai_beach_life_02.jpg',            [('', (3, 2), [780, 1200, 1600])], (0.5, 0.5)),
    'block2':          ('03_sunsets_nammos_dubai.jpg',               [M916, D169], (0.5, 0.45)),
    'celebrate-main':  ('nammos_dubai-events.jpg',                   [('', (4, 5), [780, 1200])], (0.5, 0.4)),
    'contact-bg':      ('nammos_dubai-contact_slider_01.jpg',        [M916, D169], (0.5, 0.5)),
    'footer':          ('nammos_dubai_gallery_14.jpg',               [('', (1, 1), [600, 900])], (0.5, 0.5)),
    'news-gp':         ('nammos-gp-abu-dhabi-website.jpg',           [('', (3, 2), [780, 1200])], (0.5, 0.5)),
    'news-icon':       ('nammos-dubai-nammos-world-news-1.jpg',      [('', (3, 2), [780, 1200])], (0.5, 0.5)),
    'menus-hero':      ('nammos-dubai-menu-slider.jpg',              [M45, D169], (0.5, 0.5)),
    'menus-dish':      ('nammos_dubai_small_01.jpg',                 [('', (3, 2), [780, 1200])], (0.5, 0.5)),
    'menus-2':         ('nammos_dubai_gallery_08.jpg',               [('', (3, 2), [780, 1200])], (0.5, 0.5)),
    'menus-3':         ('nammos_dubai_gallery_10.jpg',               [('', (4, 5), [780, 1200])], (0.5, 0.5)),
    'celeb-hero':      ('nammos_dubai_slider_events-private-01.jpg', [M45, D169], (0.5, 0.45)),
    'celeb-weddings':  ('nammos-dubai-private-events_01_0_1.jpg',    [('', (4, 5), [780, 1200])], (0.5, 0.5)),
    'celeb-parties':   ('nammos_dubai-events.jpg',                   [('', (4, 5), [780, 1200])], (0.5, 0.4)),
    'celeb-corporate': ('nammos-dubai-private-events-1.jpg',         [('', (4, 5), [780, 1200])], (0.5, 0.35)),
    'celeb-table':     ('nammos-dubai-events-23.jpg',                [('', (3, 2), [780, 1200])], (0.5, 0.5)),
    'contact-hero':    ('nammos_dubai-contact_slider_01.jpg',        [M45, D169], (0.5, 0.5)),
    'contact-team':    ('contact-nammos-002.jpg',                    [('', (4, 5), [560])], (0.6, 0.5)),
    'og':              ('nammos-dubai-slider-1.jpg',                 [('', (1200, 630), [1200])], (0.5, 0.55)),
}
for i in range(1, 16):
    name = {7: 'nammos_dubai_gallery_07_0.jpg', 9: 'nammos_dubai_gallery_09_1.jpg', 12: 'nammos_dubai_gallery_12_1.jpg'}.get(i, f'nammos_dubai_gallery_{i:02d}.jpg')
    SLOTS[f'gallery-{i:02d}'] = (name, [('', (4, 5), [600, 900])], (0.5, 0.5))

def crop_to(im, ratio, focus):
    w, h = im.size; rw, rh = ratio
    target = rw / rh
    if w / h > target:  # too wide → crop width
        nw = int(round(h * target)); x0 = int(round((w - nw) * focus[0])); box = (x0, 0, x0 + nw, h)
    else:
        nh = int(round(w / target)); y0 = int(round((h - nh) * focus[1])); box = (0, y0, w, y0 + nh)
    return im.crop(box)

manifest = []
for slot, (src, variants, focus) in SLOTS.items():
    im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, src)).convert('RGB'))
    for suffix, ratio, widths in variants:
        c = crop_to(im, ratio, focus)
        done = set()
        for w in widths:
            w = min(w, c.size[0])  # never upscale: fall back to the crop's native width
            if w in done:
                continue
            done.add(w)
            out = c.resize((w, int(round(w * c.size[1] / c.size[0]))), Image.LANCZOS)
            name = f"{slot}{'-' + suffix if suffix else ''}-{w}.webp"
            out.save(os.path.join(OUT, name), 'WEBP', quality=78, method=6)
            manifest.append((name, out.size, os.path.getsize(os.path.join(OUT, name)) // 1024, src))
total = sum(m[2] for m in manifest)
print(f"{len(manifest)} files, {total/1024:.1f} MB")
with open(os.path.join(os.path.dirname(__file__), '..', 'docs', 'research', 'IMAGE_MANIFEST.md'), 'w') as f:
    f.write('# Image manifest\n\n| file | size px | KB | source (nammos.com) |\n|---|---|---|---|\n')
    for n, s, k, src in manifest: f.write(f'| {n} | {s[0]}x{s[1]} | {k} | {src} |\n')
