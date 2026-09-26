# Yanji Korean Food – site vitrine

Site one-page (HTML + CSS + JS vanilla, sans dépendance) du restaurant **Yanji Korean Food**,
63 avenue de la Gare, L-1611 Luxembourg.

- `index.html` : tout le site (styles et scripts inclus).
- `assets/` : favicon, icône Apple, image de partage (Open Graph).
- `robots.txt`, `sitemap.xml` : SEO.

## À faire avant la mise en ligne
- Remplacer `https://www.yanji.lu/` par le vrai domaine (index.html, robots.txt, sitemap.xml).
- Remplacer les photos d'illustration (Wikimedia Commons) par les vraies photos des plats.
- Vérifier les coordonnées GPS des données structurées (`49.6031, 6.1329`).
- Traductions : EN, 한국어, 中文.

## Accessibilité (RAWeb 1.1, niveau AA visé)
- Contrastes AA vérifiés (texte ≥ 4,5:1, composants ≥ 3:1) ; audit axe-core sans violation.
- Bouton « pause des animations » dans l'en-tête (RAWeb 13.8), choix mémorisé ;
  la préférence système `prefers-reduced-motion` coupe les animations par défaut.
- Structure : landmarks, lien d'évitement, titres hiérarchisés, changements de langue balisés (`lang`).
- Statuts dynamiques (ouvert/fermé, résultats des filtres) annoncés via `role="status"`.
- Un audit humain reste recommandé avant la mise en ligne.
