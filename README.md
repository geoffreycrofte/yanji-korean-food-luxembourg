# Yanji Korean Food – site vitrine

Site one-page (HTML + CSS + JS vanilla, sans dépendance) du restaurant **Yanji Korean Food**,
63 avenue de la Gare, L-1611 Luxembourg.

- `index.html` : le site en français (styles et scripts inclus). **C'est la source unique.**
- `en/`, `ko/`, `zh/` : versions anglaise, coréenne et chinoise (simplifié), **générées**.
- `tools/build-i18n.py` : script qui génère les traductions.
- `assets/` : favicon, icône Apple, image de partage (Open Graph) et polices (`assets/fonts/`, licences dans `LICENSES.txt`).
- `robots.txt`, `sitemap.xml` : SEO.

## À faire avant la mise en ligne
- Compléter les mentions légales dans `index.html` (valeurs `XXXX` surlignées en jaune, classe `todo`) :
  raison sociale, email, RCS, TVA, autorisation d'établissement, hébergeur. Puis relancer `python3 tools/build-i18n.py`.
- Remplacer `https://www.yanji.lu/` par le vrai domaine (index.html, robots.txt, sitemap.xml).
- Remplacer les photos d'illustration (Wikimedia Commons) par les vraies photos des plats.
- Vérifier les coordonnées GPS des données structurées (`49.6031, 6.1329`).
- Faire relire les traductions coréenne et chinoise par l'équipe.

## Accessibilité (RAWeb 1.1, niveau AA visé)
- Contrastes AA vérifiés (texte ≥ 4,5:1, composants ≥ 3:1) ; audit axe-core sans violation.
- Bouton « pause des animations » dans l'en-tête (RAWeb 13.8), choix mémorisé ;
  la préférence système `prefers-reduced-motion` coupe les animations par défaut.
- Structure : landmarks, lien d'évitement, titres hiérarchisés, changements de langue balisés (`lang`).
- Statuts dynamiques (ouvert/fermé, résultats des filtres) annoncés via `role="status"`.
- Un audit humain reste recommandé avant la mise en ligne.

## Traductions
Ne modifiez pas `en/`, `ko/` ni `zh/` à la main : ils sont écrasés à chaque génération.

1. Modifiez `index.html` (français).
2. Si vous avez changé un texte, mettez à jour sa ligne dans `tools/build-i18n.py`
   (colonnes : français, anglais, coréen, chinois).
3. Lancez `python3 tools/build-i18n.py`.

Si un texte français n'est plus trouvé, le script s'arrête et indique lequel.
