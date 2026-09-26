#!/usr/bin/env python3
"""
Génère les versions traduites du site à partir de la page française.

    python3 tools/build-i18n.py

Source unique : index.html (français). Le script produit en/index.html,
ko/index.html et zh/index.html en remplaçant chaque fragment français par sa
traduction. Si un fragment n'est plus trouvé (parce que le texte français a
changé), le script s'arrête et indique lequel : il suffit alors de mettre à
jour la ligne correspondante ci-dessous.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "index.html"
SITE = "https://www.yanji.lu/"  # TODO : remplacer par le vrai domaine

LANGS = {
    "en": {"html": "en", "og": "en_GB", "button": "EN", "label": "Language: ", "font": None},
    # Polices système pour le coréen et le chinois (déjà présentes sur les appareils)
    "ko": {"html": "ko", "og": "ko_KR", "button": "한국어", "label": "언어: ",
           "font": '"Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", "Noto Sans CJK KR"'},
    "zh": {"html": "zh-Hans", "og": "zh_CN", "button": "中文", "label": "语言：",
           "font": '"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", "Noto Sans CJK SC"'},
}
LANG_MENU = [  # (dossier, hreflang, nom affiché)
    ("", "fr", "Français"),
    ("en/", "en", "English"),
    ("ko/", "ko", "한국어"),
    ("zh/", "zh-Hans", "中文"),
]

# --------------------------------------------------------------------------
# Plats : (français, anglais, coréen, chinois)
# --------------------------------------------------------------------------
DISHES = [
    ("Rouleau au tendon de bœuf", "Beef tendon roll", "소힘줄 김밥", "牛筋紫菜卷"),
    ("Rouleau kimchi & thon", "Tuna & kimchi roll", "참치 김치 김밥", "金枪鱼泡菜紫菜卷"),
    ("Rouleau au bœuf & saucisson", "Beef & sausage roll", "소고기 소시지 김밥", "牛肉香肠紫菜卷"),
    ("Rouleau poulet teriyaki & fromage", "Teriyaki chicken & cheese roll", "데리야끼 치킨 치즈 김밥", "照烧鸡芝士紫菜卷"),
    ("Rouleau d'algue végétarien", "Vegetarian seaweed roll", "야채 김밥", "全素紫菜卷"),
    ("Bibimbap au kimchi & porc", "Kimchi & pork bibimbap", "김치 돼지고기 비빔밥", "五花肉辣白菜石锅拌饭"),
    ("Bibimbap au poulet teriyaki", "Teriyaki chicken bibimbap", "데리야끼 치킨 비빔밥", "照烧鸡石锅拌饭"),
    ("Bibimbap végétarien", "Vegetarian bibimbap", "야채 돌솥비빔밥", "素菜石锅拌饭"),
    ("Bibimbap au bœuf", "Beef bibimbap", "소고기 돌솥비빔밥", "牛肉石锅拌饭"),
    ("Soupe de bœuf", "Beef soup", "소고기 탕", "石锅牛肉汤"),
    ("Soupe de bœuf épicée coréenne", "Korean spicy beef soup", "육개장", "韩式辣牛肉汤"),
    ("Gyudon de bœuf", "Beef gyudon", "규동", "牛丼饭"),
    ("Tteokbokki", "Tteokbokki", "떡볶이", "韩式辣炒年糕"),
    ("Soupe kimchi, porc & thon", "Kimchi, pork & tuna soup", "김치찌개", "五花肉金枪鱼泡菜汤"),
    ("Poulet frit coréen", "Korean fried chicken", "한국식 치킨", "韩式炸鸡"),
]
# Le sous-titre coréen affiché sous le nom (HTML) peut différer du nom coréen
KO_SUBTITLE = {"Poulet frit coréen": "한국식 치킨"}

DESCRIPTIONS = [
    ("Tendon de bœuf, saucisson de porc, radis jaune mariné, œufs, concombre, carottes, algue, sésame, huile de sésame, mayonnaise",
     "Beef tendon, pork sausage, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise",
     "소힘줄, 돼지고기 소시지, 단무지, 달걀, 오이, 당근, 김, 참깨, 참기름, 마요네즈",
     "牛筋、猪肉香肠、腌黄萝卜、鸡蛋、黄瓜、胡萝卜、紫菜、芝麻、芝麻油、蛋黄酱"),
    ("Thon cuit, kimchi, radis jaune mariné, œufs, concombre, carottes, algue, sésame, huile de sésame, mayonnaise",
     "Cooked tuna, kimchi, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise",
     "익힌 참치, 김치, 단무지, 달걀, 오이, 당근, 김, 참깨, 참기름, 마요네즈",
     "熟金枪鱼、泡菜、腌黄萝卜、鸡蛋、黄瓜、胡萝卜、紫菜、芝麻、芝麻油、蛋黄酱"),
    ("Bœuf, saucisson, radis jaune mariné, œufs, concombre, carottes, algue, sésame, huile de sésame, mayonnaise",
     "Beef, sausage, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise",
     "소고기, 소시지, 단무지, 달걀, 오이, 당근, 김, 참깨, 참기름, 마요네즈",
     "牛肉、香肠、腌黄萝卜、鸡蛋、黄瓜、胡萝卜、紫菜、芝麻、芝麻油、蛋黄酱"),
    ("Poulet sauce teriyaki, fromage, radis jaune mariné, œufs, concombre, carottes, algue, sésame, huile de sésame, mayonnaise",
     "Teriyaki chicken, cheese, pickled yellow radish, egg, cucumber, carrot, seaweed, sesame, sesame oil, mayonnaise",
     "데리야끼 치킨, 치즈, 단무지, 달걀, 오이, 당근, 김, 참깨, 참기름, 마요네즈",
     "照烧鸡肉、芝士、腌黄萝卜、鸡蛋、黄瓜、胡萝卜、紫菜、芝麻、芝麻油、蛋黄酱"),
    ("Champignons, concombre, carotte, radis jaune mariné, sésame, huile de sésame, algue",
     "Mushrooms, cucumber, carrot, pickled yellow radish, sesame, sesame oil, seaweed",
     "버섯, 오이, 당근, 단무지, 참깨, 참기름, 김",
     "蘑菇、黄瓜、胡萝卜、腌黄萝卜、芝麻、芝麻油、紫菜"),
    ("Kimchi, porc, algues, œufs",
     "Kimchi, pork, seaweed, egg",
     "김치, 돼지고기, 김, 달걀",
     "泡菜、五花肉、紫菜、鸡蛋"),
    ("Carottes râpées, épinards, courgettes, germes de soja, maïs, champignons, poulet, œufs",
     "Grated carrot, spinach, courgette, bean sprouts, sweetcorn, mushrooms, chicken, egg",
     "채 썬 당근, 시금치, 애호박, 콩나물, 옥수수, 버섯, 닭고기, 달걀",
     "胡萝卜丝、菠菜、西葫芦、豆芽、玉米、蘑菇、鸡肉、鸡蛋"),
    ("Carottes râpées, épinards, courgettes, fougère aigle, kimchi, champignons, germes de soja, algues, œufs",
     "Grated carrot, spinach, courgette, bracken fern, kimchi, mushrooms, bean sprouts, seaweed, egg",
     "채 썬 당근, 시금치, 애호박, 고사리, 김치, 버섯, 콩나물, 김, 달걀",
     "胡萝卜丝、菠菜、西葫芦、蕨菜、泡菜、蘑菇、豆芽、紫菜、鸡蛋"),
    ("Carottes râpées, épinards, courgettes, fougère aigle, kimchi, champignons, germes de soja, bœuf haché, œufs",
     "Grated carrot, spinach, courgette, bracken fern, kimchi, mushrooms, bean sprouts, minced beef, egg",
     "채 썬 당근, 시금치, 애호박, 고사리, 김치, 버섯, 콩나물, 다진 소고기, 달걀",
     "胡萝卜丝、菠菜、西葫芦、蕨菜、泡菜、蘑菇、豆芽、牛肉末、鸡蛋"),
    ("Bœuf, nouilles de riz, tofu, oignons, œufs",
     "Beef, rice noodles, tofu, onion, egg",
     "소고기, 쌀국수, 두부, 양파, 달걀",
     "牛肉、米粉、豆腐、洋葱、鸡蛋"),
    ("Bœuf, nouilles de riz, tofu, germes de soja, fougère, oignons, champignons, œufs",
     "Beef, rice noodles, tofu, bean sprouts, fern, onion, mushrooms, egg",
     "소고기, 쌀국수, 두부, 콩나물, 고사리, 양파, 버섯, 달걀",
     "牛肉、米粉、豆腐、豆芽、蕨菜、洋葱、蘑菇、鸡蛋"),
    ("Riz, œuf, bœuf, oignons, gingembre",
     "Rice, egg, beef, onion, ginger",
     "밥, 달걀, 소고기, 양파, 생강",
     "米饭、鸡蛋、牛肉、洋葱、生姜"),
    ("Gâteaux de riz sautés, pâte de poisson, chou blanc, œufs, fromage",
     "Stir-fried rice cakes, fish cake, white cabbage, egg, cheese",
     "떡, 어묵, 양배추, 달걀, 치즈",
     "炒年糕、鱼饼、白菜、鸡蛋、芝士"),
    ("Kimchi, tofu, porc, oignons, thon",
     "Kimchi, tofu, pork, onion, tuna",
     "김치, 두부, 돼지고기, 양파, 참치",
     "泡菜、豆腐、五花肉、洋葱、金枪鱼"),
]

# Kimchi & accompagnements : (fr, fr petit texte, coréen, en, en petit, zh, zh petit)
SIDES = [
    ("Kimchi", "Chou mariné", "배추김치", "Kimchi", "Pickled cabbage", "辣白菜", "泡菜"),
    ("Radis mariné", "Cubes de radis", "깍두기", "Pickled radish", "Diced radish kimchi", "萝卜块", "腌萝卜"),
    ("Racine de campanule marinée", "Doraji", "도라지무침", "Pickled bellflower root", "Doraji", "桔梗", "凉拌桔梗"),
    ("Fougère coréenne marinée", "Gosari", "고사리나물", "Pickled Korean fern", "Gosari", "蕨菜", "凉拌蕨菜"),
]

# Jus coréens : (fr, coréen, en, zh)
JUICES = [
    ("Jus de poire", "배 주스", "Pear juice", "梨汁"),
    ("Jus de pêche", "복숭아 주스", "Peach juice", "桃子汁"),
    ("Jus de raisin", "포도 주스", "Grape juice", "葡萄汁"),
]

# Titres de section : (fr, déco coréenne) -> par langue (titre, déco, lang de la déco)
SECTION_TITLES = [
    ("La carte", "메뉴", "Our menu", "메뉴", "菜单"),
    ("Kimbap", "김밥", "Kimbap", "김밥", "紫菜卷"),
    ("Bibimbap", "비빔밥", "Bibimbap", "비빔밥", "石锅拌饭"),
    ("Les spécialités", "특선 요리", "Specialities", "특선 요리", "特色菜"),
    ("Kimchi", "김치 · 반찬", "Kimchi", "김치 · 반찬", "泡菜"),
    ("Boissons", "음료", "Drinks", "음료", "饮品"),
    ("Comment manger le bibimbap&nbsp;?", "비벼 먹어요", "How to eat bibimbap?", "비빔밥 맛있게 먹는 법", "石锅拌饭怎么吃？"),
    ("Horaires &amp; accès", "오시는 길", "Hours &amp; location", "영업시간 · 오시는 길", "营业时间与地址"),
]

# --------------------------------------------------------------------------
# Fragments de texte : (français, anglais, coréen, chinois)
# Les fragments les plus longs sont remplacés en premier.
# --------------------------------------------------------------------------
ROWS = [
    # --- <head> ---
    ("<title>Yanji Korean Food – Restaurant coréen à Luxembourg-Gare | Kimbap, Bibimbap</title>",
     "<title>Yanji Korean Food – Korean restaurant near Luxembourg station | Kimbap, Bibimbap</title>",
     "<title>Yanji Korean Food 연길 – 룩셈부르크 역 근처 한식당 | 김밥, 비빔밥</title>",
     "<title>Yanji Korean Food 延吉 – 卢森堡火车站附近的韩国餐厅 | 紫菜卷、石锅拌饭</title>"),
    ("Yanji Korean Food, petit restaurant coréen au 63 avenue de la Gare à Luxembourg. Kimbap, bibimbap en pot de pierre, tteokbokki, soupes épicées et poulet frit coréen. Ouvert du lundi au samedi, 11h00–17h30.",
     "Yanji Korean Food, a small Korean restaurant at 63 avenue de la Gare, Luxembourg. Kimbap, stone-pot bibimbap, tteokbokki, spicy soups and Korean fried chicken. Open Monday to Saturday, 11:00–17:30.",
     "룩셈부르크 avenue de la Gare 63번지의 작은 한식당, Yanji Korean Food. 김밥, 돌솥비빔밥, 떡볶이, 매운 국물 요리와 한국식 치킨. 월요일–토요일 11:00–17:30 영업.",
     "Yanji Korean Food，位于卢森堡 avenue de la Gare 63 号的韩国小餐馆。紫菜卷、石锅拌饭、辣炒年糕、辣汤和韩式炸鸡。周一至周六 11:00–17:30 营业。"),
    ("restaurant coréen Luxembourg, Korean food Luxembourg, kimbap, bibimbap, tteokbokki, poulet frit coréen, avenue de la Gare, Luxembourg-Gare, Yanji",
     "Korean restaurant Luxembourg, Korean food Luxembourg, kimbap, bibimbap, tteokbokki, Korean fried chicken, avenue de la Gare, Luxembourg station, Yanji",
     "룩셈부르크 한식당, 룩셈부르크 한국 음식, 김밥, 비빔밥, 떡볶이, 치킨, avenue de la Gare, Yanji, 연길",
     "卢森堡韩国餐厅, 卢森堡韩国料理, 紫菜卷, 石锅拌饭, 辣炒年糕, 韩式炸鸡, avenue de la Gare, Yanji, 延吉"),
    ('content="Yanji Korean Food – Restaurant coréen à Luxembourg-Gare"',
     'content="Yanji Korean Food – Korean restaurant near Luxembourg station"',
     'content="Yanji Korean Food – 룩셈부르크 역 근처 한식당"',
     'content="Yanji Korean Food – 卢森堡火车站附近的韩国餐厅"'),
    ("Kimbap, bibimbap en pot de pierre, tteokbokki et poulet frit coréen. 63 avenue de la Gare, Luxembourg. Lun–Sam 11h00–17h30.",
     "Kimbap, stone-pot bibimbap, tteokbokki and Korean fried chicken. 63 avenue de la Gare, Luxembourg. Mon–Sat 11:00–17:30.",
     "김밥, 돌솥비빔밥, 떡볶이, 한국식 치킨. 룩셈부르크 avenue de la Gare 63. 월–토 11:00–17:30.",
     "紫菜卷、石锅拌饭、辣炒年糕和韩式炸鸡。卢森堡 avenue de la Gare 63 号。周一至周六 11:00–17:30。"),

    # --- En-tête ---
    ("Aller au contenu", "Skip to content", "본문 바로가기", "跳到主要内容"),
    ('aria-label="Yanji Korean Food – accueil"', 'aria-label="Yanji Korean Food – home"',
     'aria-label="Yanji Korean Food – 홈"', 'aria-label="Yanji Korean Food – 首页"'),
    ('aria-label="Navigation principale"', 'aria-label="Main navigation"', 'aria-label="주 메뉴"', 'aria-label="主导航"'),
    ('<li><a href="#menu">La carte</a></li>', '<li><a href="#menu">Menu</a></li>',
     '<li><a href="#menu">메뉴</a></li>', '<li><a href="#menu">菜单</a></li>'),
    ('<li><a href="#bibimbap-guide">Bibimbap</a></li>', '<li><a href="#bibimbap-guide">Bibimbap</a></li>',
     '<li><a href="#bibimbap-guide">비빔밥</a></li>', '<li><a href="#bibimbap-guide">石锅拌饭</a></li>'),
    ('<li><a href="#infos">Horaires &amp; accès</a></li>', '<li><a href="#infos">Hours &amp; location</a></li>',
     '<li><a href="#infos">영업시간 · 위치</a></li>', '<li><a href="#infos">营业时间与地址</a></li>'),
    ("Mettre en pause les animations", "Pause animations", "애니메이션 일시정지", "暂停动画"),
    ("\n        Appeler\n", "\n        Call\n", "\n        전화하기\n", "\n        致电\n"),
    ('aria-label="Appeler Yanji Korean Food"', 'aria-label="Call Yanji Korean Food"',
     'aria-label="Yanji Korean Food에 전화하기"', 'aria-label="致电 Yanji Korean Food"'),
    ('aria-label="Ouvrir le menu"', 'aria-label="Open menu"', 'aria-label="메뉴 열기"', 'aria-label="打开菜单"'),

    # --- Hero ---
    ('<span class="visually-hidden"> – restaurant coréen à Luxembourg-Gare</span>',
     '<span class="visually-hidden"> – Korean restaurant near Luxembourg station</span>',
     '<span class="visually-hidden"> – 룩셈부르크 역 근처 한식당</span>',
     '<span class="visually-hidden"> – 卢森堡火车站附近的韩国餐厅</span>'),
    ("Kimbap roulés, bibimbap en pot de pierre, soupes épicées et poulet frit coréen, à deux pas de la gare de Luxembourg.",
     "Freshly rolled kimbap, stone-pot bibimbap, spicy soups and Korean fried chicken, a short walk from Luxembourg station.",
     "갓 말은 김밥, 돌솥비빔밥, 매콤한 국물 요리와 한국식 치킨을 룩셈부르크 역 바로 앞에서 만나 보세요.",
     "现卷紫菜卷、石锅拌饭、香辣汤品和韩式炸鸡，距卢森堡火车站仅几步之遥。"),
    ("Lun – Sam · 11h00 – 17h30", "Mon – Sat · 11:00 – 17:30", "월 – 토 · 11:00 – 17:30", "周一至周六 · 11:00 – 17:30"),
    (">Voir la carte</a>", ">See the menu</a>", ">메뉴 보기</a>", ">查看菜单</a>"),
    (">Nous trouver</a>", ">Find us</a>", ">찾아오시는 길</a>", ">如何找到我们</a>"),
    ('Saveurs de Corée<small lang="ko">한국의 맛</small>', 'Flavours of Korea<small lang="ko">한국의 맛</small>',
     '한국의 맛<small lang="fr">Saveurs de Corée</small>', '韩国风味<small lang="ko">한국의 맛</small>'),
    ('Fait avec amour<small lang="ko">사랑을 담아</small>', 'Made with love<small lang="ko">사랑을 담아</small>',
     '사랑을 담아<small lang="fr">Fait avec amour</small>', '用心制作<small lang="ko">사랑을 담아</small>'),
    ('Servi bien chaud<small lang="ko">따뜻하게</small>', 'Served piping hot<small lang="ko">따뜻하게</small>',
     '따뜻하게<small lang="fr">Servi bien chaud</small>', '热腾腾上桌<small lang="ko">따뜻하게</small>'),

    # --- Bandeau défilant (décoratif) ---
    ('marquee__item">Kimbap <', 'marquee__item">Kimbap <', 'marquee__item">Kimbap <', 'marquee__item">紫菜卷 <'),
    ('marquee__item">Bibimbap <', 'marquee__item">Bibimbap <', 'marquee__item">Bibimbap <', 'marquee__item">石锅拌饭 <'),
    ('marquee__item">Tteokbokki <', 'marquee__item">Tteokbokki <', 'marquee__item">Tteokbokki <', 'marquee__item">辣炒年糕 <'),
    ('marquee__item">Poulet frit <', 'marquee__item">Fried chicken <', 'marquee__item">Chicken <', 'marquee__item">韩式炸鸡 <'),
    ('marquee__item">Kimchi <', 'marquee__item">Kimchi <', 'marquee__item">Kimchi <', 'marquee__item">泡菜 <'),
    ('marquee__item">Gyudon <', 'marquee__item">Gyudon <', 'marquee__item">Gyudon <', 'marquee__item">牛丼饭 <'),
    ('marquee__item">Soupe épicée <', 'marquee__item">Spicy soup <', 'marquee__item">Yukgaejang <', 'marquee__item">辣牛肉汤 <'),

    # --- À propos ---
    ("Petite carte, <em>grand cœur</em>", "Small menu, <em>big heart</em>", "작은 메뉴, <em>큰 정성</em>", "菜单虽小，<em>心意满满</em>"),
    ("Chez Yanji, on vous sert une cuisine coréenne simple et généreuse, au cœur du quartier de la Gare à Luxembourg. Une petite carte, une équipe aux petits soins, et des plats qui réchauffent&nbsp;: kimbap, bibimbap, tteokbokki, soupes mijotées et poulet frit croustillant.",
     "At Yanji, we serve simple, generous Korean food in the heart of Luxembourg’s Gare district. A small menu, a caring team and warming dishes: kimbap, bibimbap, tteokbokki, slow-cooked soups and crispy fried chicken.",
     "연길은 룩셈부르크 가르 지역 한가운데에서 소박하고 푸짐한 한국 음식을 선보입니다. 작은 메뉴, 세심한 직원, 그리고 속을 따뜻하게 해 주는 요리: 김밥, 비빔밥, 떡볶이, 푹 끓인 국물 요리와 바삭한 치킨.",
     "在延吉，我们在卢森堡火车站街区的中心为您提供简单而丰盛的韩国料理。菜单虽小，团队贴心，菜品暖心：紫菜卷、石锅拌饭、辣炒年糕、慢炖汤品和香脆炸鸡。"),
    ("Sur place ou à emporter, pour une pause déjeuner ou un goûter salé, passez nous voir du lundi au samedi.",
     "Eat in or take away, for a lunch break or a savoury snack: drop by Monday to Saturday.",
     "매장 식사와 포장 모두 가능합니다. 점심이나 간식이 생각날 때, 월요일부터 토요일까지 들러 주세요.",
     "堂食或外带皆可。午餐或小吃时间，周一至周六欢迎光临。"),
    ("<strong>Kimbap</strong><span>5 rouleaux coréens, dont un végétarien</span>",
     "<strong>Kimbap</strong><span>5 Korean rolls, including a vegetarian one</span>",
     "<strong>김밥</strong><span>채식 김밥을 포함한 5가지 김밥</span>",
     "<strong>紫菜卷</strong><span>5 款韩式紫菜卷，其中一款全素</span>"),
    ("<strong>Pot de pierre</strong><span>Bibimbap grésillant, servi avec soupe</span>",
     "<strong>Stone pot</strong><span>Sizzling bibimbap, served with soup</span>",
     "<strong>돌솥</strong><span>지글지글 돌솥비빔밥, 국과 함께</span>",
     "<strong>石锅</strong><span>滋滋作响的石锅拌饭，配汤</span>"),
    ("<strong>Épicé ou pas</strong><span>Chaque plat pimenté est signalé</span>",
     "<strong>Spicy or not</strong><span>Every spicy dish is marked</span>",
     "<strong>맵게 또는 순하게</strong><span>매운 메뉴는 모두 표시되어 있어요</span>",
     "<strong>辣或不辣</strong><span>所有辣味菜品均有标注</span>"),
    ("<strong>Équipe adorable</strong><span>Un accueil chaleureux, promis</span>",
     "<strong>Lovely team</strong><span>A warm welcome, promised</span>",
     "<strong>다정한 직원</strong><span>따뜻한 환대를 약속드려요</span>",
     "<strong>亲切的团队</strong><span>保证热情接待</span>"),

    # --- Carte ---
    ("Tous nos plats sont préparés sur place. Les prix sont indiqués TTC. Les photos sont des illustrations non contractuelles.",
     "All our dishes are prepared on site. Prices include VAT. Photos are for illustration only.",
     "모든 요리는 매장에서 직접 조리합니다. 가격은 부가세 포함입니다. 사진은 참고용입니다.",
     "所有菜品均现场制作。价格已含增值税。图片仅供参考。"),
    ('aria-label="Catégories de la carte"', 'aria-label="Menu categories"', 'aria-label="메뉴 분류"', 'aria-label="菜单分类"'),
    ('<a href="#kimbap">Kimbap</a>', '<a href="#kimbap">Kimbap</a>', '<a href="#kimbap">김밥</a>', '<a href="#kimbap">紫菜卷</a>'),
    ('<a href="#bibimbap">Bibimbap</a>', '<a href="#bibimbap">Bibimbap</a>', '<a href="#bibimbap">비빔밥</a>', '<a href="#bibimbap">石锅拌饭</a>'),
    ('<a href="#specialites">Spécialités</a>', '<a href="#specialites">Specialities</a>', '<a href="#specialites">특선 요리</a>', '<a href="#specialites">特色菜</a>'),
    ('<a href="#kimchi">Kimchi</a>', '<a href="#kimchi">Kimchi</a>', '<a href="#kimchi">김치</a>', '<a href="#kimchi">泡菜</a>'),
    ('<a href="#boissons">Boissons</a>', '<a href="#boissons">Drinks</a>', '<a href="#boissons">음료</a>', '<a href="#boissons">饮品</a>'),
    ('<a href="#allergenes">Allergènes</a>', '<a href="#allergenes">Allergens</a>', '<a href="#allergenes">알레르기 정보</a>', '<a href="#allergenes">过敏原</a>'),
    ('aria-label="Filtrer la carte"', 'aria-label="Filter the menu"', 'aria-label="메뉴 필터"', 'aria-label="筛选菜单"'),
    ("Filtrer&nbsp;:", "Filter:", "필터:", "筛选："),
    ("</span>Végétarien<", "</span>Vegetarian<", "</span>채식<", "</span>素食<"),
    ("</span>Sans piment<", "</span>Not spicy<", "</span>맵지 않은 메뉴<", "</span>不辣<"),
    ("Indication donnée à titre informatif&nbsp;: en cas d'allergie, merci de toujours prévenir notre équipe.",
     "For information only: if you have an allergy, please always tell our team.",
     "참고용 정보입니다. 알레르기가 있으시면 반드시 직원에게 알려 주세요.",
     "仅供参考：如有过敏，请务必告知我们的员工。"),
    ("Rouleaux d'algue et de riz assaisonné au sésame, garnis et tranchés.",
     "Seaweed rolls of sesame-seasoned rice with fillings, sliced.",
     "참기름으로 간한 밥과 속재료를 김으로 말아 썰어 낸 김밥입니다.",
     "以芝麻油调味的米饭包裹馅料，用紫菜卷起后切片。"),
    ('<span class="visually-hidden">Plat n°</span>', '<span class="visually-hidden">Dish no. </span>',
     '<span class="visually-hidden">메뉴 번호 </span>', '<span class="visually-hidden">菜品编号 </span>'),
    ('<span class="visually-hidden">n°</span>', '<span class="visually-hidden">no. </span>',
     '<span class="visually-hidden">번호 </span>', '<span class="visually-hidden">编号 </span>'),
    ('aria-hidden="true">Photo d\'illustration</span>', 'aria-hidden="true">Illustrative photo</span>',
     'aria-hidden="true">참고용 사진</span>', 'aria-hidden="true">示意图片</span>'),
    ("</span>Épicé</span>", "</span>Spicy</span>", "</span>매움</span>", "</span>辣</span>"),
    ('<span class="tag tag--side">+ soupe &amp; kimchi</span>', '<span class="tag tag--side">+ soup &amp; kimchi</span>',
     '<span class="tag tag--side">+ 국 · 김치</span>', '<span class="tag tag--side">+ 汤和泡菜</span>'),
    ('<span class="tag tag--side">+ soupe</span>', '<span class="tag tag--side">+ soup</span>',
     '<span class="tag tag--side">+ 국</span>', '<span class="tag tag--side">+ 汤</span>'),
    ('<span class="tag tag--side">Pot de pierre + soupe</span>', '<span class="tag tag--side">Stone pot + soup</span>',
     '<span class="tag tag--side">돌솥 + 국</span>', '<span class="tag tag--side">石锅 + 汤</span>'),
    ('<span class="tag tag--side">+ riz</span>', '<span class="tag tag--side">+ rice</span>',
     '<span class="tag tag--side">+ 밥</span>', '<span class="tag tag--side">+ 米饭</span>'),
    ('<span class="tag tag--side">3 saveurs au choix</span>', '<span class="tag tag--side">Choice of 3 flavours</span>',
     '<span class="tag tag--side">3가지 맛 중 선택</span>', '<span class="tag tag--side">三种口味可选</span>'),
    ("<li>Sucré &amp; épicé coréen <span", "<li>Korean sweet &amp; spicy <span", "<li>양념 (매콤달콤) <span", "<li>韩式甜辣 <span"),
    ("<li>Moutarde &amp; miel</li>", "<li>Honey mustard</li>", "<li>허니 머스터드</li>", "<li>蜂蜜芥末</li>"),
    ("<li>Soja</li>", "<li>Soy sauce</li>", "<li>간장</li>", "<li>酱油</li>"),
    ('Bol de riz garni de légumes, de viande et d\'un œuf, à mélanger avec la sauce pimentée. <a href="#bibimbap-guide">Comment le manger&nbsp;?</a>',
     'A bowl of rice topped with vegetables, meat and an egg, to mix with chilli sauce. <a href="#bibimbap-guide">How to eat it?</a>',
     '채소, 고기, 달걀을 올린 밥을 고추장과 함께 비벼 드세요. <a href="#bibimbap-guide">먹는 법 보기</a>',
     '米饭配蔬菜、肉和鸡蛋，拌入辣酱食用。<a href="#bibimbap-guide">怎么吃？</a>'),
    ("Soupes mijotées, plats sautés et poulet frit, servis avec du riz ou une soupe.",
     "Slow-cooked soups, stir-fries and fried chicken, served with rice or soup.",
     "푹 끓인 국물 요리, 볶음 요리, 치킨을 밥 또는 국과 함께 드립니다.",
     "慢炖汤品、炒菜和炸鸡，配米饭或汤。"),
    ("Légumes marinés et fermentés, à partager ou à emporter.",
     "Marinated and fermented vegetables, to share or take away.",
     "양념하고 발효한 채소 반찬, 함께 나눠 드시거나 포장해 가세요.",
     "腌制发酵的蔬菜小菜，可分享或外带。"),

    # --- Boissons ---
    ("<h4>Boissons coréennes</h4>", "<h4>Korean drinks</h4>", "<h4>한국 음료</h4>", "<h4>韩国饮品</h4>"),
    ("<h4>Thés japonais</h4>", "<h4>Japanese teas</h4>", "<h4>일본 차</h4>", "<h4>日本茶</h4>"),
    ("<h4>Softs</h4>", "<h4>Soft drinks</h4>", "<h4>탄산음료</h4>", "<h4>软饮</h4>"),
    ('Thé torréfié japonais<small lang="ja-Latn">Hojicha</small>', 'Japanese roasted tea<small lang="ja-Latn">Hojicha</small>',
     '일본 호지차<small lang="fr">Thé torréfié japonais</small>', '日本焙茶<small lang="ja-Latn">Hojicha</small>'),
    ('Thé vert japonais<small lang="ja-Latn">Sencha</small>', 'Japanese green tea<small lang="ja-Latn">Sencha</small>',
     '일본 녹차<small lang="fr">Thé vert japonais</small>', '日本绿茶<small lang="ja-Latn">Sencha</small>'),
    ("Lipton Ice Tea pêche", "Lipton Ice Tea peach", "립톤 아이스티 복숭아", "立顿桃味冰茶"),

    # --- Allergènes ---
    ("<span>Allergènes</span><span aria-hidden=\"true\">1 – 12</span>", "<span>Allergens</span><span aria-hidden=\"true\">1 – 12</span>",
     "<span>알레르기 정보</span><span aria-hidden=\"true\">1 – 12</span>", "<span>过敏原</span><span aria-hidden=\"true\">1 – 12</span>"),
    ("Les numéros indiqués sous chaque plat correspondent aux allergènes suivants. Une question&nbsp;? Notre équipe vous renseigne avec plaisir.",
     "The numbers under each dish refer to the allergens below. Any questions? Our team will be happy to help.",
     "각 메뉴 아래의 번호는 아래 알레르기 유발 성분을 나타냅니다. 궁금한 점은 언제든 직원에게 물어보세요.",
     "每道菜下方的数字对应以下过敏原。如有疑问，欢迎咨询我们的员工。"),
    ("<b>1.</b> Gluten</span>", "<b>1.</b> Gluten</span>", "<b>1.</b> 글루텐</span>", "<b>1.</b> 麸质</span>"),
    ("<b>2.</b> Crustacés</span>", "<b>2.</b> Crustaceans</span>", "<b>2.</b> 갑각류</span>", "<b>2.</b> 甲壳类</span>"),
    ("<b>3.</b> Œufs</span>", "<b>3.</b> Eggs</span>", "<b>3.</b> 달걀</span>", "<b>3.</b> 蛋类</span>"),
    ("<b>4.</b> Poissons</span>", "<b>4.</b> Fish</span>", "<b>4.</b> 생선</span>", "<b>4.</b> 鱼类</span>"),
    ("<b>5.</b> Arachides</span>", "<b>5.</b> Peanuts</span>", "<b>5.</b> 땅콩</span>", "<b>5.</b> 花生</span>"),
    ("<b>6.</b> Soja</span>", "<b>6.</b> Soy</span>", "<b>6.</b> 대두</span>", "<b>6.</b> 大豆</span>"),
    ("<b>7.</b> Lait &amp; lactose</span>", "<b>7.</b> Milk &amp; lactose</span>", "<b>7.</b> 우유 · 유당</span>", "<b>7.</b> 牛奶和乳糖</span>"),
    ("<b>8.</b> Fruits à coque</span>", "<b>8.</b> Tree nuts</span>", "<b>8.</b> 견과류</span>", "<b>8.</b> 坚果</span>"),
    ("<b>9.</b> Céleri</span>", "<b>9.</b> Celery</span>", "<b>9.</b> 셀러리</span>", "<b>9.</b> 芹菜</span>"),
    ("<b>10.</b> Moutarde</span>", "<b>10.</b> Mustard</span>", "<b>10.</b> 겨자</span>", "<b>10.</b> 芥末</span>"),
    ("<b>11.</b> Sésame</span>", "<b>11.</b> Sesame</span>", "<b>11.</b> 참깨</span>", "<b>11.</b> 芝麻</span>"),
    ("<b>12.</b> Sulfites</span>", "<b>12.</b> Sulphites</span>", "<b>12.</b> 아황산염</span>", "<b>12.</b> 亚硫酸盐</span>"),

    # --- Comment manger le bibimbap ---
    ("«&nbsp;Bibim&nbsp;» veut dire <em>mélanger</em> et «&nbsp;bap&nbsp;», le <em>riz</em>. Le secret, c'est de tout mélanger avant de déguster&nbsp;!",
     "“Bibim” means <em>mixing</em> and “bap” means <em>rice</em>. The secret: mix everything before you dig in!",
     "“비빔”은 <em>비비다</em>, “밥”은 <em>밥</em>이라는 뜻이에요. 먹기 전에 골고루 비비는 것이 비결!",
     "“Bibim”意为<em>拌</em>，“bap”意为<em>米饭</em>。秘诀就是开吃前把所有食材拌匀！"),
    ("<strong>Ajoutez la sauce pimentée</strong><span>Selon votre goût, un peu ou beaucoup de gochujang.</span>",
     "<strong>Add the chilli sauce</strong><span>A little or a lot of gochujang, to taste.</span>",
     "<strong>고추장을 넣으세요</strong><span>입맛에 따라 조금 또는 듬뿍.</span>",
     "<strong>加入辣酱</strong><span>根据口味，适量加入韩式辣酱。</span>"),
    ("<strong>Mélangez tout ensemble</strong><span>Riz, légumes, viande et œuf&nbsp;: tout doit être bien enrobé.</span>",
     "<strong>Mix everything together</strong><span>Rice, vegetables, meat and egg: everything should be well coated.</span>",
     "<strong>골고루 비비세요</strong><span>밥, 채소, 고기, 달걀에 양념이 고루 배도록.</span>",
     "<strong>全部拌匀</strong><span>米饭、蔬菜、肉和鸡蛋都要裹满酱汁。</span>"),
    ("<strong>Régalez-vous&nbsp;!</strong><span>En pot de pierre, le riz croustillant du fond est la meilleure partie.</span>",
     "<strong>Enjoy!</strong><span>In a stone pot, the crispy rice at the bottom is the best part.</span>",
     "<strong>맛있게 드세요!</strong><span>돌솥에서는 바닥의 누룽지가 최고예요.</span>",
     "<strong>开动吧！</strong><span>石锅底部的锅巴是最美味的部分。</span>"),
    ("▶ Voir la démo", "▶ Watch the demo", "▶ 시연 보기", "▶ 观看演示"),
    (">Choisir mon bibimbap</a>", ">Choose my bibimbap</a>", ">비빔밥 고르기</a>", ">选择我的石锅拌饭</a>"),

    # --- Horaires & accès ---
    ("</span> Horaires</h3>", "</span> Opening hours</h3>", "</span> 영업시간</h3>", "</span> 营业时间</h3>"),
    ("Horaires d'ouverture", "Opening hours", "영업시간", "营业时间"),
    ('<th scope="row">Lundi</th>', '<th scope="row">Monday</th>', '<th scope="row">월요일</th>', '<th scope="row">星期一</th>'),
    ('<th scope="row">Mardi</th>', '<th scope="row">Tuesday</th>', '<th scope="row">화요일</th>', '<th scope="row">星期二</th>'),
    ('<th scope="row">Mercredi</th>', '<th scope="row">Wednesday</th>', '<th scope="row">수요일</th>', '<th scope="row">星期三</th>'),
    ('<th scope="row">Jeudi</th>', '<th scope="row">Thursday</th>', '<th scope="row">목요일</th>', '<th scope="row">星期四</th>'),
    ('<th scope="row">Vendredi</th>', '<th scope="row">Friday</th>', '<th scope="row">금요일</th>', '<th scope="row">星期五</th>'),
    ('<th scope="row">Samedi</th>', '<th scope="row">Saturday</th>', '<th scope="row">토요일</th>', '<th scope="row">星期六</th>'),
    ('<th scope="row">Dimanche</th><td>Fermé</td>', '<th scope="row">Sunday</th><td>Closed</td>',
     '<th scope="row">일요일</th><td>휴무</td>', '<th scope="row">星期日</th><td>休息</td>'),
    ("</span> Contact</h3>", "</span> Contact</h3>", "</span> 연락처</h3>", "</span> 联系方式</h3>"),
    ("<strong>Téléphone</strong>", "<strong>Phone</strong>", "<strong>전화</strong>", "<strong>电话</strong>"),
    ("<strong>Adresse</strong>", "<strong>Address</strong>", "<strong>주소</strong>", "<strong>地址</strong>"),
    ("<strong>Accès</strong>Quartier Gare, à quelques minutes à pied de la gare centrale et du tram.",
     "<strong>Getting here</strong>Gare district, a few minutes’ walk from the central station and the tram.",
     "<strong>교통</strong>가르 지역, 룩셈부르크 중앙역과 트램 정류장에서 걸어서 몇 분 거리입니다.",
     "<strong>交通</strong>火车站街区，距中央火车站和有轨电车站步行几分钟。"),
    ("Itinéraire Google Maps", "Directions on Google Maps", "Google 지도 길찾기", "Google 地图导航"),
    (" (nouvelle fenêtre)", " (new window)", " (새 창)", "（新窗口）"),

    # --- Pied de page ---
    ("<p>Lundi – Samedi<br>", "<p>Monday – Saturday<br>", "<p>월요일 – 토요일<br>", "<p>周一至周六<br>"),
    ("<p>Dimanche&nbsp;: fermé</p>", "<p>Sunday: closed</p>", "<p>일요일 휴무</p>", "<p>周日休息</p>"),
    ("Photos d'illustration non contractuelles provenant de", "Illustrative photos from", "참고용 사진 출처:", "示意图片来自"),
    ("(licences CC BY / CC BY-SA, voir chaque fichier pour l'auteur).",
     "(CC BY / CC BY-SA licences, see each file for the author).",
     "(CC BY / CC BY-SA 라이선스, 저작자는 각 파일 참고).",
     "（CC BY / CC BY-SA 许可，作者见各文件）。"),

    ("\n        Site web par <a", "\n        Website by <a", "\n        웹사이트 제작: <a", "\n        网站制作：<a"),
    ("\n        Accessibilité du site par <a", "\n        Website accessibility by <a", "\n        웹 접근성: <a", "\n        网站无障碍：<a"),

    # --- Mentions légales & confidentialité ---
    ("<summary>Mentions légales &amp; confidentialité<svg", "<summary>Legal notice &amp; privacy<svg",
     "<summary>법적 고지 및 개인정보 보호<svg", "<summary>法律声明与隐私<svg"),
    ("</svg>Masquer les plats contenant un allergène…<svg", "</svg>Hide dishes containing an allergen…<svg",
     "</svg>특정 알레르기 성분이 든 메뉴 숨기기…<svg", "</svg>隐藏含有某种过敏原的菜品…<svg"),
    (", San Francisco, CA 94107, États-Unis</dd>", ", San Francisco, CA 94107, USA</dd>",
     ", San Francisco, CA 94107, 미국</dd>", ", San Francisco, CA 94107, 美国</dd>"),
    ('<h2 id="legal-title">Mentions légales</h2>', '<h2 id="legal-title">Legal notice</h2>',
     '<h2 id="legal-title">법적 고지</h2>', '<h2 id="legal-title">法律声明</h2>'),
    ("<dt>Éditeur du site</dt>", "<dt>Publisher</dt>", "<dt>운영자</dt>", "<dt>网站发布者</dt>"),
    ("<dt>Contact</dt>", "<dt>Contact</dt>", "<dt>연락처</dt>", "<dt>联系方式</dt>"),
    ("<dt>Registre de commerce (RCS)</dt>", "<dt>Trade register (RCS)</dt>", "<dt>상업등기 (RCS)</dt>", "<dt>商业登记号 (RCS)</dt>"),
    ("<dt>Numéro de TVA</dt>", "<dt>VAT number</dt>", "<dt>부가가치세 번호</dt>", "<dt>增值税号</dt>"),
    ("<dt>Autorisation d'établissement</dt>", "<dt>Business permit</dt>", "<dt>영업 허가 번호</dt>", "<dt>营业许可</dt>"),
    ("<dt>Hébergement</dt>", "<dt>Hosting</dt>", "<dt>호스팅</dt>", "<dt>网站托管</dt>"),
    ("<dt>Conception et réalisation</dt>", "<dt>Design and development</dt>", "<dt>디자인 및 개발</dt>", "<dt>设计与开发</dt>"),
    ('<h2 id="privacy-title">Confidentialité</h2>', '<h2 id="privacy-title">Privacy</h2>',
     '<h2 id="privacy-title">개인정보 보호</h2>', '<h2 id="privacy-title">隐私</h2>'),
    ("<li>Ce site ne dépose aucun cookie et n'utilise aucun outil de statistiques ni de publicité.</li>",
     "<li>This website sets no cookies and uses no analytics or advertising tools.</li>",
     "<li>이 사이트는 쿠키를 사용하지 않으며, 통계 도구나 광고 도구도 사용하지 않습니다.</li>",
     "<li>本网站不使用 Cookie，也不使用任何统计或广告工具。</li>"),
    ("<li>Il ne contient aucun formulaire&nbsp;: nous ne collectons aucune donnée personnelle par son intermédiaire.</li>",
     "<li>It contains no forms: we collect no personal data through it.</li>",
     "<li>입력 양식이 없으므로 이 사이트를 통해 개인정보를 수집하지 않습니다.</li>",
     "<li>本网站没有任何表单，我们不会通过它收集任何个人数据。</li>"),
    ("<li>Si vous mettez les animations en pause, ce choix est enregistré uniquement dans votre navigateur et n'est jamais transmis.</li>",
     "<li>If you pause the animations, this choice is stored only in your browser and is never sent anywhere.</li>",
     "<li>애니메이션 일시정지 설정은 사용자의 브라우저에만 저장되며 외부로 전송되지 않습니다.</li>",
     "<li>如果您暂停动画，该设置仅保存在您的浏览器中，不会被发送到任何地方。</li>"),
    ("<li>Les polices de caractères sont hébergées sur ce site&nbsp;: aucune donnée n'est envoyée à Google Fonts.</li>",
     "<li>Fonts are hosted on this website: no data is sent to Google Fonts.</li>",
     "<li>글꼴은 이 사이트에서 직접 제공되므로 Google Fonts로 데이터가 전송되지 않습니다.</li>",
     "<li>字体托管在本网站上，不会向 Google Fonts 发送任何数据。</li>"),
    ("<li>Les photos d'illustration sont chargées depuis Wikimedia Commons, qui reçoit alors votre adresse IP.</li>",
     "<li>Illustrative photos are loaded from Wikimedia Commons, which therefore receives your IP address.</li>",
     "<li>참고용 사진은 Wikimedia Commons에서 불러오며, 이때 사용자의 IP 주소가 전달됩니다.</li>",
     "<li>示意图片从 Wikimedia Commons 加载，因此其会获得您的 IP 地址。</li>"),
    ("<li>Le bouton «&nbsp;Itinéraire Google Maps&nbsp;» ouvre un service de Google, soumis à sa propre politique de confidentialité.</li>",
     "<li>The “Directions on Google Maps” button opens a Google service, subject to its own privacy policy.</li>",
     "<li>“Google 지도 길찾기” 버튼은 Google 서비스를 열며, 해당 서비스의 개인정보 처리방침이 적용됩니다.</li>",
     "<li>“Google 地图导航”按钮会打开 Google 的服务，适用其自身的隐私政策。</li>"),
    ("<li>Le site est hébergé par GitHub (États-Unis), qui peut conserver des journaux techniques (adresse IP, date, page consultée) pour assurer la sécurité du service.</li>",
     "<li>The website is hosted by GitHub (United States), which may keep technical logs (IP address, date, page visited) to keep the service secure.</li>",
     "<li>이 사이트는 GitHub(미국)에서 호스팅되며, GitHub는 서비스 보안을 위해 기술 로그(IP 주소, 날짜, 방문 페이지)를 보관할 수 있습니다.</li>",
     "<li>本网站由 GitHub（美国）托管，GitHub 可能会为保障服务安全而保留技术日志（IP 地址、日期、访问页面）。</li>"),
    ("<li>Pour toute question sur vos données, écrivez-nous à l'adresse indiquée ci-dessus. Vous pouvez aussi adresser une réclamation à la <a href=\"https://cnpd.public.lu/\">Commission nationale pour la protection des données (CNPD)</a>.</li>",
     "<li>For any question about your data, write to us at the address above. You can also file a complaint with the <a href=\"https://cnpd.public.lu/\" lang=\"fr\">Commission nationale pour la protection des données (CNPD)</a>, Luxembourg’s data protection authority.</li>",
     "<li>개인정보 관련 문의는 위 이메일로 보내 주세요. 룩셈부르크 개인정보 보호 기관인 <a href=\"https://cnpd.public.lu/\" lang=\"fr\">Commission nationale pour la protection des données (CNPD)</a>에 민원을 제기할 수도 있습니다.</li>",
     "<li>如对您的数据有任何疑问，请通过上述邮箱联系我们。您也可以向卢森堡数据保护机构 <a href=\"https://cnpd.public.lu/\" lang=\"fr\">Commission nationale pour la protection des données (CNPD)</a> 投诉。</li>"),

    # --- Données structurées ---
    ('"name": "Carte"', '"name": "Menu"', '"name": "메뉴"', '"name": "菜单"'),
    ('"name": "Kimbap",', '"name": "Kimbap",', '"name": "김밥",', '"name": "紫菜卷",'),
    ('"name": "Bibimbap",', '"name": "Bibimbap",', '"name": "비빔밥",', '"name": "石锅拌饭",'),
    ('"name": "Les spécialités"', '"name": "Specialities"', '"name": "특선 요리"', '"name": "特色菜"'),
    ('"name": "Kimchi & accompagnements"', '"name": "Kimchi & side dishes"', '"name": "김치 · 반찬"', '"name": "泡菜小菜"'),
    ('"name": "Kimchi (chou mariné)"', '"name": "Kimchi (pickled cabbage)"', '"name": "배추김치"', '"name": "辣白菜"'),
    ('"name": "Radis mariné"', '"name": "Pickled radish"', '"name": "깍두기"', '"name": "萝卜块"'),
    ('"name": "Racine de campanule marinée"', '"name": "Pickled bellflower root"', '"name": "도라지무침"', '"name": "桔梗"'),
    ('"name": "Fougère coréenne marinée"', '"name": "Pickled Korean fern"', '"name": "고사리나물"', '"name": "蕨菜"'),
    ('"3 saveurs au choix : sucré & épicé coréen, moutarde & miel, soja"',
     '"Choice of 3 flavours: Korean sweet & spicy, honey mustard, soy sauce"',
     '"3가지 맛 중 선택: 양념, 허니 머스터드, 간장"', '"三种口味可选：韩式甜辣、蜂蜜芥末、酱油"'),
    ('. Servi avec une soupe"', '. Served with soup"', '. 국 포함"', '。配汤"'),
    ('. En pot de pierre, avec soupe"', '. In a stone pot, with soup"', '. 돌솥, 국 포함"', '。石锅盛装，配汤"'),
    ('. Servie avec du riz"', '. Served with rice"', '. 밥 포함"', '。配米饭"'),
    ('. Servi avec du riz"', '. Served with rice"', '. 밥 포함"', '。配米饭"'),
    ('. Servi avec soupe et kimchi"', '. Served with soup and kimchi"', '. 국과 김치 포함"', '。配汤和泡菜"'),
    ('"servesCuisine": ["Coréenne", "Korean"]', '"servesCuisine": ["Korean"]', '"servesCuisine": ["한식", "Korean"]', '"servesCuisine": ["韩国料理", "Korean"]'),
]

# Textes du JavaScript (bloc entre /* i18n:start */ et /* i18n:end */)
JS_T = {
    "en": """    var T = {
      openMenu: 'Open menu',
      closeMenu: 'Close menu',
      openSoon: 'Open · closing soon (17:30)',
      openNow: 'Open now · until 17:30',
      closedToday: 'Closed · opens at 11:00',
      closedTomorrow: 'Closed · opens tomorrow at 11:00',
      closedMonday: 'Closed · opens Monday at 11:00',
      today: ' · today',
      allergens: 'Allergens:',
      notVeg: 'not vegetarian',
      spicy: 'spicy',
      contains: 'contains: ',
      count: function (n) { return n + (n > 1 ? ' dishes match' : ' dish matches'); },
      replay: '↺ Replay the demo'
    };""",
    "ko": """    var T = {
      openMenu: '메뉴 열기',
      closeMenu: '메뉴 닫기',
      openSoon: '영업 중 · 곧 마감 (17:30)',
      openNow: '지금 영업 중 · 17:30까지',
      closedToday: '영업 전 · 11:00 오픈',
      closedTomorrow: '영업 종료 · 내일 11:00 오픈',
      closedMonday: '영업 종료 · 월요일 11:00 오픈',
      today: ' · 오늘',
      allergens: '알레르기 성분:',
      notVeg: '채식 아님',
      spicy: '매움',
      contains: '포함: ',
      count: function (n) { return '해당 메뉴 ' + n + '개'; },
      replay: '↺ 다시 보기'
    };""",
    "zh": """    var T = {
      openMenu: '打开菜单',
      closeMenu: '关闭菜单',
      openSoon: '营业中 · 即将打烊（17:30）',
      openNow: '正在营业 · 至 17:30',
      closedToday: '尚未营业 · 11:00 开门',
      closedTomorrow: '已打烊 · 明天 11:00 开门',
      closedMonday: '已打烊 · 周一 11:00 开门',
      today: ' · 今天',
      allergens: '过敏原：',
      notVeg: '非素食',
      spicy: '辣',
      contains: '含有：',
      count: function (n) { return '共 ' + n + ' 道菜符合'; },
      replay: '↺ 重新播放'
    };""",
}

IDX = {"en": 1, "ko": 2, "zh": 3}


def build_rows():
    rows = list(ROWS)
    # Noms de plats : titre HTML (nom + sous-titre) et données structurées
    for fr, en, ko, zh in DISHES:
        fr_html = fr.replace("&", "&amp;")
        sub = KO_SUBTITLE.get(fr, ko)
        rows.append((
            f'{fr_html}<span class="dish__ko" lang="ko">{sub}</span>',
            f'{en.replace("&", "&amp;")}<span class="dish__ko" lang="ko">{sub}</span>',
            f'{ko}<span class="dish__ko" lang="fr">{fr_html}</span>',
            f'{zh}<span class="dish__ko" lang="ko">{sub}</span>',
        ))
        rows.append((f'"name": "{fr}"', f'"name": "{en}"', f'"name": "{ko}"', f'"name": "{zh}"'))
    # Descriptions : paragraphe HTML (avec point final) et données structurées
    for fr, en, ko, zh in DESCRIPTIONS:
        rows.append((f">{fr}.</p>", f">{en}.</p>", f">{ko}.</p>", f">{zh}。</p>"))
        rows.append((f'"description": "{fr}', f'"description": "{en}', f'"description": "{ko}', f'"description": "{zh}'))
    # Kimchi & accompagnements
    for fr, fr_small, ko, en, en_small, zh, zh_small in SIDES:
        spicy = '<span aria-hidden="true">🌶️</span><span class="visually-hidden">({})</span>'
        rows.append((
            f'<span class="side__name">{fr} {spicy.format("épicé")}<small>{fr_small}</small><span class="dish__ko" lang="ko">{ko}</span></span>',
            f'<span class="side__name">{en} {spicy.format("spicy")}<small>{en_small}</small><span class="dish__ko" lang="ko">{ko}</span></span>',
            f'<span class="side__name">{ko} {spicy.format("매움")}<small lang="fr">{fr}</small></span>',
            f'<span class="side__name">{zh} {spicy.format("辣")}<small>{zh_small}</small><span class="dish__ko" lang="ko">{ko}</span></span>',
        ))
    # Jus coréens
    for fr, ko, en, zh in JUICES:
        rows.append((
            f'{fr}<small lang="ko">{ko}</small>',
            f'{en}<small lang="ko">{ko}</small>',
            f'{ko}<small lang="fr">{fr}</small>',
            f'{zh}<small lang="ko">{ko}</small>',
        ))
    # Titres de section
    for fr, deco, en, ko, zh in SECTION_TITLES:
        src = f'<span>{fr}</span><span lang="ko" aria-hidden="true">{deco}</span>'
        rows.append((
            src,
            f'<span>{en}</span><span lang="ko" aria-hidden="true">{deco}</span>',
            f'<span>{ko}</span><span lang="fr" aria-hidden="true">{fr}</span>',
            f'<span>{zh}</span><span lang="ko" aria-hidden="true">{deco}</span>',
        ))
    return rows


def lang_menu(current, prefix):
    items = []
    for folder, hreflang, name in LANG_MENU:
        href = (prefix + folder) or "./"
        if hreflang.split("-")[0] == current:
            items.append(f'            <li><a href="{href}" hreflang="{hreflang}" lang="{hreflang}" aria-current="page">{name} <span aria-hidden="true">✓</span></a></li>')
        else:
            items.append(f'            <li><a href="{href}" hreflang="{hreflang}" lang="{hreflang}">{name}</a></li>')
    return "<!-- i18n:langs -->\n          <ul>\n" + "\n".join(items) + "\n          </ul>\n          <!-- /i18n:langs -->"


def replace_once(html, old, new, what):
    if old not in html:
        sys.exit(f"[i18n] Introuvable dans index.html ({what}) :\n  {old[:120]}")
    return html.replace(old, new)


def build(code):
    cfg = LANGS[code]
    html = SOURCE.read_text(encoding="utf-8")
    missing = []

    # 1. Textes (fragments les plus longs d'abord)
    for row in sorted(build_rows(), key=lambda r: len(r[0]), reverse=True):
        fr, target = row[0], row[IDX[code]]
        if fr not in html:
            missing.append(fr)
            continue
        html = html.replace(fr, target)
    if missing:
        sys.exit("[i18n] Fragments français introuvables (texte source modifié ?) :\n  - " + "\n  - ".join(m[:110] for m in missing))

    # 2. JavaScript
    html = re.sub(r"(/\* i18n:start[^\n]*\n).*?(\n    /\* i18n:end \*/)",
                  lambda m: m.group(1) + JS_T[code] + m.group(2), html, flags=re.S)

    # 3. Langue, URL, chemins
    url = f"{SITE}{code}/"
    html = replace_once(html, '<html lang="fr">', f'<html lang="{cfg["html"]}">', "html lang")
    html = replace_once(html, f'<link rel="canonical" href="{SITE}">', f'<link rel="canonical" href="{url}">', "canonical")
    html = replace_once(html, f'<meta property="og:url" content="{SITE}">', f'<meta property="og:url" content="{url}">', "og:url")
    html = replace_once(html, '<meta property="og:locale" content="fr_FR">', f'<meta property="og:locale" content="{cfg["og"]}">', "og:locale")
    html = replace_once(html, '"inLanguage": "fr"', f'"inLanguage": "{cfg["html"]}"', "inLanguage")
    html = replace_once(html, '"url": "https://www.yanji.lu/"', f'"url": "{url}"', "json url")
    html = html.replace('href="assets/', 'href="../assets/').replace("url(assets/", "url(../assets/")
    html = re.sub(r"<!-- i18n:langs -->.*?<!-- /i18n:langs -->", lambda m: lang_menu(code, "../"), html, flags=re.S)
    html = replace_once(html, '<span class="visually-hidden">Langue : </span>FR',
                        f'<span class="visually-hidden">{cfg["label"]}</span>{cfg["button"]}', "bouton langue")

    # L'adresse reste en français : on le signale aux lecteurs d'écran
    html = replace_once(html, "<address>", '<address lang="fr">', "adresse")
    html = replace_once(html, "<p><strong>63, avenue de la Gare</strong>", '<p lang="fr"><strong>63, avenue de la Gare</strong>', "adresse footer")

    # 4. Formats : prix « €12.99 », heures « 11:00 »
    html = re.sub(r"(\d+)(?:,(\d+))?&nbsp;€", lambda m: "€" + m.group(1) + ("." + m.group(2) if m.group(2) else ""), html)
    html = html.replace("11h00", "11:00").replace("17h30", "17:30")

    # 5. Police coréenne / chinoise (polices système, rien à télécharger)
    if cfg["font"]:
        f = cfg["font"]
        html = replace_once(html, "  </style>\n</head>",
                            "\n    /* Version " + code + " : police adaptée à l'écriture */\n"
                            f"    :root {{ --font-body: \"Nunito\", {f}, system-ui, sans-serif; --font-title: \"Anton\", {f}, Impact, sans-serif; }}\n"
                            + ("    body { word-break: keep-all; }\n" if code == "ko" else "")
                            + f"    .section-title > span:first-child, .about h2, .info-card h3, .panel__label, .drinks__group h4, .legal h2 {{ font-family: {f}, var(--font-body); font-weight: 700; }}\n"
                            + "    .section-title > span:first-child { -webkit-text-stroke: 0; text-shadow: 2px 2px 0 var(--ink); }\n"
                            "  </style>\n</head>", "police")

    out = ROOT / code / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"[i18n] {code}/index.html généré")


if __name__ == "__main__":
    for code in LANGS:
        build(code)
