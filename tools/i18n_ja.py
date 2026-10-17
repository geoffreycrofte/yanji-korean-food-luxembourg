"""
Traductions japonaises (ja), utilisées par build-i18n.py.

Comme pour tools/i18n_de_lb.py, chaque entrée est indexée par la version
ANGLAISE du fragment (colonne « en » de build-i18n.py). Si vous modifiez un
texte anglais dans build-i18n.py, mettez à jour la clé correspondante ici : le
build s'arrête et indique les fragments sans traduction.
Les {{variables}} (horaires, téléphone) viennent de infos.md : les garder telles quelles.
"""

# --- Fragments de texte : anglais -> japonais ---
ROWS = {
    # <head>
    "<title>Yanji Korean Food – Korean restaurant near Luxembourg station | Kimbap, Bibimbap</title>":
        "<title>Yanji Korean Food – ルクセンブルク駅近くの韓国料理店 | キンパ、ビビンバ</title>",
    "Yanji Korean Food, a small Korean restaurant at 63 avenue de la Gare, Luxembourg. Kimbap, stone-pot bibimbap, tteokbokki, spicy soups and Korean fried chicken. Open Monday to Saturday, {{open}}–{{close}}.":
        "Yanji Korean Food は、ルクセンブルクの avenue de la Gare 63 番地にある小さな韓国料理店です。キンパ、石焼ビビンバ、トッポッキ、辛いスープ、韓国風フライドチキン。月曜〜土曜 {{open}}–{{close}} 営業。",
    "Korean restaurant Luxembourg, Korean food Luxembourg, kimbap, bibimbap, tteokbokki, Korean fried chicken, avenue de la Gare, Luxembourg station, Yanji":
        "ルクセンブルク 韓国料理店, ルクセンブルク 韓国料理, キンパ, ビビンバ, トッポッキ, 韓国風フライドチキン, avenue de la Gare, ルクセンブルク駅, Yanji, 延吉",
    'content="Yanji Korean Food – Korean restaurant near Luxembourg station"':
        'content="Yanji Korean Food – ルクセンブルク駅近くの韓国料理店"',
    "Kimbap, stone-pot bibimbap, tteokbokki and Korean fried chicken. 63 avenue de la Gare, Luxembourg. Mon–Sat {{open}}–{{close}}.":
        "キンパ、石焼ビビンバ、トッポッキ、韓国風フライドチキン。ルクセンブルク avenue de la Gare 63。月〜土 {{open}}–{{close}}。",

    # En-tête
    "Skip to content": "本文へスキップ",
    '<span class="visually-hidden"> Korean Food – home</span>': '<span class="visually-hidden"> Korean Food – ホーム</span>',
    'aria-label="Main navigation"': 'aria-label="メインナビゲーション"',
    '<li><a href="#menu">Menu</a></li>': '<li><a href="#menu">メニュー</a></li>',
    '<li><a href="#bibimbap-guide">Bibimbap</a></li>': '<li><a href="#bibimbap-guide">ビビンバ</a></li>',
    '<li><a href="#infos">Hours &amp; location</a></li>': '<li><a href="#infos">営業時間・アクセス</a></li>',
    "Pause animations": "アニメーションを一時停止",
    "\n        Call\n": "\n        電話する\n",
    'aria-label="Call Yanji Korean Food"': 'aria-label="Yanji Korean Food に電話する"',
    'aria-label="Open menu"': 'aria-label="メニューを開く"',

    # Hero
    '<span class="visually-hidden"> – Korean restaurant near Luxembourg station</span>':
        '<span class="visually-hidden"> – ルクセンブルク駅近くの韓国料理店</span>',
    "Freshly rolled kimbap, stone-pot bibimbap, spicy soups and Korean fried chicken, a short walk from Luxembourg station.":
        "巻きたてのキンパ、石焼ビビンバ、辛いスープ、韓国風フライドチキン。ルクセンブルク駅からすぐです。",
    "Mon – Sat · {{open}} – {{close}}": "月 – 土 · {{open}} – {{close}}",
    ">See the menu</a>": ">メニューを見る</a>",
    ">Find us</a>": ">アクセス</a>",
    'Flavours of Korea<small lang="ko">한국의 맛</small>': '韓国の味<small lang="ko">한국의 맛</small>',
    'Made with love<small lang="ko">사랑을 담아</small>': '愛情をこめて<small lang="ko">사랑을 담아</small>',
    'Served piping hot<small lang="ko">따뜻하게</small>': 'あつあつでどうぞ<small lang="ko">따뜻하게</small>',

    # Bandeau défilant (décoratif)
    'marquee__item">Kimbap <': 'marquee__item">キンパ <',
    'marquee__item">Bibimbap <': 'marquee__item">ビビンバ <',
    'marquee__item">Tteokbokki <': 'marquee__item">トッポッキ <',
    'marquee__item">Fried chicken <': 'marquee__item">フライドチキン <',
    'marquee__item">Kimchi <': 'marquee__item">キムチ <',
    'marquee__item">Gyudon <': 'marquee__item">牛丼 <',
    'marquee__item">Spicy soup <': 'marquee__item">ユッケジャン <',

    # À propos
    "Small menu, <em>big heart</em>": "小さなメニューに、<em>大きな真心</em>",
    "At Yanji, we serve simple, generous Korean food in the heart of Luxembourg’s Gare district. A small menu, a caring team and warming dishes: kimbap, bibimbap, tteokbokki, slow-cooked soups and crispy fried chicken.":
        "Yanji（延吉）では、ルクセンブルクの駅前地区の中心で、素朴でボリュームたっぷりの韓国料理をお出ししています。小さなメニュー、心のこもったおもてなし、そして体が温まる料理：キンパ、ビビンバ、トッポッキ、じっくり煮込んだスープ、カリカリのフライドチキン。",
    "Eat in or take away, for a lunch break or a savoury snack: drop by Monday to Saturday.":
        "店内でもテイクアウトでも。ランチや軽食に、月曜から土曜までお気軽にお立ち寄りください。",
    "<strong>Kimbap</strong><span>5 Korean rolls, including a vegetarian one</span>":
        "<strong>キンパ</strong><span>ベジタリアン向けを含む 5 種類の韓国のり巻き</span>",
    "<strong>Stone pot</strong><span>Sizzling bibimbap, served with soup</span>":
        "<strong>石焼</strong><span>ジュージューの石焼ビビンバ、スープ付き</span>",
    "<strong>Spicy or not</strong><span>Every spicy dish is marked</span>":
        "<strong>辛い？辛くない？</strong><span>辛い料理にはすべて印があります</span>",
    "<strong>Lovely team</strong><span>A warm welcome, promised</span>":
        "<strong>やさしいスタッフ</strong><span>温かくお迎えします</span>",

    # Carte
    "All our dishes are prepared on site. Prices include VAT. Photos are for illustration only.":
        "すべての料理は店内で調理しています。価格は税込みです。写真はイメージです。",
    'aria-label="Menu categories"': 'aria-label="メニューのカテゴリー"',
    '<a href="#kimbap">Kimbap</a>': '<a href="#kimbap">キンパ</a>',
    '<a href="#bibimbap">Bibimbap</a>': '<a href="#bibimbap">ビビンバ</a>',
    '<a href="#specialites">Specialities</a>': '<a href="#specialites">おすすめ料理</a>',
    '<a href="#kimchi">Kimchi</a>': '<a href="#kimchi">キムチ</a>',
    '<a href="#boissons">Drinks</a>': '<a href="#boissons">ドリンク</a>',
    '<a href="#allergenes">Allergens</a>': '<a href="#allergenes">アレルゲン</a>',
    'aria-label="Filter the menu"': 'aria-label="メニューを絞り込む"',
    "Filter:": "絞り込み：",
    "</span>Vegetarian<": "</span>ベジタリアン<",
    "</span>Not spicy<": "</span>辛くない<",
    "For information only: if you have an allergy, please always tell our team.":
        "参考情報です。アレルギーのある方は、必ずスタッフにお知らせください。",
    "Seaweed rolls of sesame-seasoned rice with fillings, sliced.":
        "ごま油で味付けしたご飯と具材をのりで巻き、切り分けた韓国のり巻きです。",
    '<span class="visually-hidden">Dish no. </span>': '<span class="visually-hidden">料理番号 </span>',
    '<span class="visually-hidden">no. </span>': '<span class="visually-hidden">番号 </span>',
    'aria-hidden="true">Illustrative photo</span>': 'aria-hidden="true">イメージ写真</span>',
    "</span>Spicy</span>": "</span>辛い</span>",
    '<span class="tag tag--side">+ soup &amp; kimchi</span>': '<span class="tag tag--side">+ スープ・キムチ</span>',
    '<span class="tag tag--side">+ soup</span>': '<span class="tag tag--side">+ スープ</span>',
    '<span class="tag tag--side">Stone pot + soup</span>': '<span class="tag tag--side">石焼 + スープ</span>',
    '<span class="tag tag--side">+ rice</span>': '<span class="tag tag--side">+ ご飯</span>',
    '<span class="tag tag--side">Choice of 3 flavours</span>': '<span class="tag tag--side">3 種類の味から選択</span>',
    "<li>Korean sweet &amp; spicy <span": "<li>ヤンニョム（甘辛） <span",
    "<li>Honey mustard</li>": "<li>ハニーマスタード</li>",
    "<li>Soy sauce</li>": "<li>醤油</li>",
    'A bowl of rice topped with vegetables, meat and an egg, to mix with chilli sauce. <a href="#bibimbap-guide">How to eat it?</a>':
        'ご飯に野菜、肉、卵をのせ、コチュジャンと混ぜて食べる料理です。<a href="#bibimbap-guide">食べ方は？</a>',
    "Slow-cooked soups, stir-fries and fried chicken, served with rice or soup.":
        "じっくり煮込んだスープ、炒め物、フライドチキン。ご飯またはスープ付きです。",
    "Marinated and fermented vegetables, to share or take away.":
        "漬けて発酵させた野菜のおかず。シェアにもテイクアウトにも。",

    # Boissons
    "<h4>Korean drinks</h4>": "<h4>韓国のドリンク</h4>",
    "<h4>Japanese teas</h4>": "<h4>日本茶</h4>",
    "<h4>Soft drinks</h4>": "<h4>ソフトドリンク</h4>",
    'Japanese roasted tea<small lang="ja-Latn">Hojicha</small>': 'ほうじ茶<small lang="ja-Latn">Hojicha</small>',
    'Japanese green tea<small lang="ja-Latn">Sencha</small>': '煎茶<small lang="ja-Latn">Sencha</small>',
    "Lipton Ice Tea peach": "リプトン アイスティー ピーチ",

    # Allergènes
    '<span>Allergens</span><span aria-hidden="true">1 – 12</span>': '<span>アレルゲン</span><span aria-hidden="true">1 – 12</span>',
    "The numbers under each dish refer to the allergens below. Any questions? Our team will be happy to help.":
        "各料理の下の番号は、以下のアレルゲンを示しています。ご不明な点はお気軽にスタッフへお尋ねください。",
    "<b>1.</b> Gluten</span>": "<b>1.</b> グルテン</span>",
    "<b>2.</b> Crustaceans</span>": "<b>2.</b> 甲殻類</span>",
    "<b>3.</b> Eggs</span>": "<b>3.</b> 卵</span>",
    "<b>4.</b> Fish</span>": "<b>4.</b> 魚</span>",
    "<b>5.</b> Peanuts</span>": "<b>5.</b> 落花生</span>",
    "<b>6.</b> Soy</span>": "<b>6.</b> 大豆</span>",
    "<b>7.</b> Milk &amp; lactose</span>": "<b>7.</b> 乳・乳糖</span>",
    "<b>8.</b> Tree nuts</span>": "<b>8.</b> ナッツ類</span>",
    "<b>9.</b> Celery</span>": "<b>9.</b> セロリ</span>",
    "<b>10.</b> Mustard</span>": "<b>10.</b> マスタード</span>",
    "<b>11.</b> Sesame</span>": "<b>11.</b> ごま</span>",
    "<b>12.</b> Sulphites</span>": "<b>12.</b> 亜硫酸塩</span>",

    # Comment manger le bibimbap
    "“Bibim” means <em>mixing</em> and “bap” means <em>rice</em>. The secret: mix everything before you dig in!":
        "「ビビム」は<em>混ぜる</em>、「パプ」は<em>ご飯</em>という意味。食べる前に全部よく混ぜるのがコツです！",
    "<strong>Add the chilli sauce</strong><span>A little or a lot of gochujang, to taste.</span>":
        "<strong>コチュジャンを入れる</strong><span>お好みで少しでも、たっぷりでも。</span>",
    "<strong>Mix everything together</strong><span>Rice, vegetables, meat and egg: everything should be well coated.</span>":
        "<strong>よく混ぜる</strong><span>ご飯、野菜、肉、卵にたれがよく絡むように。</span>",
    "<strong>Enjoy!</strong><span>Time to savour a moment of simple happiness.</span>":
        "<strong>召し上がれ！</strong><span>ささやかな幸せのひとときをお楽しみください。</span>",
    "▶ Watch the demo": "▶ デモを見る",
    ">Choose my bibimbap</a>": ">ビビンバを選ぶ</a>",

    # Easter egg : nurungji
    "</span>Did you know?</span>": "</span>ご存じですか？</span>",
    '<p class="nurungji-tip__title"><span lang="ko">누룽지</span> · Nurungji</p>':
        '<p class="nurungji-tip__title"><span lang="ko">누룽지</span> · おこげ（ヌルンジ）</p>',
    "<p>In the sizzling stone bowl, the rice at the bottom turns golden and crispy. In Korea it’s often the favourite part: people scrape it up with their spoon down to the very last bite!</p>":
        "<p>熱々の石鍋の底のご飯は、こんがりきつね色のおこげになります。韓国ではここがいちばん人気。最後のひと口までスプーンでこそげてどうぞ！</p>",
    '<p class="nurungji-tip__hint">Try it with our stone-pot bibimbaps, no. 8 and no. 9.</p>':
        '<p class="nurungji-tip__hint">8 番・9 番の石焼ビビンバでお試しください。</p>',

    # Modale avant appel
    '<h2 id="call-dialog-title">Before you call</h2>': '<h2 id="call-dialog-title">お電話の前に</h2>',
    '<p id="call-dialog-text">On the phone, we speak the languages below. Please keep this in mind before calling. Thank you!</p>':
        '<p id="call-dialog-text">お電話では下記の言語で対応いたします。お電話の前にご確認ください。ありがとうございます！</p>',
    'aria-label="Languages spoken"': 'aria-label="対応言語"',
    '<span>Call <span class="tel-num">{{phone}}</span></span>': '<span><span class="tel-num">{{phone}}</span> に電話</span>',
    'id="call-dialog-cancel">Cancel</button>': 'id="call-dialog-cancel">キャンセル</button>',

    # PWA : bannière d'installation
    '<p class="install-banner__title" id="install-title">Yanji’s menu in your pocket?</p>':
        '<p class="install-banner__title" id="install-title">Yanji のメニューをポケットに</p>',
    '<p data-install="prompt">Install our app: the menu, opening hours and directions stay available, even offline.</p>':
        '<p data-install="prompt">アプリをインストールすると、メニュー、営業時間、アクセスをオフラインでも確認できます。</p>',
    "<span>On iPhone: tap</span>": "<span>iPhone の場合：</span>",
    "<span>“Share”, then “Add to Home Screen”.</span>": "<span>「共有」をタップし、「ホーム画面に追加」を選んでください。</span>",
    'id="install-accept" data-install="prompt">Install</button>': 'id="install-accept" data-install="prompt">インストール</button>',
    'id="install-dismiss">Not now</button>': 'id="install-dismiss">あとで</button>',

    # Horaires & accès
    "</span> Opening hours</h3>": "</span> 営業時間</h3>",
    "Opening hours": "営業時間",
    '<th scope="row">Monday</th>': '<th scope="row">月曜日</th>',
    '<th scope="row">Tuesday</th>': '<th scope="row">火曜日</th>',
    '<th scope="row">Wednesday</th>': '<th scope="row">水曜日</th>',
    '<th scope="row">Thursday</th>': '<th scope="row">木曜日</th>',
    '<th scope="row">Friday</th>': '<th scope="row">金曜日</th>',
    '<th scope="row">Saturday</th>': '<th scope="row">土曜日</th>',
    '<th scope="row">Sunday</th><td>Closed</td>': '<th scope="row">日曜日</th><td>定休日</td>',
    "</span> Contact</h3>": "</span> お問い合わせ</h3>",
    "<strong>Phone</strong>": "<strong>電話</strong>",
    "<strong>Email</strong>": "<strong>メール</strong>",
    "<strong>Address</strong>": "<strong>住所</strong>",
    "<strong>Getting here</strong>Gare district, a few minutes’ walk from the central station and the tram.":
        "<strong>アクセス</strong>駅前地区（Gare）、ルクセンブルク中央駅とトラム停留所から徒歩数分です。",
    "Directions on Google Maps": "Google マップで経路を見る",
    " (new window)": "（新しいウィンドウ）",

    # Pied de page
    "<p>Monday – Saturday<br>": "<p>月曜日 – 土曜日<br>",
    "<p>Sunday: closed</p>": "<p>日曜日：定休日</p>",
    "Illustrative photos from": "イメージ写真の出典：",
    "(CC BY / CC BY-SA licences, see each file for the author).": "（CC BY / CC BY-SA ライセンス。作者は各ファイルをご覧ください）。",
    "\n        Website by <a": "\n        ウェブサイト制作：<a",
    "\n        Website accessibility by <a": "\n        ウェブアクセシビリティ：<a",

    # Mentions légales & confidentialité
    "<summary>Legal notice &amp; privacy<svg": "<summary>法的表示・プライバシー<svg",
    "</svg>Hide dishes containing an allergen…<svg": "</svg>特定のアレルゲンを含む料理を非表示…<svg",
    ", San Francisco, CA 94107, USA</dd>": ", San Francisco, CA 94107, アメリカ合衆国</dd>",
    '<h2 id="legal-title">Legal notice</h2>': '<h2 id="legal-title">法的表示</h2>',
    "<dt>Publisher</dt>": "<dt>運営者</dt>",
    "<dt>Contact</dt>": "<dt>連絡先</dt>",
    "<dt>Trade register (RCS)</dt>": "<dt>商業登記番号（RCS）</dt>",
    "<dt>VAT number</dt>": "<dt>付加価値税番号</dt>",
    "<dt>Business permit</dt>": "<dt>営業許可番号</dt>",
    "<dt>Hosting</dt>": "<dt>ホスティング</dt>",
    "<dt>Design and development</dt>": "<dt>デザイン・開発</dt>",
    '<h2 id="privacy-title">Privacy</h2>': '<h2 id="privacy-title">プライバシー</h2>',
    "<li>This website sets no cookies and uses no analytics or advertising tools.</li>":
        "<li>このサイトは Cookie を使用せず、アクセス解析ツールや広告ツールも使用していません。</li>",
    "<li>It contains no forms: we collect no personal data through it.</li>":
        "<li>入力フォームはなく、このサイトを通じて個人情報を収集することはありません。</li>",
    "<li>If you pause the animations, this choice is stored only in your browser and is never sent anywhere.</li>":
        "<li>アニメーションの一時停止設定はお使いのブラウザにのみ保存され、外部に送信されることはありません。</li>",
    "<li>Fonts are hosted on this website: no data is sent to Google Fonts.</li>":
        "<li>フォントはこのサイト上でホストしているため、Google Fonts にデータは送信されません。</li>",
    "<li>Illustrative photos are loaded from Wikimedia Commons, which therefore receives your IP address.</li>":
        "<li>イメージ写真は Wikimedia Commons から読み込まれるため、同サービスにお客様の IP アドレスが送信されます。</li>",
    "<li>The “Directions on Google Maps” button opens a Google service, subject to its own privacy policy.</li>":
        "<li>「Google マップで経路を見る」ボタンは Google のサービスを開きます。同サービスのプライバシーポリシーが適用されます。</li>",
    "<li>The website is hosted by GitHub (United States), which may keep technical logs (IP address, date, page visited) to keep the service secure.</li>":
        "<li>このサイトは GitHub（アメリカ合衆国）でホストされており、GitHub はサービスの安全のために技術ログ（IP アドレス、日時、閲覧ページ）を保管する場合があります。</li>",
    "<li>For any question about your data, write to us at the address above. You can also file a complaint with the <a href=\"https://cnpd.public.lu/\" lang=\"fr\">Commission nationale pour la protection des données (CNPD)</a>, Luxembourg’s data protection authority.</li>":
        "<li>個人データに関するご質問は、上記の連絡先までお寄せください。ルクセンブルクのデータ保護機関である <a href=\"https://cnpd.public.lu/\" lang=\"fr\">Commission nationale pour la protection des données (CNPD)</a> に苦情を申し立てることもできます。</li>",

    # Données structurées
    '"name": "Menu"': '"name": "メニュー"',
    '"name": "Kimbap",': '"name": "キンパ",',
    '"name": "Bibimbap",': '"name": "ビビンバ",',
    '"name": "Specialities"': '"name": "おすすめ料理"',
    '"name": "Kimchi & side dishes"': '"name": "キムチ・おかず"',
    '"name": "Kimchi (pickled cabbage)"': '"name": "白菜キムチ"',
    '"name": "Pickled radish"': '"name": "カクテキ"',
    '"name": "Pickled bellflower root"': '"name": "トラジの和え物"',
    '"name": "Pickled Korean fern"': '"name": "ワラビのナムル"',
    '"Choice of 3 flavours: Korean sweet & spicy, honey mustard, soy sauce"':
        '"3 種類の味から選択：ヤンニョム（甘辛）、ハニーマスタード、醤油"',
    '. Served with soup"': '。スープ付き"',
    '. In a stone pot, with soup"': '。石鍋で提供、スープ付き"',
    '. Served with rice"': '。ご飯付き"',
    '. Served with soup and kimchi"': '。スープ・キムチ付き"',
    '"servesCuisine": ["Korean"]': '"servesCuisine": ["韓国料理", "Korean"]',
}

# --- Plats : nom anglais -> japonais ---
DISHES = {
    "Beef tendon roll": "牛すじキンパ",
    "Tuna & kimchi roll": "ツナキムチキンパ",
    "Beef & sausage roll": "牛肉ソーセージキンパ",
    "Teriyaki chicken & cheese roll": "照り焼きチキンチーズキンパ",
    "Vegetarian seaweed roll": "野菜キンパ",
    "Kimchi & pork bibimbap": "キムチ豚肉ビビンバ",
    "Teriyaki chicken bibimbap": "照り焼きチキンビビンバ",
    "Vegetarian bibimbap": "野菜石焼ビビンバ",
    "Beef bibimbap": "牛肉石焼ビビンバ",
    "Beef soup": "牛肉スープ",
    "Korean spicy beef soup": "ユッケジャン（韓国風辛口牛肉スープ）",
    "Beef gyudon": "牛丼",
    "Tteokbokki": "トッポッキ",
    "Kimchi, pork & tuna soup": "キムチチゲ（豚肉・ツナ）",
    "Korean fried chicken": "韓国風フライドチキン",
}

# --- Ingrédients : anglais -> japonais ---
DESCRIPTIONS = {
    "Beef tendon, pork sausage, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise":
        "牛すじ、豚肉ソーセージ、たくあん、卵、きゅうり、にんじん、のり、ごま、ごま油、マヨネーズ",
    "Cooked tuna, kimchi, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise":
        "加熱したツナ、キムチ、たくあん、卵、きゅうり、にんじん、のり、ごま、ごま油、マヨネーズ",
    "Beef, sausage, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise":
        "牛肉、ソーセージ、たくあん、卵、きゅうり、にんじん、のり、ごま、ごま油、マヨネーズ",
    "Teriyaki chicken, cheese, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise":
        "照り焼きチキン、チーズ、たくあん、卵、きゅうり、にんじん、のり、ごま、ごま油、マヨネーズ",
    "Mushrooms, cucumber, carrot, pickled yellow radish, sesame, sesame oil, seaweed":
        "きのこ、きゅうり、にんじん、たくあん、ごま、ごま油、のり",
    "Kimchi, pork, seaweed, egg": "キムチ、豚肉、のり、卵",
    "Grated carrot, spinach, courgette, bean sprouts, sweetcorn, mushrooms, chicken, egg":
        "千切りにんじん、ほうれん草、ズッキーニ、豆もやし、コーン、きのこ、鶏肉、卵",
    "Grated carrot, spinach, courgette, bracken fern, kimchi, mushrooms, bean sprouts, seaweed, egg":
        "千切りにんじん、ほうれん草、ズッキーニ、ぜんまい、キムチ、きのこ、豆もやし、のり、卵",
    "Grated carrot, spinach, courgette, bracken fern, kimchi, mushrooms, bean sprouts, minced beef, egg":
        "千切りにんじん、ほうれん草、ズッキーニ、ぜんまい、キムチ、きのこ、豆もやし、牛ひき肉、卵",
    "Beef, rice noodles, tofu, onion, egg": "牛肉、米麺、豆腐、玉ねぎ、卵",
    "Beef, rice noodles, tofu, bean sprouts, fern, onion, mushrooms, egg":
        "牛肉、米麺、豆腐、豆もやし、ぜんまい、玉ねぎ、きのこ、卵",
    "Rice, egg, beef, onion, ginger": "ご飯、卵、牛肉、玉ねぎ、しょうが",
    "Stir-fried rice cakes, fish cake, white cabbage, egg, cheese": "炒めたトック（餅）、さつま揚げ、キャベツ、卵、チーズ",
    "Kimchi, tofu, pork, onion, tuna": "キムチ、豆腐、豚肉、玉ねぎ、ツナ",
}

# --- Kimchi & accompagnements : nom anglais -> (nom, petit texte) ---
SIDES = {
    "Kimchi": ("白菜キムチ", "Kimchi"),
    "Pickled radish": ("カクテキ", "大根キムチ"),
    "Pickled bellflower root": ("トラジの和え物", "Doraji"),
    "Pickled Korean fern": ("ワラビのナムル", "Gosari"),
}
SPICY = ("辛い",)

# --- Jus coréens : anglais -> japonais ---
JUICES = {
    "Pear juice": "梨ジュース",
    "Peach juice": "桃ジュース",
    "Grape juice": "ぶどうジュース",
}

# --- Titres de section : anglais -> japonais ---
SECTION_TITLES = {
    "Our menu": "メニュー",
    "Kimbap": "キンパ",
    "Bibimbap": "ビビンバ",
    "Specialities": "おすすめ料理",
    "Kimchi": "キムチ",
    "Drinks": "ドリンク",
    "How to eat bibimbap?": "ビビンバの食べ方",
    "Hours &amp; location": "営業時間・アクセス",
}

# --- Textes du JavaScript ---
JS_T = {
    "ja": """    var T = {
      openMenu: 'メニューを開く',
      closeMenu: 'メニューを閉じる',
      openSoon: '営業中 · まもなく閉店（{{close}}）',
      openNow: '営業中 · {{close}} まで',
      closedToday: '準備中 · {{open}} 開店',
      closedTomorrow: '閉店 · 明日 {{open}} 開店',
      closedMonday: '閉店 · 月曜日 {{open}} 開店',
      today: ' · 本日',
      allergens: 'アレルゲン：',
      notVeg: 'ベジタリアン不可',
      spicy: '辛い',
      contains: '含む：',
      count: function (n) { return '該当する料理：' + n + ' 品'; },
      replay: '↺ もう一度見る',
      updateMsg: 'サイトの新しいバージョンがあります。',
      updateBtn: '更新'
    };""",
}

MANIFEST_TEXT = {
    "ja": "ルクセンブルク駅近くの韓国料理店：メニュー、営業時間、アクセスをオフラインでも確認できます。",
}
