/* Service worker Yanji Korean Food
   - Pré-cache : les 4 langues, polices, icônes, manifestes.
   - Pages : réseau d'abord (contenu à jour), cache en secours hors connexion.
   - Fichiers statiques : cache d'abord.
   - Mise à jour : la nouvelle version attend que l'utilisateur clique sur
     « Mettre à jour » (message SKIP_WAITING envoyé par la page).
   __VERSION__ et __PRECACHE__ sont remplacés par tools/minify.mjs. */
'use strict';

const VERSION = '__VERSION__';
const CACHE = 'yanji-' + VERSION;
const PRECACHE = __PRECACHE__;
const NETWORK_TIMEOUT = 4000; // au-delà, on sert la page en cache

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(PRECACHE)));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('yanji-') && k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') self.skipWaiting();
});

function timeout(ms) {
  return new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), ms));
}

async function networkFirst(request) {
  const cache = await caches.open(CACHE);
  try {
    const response = await Promise.race([fetch(request), timeout(NETWORK_TIMEOUT)]);
    if (response && response.ok) cache.put(request, response.clone());
    return response;
  } catch (err) {
    const cached = await cache.match(request, { ignoreSearch: true });
    // dernier recours : la page française
    return cached || cache.match(new URL('./', self.registration.scope).href);
  }
}

async function cacheFirst(request) {
  const cache = await caches.open(CACHE);
  const cached = await cache.match(request);
  if (cached) return cached;
  const response = await fetch(request);
  if (response && response.ok) cache.put(request, response.clone());
  return response;
}

self.addEventListener('fetch', (event) => {
  const { request } = event;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return; // photos Wikimedia, Google Maps… : navigateur
  if (request.mode === 'navigate') {
    event.respondWith(networkFirst(request));
  } else {
    event.respondWith(cacheFirst(request));
  }
});
