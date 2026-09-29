#!/usr/bin/env node
/*
 * Minifie les pages générées par tools/build-i18n.py et produit le service worker.
 *
 *   npm run build   (build-i18n.py puis ce script)
 *
 * - index.html, en/, ko/, zh/ : HTML, CSS et JS inline minifiés, JSON-LD compacté.
 * - Manifestes : JSON compacté.
 * - sw.js : généré depuis src/sw.js avec la liste des fichiers à pré-cacher et
 *   une version = empreinte de leur contenu. Tout changement du site change
 *   l'empreinte, donc le service worker : les visiteurs se voient proposer la
 *   mise à jour.
 */
import { readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { minify as minifyHtml } from 'html-minifier-terser';
import { minify as minifyJs } from 'terser';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const LANG_DIRS = ['', 'en/', 'ko/', 'zh/'];

// Fichiers pré-cachés par le service worker (chemins relatifs à sw.js)
const PRECACHE = [
  ...LANG_DIRS.map((d) => d || './'),
  ...LANG_DIRS.map((d) => `${d}manifest.webmanifest`),
  'assets/fonts/anton-latin.woff2',
  'assets/fonts/anton-latin-ext.woff2',
  'assets/fonts/nunito-latin.woff2',
  'assets/fonts/nunito-latin-ext.woff2',
  'assets/fonts/permanent-marker-latin.woff2',
  'assets/favicon.svg',
  'assets/apple-touch-icon.png',
  'assets/icons/icon-192.png',
  'assets/icons/icon-512.png',
  'assets/icons/icon-maskable-512.png',
];

const HTML_OPTIONS = {
  collapseWhitespace: true,
  conservativeCollapse: true, // garde un espace entre éléments en ligne
  removeComments: true,
  collapseBooleanAttributes: true,
  minifyCSS: true,
  minifyJS: true,
  sortClassName: false,
};

const kb = (n) => `${(n / 1024).toFixed(1)} Ko`;

async function minifyPage(dir) {
  const file = join(ROOT, dir, 'index.html');
  const src = await readFile(file, 'utf8');
  // JSON-LD : compacté à part (le minifieur HTML n'y touche pas)
  const withJson = src.replace(
    /(<script type="application\/ld\+json">)([\s\S]*?)(<\/script>)/,
    (_, open, json, close) => open + JSON.stringify(JSON.parse(json)) + close
  );
  const out = await minifyHtml(withJson, HTML_OPTIONS);
  await writeFile(file, out);
  console.log(`[minify] ${dir || './'}index.html  ${kb(src.length)} → ${kb(out.length)}`);
}

async function minifyManifest(dir) {
  const file = join(ROOT, dir, 'manifest.webmanifest');
  const json = JSON.parse(await readFile(file, 'utf8'));
  await writeFile(file, JSON.stringify(json));
}

async function buildServiceWorker() {
  const hash = createHash('sha256');
  for (const path of PRECACHE) {
    const file = path === './' ? 'index.html' : path.endsWith('/') ? `${path}index.html` : path;
    hash.update(path).update(await readFile(join(ROOT, file)));
  }
  const version = hash.digest('hex').slice(0, 12);
  const src = await readFile(join(ROOT, 'src/sw.js'), 'utf8');
  const code = src
    .replace("const VERSION = '__VERSION__';", `const VERSION = ${JSON.stringify(version)};`)
    .replace('const PRECACHE = __PRECACHE__;', `const PRECACHE = ${JSON.stringify(PRECACHE)};`);
  if (code.includes("= '__VERSION__'") || code.includes('= __PRECACHE__')) throw new Error('sw.js : marqueurs non remplacés');
  const { code: min } = await minifyJs(code, { ecma: 2018, compress: true, mangle: true });
  await writeFile(join(ROOT, 'sw.js'), min);
  console.log(`[minify] sw.js  version ${version}, ${PRECACHE.length} fichiers pré-cachés`);
}

for (const dir of LANG_DIRS) await minifyPage(dir);
for (const dir of LANG_DIRS) await minifyManifest(dir);
await buildServiceWorker();
