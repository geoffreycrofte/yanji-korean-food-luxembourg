"""
Traductions allemandes (de) et luxembourgeoises (lb), utilisées par build-i18n.py.

Chaque entrée est indexée par la version ANGLAISE du fragment (colonne « en »
de build-i18n.py) et donne (allemand, luxembourgeois). Si vous modifiez un texte
anglais dans build-i18n.py, mettez à jour la clé correspondante ici : le build
s'arrête et indique les fragments sans traduction.
"""

# --- Fragments de texte : anglais -> (allemand, luxembourgeois) ---
ROWS = {
    # <head>
    "<title>Yanji Korean Food – Korean restaurant near Luxembourg station | Kimbap, Bibimbap</title>": (
        "<title>Yanji Korean Food – Koreanisches Restaurant am Bahnhof Luxemburg | Kimbap, Bibimbap</title>",
        "<title>Yanji Korean Food – Koreanescht Restaurant bei der Gare zu Lëtzebuerg | Kimbap, Bibimbap</title>"),
    "Yanji Korean Food, a small Korean restaurant at 63 avenue de la Gare, Luxembourg. Kimbap, stone-pot bibimbap, tteokbokki, spicy soups and Korean fried chicken. Open Monday to Saturday, 11:00–17:30.": (
        "Yanji Korean Food, ein kleines koreanisches Restaurant in der 63, avenue de la Gare in Luxemburg. Kimbap, Bibimbap im Steintopf, Tteokbokki, scharfe Suppen und koreanisches Brathähnchen. Geöffnet Montag bis Samstag, 11:00–17:30 Uhr.",
        "Yanji Korean Food, e klengt koreanescht Restaurant op der 63, avenue de la Gare zu Lëtzebuerg. Kimbap, Bibimbap am Steendëppen, Tteokbokki, schaarf Zoppen a koreanesche Poulet frit. Op vu Méindes bis Samschdes, 11:00–17:30 Auer."),
    "Korean restaurant Luxembourg, Korean food Luxembourg, kimbap, bibimbap, tteokbokki, Korean fried chicken, avenue de la Gare, Luxembourg station, Yanji": (
        "Koreanisches Restaurant Luxemburg, koreanisches Essen Luxemburg, Kimbap, Bibimbap, Tteokbokki, koreanisches Brathähnchen, avenue de la Gare, Bahnhofsviertel, Yanji",
        "Koreanescht Restaurant Lëtzebuerg, koreanescht Iessen Lëtzebuerg, Kimbap, Bibimbap, Tteokbokki, Poulet frit, avenue de la Gare, Garer Quartier, Yanji"),
    'content="Yanji Korean Food – Korean restaurant near Luxembourg station"': (
        'content="Yanji Korean Food – Koreanisches Restaurant am Bahnhof Luxemburg"',
        'content="Yanji Korean Food – Koreanescht Restaurant bei der Gare zu Lëtzebuerg"'),
    "Kimbap, stone-pot bibimbap, tteokbokki and Korean fried chicken. 63 avenue de la Gare, Luxembourg. Mon–Sat 11:00–17:30.": (
        "Kimbap, Bibimbap im Steintopf, Tteokbokki und koreanisches Brathähnchen. 63, avenue de la Gare, Luxemburg. Mo–Sa 11:00–17:30 Uhr.",
        "Kimbap, Bibimbap am Steendëppen, Tteokbokki a koreanesche Poulet frit. 63, avenue de la Gare, Lëtzebuerg. Mé–Sa 11:00–17:30 Auer."),

    # En-tête
    "Skip to content": ("Zum Inhalt springen", "Direkt zum Inhalt"),
    '<span class="visually-hidden"> Korean Food – home</span>': (
        '<span class="visually-hidden"> Korean Food – Startseite</span>',
        '<span class="visually-hidden"> Korean Food – Startsäit</span>'),
    'aria-label="Main navigation"': ('aria-label="Hauptnavigation"', 'aria-label="Haaptnavigatioun"'),
    '<li><a href="#menu">Menu</a></li>': ('<li><a href="#menu">Speisekarte</a></li>', '<li><a href="#menu">Menü</a></li>'),
    '<li><a href="#bibimbap-guide">Bibimbap</a></li>': ('<li><a href="#bibimbap-guide">Bibimbap</a></li>', '<li><a href="#bibimbap-guide">Bibimbap</a></li>'),
    '<li><a href="#infos">Hours &amp; location</a></li>': (
        '<li><a href="#infos">Öffnungszeiten &amp; Anfahrt</a></li>',
        '<li><a href="#infos">Ëffnungszäiten &amp; Uweeg</a></li>'),
    "Pause animations": ("Animationen anhalten", "Animatiounen stoppen"),
    "\n        Call\n": ("\n        Anrufen\n", "\n        Uruffen\n"),
    'aria-label="Call Yanji Korean Food"': ('aria-label="Yanji Korean Food anrufen"', 'aria-label="Yanji Korean Food uruffen"'),
    'aria-label="Open menu"': ('aria-label="Menü öffnen"', 'aria-label="Menü opmaachen"'),

    # Hero
    '<span class="visually-hidden"> – Korean restaurant near Luxembourg station</span>': (
        '<span class="visually-hidden"> – Koreanisches Restaurant am Bahnhof Luxemburg</span>',
        '<span class="visually-hidden"> – Koreanescht Restaurant bei der Gare zu Lëtzebuerg</span>'),
    "Freshly rolled kimbap, stone-pot bibimbap, spicy soups and Korean fried chicken, a short walk from Luxembourg station.": (
        "Frisch gerollte Kimbap, Bibimbap im Steintopf, scharfe Suppen und koreanisches Brathähnchen – nur ein paar Schritte vom Bahnhof Luxemburg.",
        "Frësch gerullte Kimbap, Bibimbap am Steendëppen, schaarf Zoppen a koreanesche Poulet frit – just e puer Schrëtt vun der Gare."),
    "Mon – Sat · 11:00 – 17:30": ("Mo – Sa · 11:00 – 17:30", "Mé – Sa · 11:00 – 17:30"),
    ">See the menu</a>": (">Zur Speisekarte</a>", ">Menü kucken</a>"),
    ">Find us</a>": (">So finden Sie uns</a>", ">Esou fannt Dir eis</a>"),
    'Flavours of Korea<small lang="ko">한국의 맛</small>': (
        'Geschmack Koreas<small lang="ko">한국의 맛</small>', 'Goût vu Korea<small lang="ko">한국의 맛</small>'),
    'Made with love<small lang="ko">사랑을 담아</small>': (
        'Mit Liebe gemacht<small lang="ko">사랑을 담아</small>', 'Mat Léift gemaach<small lang="ko">사랑을 담아</small>'),
    'Served piping hot<small lang="ko">따뜻하게</small>': (
        'Heiß serviert<small lang="ko">따뜻하게</small>', 'Waarm zerwéiert<small lang="ko">따뜻하게</small>'),

    # Bandeau défilant
    'marquee__item">Kimbap <': ('marquee__item">Kimbap <', 'marquee__item">Kimbap <'),
    'marquee__item">Bibimbap <': ('marquee__item">Bibimbap <', 'marquee__item">Bibimbap <'),
    'marquee__item">Tteokbokki <': ('marquee__item">Tteokbokki <', 'marquee__item">Tteokbokki <'),
    'marquee__item">Fried chicken <': ('marquee__item">Brathähnchen <', 'marquee__item">Poulet frit <'),
    'marquee__item">Kimchi <': ('marquee__item">Kimchi <', 'marquee__item">Kimchi <'),
    'marquee__item">Gyudon <': ('marquee__item">Gyudon <', 'marquee__item">Gyudon <'),
    'marquee__item">Spicy soup <': ('marquee__item">Scharfe Suppe <', 'marquee__item">Schaarf Zopp <'),

    # À propos
    "Small menu, <em>big heart</em>": ("Kleine Karte, <em>großes Herz</em>", "Kleng Kaart, <em>grousst Häerz</em>"),
    "At Yanji, we serve simple, generous Korean food in the heart of Luxembourg’s Gare district. A small menu, a caring team and warming dishes: kimbap, bibimbap, tteokbokki, slow-cooked soups and crispy fried chicken.": (
        "Bei Yanji servieren wir einfache, großzügige koreanische Küche mitten im Bahnhofsviertel von Luxemburg. Eine kleine Karte, ein herzliches Team und Gerichte, die wärmen: Kimbap, Bibimbap, Tteokbokki, lange gekochte Suppen und knuspriges Brathähnchen.",
        "Bei Yanji kritt Dir einfach a generéis koreanesch Kichen, mëttst am Garer Quartier. Eng kleng Kaart, eng léif Equipe a Platen, déi eng erwiermen: Kimbap, Bibimbap, Tteokbokki, laang gekachten Zoppen a knusprege Poulet frit."),
    "Eat in or take away, for a lunch break or a savoury snack: drop by Monday to Saturday.": (
        "Vor Ort oder zum Mitnehmen, für die Mittagspause oder einen herzhaften Snack: Besuchen Sie uns von Montag bis Samstag.",
        "Hei iessen oder matuelen, fir d'Mëttespaus oder e klenge Snack: Kommt eis vu Méindes bis Samschdes besichen."),
    "<strong>Kimbap</strong><span>5 Korean rolls, including a vegetarian one</span>": (
        "<strong>Kimbap</strong><span>5 koreanische Rollen, davon eine vegetarisch</span>",
        "<strong>Kimbap</strong><span>5 koreanesch Rollen, dovun eng vegetaresch</span>"),
    "<strong>Stone pot</strong><span>Sizzling bibimbap, served with soup</span>": (
        "<strong>Steintopf</strong><span>Brutzelnder Bibimbap, mit Suppe serviert</span>",
        "<strong>Steendëppen</strong><span>Brutzelende Bibimbap, mat Zopp</span>"),
    "<strong>Spicy or not</strong><span>Every spicy dish is marked</span>": (
        "<strong>Scharf oder nicht</strong><span>Jedes scharfe Gericht ist gekennzeichnet</span>",
        "<strong>Schaarf oder net</strong><span>All schaarf Plat ass markéiert</span>"),
    "<strong>Lovely team</strong><span>A warm welcome, promised</span>": (
        "<strong>Liebes Team</strong><span>Ein herzlicher Empfang, versprochen</span>",
        "<strong>Léif Equipe</strong><span>E waarmen Empfang, versprach</span>"),

    # Carte
    "All our dishes are prepared on site. Prices include VAT. Photos are for illustration only.": (
        "Alle Gerichte werden vor Ort zubereitet. Preise inkl. MwSt. Die Fotos dienen nur zur Illustration.",
        "All eis Platen ginn hei preparéiert. D'Präisser sinn inklusiv TVA. D'Fotoen sinn nëmmen Illustratiounen."),
    'aria-label="Menu categories"': ('aria-label="Kategorien der Speisekarte"', 'aria-label="Kategorien vum Menü"'),
    '<a href="#kimbap">Kimbap</a>': ('<a href="#kimbap">Kimbap</a>', '<a href="#kimbap">Kimbap</a>'),
    '<a href="#bibimbap">Bibimbap</a>': ('<a href="#bibimbap">Bibimbap</a>', '<a href="#bibimbap">Bibimbap</a>'),
    '<a href="#specialites">Specialities</a>': ('<a href="#specialites">Spezialitäten</a>', '<a href="#specialites">Spezialitéiten</a>'),
    '<a href="#kimchi">Kimchi</a>': ('<a href="#kimchi">Kimchi</a>', '<a href="#kimchi">Kimchi</a>'),
    '<a href="#boissons">Drinks</a>': ('<a href="#boissons">Getränke</a>', '<a href="#boissons">Gedrénks</a>'),
    '<a href="#allergenes">Allergens</a>': ('<a href="#allergenes">Allergene</a>', '<a href="#allergenes">Allergenen</a>'),
    'aria-label="Filter the menu"': ('aria-label="Speisekarte filtern"', 'aria-label="Menü filteren"'),
    "Filter:": ("Filtern:", "Filteren:"),
    "</span>Vegetarian<": ("</span>Vegetarisch<", "</span>Vegetaresch<"),
    "</span>Not spicy<": ("</span>Nicht scharf<", "</span>Net schaarf<"),
    "For information only: if you have an allergy, please always tell our team.": (
        "Nur zur Information: Bei Allergien sprechen Sie bitte immer unser Team an.",
        "Just zur Informatioun: Wann Dir eng Allergie hutt, sot et w.e.g. ëmmer eiser Equipe."),
    "Seaweed rolls of sesame-seasoned rice with fillings, sliced.": (
        "Algenrollen aus mit Sesam gewürztem Reis, gefüllt und in Scheiben geschnitten.",
        "Algenrollen aus Räis mat Sesam, gefëllt an a Scheiwen geschnidden."),
    '<span class="visually-hidden">Dish no. </span>': ('<span class="visually-hidden">Gericht Nr. </span>', '<span class="visually-hidden">Plat Nr. </span>'),
    '<span class="visually-hidden">no. </span>': ('<span class="visually-hidden">Nr. </span>', '<span class="visually-hidden">Nr. </span>'),
    'aria-hidden="true">Illustrative photo</span>': ('aria-hidden="true">Beispielfoto</span>', 'aria-hidden="true">Beispillfoto</span>'),
    "</span>Spicy</span>": ("</span>Scharf</span>", "</span>Schaarf</span>"),
    '<span class="tag tag--side">+ soup &amp; kimchi</span>': (
        '<span class="tag tag--side">+ Suppe &amp; Kimchi</span>', '<span class="tag tag--side">+ Zopp &amp; Kimchi</span>'),
    '<span class="tag tag--side">+ soup</span>': ('<span class="tag tag--side">+ Suppe</span>', '<span class="tag tag--side">+ Zopp</span>'),
    '<span class="tag tag--side">Stone pot + soup</span>': (
        '<span class="tag tag--side">Steintopf + Suppe</span>', '<span class="tag tag--side">Steendëppen + Zopp</span>'),
    '<span class="tag tag--side">+ rice</span>': ('<span class="tag tag--side">+ Reis</span>', '<span class="tag tag--side">+ Räis</span>'),
    '<span class="tag tag--side">Choice of 3 flavours</span>': (
        '<span class="tag tag--side">3 Geschmacksrichtungen zur Wahl</span>', '<span class="tag tag--side">3 Goûten zur Auswiel</span>'),
    "<li>Korean sweet &amp; spicy <span": ("<li>Koreanisch süß &amp; scharf <span", "<li>Koreanesch séiss &amp; schaarf <span"),
    "<li>Honey mustard</li>": ("<li>Honig-Senf</li>", "<li>Hunneg-Moschter</li>"),
    "<li>Soy sauce</li>": ("<li>Sojasauce</li>", "<li>Sojazooss</li>"),
    'A bowl of rice topped with vegetables, meat and an egg, to mix with chilli sauce. <a href="#bibimbap-guide">How to eat it?</a>': (
        'Eine Schüssel Reis mit Gemüse, Fleisch und Ei, die mit Chilisauce vermischt wird. <a href="#bibimbap-guide">Wie isst man das?</a>',
        'Eng Schossel Räis mat Geméis, Fleesch an engem Ee, déi een mat Pikantzooss vermëscht. <a href="#bibimbap-guide">Wéi iesst een dat?</a>'),
    "Slow-cooked soups, stir-fries and fried chicken, served with rice or soup.": (
        "Lange gekochte Suppen, Pfannengerichte und Brathähnchen, serviert mit Reis oder Suppe.",
        "Laang gekachten Zoppen, gebroden Platen a Poulet frit, mat Räis oder Zopp."),
    "Marinated and fermented vegetables, to share or take away.": (
        "Eingelegtes und fermentiertes Gemüse, zum Teilen oder Mitnehmen.",
        "Agemaacht a fermentéiert Geméis, fir ze deelen oder matzehuelen."),

    # Boissons
    "<h4>Korean drinks</h4>": ("<h4>Koreanische Getränke</h4>", "<h4>Koreanesch Gedrénks</h4>"),
    "<h4>Japanese teas</h4>": ("<h4>Japanische Tees</h4>", "<h4>Japanesch Téien</h4>"),
    "<h4>Soft drinks</h4>": ("<h4>Erfrischungsgetränke</h4>", "<h4>Softdrinks</h4>"),
    'Japanese roasted tea<small lang="ja-Latn">Hojicha</small>': (
        'Gerösteter japanischer Tee<small lang="ja-Latn">Hojicha</small>', 'Geréischtert japanesch Téi<small lang="ja-Latn">Hojicha</small>'),
    'Japanese green tea<small lang="ja-Latn">Sencha</small>': (
        'Japanischer Grüntee<small lang="ja-Latn">Sencha</small>', 'Japanesche gréngen Téi<small lang="ja-Latn">Sencha</small>'),
    "Lipton Ice Tea peach": ("Lipton Ice Tea Pfirsich", "Lipton Ice Tea Piisch"),

    # Allergènes
    '<span>Allergens</span><span aria-hidden="true">1 – 12</span>': (
        '<span>Allergene</span><span aria-hidden="true">1 – 12</span>', '<span>Allergenen</span><span aria-hidden="true">1 – 12</span>'),
    "The numbers under each dish refer to the allergens below. Any questions? Our team will be happy to help.": (
        "Die Nummern unter jedem Gericht verweisen auf die folgenden Allergene. Fragen? Unser Team hilft Ihnen gern.",
        "D'Nummeren ënner all Plat verweisen op dës Allergenen. Froen? Eis Equipe hëlleft Iech gär."),
    "<b>1.</b> Gluten</span>": ("<b>1.</b> Gluten</span>", "<b>1.</b> Gluten</span>"),
    "<b>2.</b> Crustaceans</span>": ("<b>2.</b> Krebstiere</span>", "<b>2.</b> Krustendéieren</span>"),
    "<b>3.</b> Eggs</span>": ("<b>3.</b> Eier</span>", "<b>3.</b> Eeër</span>"),
    "<b>4.</b> Fish</span>": ("<b>4.</b> Fisch</span>", "<b>4.</b> Fësch</span>"),
    "<b>5.</b> Peanuts</span>": ("<b>5.</b> Erdnüsse</span>", "<b>5.</b> Äerdnëss</span>"),
    "<b>6.</b> Soy</span>": ("<b>6.</b> Soja</span>", "<b>6.</b> Soja</span>"),
    "<b>7.</b> Milk &amp; lactose</span>": ("<b>7.</b> Milch &amp; Laktose</span>", "<b>7.</b> Mëllech &amp; Laktos</span>"),
    "<b>8.</b> Tree nuts</span>": ("<b>8.</b> Schalenfrüchte</span>", "<b>8.</b> Nëss</span>"),
    "<b>9.</b> Celery</span>": ("<b>9.</b> Sellerie</span>", "<b>9.</b> Zelleri</span>"),
    "<b>10.</b> Mustard</span>": ("<b>10.</b> Senf</span>", "<b>10.</b> Moschter</span>"),
    "<b>11.</b> Sesame</span>": ("<b>11.</b> Sesam</span>", "<b>11.</b> Sesam</span>"),
    "<b>12.</b> Sulphites</span>": ("<b>12.</b> Sulfite</span>", "<b>12.</b> Sulfitter</span>"),

    # Comment manger le bibimbap
    "“Bibim” means <em>mixing</em> and “bap” means <em>rice</em>. The secret: mix everything before you dig in!": (
        "„Bibim“ bedeutet <em>mischen</em> und „bap“ <em>Reis</em>. Das Geheimnis: vor dem Essen alles gut vermischen!",
        "„Bibim“ heescht <em>mëschen</em> an „bap“ <em>Räis</em>. D'Geheimnis: alles gutt mëschen, ier een iesst!"),
    "<strong>Add the chilli sauce</strong><span>A little or a lot of gochujang, to taste.</span>": (
        "<strong>Chilisauce hinzufügen</strong><span>Je nach Geschmack wenig oder viel Gochujang.</span>",
        "<strong>Pikantzooss derbäi</strong><span>No Loscht e bëssen oder vill Gochujang.</span>"),
    "<strong>Mix everything together</strong><span>Rice, vegetables, meat and egg: everything should be well coated.</span>": (
        "<strong>Alles gut vermischen</strong><span>Reis, Gemüse, Fleisch und Ei: Alles sollte gut umhüllt sein.</span>",
        "<strong>Alles gutt mëschen</strong><span>Räis, Geméis, Fleesch an Ee: alles soll gutt mat der Zooss iwwerzu sinn.</span>"),
    "<strong>Enjoy!</strong><span>Time to savour a moment of simple happiness.</span>": (
        "<strong>Guten Appetit!</strong><span>Zeit, diesen Moment einfachen Glücks zu genießen.</span>",
        "<strong>Gudden Appetit!</strong><span>Elo ass et Zäit, dëse Moment vu klengem Gléck ze genéissen.</span>"),
    "▶ Watch the demo": ("▶ Demo ansehen", "▶ Demo kucken"),
    ">Choose my bibimbap</a>": (">Meinen Bibimbap wählen</a>", ">Mäi Bibimbap auswielen</a>"),
    "</span>Did you know?</span>": ("</span>Schon gewusst?</span>", "</span>Wosst Dir?</span>"),
    '<p class="nurungji-tip__title"><span lang="ko">누룽지</span> · Nurungji</p>': (
        '<p class="nurungji-tip__title"><span lang="ko">누룽지</span> · Nurungji</p>',
        '<p class="nurungji-tip__title"><span lang="ko">누룽지</span> · Nurungji</p>'),
    "<p>In the sizzling stone bowl, the rice at the bottom turns golden and crispy. In Korea it’s often the favourite part: people scrape it up with their spoon down to the very last bite!</p>": (
        "<p>In der heißen Steinschüssel wird der Reis am Boden goldbraun und knusprig. In Korea ist das oft der beliebteste Teil: Man kratzt ihn bis zum letzten Bissen mit dem Löffel heraus!</p>",
        "<p>Am brennegwaarme Steendëppen gëtt de Räis um Buedem gëllen a knusprech. A Korea ass dat dacks dat Beléifsten: Et kraazt een en bis zum leschte Bëssen mam Läffel eraus!</p>"),
    '<p class="nurungji-tip__hint">Try it with our stone-pot bibimbaps, no. 8 and no. 9.</p>': (
        '<p class="nurungji-tip__hint">Probieren Sie es mit unseren Bibimbaps im Steintopf, Nr. 8 und Nr. 9.</p>',
        '<p class="nurungji-tip__hint">Probéiert et mat eise Bibimbape am Steendëppen, Nr. 8 an Nr. 9.</p>'),

    # Modale avant appel
    '<h2 id="call-dialog-title">Before you call</h2>': (
        '<h2 id="call-dialog-title">Bevor Sie anrufen</h2>', '<h2 id="call-dialog-title">Ier Dir urufft</h2>'),
    '<p id="call-dialog-text">We only speak English, Korean and a little French. Please keep this in mind before calling. Thank you!</p>': (
        '<p id="call-dialog-text">Wir sprechen nur Englisch, Koreanisch und ein wenig Französisch. Bitte berücksichtigen Sie das vor Ihrem Anruf. Danke!</p>',
        '<p id="call-dialog-text">Mir schwätzen nëmmen Englesch, Koreanesch an e bëssi Franséisch. Denkt w.e.g. drun, ier Dir urufft. Merci!</p>'),
    'aria-label="Languages spoken"': ('aria-label="Gesprochene Sprachen"', 'aria-label="Geschwate Sproochen"'),
    "</span> <small>(a little)</small>": ("</span> <small>(ein wenig)</small>", "</span> <small>(e bëssi)</small>"),
    '<span>Call <span class="tel-num">+352 28 99 61 11</span></span>': (
        '<span><span class="tel-num">+352 28 99 61 11</span> anrufen</span>',
        '<span><span class="tel-num">+352 28 99 61 11</span> uruffen</span>'),
    'id="call-dialog-cancel">Cancel</button>': ('id="call-dialog-cancel">Abbrechen</button>', 'id="call-dialog-cancel">Ofbriechen</button>'),

    # Bannière d'installation (iOS n'existe pas en luxembourgeois : libellés allemands)
    '<p class="install-banner__title" id="install-title">Yanji’s menu in your pocket?</p>': (
        '<p class="install-banner__title" id="install-title">Die Yanji-Karte in der Hosentasche?</p>',
        '<p class="install-banner__title" id="install-title">D’Yanji-Kaart an der Täsch?</p>'),
    '<p data-install="prompt">Install our app: the menu, opening hours and directions stay available, even offline.</p>': (
        '<p data-install="prompt">Installieren Sie unsere App: Speisekarte, Öffnungszeiten und Anfahrt bleiben verfügbar, auch offline.</p>',
        '<p data-install="prompt">Installéiert eis App: Menü, Ëffnungszäiten an Uweeg bleiwen disponibel, och offline.</p>'),
    "<span>On iPhone: tap</span>": ("<span>Auf dem iPhone: Tippen Sie auf</span>", "<span>Um iPhone: Tippt op</span>"),
    "<span>“Share”, then “Add to Home Screen”.</span>": (
        "<span>„Teilen“ und dann auf „Zum Home-Bildschirm“.</span>",
        "<span>„Teilen“ an duerno op „Zum Home-Bildschirm“.</span>"),
    'id="install-accept" data-install="prompt">Install</button>': (
        'id="install-accept" data-install="prompt">Installieren</button>', 'id="install-accept" data-install="prompt">Installéieren</button>'),
    'id="install-dismiss">Not now</button>': ('id="install-dismiss">Später</button>', 'id="install-dismiss">Méi spéit</button>'),

    # Horaires & accès
    "</span> Opening hours</h3>": ("</span> Öffnungszeiten</h3>", "</span> Ëffnungszäiten</h3>"),
    "Opening hours": ("Öffnungszeiten", "Ëffnungszäiten"),
    '<th scope="row">Monday</th>': ('<th scope="row">Montag</th>', '<th scope="row">Méindeg</th>'),
    '<th scope="row">Tuesday</th>': ('<th scope="row">Dienstag</th>', '<th scope="row">Dënschdeg</th>'),
    '<th scope="row">Wednesday</th>': ('<th scope="row">Mittwoch</th>', '<th scope="row">Mëttwoch</th>'),
    '<th scope="row">Thursday</th>': ('<th scope="row">Donnerstag</th>', '<th scope="row">Donneschdeg</th>'),
    '<th scope="row">Friday</th>': ('<th scope="row">Freitag</th>', '<th scope="row">Freideg</th>'),
    '<th scope="row">Saturday</th>': ('<th scope="row">Samstag</th>', '<th scope="row">Samschdeg</th>'),
    '<th scope="row">Sunday</th><td>Closed</td>': (
        '<th scope="row">Sonntag</th><td>Geschlossen</td>', '<th scope="row">Sonndeg</th><td>Zou</td>'),
    "</span> Contact</h3>": ("</span> Kontakt</h3>", "</span> Kontakt</h3>"),
    "<strong>Phone</strong>": ("<strong>Telefon</strong>", "<strong>Telefon</strong>"),
    "<strong>Address</strong>": ("<strong>Adresse</strong>", "<strong>Adress</strong>"),
    "<strong>Getting here</strong>Gare district, a few minutes’ walk from the central station and the tram.": (
        "<strong>Anfahrt</strong>Bahnhofsviertel, wenige Gehminuten vom Hauptbahnhof und der Tram entfernt.",
        "<strong>Uweeg</strong>Garer Quartier, e puer Minutten zu Fouss vun der Gare an dem Tram."),
    "Directions on Google Maps": ("Route in Google Maps", "Wee op Google Maps"),
    " (new window)": (" (neues Fenster)", " (nei Fënster)"),

    # Pied de page
    "<p>Monday – Saturday<br>": ("<p>Montag – Samstag<br>", "<p>Méindeg – Samschdeg<br>"),
    "<p>Sunday: closed</p>": ("<p>Sonntag: geschlossen</p>", "<p>Sonndes: zou</p>"),
    "Illustrative photos from": ("Beispielfotos von", "Beispillfotoe vu"),
    "(CC BY / CC BY-SA licences, see each file for the author).": (
        "(Lizenzen CC BY / CC BY-SA, Urheber siehe jeweilige Datei).",
        "(Lizenzen CC BY / CC BY-SA, den Auteur steet bei all Fichier)."),
    "\n        Website by <a": ("\n        Website von <a", "\n        Websäit vun <a"),
    "\n        Website accessibility by <a": ("\n        Barrierefreiheit von <a", "\n        Accessibilitéit vun <a"),

    # Mentions légales & confidentialité
    "<summary>Legal notice &amp; privacy<svg": ("<summary>Impressum &amp; Datenschutz<svg", "<summary>Impressum &amp; Dateschutz<svg"),
    "</svg>Hide dishes containing an allergen…<svg": (
        "</svg>Gerichte mit einem bestimmten Allergen ausblenden…<svg", "</svg>Platen mat engem Allergen verstoppen…<svg"),
    ", San Francisco, CA 94107, USA</dd>": (", San Francisco, CA 94107, USA</dd>", ", San Francisco, CA 94107, USA</dd>"),
    '<h2 id="legal-title">Legal notice</h2>': ('<h2 id="legal-title">Impressum</h2>', '<h2 id="legal-title">Impressum</h2>'),
    "<dt>Publisher</dt>": ("<dt>Betreiber</dt>", "<dt>Bedreiwer</dt>"),
    "<dt>Contact</dt>": ("<dt>Kontakt</dt>", "<dt>Kontakt</dt>"),
    "<dt>Trade register (RCS)</dt>": ("<dt>Handelsregister (RCS)</dt>", "<dt>Handelsregister (RCS)</dt>"),
    "<dt>VAT number</dt>": ("<dt>USt-IdNr.</dt>", "<dt>TVA-Nummer</dt>"),
    "<dt>Business permit</dt>": ("<dt>Niederlassungsgenehmigung</dt>", "<dt>Geschäftserlaabnes</dt>"),
    "<dt>Hosting</dt>": ("<dt>Hosting</dt>", "<dt>Hosting</dt>"),
    "<dt>Design and development</dt>": ("<dt>Gestaltung und Umsetzung</dt>", "<dt>Konzeptioun a Realisatioun</dt>"),
    '<h2 id="privacy-title">Privacy</h2>': ('<h2 id="privacy-title">Datenschutz</h2>', '<h2 id="privacy-title">Dateschutz</h2>'),
    "<li>This website sets no cookies and uses no analytics or advertising tools.</li>": (
        "<li>Diese Website setzt keine Cookies und verwendet keine Statistik- oder Werbetools.</li>",
        "<li>Dëse Site setzt keng Cookien a benotzt keng Statistik- oder Reklammstools.</li>"),
    "<li>It contains no forms: we collect no personal data through it.</li>": (
        "<li>Sie enthält keine Formulare: Wir erheben darüber keine personenbezogenen Daten.</li>",
        "<li>Hien huet keng Formulairen: Mir sammelen doriwwer keng perséinlech Donnéeën.</li>"),
    "<li>If you pause the animations, this choice is stored only in your browser and is never sent anywhere.</li>": (
        "<li>Wenn Sie die Animationen anhalten, wird diese Wahl nur in Ihrem Browser gespeichert und nie übertragen.</li>",
        "<li>Wann Dir d'Animatiounen stoppt, gëtt dës Wiel nëmmen an Ärem Browser gespäichert a ni iwwerdroen.</li>"),
    "<li>Fonts are hosted on this website: no data is sent to Google Fonts.</li>": (
        "<li>Die Schriftarten werden auf dieser Website gehostet: Es werden keine Daten an Google Fonts gesendet.</li>",
        "<li>D'Schrëften ginn op dësem Site gehost: Et ginn keng Donnéeën un Google Fonts geschéckt.</li>"),
    "<li>Illustrative photos are loaded from Wikimedia Commons, which therefore receives your IP address.</li>": (
        "<li>Die Beispielfotos werden von Wikimedia Commons geladen, das dabei Ihre IP-Adresse erhält.</li>",
        "<li>D'Beispillfotoe ginn vu Wikimedia Commons gelueden, dat dobäi Är IP-Adress kritt.</li>"),
    "<li>The “Directions on Google Maps” button opens a Google service, subject to its own privacy policy.</li>": (
        "<li>Die Schaltfläche „Route in Google Maps“ öffnet einen Dienst von Google, für den dessen eigene Datenschutzerklärung gilt.</li>",
        "<li>De Knäppchen „Wee op Google Maps“ mécht e Service vu Google op, fir deen seng eege Dateschutzerklärung gëllt.</li>"),
    "<li>The website is hosted by GitHub (United States), which may keep technical logs (IP address, date, page visited) to keep the service secure.</li>": (
        "<li>Die Website wird von GitHub (USA) gehostet, das zur Sicherheit des Dienstes technische Protokolle (IP-Adresse, Datum, aufgerufene Seite) speichern kann.</li>",
        "<li>De Site gëtt vu GitHub (USA) gehost, dat fir d'Sécherheet vum Service technesch Protokoller (IP-Adress, Datum, besicht Säit) späichere kann.</li>"),
    '<li>For any question about your data, write to us at the address above. You can also file a complaint with the <a href="https://cnpd.public.lu/" lang="fr">Commission nationale pour la protection des données (CNPD)</a>, Luxembourg’s data protection authority.</li>': (
        '<li>Bei Fragen zu Ihren Daten schreiben Sie uns an die oben genannte Adresse. Sie können auch eine Beschwerde bei der <a href="https://cnpd.public.lu/" lang="fr">Commission nationale pour la protection des données (CNPD)</a>, der luxemburgischen Datenschutzbehörde, einreichen.</li>',
        '<li>Fir all Fro iwwer Är Donnéeë schreift eis op déi uewe genannten Adress. Dir kënnt och eng Plainte bei der <a href="https://cnpd.public.lu/" lang="fr">Commission nationale pour la protection des données (CNPD)</a> maachen, der Lëtzebuerger Dateschutzautoritéit.</li>'),

    # Données structurées
    '"name": "Menu"': ('"name": "Speisekarte"', '"name": "Menü"'),
    '"name": "Kimbap",': ('"name": "Kimbap",', '"name": "Kimbap",'),
    '"name": "Bibimbap",': ('"name": "Bibimbap",', '"name": "Bibimbap",'),
    '"name": "Specialities"': ('"name": "Spezialitäten"', '"name": "Spezialitéiten"'),
    '"name": "Kimchi & side dishes"': ('"name": "Kimchi & Beilagen"', '"name": "Kimchi & Bäilagen"'),
    '"name": "Kimchi (pickled cabbage)"': ('"name": "Kimchi (eingelegter Kohl)"', '"name": "Kimchi (agemaachte Kabes)"'),
    '"name": "Pickled radish"': ('"name": "Eingelegter Rettich"', '"name": "Agemaachte Rettech"'),
    '"name": "Pickled bellflower root"': ('"name": "Eingelegte Ballonblumenwurzel"', '"name": "Agemaachte Doraji-Wuerzel"'),
    '"name": "Pickled Korean fern"': ('"name": "Eingelegter koreanischer Farn"', '"name": "Agemaachte koreanesche Farn"'),
    '"Choice of 3 flavours: Korean sweet & spicy, honey mustard, soy sauce"': (
        '"3 Geschmacksrichtungen zur Wahl: koreanisch süß & scharf, Honig-Senf, Sojasauce"',
        '"3 Goûten zur Auswiel: koreanesch séiss & schaarf, Hunneg-Moschter, Sojazooss"'),
    '. Served with soup"': ('. Mit Suppe serviert"', '. Mat Zopp"'),
    '. In a stone pot, with soup"': ('. Im Steintopf, mit Suppe"', '. Am Steendëppen, mat Zopp"'),
    '. Served with rice"': ('. Mit Reis serviert"', '. Mat Räis"'),
    '. Served with soup and kimchi"': ('. Mit Suppe und Kimchi serviert"', '. Mat Zopp a Kimchi"'),
    '"servesCuisine": ["Korean"]': ('"servesCuisine": ["Koreanisch", "Korean"]', '"servesCuisine": ["Koreanesch", "Korean"]'),
}

# --- Plats : nom anglais -> (allemand, luxembourgeois) ---
DISHES = {
    "Beef tendon roll": ("Rolle mit Rindersehne", "Roll mat Rannersehn"),
    "Tuna & kimchi roll": ("Rolle mit Thunfisch & Kimchi", "Roll mat Thon & Kimchi"),
    "Beef & sausage roll": ("Rolle mit Rind & Wurst", "Roll mat Rëndfleesch & Wurscht"),
    "Teriyaki chicken & cheese roll": ("Rolle mit Teriyaki-Hähnchen & Käse", "Roll mat Teriyaki-Poulet & Kéis"),
    "Vegetarian seaweed roll": ("Vegetarische Algenrolle", "Vegetaresch Algenroll"),
    "Kimchi & pork bibimbap": ("Bibimbap mit Kimchi & Schweinefleisch", "Bibimbap mat Kimchi & Schwéngefleesch"),
    "Teriyaki chicken bibimbap": ("Bibimbap mit Teriyaki-Hähnchen", "Bibimbap mat Teriyaki-Poulet"),
    "Vegetarian bibimbap": ("Vegetarischer Bibimbap", "Vegetaresche Bibimbap"),
    "Beef bibimbap": ("Bibimbap mit Rindfleisch", "Bibimbap mat Rëndfleesch"),
    "Beef soup": ("Rindfleischsuppe", "Rëndfleeschzopp"),
    "Korean spicy beef soup": ("Scharfe koreanische Rindfleischsuppe", "Schaarf koreanesch Rëndfleeschzopp"),
    "Beef gyudon": ("Gyudon mit Rindfleisch", "Gyudon mat Rëndfleesch"),
    "Tteokbokki": ("Tteokbokki", "Tteokbokki"),
    "Kimchi, pork & tuna soup": ("Kimchi-Suppe mit Schweinefleisch & Thunfisch", "Kimchizopp mat Schwéngefleesch & Thon"),
    "Korean fried chicken": ("Koreanisches Brathähnchen", "Koreanesche Poulet frit"),
}

# --- Ingrédients : anglais -> (allemand, luxembourgeois) ---
DESCRIPTIONS = {
    "Beef tendon, pork sausage, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise": (
        "Rindersehne, Schweinewurst, eingelegter gelber Rettich, Ei, Gurke, Karotte, Algen, Sesam, Sesamöl, Mayonnaise",
        "Rannersehn, Schwéngswurscht, agemaachte giele Rettech, Ee, Kombier, Muert, Algen, Sesam, Sesamueleg, Mayonnaise"),
    "Cooked tuna, kimchi, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise": (
        "Gekochter Thunfisch, Kimchi, eingelegter gelber Rettich, Ei, Gurke, Karotte, Algen, Sesam, Sesamöl, Mayonnaise",
        "Gekachten Thon, Kimchi, agemaachte giele Rettech, Ee, Kombier, Muert, Algen, Sesam, Sesamueleg, Mayonnaise"),
    "Beef, sausage, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise": (
        "Rindfleisch, Wurst, eingelegter gelber Rettich, Ei, Gurke, Karotte, Algen, Sesam, Sesamöl, Mayonnaise",
        "Rëndfleesch, Wurscht, agemaachte giele Rettech, Ee, Kombier, Muert, Algen, Sesam, Sesamueleg, Mayonnaise"),
    "Teriyaki chicken, cheese, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise": (
        "Teriyaki-Hähnchen, Käse, eingelegter gelber Rettich, Ei, Gurke, Karotte, Algen, Sesam, Sesamöl, Mayonnaise",
        "Teriyaki-Poulet, Kéis, agemaachte giele Rettech, Ee, Kombier, Muert, Algen, Sesam, Sesamueleg, Mayonnaise"),
    "Mushrooms, cucumber, carrot, pickled yellow radish, sesame, sesame oil, seaweed": (
        "Pilze, Gurke, Karotte, eingelegter gelber Rettich, Sesam, Sesamöl, Algen",
        "Champignonen, Kombier, Muert, agemaachte giele Rettech, Sesam, Sesamueleg, Algen"),
    "Kimchi, pork, seaweed, egg": ("Kimchi, Schweinefleisch, Algen, Ei", "Kimchi, Schwéngefleesch, Algen, Ee"),
    "Grated carrot, spinach, courgette, bean sprouts, sweetcorn, mushrooms, chicken, egg": (
        "Geraspelte Karotte, Spinat, Zucchini, Sojasprossen, Mais, Pilze, Hähnchen, Ei",
        "Gerappte Muert, Spinat, Zucchini, Sojakäimen, Mais, Champignonen, Poulet, Ee"),
    "Grated carrot, spinach, courgette, bracken fern, kimchi, mushrooms, bean sprouts, seaweed, egg": (
        "Geraspelte Karotte, Spinat, Zucchini, Adlerfarn, Kimchi, Pilze, Sojasprossen, Algen, Ei",
        "Gerappte Muert, Spinat, Zucchini, Farn, Kimchi, Champignonen, Sojakäimen, Algen, Ee"),
    "Grated carrot, spinach, courgette, bracken fern, kimchi, mushrooms, bean sprouts, minced beef, egg": (
        "Geraspelte Karotte, Spinat, Zucchini, Adlerfarn, Kimchi, Pilze, Sojasprossen, Rinderhack, Ei",
        "Gerappte Muert, Spinat, Zucchini, Farn, Kimchi, Champignonen, Sojakäimen, gehackt Rëndfleesch, Ee"),
    "Beef, rice noodles, tofu, onion, egg": ("Rindfleisch, Reisnudeln, Tofu, Zwiebel, Ei", "Rëndfleesch, Räisnuddelen, Tofu, Ënn, Ee"),
    "Beef, rice noodles, tofu, bean sprouts, fern, onion, mushrooms, egg": (
        "Rindfleisch, Reisnudeln, Tofu, Sojasprossen, Farn, Zwiebel, Pilze, Ei",
        "Rëndfleesch, Räisnuddelen, Tofu, Sojakäimen, Farn, Ënn, Champignonen, Ee"),
    "Rice, egg, beef, onion, ginger": ("Reis, Ei, Rindfleisch, Zwiebel, Ingwer", "Räis, Ee, Rëndfleesch, Ënn, Ingwer"),
    "Stir-fried rice cakes, fish cake, white cabbage, egg, cheese": (
        "Gebratene Reiskuchen, Fischkuchen, Weißkohl, Ei, Käse",
        "Gebroden Räiskuchen, Fëschkuchen, wäisse Kabes, Ee, Kéis"),
    "Kimchi, tofu, pork, onion, tuna": ("Kimchi, Tofu, Schweinefleisch, Zwiebel, Thunfisch", "Kimchi, Tofu, Schwéngefleesch, Ënn, Thon"),
}

# --- Kimchi & accompagnements : nom anglais -> (de, de petit texte, lb, lb petit texte) ---
SIDES = {
    "Kimchi": ("Kimchi", "Eingelegter Kohl", "Kimchi", "Agemaachte Kabes"),
    "Pickled radish": ("Eingelegter Rettich", "Rettichwürfel", "Agemaachte Rettech", "Rettechwierfelen"),
    "Pickled bellflower root": ("Eingelegte Ballonblumenwurzel", "Doraji", "Agemaachte Doraji-Wuerzel", "Doraji"),
    "Pickled Korean fern": ("Eingelegter koreanischer Farn", "Gosari", "Agemaachte koreanesche Farn", "Gosari"),
}
SPICY = ("scharf", "schaarf")

# --- Jus coréens : anglais -> (allemand, luxembourgeois) ---
JUICES = {
    "Pear juice": ("Birnensaft", "Bierejus"),
    "Peach juice": ("Pfirsichsaft", "Piischejus"),
    "Grape juice": ("Traubensaft", "Drauwejus"),
}

# --- Titres de section : anglais -> (allemand, luxembourgeois) ---
SECTION_TITLES = {
    "Our menu": ("Speisekarte", "Menü"),
    "Kimbap": ("Kimbap", "Kimbap"),
    "Bibimbap": ("Bibimbap", "Bibimbap"),
    "Specialities": ("Spezialitäten", "Spezialitéiten"),
    "Kimchi": ("Kimchi", "Kimchi"),
    "Drinks": ("Getränke", "Gedrénks"),
    "How to eat bibimbap?": ("Wie isst man Bibimbap?", "Wéi iesst een Bibimbap?"),
    "Hours &amp; location": ("Öffnungszeiten &amp; Anfahrt", "Ëffnungszäiten &amp; Uweeg"),
}

# --- Textes du JavaScript ---
JS_T = {
    "de": """    var T = {
      openMenu: 'Menü öffnen',
      closeMenu: 'Menü schließen',
      openSoon: 'Geöffnet · schließt bald (17:30)',
      openNow: 'Jetzt geöffnet · bis 17:30',
      closedToday: 'Geschlossen · öffnet um 11:00',
      closedTomorrow: 'Geschlossen · öffnet morgen um 11:00',
      closedMonday: 'Geschlossen · öffnet Montag um 11:00',
      today: ' · heute',
      allergens: 'Allergene:',
      notVeg: 'nicht vegetarisch',
      spicy: 'scharf',
      contains: 'enthält: ',
      count: function (n) { return n + (n > 1 ? ' Gerichte passen' : ' Gericht passt'); },
      replay: '↺ Demo wiederholen',
      updateMsg: 'Eine neue Version der Website ist verfügbar.',
      updateBtn: 'Aktualisieren'
    };""",
    "lb": """    var T = {
      openMenu: 'Menü opmaachen',
      closeMenu: 'Menü zoumaachen',
      openSoon: 'Op · mécht geschwënn zou (17:30)',
      openNow: 'Elo op · bis 17:30',
      closedToday: 'Zou · mécht um 11:00 op',
      closedTomorrow: 'Zou · mécht muer um 11:00 op',
      closedMonday: 'Zou · mécht e Méindeg um 11:00 op',
      today: ' · haut',
      allergens: 'Allergenen:',
      notVeg: 'net vegetaresch',
      spicy: 'schaarf',
      contains: 'enthält: ',
      count: function (n) { return n + (n > 1 ? ' Platen passen' : ' Plat passt'); },
      replay: '↺ Demo nach eng Kéier',
      updateMsg: 'Eng nei Versioun vum Site ass disponibel.',
      updateBtn: 'Aktualiséieren'
    };""",
}

MANIFEST_TEXT = {
    "de": "Koreanisches Restaurant am Bahnhof Luxemburg: Speisekarte, Öffnungszeiten und Anfahrt, auch offline.",
    "lb": "Koreanescht Restaurant bei der Gare zu Lëtzebuerg: Menü, Ëffnungszäiten an Uweeg, och offline.",
}
