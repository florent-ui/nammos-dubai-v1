# -*- coding: utf-8 -*-
"""All Nammos Dubai content used by the V1 site and the Framer kit.
Every string is verbatim from nammos.com/dubai (+ /menus, /private-celebrations, /contact, /events, /news)
unless noted in `NOTES` below.
"""

SITE = {
    'name': 'Nammos Dubai',
    'tagline': 'Sun, Sea, Celebration',
    'reservations_url': 'https://www.sevenrooms.com/explore/nammosdubai/reservations/create/search',
    'phone': '+971 58 121 0000',
    'phone_raw': '+971581210000',
    'email_reservations': 'reservations@nammos.ae',
    'email_events': 'events@nammos.ae',
    'email_press': 'press@nammos.com',
    'address': ['Four Seasons Resort, Jumeirah 2', 'Dubai, United Arab Emirates'],
    'map_url': 'https://maps.app.goo.gl/TfYv9uBtnpA5pKYE9',
    'hours': [('Beach', '11.00 – 19.00'), ('Restaurant', '12.30 – 02.00'), ('Lounge', '11.00 – 02.00')],
    'socials': [
        ('Instagram', 'https://instagram.com/nammos.dubai'),
        ('Facebook', 'https://www.facebook.com/NAMMOSDubai'),
        ('LinkedIn', 'https://www.linkedin.com/company/nammos-world'),
        ('YouTube', 'https://www.youtube.com/user/nammosmykonos'),
    ],
    'world': [
        ('Nammos Mykonos', 'https://www.nammos.com/mykonos'),
        ('Nammos Village', 'https://www.nammos.com/nammos-village'),
        ('Nammos Dubai', 'index.html'),
        ('Nammos London', 'https://www.nammos.com/london'),
        ('Nammos Doha', 'https://www.nammos.com/doha'),
        ('Nammos Cannes', 'https://www.nammos.com/cannes'),
        ('Nammos Limassol', 'https://www.nammos.com/limassol'),
        ('Nammos Baja Sardinia', 'https://www.nammos.com/sardinia'),
        ('Nammos Montenegro', 'https://www.nammos.com/montenegro'),
    ],
    'legal': [('Terms Of Service', 'https://www.nammos.com/terms-service'), ('Privacy policy', 'https://www.nammos.com/privacy-policy')],
    'copyright': '© Nammos 2026.',
}

NAV = [
    ('Home', 'index.html'),
    ('Menus', 'menus.html'),
    ('Private Celebrations', 'private-celebrations.html'),
    ('Events', 'https://www.nammos.com/events'),
    ('News', 'https://www.nammos.com/news'),
    ('Contact', 'contact.html'),
]
# anchors shown in the desktop nav bar (one-page)
ANCHORS = [('Experience', '#experience'), ('Menu', '#menu'), ('Beach', '#beach'), ('Celebrations', '#celebrations'), ('Contact', '#contact')]

HOME = {
    'meta_title': 'NAMMOS Dubai | Nammos',
    'meta_desc': 'Nammos Dubai brings the spirit of the Mediterranean to the shores of the Arabian Gulf, nestled in the iconic Four Seasons Resort, Jumeirah.',
    'hero': {
        'label': 'Four Seasons Resort, Jumeirah',
        'statement': 'When Mediterranean elegance met Dubai’s magic, NAMMOS Dubai was born.',
        'text': 'The golden dunes that felt so familiar emitted a fresh allure under the Arabian sun.',
        'cta': 'Reservations',
        'giant': 'Nammos',
        'image': 'hero',
        'alt': 'The striped entrance of Nammos Dubai at Four Seasons Resort, Jumeirah',
    },
    'about': {
        'label': 'Sun, Sea, Celebration',
        'text': 'Nammos Dubai brings the spirit of the Mediterranean to the shores of the Arabian Gulf, nestled in the iconic Four Seasons Resort, Jumeirah. Rooted in Mykonian authenticity yet infused with Dubai’s cosmopolitan energy, it’s a destination for sunlit lunches, golden sunsets, and vibrant evenings defined by endless joy.',
        'line': 'Be in the heart of summer',
    },
    'experience': {
        'label': 'The Nammos Dubai experience',
        'title': 'A Creative Twist to Beloved Classics',
        'rows': [
            {'label': 'Taste', 'title': 'Taste of the Mediterranean', 'image': 'row-taste', 'alt': 'Beetroot and fig salad at Nammos Dubai',
             'text': 'At the heart of the experience is Nammos’ signature cuisine: a sun-soaked symphony of Mediterranean flavours with an international twist. The menu blends refined Greek classics with contemporary global influences, where creativity and simplicity come together to define a dining experience that is both timeless and modern.'},
            {'label': 'Beach Life', 'title': 'Under the Arabian Sun', 'image': 'row-sun', 'alt': 'Striped umbrellas and sea loungers on Nammos Beach',
             'text': 'By day, Nammos Dubai is bathed in light, a sun-drenched escape where Mediterranean leisure comes alive. From leisurely lunches with chilled rosé to the sound of lively music and laughter, every detail evokes the charm of sunlit Mykonian afternoons, where time slows, and every moment feels endless.'},
            {'label': 'Sunsets', 'title': 'When the Sun Sets', 'image': 'row-sunset', 'alt': 'The lit colonnade of Nammos Dubai at dusk',
             'text': 'After dark, Nammos Dubai comes alive in a new light. The sea shimmers under the stars, music fills the air, and the energy turns magnetic. It’s where elevated dining blends with celebration, creating nights that feel spontaneous, stylish, and unforgettable.'},
        ],
    },
    'block1': {
        'statement': 'Out of the Arabian Sea Blue',
        'text': 'Rooted in Mykonian authenticity yet infused with Dubai’s cosmopolitan energy.',
        'cta': 'Reservations',
        'image': 'block1', 'alt': 'Nammos Dubai terrace with palm trees facing the sea',
    },
    'menu_teaser': {
        'label': 'Menus',
        'statement': 'Authentic Inspiration, Iconic Bites',
        'pairs': [
            ('Signature Flavours', 'From pristine seafood and elevated classics to globally inspired creations, the Nammos Dubai menu is a reflection of authenticity, quality, and unmistakable style. Every plate tells a story of the sea, the sun, and the joy of gathering around exceptional food.'),
            ('Crafted to be shared', 'Freshly sourced ingredients, meticulous craftsmanship, and a passion for unforgettable moments.'),
        ],
        'cta': ('See our menus', 'menus.html'),
        'image': 'menu-teaser', 'alt': 'Beetroot salad served on a turquoise table at Nammos Dubai',
    },
    'celeb_teaser': {
        'label': 'Private Celebrations',
        'statement': 'Celebrate the Nammos Way',
        'pairs': [
            ('Where private events become moments of effortless luxury & endless joy', 'Make every occasion unforgettable at Nammos Dubai. From intimate gatherings to grand celebrations, Nammos offers a setting where every occasion feels effortless and extraordinary. Whether a sunset dinner by the sea or milestone celebration each detail is curated with signature elegance and exceptional service.'),
        ],
        'cta': ('Plan your celebration', 'private-celebrations.html'),
        'image': 'celeb-teaser', 'alt': 'Table setting with roses for a private celebration at Nammos Dubai',
    },
    'shutter': {'left': 'Sun, Sea', 'right': 'Celebration', 'image': 'shutter', 'alt': 'Guests dining at Nammos Dubai as singers perform'},
    'ticker': 'Be in the heart of summer',
    'menu': {
        'label': 'The menu',
        'statement': 'An invitation to savour the essence of the Mediterranean, where time-honoured recipes meet contemporary culinary artistry.',
        'text': 'Each dish is crafted with the finest ingredients, designed to be shared, celebrated, and remembered.',
        'image': 'menu-side', 'alt': 'Nigiri with caviar at Nammos Dubai',
        'note': 'A selection from the Nammos Dubai restaurant menu. All prices are in AED and inclusive of 7% municipality fee and 5% VAT. (A) Dishes containing alcohol.',
        'tabs': [
            ('Starters', [
                ('Aubergine Mille-Feuille', 'feta cream cheese', '95'),
                ('Greek Salad', 'tomato, cucumber, onion, green pepper, olives & feta cheese', '120'),
                ('Tuna Tartare', 'baked aubergine, smoked eel & bottarga sauce', '185'),
                ('Mediterranean Spread Platter', 'hummus, white taramosalata with bottarga, tzatziki & tirokafteri', '130'),
                ('Grilled Octopus', 'pepper relish', '135'),
                ('Santorini Fava “Saganaki”', 'prawns & Greek spicy sauce', '120'),
                ('Fried Calamari', 'smoky Florina pepper mayonnaise', '160'),
            ]),
            ('Mains', [
                ('Nammos Risotto', 'lobster & carabineros (A)', '420'),
                ('Black Squid Ink Tonnarello', 'carabineros & bottarga', '395'),
                ('Pappardelle Seafood', 'white sauce', '310'),
                ('Pici Veal Cheeks', '24h slow cooked veal cheeks', '180'),
                ('Baby Chicken', 'yogurt, lemon balm vinaigrette & roasted potatoes', '190'),
                ('Fresh Fish from display', 'our daily fish market offers a large range of freshly caught Mediterranean fish and seafood', '775 / kg'),
                ('Fresh Lobster', 'from the daily fish market', '1300 / kg'),
            ]),
            ('Desserts', [
                ('Almond Pie', 'blueberries & kaymak ice cream', '55'),
                ('All-time Classic Nammos Chocolate Mousse', 'dark, milk & white chocolate', '60'),
                ('Baklava', 'kaymak ice cream', '65'),
                ('Cheesecake', 'figs & honeycomb', '75'),
                ('Profiteroles', 'caramel cream, pistachio ice cream, warm chocolate sauce', '60'),
                ('Caprese Cake (GF)', 'dark chocolate (75%)', '55'),
            ]),
        ],
    },
    'beach': {
        'label': 'Beach Life',
        'statement': 'Bask in the essence of Mediterranean leisure at Nammos Beach, where golden sands and crystal waters set the scene for pure relaxation.',
        'text': 'Designed for comfort and style, plush sea loungers and private cabanas offer a serene escape beneath the Arabian sun. With discreet service, refined cocktails, and a laid-back yet sophisticated atmosphere, it’s the ultimate expression of barefoot luxury by the sea.',
        'image': 'beach-main', 'alt': 'Nammos Beach with turquoise striped umbrellas',
        'gallery_alt': 'Nammos Dubai gallery',
    },
    'block2': {
        'statement': 'Where private events become moments of effortless luxury & endless joy',
        'text': 'From intimate gatherings to grand celebrations, Nammos offers a setting where every occasion feels effortless and extraordinary.',
        'cta': ('Plan your celebration', 'private-celebrations.html'),
        'image': 'block2', 'alt': 'The glowing entrance of Nammos Dubai at sunset',
    },
    'celebrate': {
        'label': 'Your Special Moments, The Nammos Way',
        'title': 'Celebrate the Nammos Way',
        'image': 'celebrate-main', 'alt': 'Live performance during a private event at Nammos Dubai',
        'items': [
            ('Celebrating Love', 'Weddings', 'Celebrate your love story with the timeless charm of Nammos Dubai. From intimate beachfront ceremonies to vibrant evening receptions, we create weddings that blend Mediterranean elegance with signature Nammos energy.'),
            ('There’s Always a Reason to Celebrate', 'Parties & Private Events', 'Birthdays, milestones, and new beginnings deserve to be celebrated with style and joy. At Nammos Dubai, we create the perfect setting to share these moments with the people who matter most.'),
            ('Celebrate Your Business Milestones', 'Corporate Events', 'Nammos Dubai offers an exceptional setting for your corporate events, ensuring a seamless and memorable experience from start to finish.'),
            ('Events — 4-6.12.2026', 'Nammos Takes the Fast Lane at the Abu Dhabi Grand Prix', 'Nammos meets the thrill of Formula 1 at Yas Marina Circuit. Three days of exhilarating racing, bringing signature flavours, vibrant atmosphere and DJ sets to an unforgettable Grand Prix weekend.'),
        ],
        'quote': 'When it comes to private events, our possibilities are limitless. Connect with our dedicated Nammos events team, who will craft an experience tailored with refinement, care, and unmistakable Nammos spirit.',
        'contact_line': 'To book your special occasion at Nammos, please contact us at:',
    },
    'news': {
        'label': 'Latest News',
        'items': [
            ('01.12.2025', 'Nammos Dubai: The Icon Returns', 'After six celebrated years, Nammos Dubai is set to reopen its doors next month, December 2025, unveiling a reimagined destination where the Mykonian soul meets Dubai’s dynamic energy.', 'https://www.nammos.com/news/nammos-dubai-icon-returns', 'news-icon', 'Nammos Beach, Dubai'),
            ('31.08.2026', 'Nammos Takes the Fast Lane at the Abu Dhabi Grand Prix', 'Nammos meets the thrill of Formula 1 at Yas Marina Circuit. Three days of exhilarating racing, bringing signature flavours, vibrant atmosphere and DJ sets to an unforgettable Grand Prix weekend.', 'https://www.nammos.com/events/nammos-takes-fast-lane-abu-dhabi-grand-prix', 'news-gp', 'Nammos Pit Lane at Yas Marina Circuit'),
        ],
        'more': ('All news', 'https://www.nammos.com/news'),
    },
    'contact': {
        'label': 'Contact & Reservations',
        'statement': 'Whether you’re booking a table, planning a special event, or seeking more information, our team at Nammos Dubai is ready to assist.',
        'cta': 'Book online',
        'image': 'contact-bg', 'alt': 'The lounge of Nammos Dubai',
    },
    'footer': {
        'text': 'At Nammos Dubai, we curate moments of endless joy.',
        'cta': 'Make a reservation',
        'image': 'footer', 'alt': 'The Nammos sign at the entrance of Nammos Dubai',
        'newsletter': 'Newsletter',
        'subscribe': 'Subscribe',
        'thanks': 'Thank you — you’re on the list.',
    },
}

MENUS_PAGE = {
    'meta_title': 'NAMMOS Dubai Menus | Nammos',
    'meta_desc': 'An invitation to savour the essence of the Mediterranean, where time-honoured recipes meet contemporary culinary artistry.',
    'hero': {'label': 'Nammos Dubai', 'title': 'Menus', 'text': 'An invitation to savour the essence of the Mediterranean, where time-honoured recipes meet contemporary culinary artistry. Each dish is crafted with the finest ingredients, designed to be shared, celebrated, and remembered.', 'image': 'menus-hero', 'alt': 'Beetroot salad on a turquoise table at Nammos Dubai'},
    'intro': {'label': 'Authentic Inspiration, Iconic Bites', 'title': 'Signature Flavours',
              'text': 'From pristine seafood and elevated classics to globally inspired creations, the Nammos Dubai menu is a reflection of authenticity, quality, and unmistakable style. Every plate tells a story of the sea, the sun, and the joy of gathering around exceptional food.',
              'line': 'Freshly sourced ingredients, meticulous craftsmanship, and a passion for unforgettable moments.',
              'image': 'menus-dish', 'alt': 'Nigiri with caviar at Nammos Dubai'},
    'note': 'Please inform your waiter in case of allergies or dietary requirements. (A) Dishes containing alcohol. All prices are in AED and inclusive of 7% municipality fee and 5% VAT.',
    'reference': 'Menu reference: Nammos Dubai restaurant menu — to be replaced by the current menus supplied by Nammos.',
    'categories': [
        ('Japanese Touch', 'Appetizers', [
            ('Seabass Crudo', 'yuzu wasabi', '145'), ('Tuna Tartare', 'yuke sauce (A)', '150'), ('Spicy Crab Tartare', 'yuzu truffle', '340'),
            ('Greek White Fish Carpaccio', 'jalapeno dressing', '145'), ('Salmon Carpaccio', 'truffle ponzu (A)', '112'),
            ('Usuzukuri', 'tuna, salmon, yellowtail or mix', '125'), ('Prawn Tempura', 'chili sesame dressing', '125'), ('Bluefin Tuna Tataki', 'mango salsa & ponzu', '132'),
        ]),
        ('Nammos Signatures', 'Japanese Touch', [
            ('Spicy Tuna', 'on spider roll & soft-shell crab', '145'), ('Salmon Teriyaki', 'on shrimp tempura roll (A)', '145'), ('Baked Spicy Crab Maki', '', '155'),
            ('Kobe Beef Tataki', '(A)', '360'), ('Nigiri Kobe', 'caviar & gold leaf (2 pcs)', '530'), ('Wagyu Beef Maki', 'citrus soy dressing (8 pcs) (A)', '355'), ('Kobe & Foie Gras Maki', '(A)', '430'),
        ]),
        ('Nigiri & Sashimi', '2 pcs — seared or raw', [
            ('Toro', '', '129'), ('Chutoro', '', '99'), ('Tuna', '', '65'), ('Salmon', '', '50'), ('Yellowtail', '', '75'), ('Shrimp', 'cooked', '65'), ('Greek White Fish', '', '65'), ('Freshwater Eel', '(A)', '65'),
            ('Whole Line-caught Greek Fish', 'special sashimi', '860 / kg'),
        ]),
        ('Maki', '8 pcs inside out', [
            ('Spicy Shrimp & King Crab', '', '140'), ('Avocado & Asparagus', '', '60'), ('Rainbow', 'topped with salmon, tuna, yellowtail & shrimp', '109'), ('Dragon', '(A)', '153'), ('Crunchy Spicy Tuna', '', '135'),
        ]),
        ('Cold Appetizers & Salads', 'Appetizers', [
            ('Anchovies', 'green gazpacho', '60'), ('Black Angus Beef Tartare', 'olive marmalade & truffle yogurt', '210'), ('Tuna Tartare', 'baked aubergine, smoked eel & bottarga sauce', '185'),
            ('Tuna Carpaccio', 'seared bluefin tuna, tomato, bottarga & Greek dried fig', '180'), ('Mediterranean Spread Platter', 'hummus, white taramosalata with bottarga, tzatziki & tirokafteri', '130'),
            ('Quinoa Salad', 'watermelon & manouri cheese', '80'), ('Green Salad', 'asparagus, avocado & Kalamansi vinaigrette', '65'),
            ('Beetroot Salad', 'marinated beetroot, rainbow carrots, beluga lentils, celery, manouri cheese, honey & balsamic vinaigrette', '90'),
            ('Louza Salad', 'rocket salad, “xinotiro” Mykonian cheese, fresh figs & balsamic vinaigrette', '125'), ('Greek Salad', 'tomato, cucumber, onion, green pepper, olives & feta cheese', '120'),
            ('Burrata Salad', 'heritage tomatoes, grilled asparagus, avocado, Greek olives with lemon olive oil & chili flakes', '190'), ('Mushrooms Caesar Salad', 'parmesan cheese & quail eggs', '90'),
            ('Octopus Salad', 'with potato & Greek artichoke', '160'), ('King Crab Salad', 'green leaves salad & fresh bottarga dressing', '310'),
            ('Nammos Salad', 'medley of greens, red & white cabbage, carrot, avocado, parmesan flakes with orange soya & balsamic vinaigrette', '85'),
        ]),
        ('Hot Appetizers', 'Appetizers', [
            ('Homemade Pita', '', '75'), ('Soup of the Day', '', '75'), ('Arabic Pita', 'stuffed with feta cheese, olives & tomatoes', '72'), ('Grilled Halloumi Cheese', 'lemon purée & green olive harissa', '65'),
            ('Grilled Vegetables', 'basil & lemon dressing', '95'), ('Fried Zucchini', 'tzatziki', '60'), ('Aubergine Mille-Feuille', 'feta cream cheese', '95'), ('Mykonian Meatballs', 'Greek yogurt with dried mint', '105'),
            ('Santorini Fava “Saganaki”', 'prawns & Greek spicy sauce', '120'), ('Fresh Langoustine Tempura', 'saffron & lemon aioli', '200'), ('Mussels', 'white wine, garlic & lemon (A)', '135'),
            ('Fried Calamari', 'smoky Florina pepper mayonnaise', '160'), ('Sautéed Baby Eel', 'garlic & olive oil', '130'), ('Grilled Calamari', 'zucchini salsa, mint & lemon olive oil', '135'),
            ('Stuffed Calamari', 'feta cheese & sundried tomatoes', '150'), ('Grilled Octopus', 'pepper relish', '135'), ('Baked Saganaki Cheese', '', '55'),
        ]),
        ('Pasta', 'Nammos Experience — homemade pasta', [
            ('Pappardelle', 'baked with tomato sauce & burrata', '120'), ('Mushroom Risotto', 'seasonal mushrooms & parmesan (A)', '130'), ('Nammos Risotto', 'lobster & carabineros (A)', '420'),
            ('Ravioli “Anthotiro”', 'arrabbiata sauce', '120'), ('Ravioli “Anthotiro”', 'truffle', '180'), ('Pici Veal Cheeks', '24h slow cooked veal cheeks', '180'),
            ('Pappardelle Seafood', 'white sauce', '310'), ('Black Squid Ink Tonnarello', 'carabineros & bottarga', '395'),
        ]),
        ('Seafood', 'Our daily fish market offers a large range of freshly caught Mediterranean fish and seafood.', [
            ('Fresh Fish from display', '', '775 / kg'), ('Fresh Lobster', '', '1300 / kg'), ('Carabineros Prawns', '', '1600 / kg'), ('Jumbo King Prawns', '', '825 / kg'), ('King Crab Legs', '', '1300 / kg'),
        ]),
        ('Great Meats', 'Our Meat is sourced from unique farms around the world. Prices per 100 gr.', [
            ('Black Angus Tenderloin', 'Premium Farms Black Angus (USA) — Choice or Prime', '116'), ('Black Angus Ribeye', 'Premium Farms Black Angus (USA)', '72'),
            ('Black Angus Striploin', 'Premium Farms Black Angus (USA)', '64'), ('Black Angus Tomahawk', 'Premium Farms Black Angus (USA)', '84'),
            ('Wagyu Tenderloin', 'Premium Farm Wagyu (Australia) — 8/9 MB grade, 350-day grain fed', '268'), ('Wagyu Ribeye', 'Premium Farm Wagyu (Australia)', '200'),
            ('Wagyu Striploin', 'Premium Farm Wagyu (Australia)', '168'), ('Wagyu Tomahawk', 'Premium Farm Wagyu (Australia)', '128'),
            ('Constantino Moro Striploin', 'Nammos Special Farm — Spanish Superior, grass & grain fed', '208'),
            ('Kobe Tenderloin', 'Kobe Beef (Japan) — 300-day corn fed, certified A5 and 10+', '871'), ('Kobe Ribeye', 'Kobe Beef (Japan)', '572'), ('Kobe Striploin', 'Kobe Beef (Japan)', '594'),
            ('Ozaki Miyazaki Tenderloin', 'Winner of the 2007 & 2012 “Wagyu Olympics” — 600-day grain fed', '924'), ('Ozaki Miyazaki Ribeye', 'Ozaki Miyazaki Beef (Japan)', '682'), ('Ozaki Miyazaki Striploin', 'Ozaki Miyazaki Beef (Japan)', '682'),
            ('Baby Chicken', 'yogurt, lemon balm vinaigrette & roasted potatoes (per dish)', '190'),
        ]),
        ('Desserts', '', [
            ('Almond Pie', 'blueberries & kaymak ice cream', '55'), ('Caprese Cake (GF)', 'dark chocolate (75%)', '55'), ('All-time Classic Nammos Chocolate Mousse', 'dark, milk & white chocolate', '60'),
            ('Baklava', 'kaymak ice cream', '65'), ('Cheesecake', 'figs & honeycomb', '75'), ('Profiteroles', 'caramel cream, pistachio ice cream, warm chocolate sauce', '60'),
            ('Homemade Ice Creams & Sorbets', 'ask your waiter for the selection of the day', '55'), ('Nammos Dessert Platter', 'selection of desserts, fruits & ice cream', '470'),
        ]),
    ],
    'gallery': [('menus-2', 'Prawn risotto at Nammos Dubai'), ('menus-3', 'Sharing plates at Nammos Dubai')],
}

CELEB_PAGE = {
    'meta_title': 'NAMMOS Dubai Private Celebrations | Nammos',
    'meta_desc': 'At Nammos Dubai, we curate moments of endless joy.',
    'hero': {'label': 'Nammos Dubai', 'title': 'Private Celebrations',
             'text': 'At Nammos Dubai, we curate moments of endless joy. Whether you are hosting an intimate dinner by the beach or a grand celebration filled with music and vibrancy, our team will bring to life your special day with signature Nammos energy. Delectable Mediterranean-inspired cuisine, warm hospitality, and an unforgettable ambience will come together in perfect harmony.',
             'image': 'celeb-hero', 'alt': 'A couple celebrating at Nammos Dubai'},
    'statement': 'Your Special Moments, The Nammos Way',
    'features': [
        ('Celebrating Love', 'Weddings', 'Celebrate your love story with the timeless charm of Nammos Dubai. From intimate beachfront ceremonies to vibrant evening receptions, we create weddings that blend Mediterranean elegance with signature Nammos energy. Exceptional Greek-inspired cuisine, warm hospitality, and unforgettable ambience come together to make your day truly extraordinary and unforgettable.', 'celeb-weddings', 'Wedding table setting with roses at Nammos Dubai'),
        ('There’s Always a Reason to Celebrate', 'Parties & Private Events', 'Birthdays, milestones, and new beginnings deserve to be celebrated with style and joy. At Nammos Dubai, we create the perfect setting to share these moments with the people who matter most. Let our signature hospitality, impeccable service, and Mediterranean spirit elevate your occasion, while you simply revel in the beauty of the moment.', 'celeb-parties', 'Live performers at a private party at Nammos Dubai'),
        ('Celebrate Your Business Milestones', 'Corporate Events', 'Nammos Dubai offers an exceptional setting for your corporate events, ensuring a seamless and memorable experience from start to finish. With impeccable attention to detail, a vibrant yet polished atmosphere, and a level of care that defines the Nammos philosophy, we help elevate your company’s occasion and leave a lasting impression on partners, clients, and colleagues. Entrust us with your event, and we’ll create a moment your team will truly value.', 'celeb-corporate', 'A speaker addressing guests at a corporate event at Nammos Dubai'),
    ],
    'quote': 'When it comes to private events, our possibilities are limitless. Connect with our dedicated Nammos events team, who will craft an experience tailored with refinement, care, and unmistakable Nammos spirit.',
    'contact_line': 'To book your special occasion at Nammos, please contact us at:',
    'image': 'celeb-table', 'alt': 'Evening table decoration at Nammos Dubai',
}

CONTACT_PAGE = {
    'meta_title': 'NAMMOS Dubai Contact | Nammos',
    'meta_desc': 'Whether you’re booking a table, planning a special event, or seeking more information, our team at Nammos Dubai is ready to assist.',
    'hero': {'label': 'Nammos Dubai', 'title': 'Contact', 'text': 'Whether you’re booking a table, planning a special event, or seeking more information, our team at Nammos Dubai is ready to assist.', 'image': 'contact-hero', 'alt': 'The lounge of Nammos Dubai'},
    'book': 'Book online',
    'find_us': 'Find us',
    'form': {
        'label': 'Contact Form', 'title': 'Drop us a line',
        'text': 'Fill in your details on the form and give us more hints on your inquiry. We will get back to you with information and all you need to know regarding your request.',
        'fields': [('name', 'Name *', 'text'), ('surname', 'Surname *', 'text'), ('phone', 'Phone Number *', 'tel'), ('email', 'Email *', 'email'), ('subject', 'Subject', 'text')],
        'message': 'Message',
        'consent': 'I have read and agreed to the Privacy Policy Notice.',
        'submit': 'Send message',
    },
    'image': 'contact-team', 'alt': 'A Nammos Dubai host welcoming guests',
}

NOTES = [
    'Hero statement / text: the original hero sentence “When Mediterranean elegance met Dubai’s magic, NAMMOS Dubai was born and the golden dunes that felt so familiar emitted a fresh allure under the Arabian sun.” is split in two for the mobile hero.',
    'Experience label “The Nammos Dubai experience”, menu label “The menu”, pair title “Crafted to be shared”, block1 text and block2 text are editorial connectors written for the template slots (short, non-factual).',
    'Menu items and prices come from the Nammos Dubai restaurant menu PDF (2022 edition) found online; the current menus must be supplied by Nammos before launch.',
    'Newsletter and contact forms are front-end only in this V1 (the contact form opens a pre-filled e-mail to reservations@nammos.ae).',
]
