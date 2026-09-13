# Nammos Dubai — Framer kit (template Gaststätte)

Tout le contenu ci-dessous est prêt à coller dans la template remixée. Les textes sont ceux de nammos.com/dubai. Les images sont déjà recadrées dans `assets/img/` (WebP). Les polices sont dans `assets/fonts/`.

## 1. Réglages globaux dans Framer

**Polices (Site settings → Fonts → Custom)** : uploader `SaolDisplay-Regular.woff2`, `SaolDisplay-LightItalic.woff2`, `SangBleuOGSans-Medium.woff2`, `HelveticaNeueLTPro-Roman.woff2`. Licence à confirmer avec Nammos (polices commerciales, fichiers récupérés depuis leur site).

**Styles de texte de la template → styles Nammos**

| Style Framer (template) | Desktop / Tablet / Phone | Remplacer par |
|---|---|---|
| Heading 1 (Aboreto) | 360 / 250 / 150 px, lh .8, ls -5% | Saol Display Regular, majuscules, 354 / 250 / 96 px, lh .8, ls -2% |
| Heading 2 (Aboreto) | 44 / 36 / 28 px, lh 1.2 | Saol Display Regular, 44 / 36 / 30 px, lh 1.08 |
| Heading 3 (Zalando Sans) | 36 / 30 / 24 px | SangBleu OG Sans Medium, 20 / 20 / 20 px |
| Heading 4 (Zalando Sans) | 20 / 18 / 16 px | SangBleu OG Sans Medium, 11 px, majuscules, ls 14% |
| Paragraph (Zalando Sans) | 14 px, lh 1.4 | Helvetica Neue LT Pro Roman, 14 / 15 px, lh 1.6 |
| Small labels (Zalando 12 px) | 12 px | SangBleu OG Sans Medium 11 px, majuscules, ls 14%, couleur #6f6c68 |
| Buttons (Zalando 16 px) | 16 px | SangBleu OG Sans Medium 11 px, majuscules, ls 16% |
| Dish names (Heading 2) | 44 / 36 / 28 px | Saol Display 32 / 28 / 24 px |

**Couleurs (Assets → Color styles)**

| Token template | Valeur | Nammos |
|---|---|---|
| Text (#0e0005) | noir chaud | `#000000` |
| Cream (#ebeadf) | crème | `#f4f4f2` |
| Sage (#7d9482) — blocs colorés | vert | `#f4f4f2` pour le bloc “About”, `#000000` (84 %) pour la carte Contact |
| Muted (#908482) | gris | `#6f6c68` |
| Tabs bg (#f1e8e6) | rose pâle | `#ededed` |
| Accent (hover) | — | `#08c6d2` (aqua Nammos, utilisé sur nammos.com) |

**Boutons** : rayon 0 (angles droits), bordure 1 px, texte majuscules 11 px espacé. Variante “glass” sur photo : fond blanc 12 %, bordure blanche 70 %, flou 12 px.

**Liens** : Réservations → https://www.sevenrooms.com/explore/nammosdubai/reservations/create/search · Carte → https://maps.app.goo.gl/TfYv9uBtnpA5pKYE9

## 2. Page d’accueil — section par section

### Navigation

*Calque Framer : `Desktop - Transparent / Phone - Close`*

- **Logo** : nammos_world_logo_black.svg
- **Texte centre** : Nammos Dubai
- **Liens desktop** : Experience / Menu / Beach / Celebrations / Contact
- **Bouton** : Menu
- **Overlay** : Home / Menus / Private Celebrations / Events / News / Contact + Reservations + réseaux

### Hero

*Calque Framer : `Section - Hero`*

- **Label** : Four Seasons Resort, Jumeirah
- **Titre (Heading 2)** : When Mediterranean elegance met Dubai’s magic, NAMMOS Dubai was born.
- **Bouton glass** : Reservations → SevenRooms
- **Paragraphe** : The golden dunes that felt so familiar emitted a fresh allure under the Arabian sun.
- **Mot géant (Heading 1)** : NAMMOS
- **Image** : `assets/img/hero-m-864.webp` (mobile), `assets/img/hero-d-1620.webp` (desktop) — mobile 4:5 ou 3:4 / desktop 16:9

### About (bloc crème, texte révélé au scroll)

*Calque Framer : `Section - About`*

- **Label** : Sun, Sea, Celebration
- **Texte (Heading 2, centré)** : Nammos Dubai brings the spirit of the Mediterranean to the shores of the Arabian Gulf, nestled in the iconic Four Seasons Resort, Jumeirah. Rooted in Mykonian authenticity yet infused with Dubai’s cosmopolitan energy, it’s a destination for sunlit lunches, golden sunsets, and vibrant evenings defined by endless joy.
- **Ligne basse** : Be in the heart of summer
- **Filigrane** : logo Nammos à 6 % d’opacité

### Experience (3 lignes, image sticky)

*Calque Framer : `Section -  experience`*

- **Label** : The Nammos Dubai experience
- **Titre** : A Creative Twist to Beloved Classics
- **Ligne 1** : Taste — **Taste of the Mediterranean** — At the heart of the experience is Nammos’ signature cuisine: a sun-soaked symphony of Mediterranean flavours with an international twist. The menu blends refined Greek classics with contemporary global influences, where creativity and simplicity come together to define a dining experience that is both timeless and modern.
- **Ligne 2** : Beach Life — **Under the Arabian Sun** — By day, Nammos Dubai is bathed in light, a sun-drenched escape where Mediterranean leisure comes alive. From leisurely lunches with chilled rosé to the sound of lively music and laughter, every detail evokes the charm of sunlit Mykonian afternoons, where time slows, and every moment feels endless.
- **Ligne 3** : Sunsets — **When the Sun Sets** — After dark, Nammos Dubai comes alive in a new light. The sea shimmers under the stars, music fills the air, and the energy turns magnetic. It’s where elevated dining blends with celebration, creating nights that feel spontaneous, stylish, and unforgettable.
- **Image** : `assets/img/row-taste-1200.webp` — ligne 1, 6:7
- **Image** : `assets/img/row-sun-926.webp` — ligne 2, 6:7
- **Image** : `assets/img/row-sunset-720.webp` — ligne 3, 6:7

### Bloc photo plein écran 1

*Calque Framer : `Section - Block`*

- **Titre** : Out of the Arabian Sea Blue
- **Texte** : Rooted in Mykonian authenticity yet infused with Dubai’s cosmopolitan energy.
- **Bouton glass** : Reservations
- **Image** : `assets/img/block1-m-810.webp` (mobile), `assets/img/block1-d-1620.webp` (desktop) — mobile 4:5 ou 3:4 / desktop 16:9

### Menu teaser

*Calque Framer : `Section - Menu - quote`*

- **Label** : Menus
- **Titre** : Authentic Inspiration, Iconic Bites
- **Signature Flavours** : From pristine seafood and elevated classics to globally inspired creations, the Nammos Dubai menu is a reflection of authenticity, quality, and unmistakable style. Every plate tells a story of the sea, the sun, and the joy of gathering around exceptional food.
- **Crafted to be shared** : Freshly sourced ingredients, meticulous craftsmanship, and a passion for unforgettable moments.
- **Bouton** : See our menus → page Menus
- **Image** : `assets/img/menu-teaser-1600.webp` — 3:2

### Private Celebrations teaser

*Calque Framer : `Section - Philosophy - quote`*

- **Label** : Private Celebrations
- **Titre** : Celebrate the Nammos Way
- **Where private events become moments of effortless luxury & endless joy** : Make every occasion unforgettable at Nammos Dubai. From intimate gatherings to grand celebrations, Nammos offers a setting where every occasion feels effortless and extraordinary. Whether a sunset dinner by the sea or milestone celebration each detail is curated with signature elegance and exceptional service.
- **Bouton** : Plan your celebration → page Private Celebrations
- **Image** : `assets/img/celeb-teaser-1200.webp` — 4:5

### Photo “volets” (scroll)

*Calque Framer : `Section - Our menu › left shutter / right shutter`*

- **Mot gauche** : Sun, Sea
- **Mot droite** : Celebration
- **Image** : `assets/img/shutter-m-960.webp` (mobile), `assets/img/shutter-d-1800.webp` (desktop) — mobile 4:5 ou 3:4 / desktop 16:9

### Ticker

*Calque Framer : `Section - Our menu › Ticker wrapper`*

- **Texte défilant (Heading 1)** : Be in the heart of summer (texte réel du bandeau nammos.com/dubai)
- **Séparateur** : point aqua #08c6d2

### Menu à onglets

*Calque Framer : `Section - Our menu › tabs - container / menu - tabs`*

- **Label** : The menu
- **Titre** : An invitation to savour the essence of the Mediterranean, where time-honoured recipes meet contemporary culinary artistry.
- **Texte** : Each dish is crafted with the finest ingredients, designed to be shared, celebrated, and remembered.
- **Note** : A selection from the Nammos Dubai restaurant menu. All prices are in AED and inclusive of 7% municipality fee and 5% VAT. (A) Dishes containing alcohol.
- **Onglet “Starters”** : Aubergine Mille-Feuille (feta cream cheese) — 95 · Greek Salad (tomato, cucumber, onion, green pepper, olives & feta cheese) — 120 · Tuna Tartare (baked aubergine, smoked eel & bottarga sauce) — 185 · Mediterranean Spread Platter (hummus, white taramosalata with bottarga, tzatziki & tirokafteri) — 130 · Grilled Octopus (pepper relish) — 135 · Santorini Fava “Saganaki” (prawns & Greek spicy sauce) — 120 · Fried Calamari (smoky Florina pepper mayonnaise) — 160
- **Onglet “Mains”** : Nammos Risotto (lobster & carabineros (A)) — 420 · Black Squid Ink Tonnarello (carabineros & bottarga) — 395 · Pappardelle Seafood (white sauce) — 310 · Pici Veal Cheeks (24h slow cooked veal cheeks) — 180 · Baby Chicken (yogurt, lemon balm vinaigrette & roasted potatoes) — 190 · Fresh Fish from display (our daily fish market offers a large range of freshly caught Mediterranean fish and seafood) — 775 / kg · Fresh Lobster (from the daily fish market) — 1300 / kg
- **Onglet “Desserts”** : Almond Pie (blueberries & kaymak ice cream) — 55 · All-time Classic Nammos Chocolate Mousse (dark, milk & white chocolate) — 60 · Baklava (kaymak ice cream) — 65 · Cheesecake (figs & honeycomb) — 75 · Profiteroles (caramel cream, pistachio ice cream, warm chocolate sauce) — 60 · Caprese Cake (GF) (dark chocolate (75%)) — 55
- **Image** : `assets/img/menu-side-900.webp` — image sticky 4:5 (desktop)

### Beach Life + galerie

*Calque Framer : `Nature Retreat`*

- **Label** : Beach Life
- **Titre** : Bask in the essence of Mediterranean leisure at Nammos Beach, where golden sands and crystal waters set the scene for pure relaxation.
- **Texte** : Designed for comfort and style, plush sea loungers and private cabanas offer a serene escape beneath the Arabian sun. With discreet service, refined cocktails, and a laid-back yet sophisticated atmosphere, it’s the ultimate expression of barefoot luxury by the sea.
- **Galerie** : 15 photos gallery-01…15 (4:5), défilement horizontal avec compteur 01 / 15 comme sur nammos.com
- **Image** : `assets/img/beach-main-1600.webp` — 3:2

### Bloc photo plein écran 2

*Calque Framer : `Section - Block (2)`*

- **Titre** : Where private events become moments of effortless luxury & endless joy
- **Texte** : From intimate gatherings to grand celebrations, Nammos offers a setting where every occasion feels effortless and extraordinary.
- **Bouton glass** : Plan your celebration
- **Image** : `assets/img/block2-m-1170.webp` (mobile), `assets/img/block2-d-1500.webp` (desktop) — mobile 4:5 ou 3:4 / desktop 16:9

### Celebrate the Nammos Way (grille 4 items + citation)

*Calque Framer : `Our philosophy`*

- **Label** : Your Special Moments, The Nammos Way
- **Titre** : Celebrate the Nammos Way
- **Item 1** : Celebrating Love — **Weddings** — Celebrate your love story with the timeless charm of Nammos Dubai. From intimate beachfront ceremonies to vibrant evening receptions, we create weddings that blend Mediterranean elegance with signature Nammos energy.
- **Item 2** : There’s Always a Reason to Celebrate — **Parties & Private Events** — Birthdays, milestones, and new beginnings deserve to be celebrated with style and joy. At Nammos Dubai, we create the perfect setting to share these moments with the people who matter most.
- **Item 3** : Celebrate Your Business Milestones — **Corporate Events** — Nammos Dubai offers an exceptional setting for your corporate events, ensuring a seamless and memorable experience from start to finish.
- **Item 4** : Events — 4-6.12.2026 — **Nammos Takes the Fast Lane at the Abu Dhabi Grand Prix** — Nammos meets the thrill of Formula 1 at Yas Marina Circuit. Three days of exhilarating racing, bringing signature flavours, vibrant atmosphere and DJ sets to an unforgettable Grand Prix weekend.
- **Citation** : When it comes to private events, our possibilities are limitless. Connect with our dedicated Nammos events team, who will craft an experience tailored with refinement, care, and unmistakable Nammos spirit.
- **Contact** : To book your special occasion at Nammos, please contact us at: events@nammos.ae / +971 58 121 0000
- **Image** : `assets/img/celebrate-main-1040.webp` — 4:5

### Latest News (2 cartes)

*Calque Framer : `ajout — dupliquer un bloc “Philosophy - quote”`*

- **Carte 1** : 01.12.2025 — **Nammos Dubai: The Icon Returns** — After six celebrated years, Nammos Dubai is set to reopen its doors next month, December 2025, unveiling a reimagined destination where the Mykonian soul meets Dubai’s dynamic energy. → https://www.nammos.com/news/nammos-dubai-icon-returns
- **Carte 2** : 31.08.2026 — **Nammos Takes the Fast Lane at the Abu Dhabi Grand Prix** — Nammos meets the thrill of Formula 1 at Yas Marina Circuit. Three days of exhilarating racing, bringing signature flavours, vibrant atmosphere and DJ sets to an unforgettable Grand Prix weekend. → https://www.nammos.com/events/nammos-takes-fast-lane-abu-dhabi-grand-prix
- **Image** : `assets/img/news-icon-1200.webp` — 3:2
- **Image** : `assets/img/news-gp-1200.webp` — 3:2

### Contact & Reservations (carte sur photo)

*Calque Framer : `Contact & Location`*

- **Label** : Contact & Reservations
- **Titre** : Whether you’re booking a table, planning a special event, or seeking more information, our team at Nammos Dubai is ready to assist.
- **Horaires** : Beach 11.00 – 19.00 · Restaurant 12.30 – 02.00 · Lounge 11.00 – 02.00
- **Téléphone** : +971 58 121 0000
- **Adresse** : Four Seasons Resort, Jumeirah 2, Dubai, United Arab Emirates
- **E-mails** : reservations@nammos.ae / events@nammos.ae
- **Boutons** : Book online → SevenRooms · Find us → Google Maps
- **Image** : `assets/img/contact-bg-m-900.webp` (mobile), `assets/img/contact-bg-d-1920.webp` (desktop) — mobile 4:5 ou 3:4 / desktop 16:9

### Footer

*Calque Framer : `Footer`*

- **Texte** : At Nammos Dubai, we curate moments of endless joy.
- **Bouton** : Make a reservation
- **Navigation** : Home / Menus / Private Celebrations / Events / News / Contact
- **Réseaux** : Instagram / Facebook / LinkedIn / YouTube
- **Newsletter** : Email + Name + Subscribe
- **Nammos World** : Nammos Mykonos / Nammos Village / Nammos Dubai / Nammos London / Nammos Doha / Nammos Cannes / Nammos Limassol / Nammos Baja Sardinia / Nammos Montenegro
- **Mot géant** : NAMMOS
- **Bas de page** : © Nammos 2026. · Terms Of Service · Privacy policy
- **Image** : `assets/img/footer-900.webp` — 1:1

## 3. Pages secondaires

- **Menus** (`menus.html`) : hero + intro “Signature Flavours” + carte complète par catégorie (Japanese Touch, Nammos Signatures, Nigiri & Sashimi, Maki, Cold Appetizers & Salads, Hot Appetizers, Pasta, Seafood, Great Meats, Desserts). Source : carte Nammos Dubai 2022 — à remplacer par les menus actuels fournis par Nammos.
- **Private Celebrations** (`private-celebrations.html`) : hero + 3 blocs Weddings / Parties & Private Events / Corporate Events + citation + contact events@nammos.ae.
- **Contact** (`contact.html`) : hero + coordonnées + horaires + formulaire (Name, Surname, Phone, Email, Subject, Message, consentement).

## 4. Notes / à valider avec Nammos

- Hero statement / text: the original hero sentence “When Mediterranean elegance met Dubai’s magic, NAMMOS Dubai was born and the golden dunes that felt so familiar emitted a fresh allure under the Arabian sun.” is split in two for the mobile hero.
- Experience label “The Nammos Dubai experience”, menu label “The menu”, pair title “Crafted to be shared”, block1 text and block2 text are editorial connectors written for the template slots (short, non-factual).
- Menu items and prices come from the Nammos Dubai restaurant menu PDF (2022 edition) found online; the current menus must be supplied by Nammos before launch.
- Newsletter and contact forms are front-end only in this V1 (the contact form opens a pre-filled e-mail to reservations@nammos.ae).
