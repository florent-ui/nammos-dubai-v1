# Nammos Dubai — site V1 (maquette HTML + kit Framer)

Reconstruction de la template Framer **Gaststätte** (https://gaststatte.framer.website/) avec le contenu, les photos et la charte de **Nammos Dubai** (https://www.nammos.com/dubai). Mobile d'abord.

## Pages

| Fichier | Contenu |
|---|---|
| `index.html` | Home one-page : hero, About, Experience (Taste / Beach / Sunsets), blocs photo, teasers Menus & Private Celebrations, volets + ticker, menu à onglets, Beach Life + galerie 15 photos, Celebrate the Nammos Way, Latest News, Contact & Reservations, footer |
| `menus.html` | Carte complète par catégorie (source : carte Nammos Dubai 2022 — à remplacer par les menus actuels) |
| `private-celebrations.html` | Weddings / Parties & Private Events / Corporate Events |
| `contact.html` | Coordonnées, horaires, formulaire |

## Structure

- `assets/css/styles.css` — design tokens Nammos (Saol Display, SangBleu OG Sans, Helvetica Neue LT Pro ; noir / blanc / crème `#f4f4f2` / aqua `#08c6d2`) et composants.
- `assets/js/main.js` — nav transparente → solide, overlay menu, reveal au scroll, texte révélé mot à mot, image sticky (desktop), volets, onglets, compteur galerie, formulaires front-only.
- `assets/img/` — photos nammos.com recadrées en WebP (mobile 4:5 / 3:4, desktop 16:9, vignettes 6:7, galerie 4:5). Voir `docs/research/IMAGE_MANIFEST.md`.
- `assets/fonts/` — fichiers récupérés depuis nammos.com (licence à confirmer avec Nammos).
- `tools/content.py` — **tout le contenu** (textes verbatim, plats, coordonnées). Modifier ici puis rebuild.
- `tools/build.py` — génère les 4 pages, `docs/framer-kit.md` et `dist-artifact/`.
- `tools/images.py` — pipeline de recadrage / export WebP depuis les photos sources.
- `docs/framer-kit.md` — **kit prêt à coller dans Framer** : réglages polices/couleurs, mapping des styles, contenu section par section, images à uploader.
- `docs/research/` — topologie de la template, manifeste images, screenshots de référence, carte 2022.
- `docs/screens/` — screenshots QA mobile / desktop de la V1.

## Rebuild

```bash
python3 -m venv .venv && .venv/bin/pip install pillow
.venv/bin/python tools/images.py <dossier des photos sources>   # optionnel, si nouvelles photos
.venv/bin/python tools/build.py
python3 -m http.server 8765   # puis http://127.0.0.1:8765/
```
