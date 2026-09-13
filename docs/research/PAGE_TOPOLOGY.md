# Page topology — Gaststätte template → Nammos Dubai V1

Source template: https://gaststatte.framer.website/ (Framer, one-page, breakpoints 809 / 1199)
Source content: https://www.nammos.com/dubai (+ /dubai/menus, /dubai/private-celebrations, /dubai/contact, /events, /news)

Mobile is the primary target (390 px). Desktop (1440 px) is derived from the same sections.

| # | Template section (Framer name) | Interaction model | Nammos Dubai mapping |
|---|---|---|---|
| 0 | Nav "Desktop - Transparent / Phone - Close" | scroll-driven (transparent over hero → solid), click (Menu overlay) | Brand "Nammos Dubai" + "Menu" button. Overlay: Home, Menus, Private Celebrations, Events, News, Contact, Reservations (SevenRooms), socials |
| 1 | Section - Hero (photo, h2 statement, glass CTA, paragraph, giant clipped h1) | static + parallax | Photo entrance (slider-1). Statement = hero sentence of nammos.com/dubai. CTA "Reservations". Giant clipped "NAMMOS" |
| 2 | Section - About (sage block, word-by-word scroll reveal, watermark, small line) | scroll-driven text reveal | Cream block. Label "Sun, Sea, Celebration". Text = "Nammos Dubai brings the spirit…". Line "Be in the heart of summer" |
| 3 | Section - experience (heading + 3 sticky-scroller rows with images) | scroll-driven (desktop sticky image switch) | Heading "Out of the Arabian Sea Blue". Rows: Taste of the Mediterranean / Under the Arabian Sun / When the Sun Sets |
| 4 | Section - Block (full-bleed photo + statement + glass CTA) | parallax + reveal | Sunsets portrait photo. "A Creative Twist to Beloved Classics". CTA Reservations |
| 5 | Section - Menu - quote (image, heading, 2 label+text, CTA) | reveal | Menu slider photo. "Authentic Inspiration, Iconic Bites" + Signature Flavours text. CTA "See our menus" → menus.html |
| 6 | Section - Philosophy - quote (image, heading, label+text, CTA) | reveal | Private events photo. "Celebrate the Nammos Way". CTA "Private celebrations" → private-celebrations.html |
| 7 | Section - Our menu: shutters photo, giant ticker, heading, tabs, dish list | scroll-driven shutters, marquee, click tabs | Gallery photo with shutters. Ticker "Be in the heart of summer" (real Nammos marquee). Tabs Starters / Mains / Desserts from 2022 Nammos Dubai menu |
| 8 | Nature Retreat (label, image, heading, text) | reveal | "Beach Life" → Nammos Beach text + swipeable 15-photo gallery strip (added, real Nammos gallery) |
| 9 | Block 2 (full-bleed photo, statement, CTA) | parallax | "When the Sun Sets" text, sunsets photo |
| 10 | Our philosophy (image, heading, 4 items grid, big quote) | reveal | "Your Special Moments, The Nammos Way": Weddings / Parties & Private Events / Corporate Events / Events (Grand Prix). Quote = "When it comes to private events…" |
| 11 | Contact & Location (photo + colour card) | reveal | Contact slider photo + black card: hours, phone, address, emails, Book online |
| 12 | Footer (logo, image, text, CTA, nav, newsletter, giant clipped name) | static | Nammos World logo, nav, Nammos World destinations, newsletter, giant "NAMMOS" |

Extra pages (derived from the same components): `menus.html`, `private-celebrations.html`, `contact.html`.
