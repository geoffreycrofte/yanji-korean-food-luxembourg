# Yanji Korean Food – site vitrine

Site one-page (HTML + CSS + JS vanilla) du restaurant **Yanji Korean Food**,
63 avenue de la Gare, L-1611 Luxembourg. Disponible en français, luxembourgeois,
allemand, anglais, coréen, chinois (simplifié) et japonais, installable en application (PWA) et consultable hors connexion.

## Organisation

| Chemin | Rôle |
|---|---|
| `infos.md` | **Horaires, téléphone, email, langues parlées** : modifiable directement sur GitHub |
| `src/index.html` | Page française (source) |
| `src/styles.css` | Styles (source, lisible) |
| `src/main.js` | Scripts de la page (source, lisible) |
| `src/sw.js` | Service worker (source) |
| `tools/build-i18n.py` | Assemble la page, génère les traductions (en, ko, zh) et les manifestes |
| `tools/i18n_de_lb.py` | Traductions allemandes et luxembourgeoises (indexées par le texte anglais) |
| `tools/i18n_ja.py` | Traductions japonaises (indexées par le texte anglais) |
| `tools/minify.mjs` | Minifie les pages et génère `sw.js` |
| `index.html`, `lb/`, `de/`, `en/`, `ko/`, `zh/`, `ja/`, `sw.js`, `*.webmanifest`, `sitemap.xml` | **Générés** : ne pas modifier à la main |
| `.github/workflows/publish.yml` | Regénère et publie le site à chaque modification sur `main` |
| `assets/` | Polices, icônes, favicon, image de partage |
| `robots.txt` | SEO |

## Modifier les horaires, le téléphone ou l'email

Tout est dans **`infos.md`** : sur GitHub, ouvrez le fichier, cliquez sur le crayon ✏️,
changez ce qui suit les deux-points, puis « Commit changes ». Le workflow
« Publier le site » (onglet Actions) regénère les 7 langues, commite les pages
et GitHub Pages les met en ligne en quelques minutes. En cas de valeur invalide
(heure, numéro, langue inconnue), le workflow échoue avec un message explicite
et le site en ligne reste inchangé.

Dans les sources, ces valeurs s'écrivent `{{open}}`, `{{close}}` (heures au format
de la langue : 11h00 en français, 11:00 ailleurs), `{{open_iso}}`, `{{close_iso}}`,
`{{phone}}`, `{{phone_href}}`, `{{email}}` et `{{phone_langs}}` ; un bloc entre
`<!-- if:email -->` et `<!-- /if:email -->` n'est affiché que si l'email est renseigné.
Les jours d'ouverture (lundi au samedi) restent fixes.

## Modifier le site

Prérequis : Python 3 et Node.js 18+ (`npm install` une première fois).

1. Modifiez les fichiers de `src/`.
2. Si vous avez changé un texte affiché, mettez à jour sa ligne dans `tools/build-i18n.py`
   (colonnes : français, anglais, coréen, chinois), puis les entrées allemande / luxembourgeoise
   (`tools/i18n_de_lb.py`) et japonaise (`tools/i18n_ja.py`), dont la clé est le texte anglais. Le script s'arrête et
   indique tout texte introuvable ou sans traduction.
3. Lancez **`npm run build`**, puis commitez les fichiers générés avec les sources
   (sur `main`, le workflow le fait aussi automatiquement).

`npm run build:dev` génère les pages sans les minifier (pratique pour déboguer).

## PWA : hors connexion et mises à jour

- Le service worker pré-cache les 7 langues, les polices et les icônes.
  Pages : réseau d'abord, cache si hors connexion. Fichiers statiques : cache d'abord.
- La version du cache est une empreinte du contenu généré : chaque `npm run build`
  qui change quelque chose produit un nouveau `sw.js`. Les visiteurs voient alors
  « Une nouvelle version du site est disponible · Mettre à jour ».
- Les photos d'illustration (Wikimedia) ne sont pas mises en cache : hors connexion,
  l'illustration de secours s'affiche.
- Bannière d'installation : affichée en arrivant à la fin de la carte (section Allergènes).
  Invite native sur Chrome / Edge / Android ; explication « Partager → Sur l'écran d'accueil »
  sur iPhone. « Plus tard » la masque 30 jours.
- Manifestes : `id`, `start_url` et `scope` en URL complète (`APP_URL` dans `tools/build-i18n.py`,
  actuellement `https://geoffreycrofte.github.io/yanji-korean-food-luxembourg/`), pour que l'app
  ne soit pas confondue avec les autres sites de `geoffreycrofte.github.io`. Les 7 langues
  partagent le même `id` : c'est une seule application. **À changer en cas de nouveau domaine.**
- Le reste est en chemins relatifs.

## À faire avant la mise en ligne
- Compléter les mentions légales dans `src/index.html` (valeurs `XXXX` surlignées, classe `todo`) :
  raison sociale, RCS, TVA, autorisation d'établissement. Puis `npm run build`.
  L'email se renseigne dans `infos.md`.
- Domaine : remplacer `https://yanji.lu/` si besoin (`src/index.html`, `tools/build-i18n.py`,
  `robots.txt`), ainsi que `APP_URL` (`tools/build-i18n.py`), et ajouter un fichier `CNAME`.
- Remplacer les photos d'illustration (Wikimedia Commons) par les vraies photos des plats.
- Vérifier les coordonnées GPS des données structurées (`49.6031, 6.1329`).
- Faire relire les traductions (coréen, chinois, japonais, luxembourgeois, allemand).

## Accessibilité (RAWeb 1.1, niveau AA visé)
- Contrastes AA vérifiés (texte ≥ 4,5:1, composants ≥ 3:1) ; audits axe-core et Lighthouse sans violation.
- Bouton « pause des animations » dans l'en-tête (RAWeb 13.8), choix mémorisé ;
  la préférence système `prefers-reduced-motion` coupe les animations par défaut.
- Structure : landmarks, lien d'évitement, titres hiérarchisés, changements de langue balisés (`lang`).
- Statuts dynamiques (ouvert/fermé, résultats des filtres, mise à jour) annoncés via `role="status"`.
- Un audit humain reste recommandé avant la mise en ligne.
