(function () {
  'use strict';

  /* i18n:start — textes de l'interface (remplacés par tools/build-i18n.py pour les autres langues) */
  var T = {
    openMenu: 'Ouvrir le menu',
    closeMenu: 'Fermer le menu',
    openSoon: 'Ouvert · ferme bientôt (17h30)',
    openNow: 'Ouvert maintenant · jusqu\'à 17h30',
    closedToday: 'Fermé · ouvre à 11h00',
    closedTomorrow: 'Fermé · ouvre demain à 11h00',
    closedMonday: 'Fermé · ouvre lundi à 11h00',
    today: ' · aujourd\'hui',
    allergens: 'Allergènes :',
    notVeg: 'non végétarien',
    spicy: 'épicé',
    contains: 'contient : ',
    count: function (n) { return n + (n > 1 ? ' plats correspondent' : ' plat correspond'); },
    replay: '↺ Rejouer la démo',
    updateMsg: 'Une nouvelle version du site est disponible.',
    updateBtn: 'Mettre à jour'
  };
  /* i18n:end */

  var root = document.documentElement;
  var motionOff = function () { return root.classList.contains('motion-off'); };

  /* ---------- Bouton pause / lecture des animations ---------- */
  var motionBtn = document.getElementById('motion-toggle');
  function syncMotionBtn() { motionBtn.setAttribute('aria-pressed', String(motionOff())); }
  motionBtn.addEventListener('click', function () {
    var off = !motionOff();
    root.classList.toggle('motion-off', off);
    try { localStorage.setItem('yanji-motion', off ? 'off' : 'on'); } catch (e) {}
    syncMotionBtn();
  });
  syncMotionBtn();
  var $ = function (s, ctx) { return (ctx || document).querySelector(s); };
  var $$ = function (s, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(s)); };

  /* ---------- Header : ombre au scroll ---------- */
  var header = $('.site-header');
  var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 10); };
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------- Menu mobile ---------- */
  var toggle = $('.nav-toggle');
  var nav = $('#nav');
  function setNav(open) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? T.closeMenu : T.openMenu);
    nav.classList.toggle('is-open', open);
  }
  toggle.addEventListener('click', function () { setNav(toggle.getAttribute('aria-expanded') !== 'true'); });
  $$('a', nav).forEach(function (a) { a.addEventListener('click', function () { setNav(false); }); });

  /* ---------- Sélecteur de langue ---------- */
  var lang = $('#lang');
  var langBtn = $('.lang__btn', lang);
  langBtn.addEventListener('click', function (e) {
    e.stopPropagation();
    var open = !lang.classList.contains('is-open');
    lang.classList.toggle('is-open', open);
    langBtn.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('click', function () {
    lang.classList.remove('is-open');
    langBtn.setAttribute('aria-expanded', 'false');
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (lang.classList.contains('is-open')) {
      lang.classList.remove('is-open');
      langBtn.setAttribute('aria-expanded', 'false');
      langBtn.focus();
    }
    if (toggle.getAttribute('aria-expanded') === 'true') { setNav(false); toggle.focus(); }
  });
  // ferme le menu des langues quand le focus en sort
  lang.addEventListener('focusout', function (e) {
    if (!lang.contains(e.relatedTarget)) { lang.classList.remove('is-open'); langBtn.setAttribute('aria-expanded', 'false'); }
  });

  /* ---------- Ouvert / fermé (heure de Luxembourg) ---------- */
  function luxNow() {
    try {
      var parts = new Intl.DateTimeFormat('en-GB', {
        timeZone: 'Europe/Luxembourg', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false
      }).formatToParts(new Date());
      var get = function (t) { return (parts.filter(function (p) { return p.type === t; })[0] || {}).value; };
      var days = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
      return { day: days[get('weekday')], minutes: (parseInt(get('hour'), 10) % 24) * 60 + parseInt(get('minute'), 10) };
    } catch (e) {
      var d = new Date();
      return { day: d.getDay(), minutes: d.getHours() * 60 + d.getMinutes() };
    }
  }
  var OPEN = 11 * 60, CLOSE = 17 * 60 + 30;
  function updateStatus() {
    var now = luxNow();
    var el = $('#open-status');
    var openDay = now.day >= 1 && now.day <= 6;
    var isOpen = openDay && now.minutes >= OPEN && now.minutes < CLOSE;
    el.classList.toggle('is-open', isOpen);
    el.classList.toggle('is-closed', !isOpen);
    if (isOpen) {
      var left = CLOSE - now.minutes;
      el.textContent = left <= 45 ? T.openSoon : T.openNow;
    } else if (openDay && now.minutes < OPEN) {
      el.textContent = T.closedToday;
    } else {
      el.textContent = now.day === 6 || now.day === 0 ? T.closedMonday : T.closedTomorrow;
    }
    $$('#hours tr').forEach(function (tr) {
      var today = Number(tr.dataset.day) === now.day;
      tr.classList.toggle('is-today', today);
      var flag = tr.querySelector('.today-flag');
      if (today && !flag) {
        flag = document.createElement('span');
        flag.className = 'today-flag';
        flag.textContent = T.today;
        tr.querySelector('th').appendChild(flag);
      } else if (!today && flag) {
        flag.remove();
      }
    });
  }
  updateStatus();
  setInterval(updateStatus, 60 * 1000);

  /* ---------- Allergènes : chips générées depuis la légende ---------- */
  var ALLERGENS = {};
  $$('#allergen-legend li').forEach(function (li) {
    ALLERGENS[li.dataset.id] = {
      name: li.querySelector('span:last-child').textContent.replace(/^\d+\.\s*/, '').trim(),
      icon: li.querySelector('.ico').textContent
    };
  });
  $$('.allergens[data-list]').forEach(function (ul) {
    var ids = ul.dataset.list.split(',').filter(Boolean);
    if (!ids.length) return;
    ul.setAttribute('aria-label', 'Allergènes');
    var label = document.createElement('li');
    label.className = 'allergens__label';
    label.setAttribute('aria-hidden', 'true');
    label.textContent = T.allergens;
    label.style.background = 'none';
    ul.appendChild(label);
    ids.forEach(function (id) {
      var li = document.createElement('li');
      li.innerHTML = '<b aria-hidden="true">' + id + '</b>' + ALLERGENS[id].name;
      ul.appendChild(li);
    });
  });

  /* ---------- Filtres ---------- */
  var picker = $('#allergen-picker');
  Object.keys(ALLERGENS).forEach(function (id) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'chip chip--allergen';
    b.dataset.allergen = id;
    b.setAttribute('aria-pressed', 'false');
    b.innerHTML = '<span aria-hidden="true">' + ALLERGENS[id].icon + ' </span>' + ALLERGENS[id].name;
    picker.appendChild(b);
  });

  var dishes = $$('.dish');
  var sides = $$('.side');
  var countEl = $('#filter-count');
  function applyFilters() {
    var veg = $('[data-filter="veg"]').getAttribute('aria-pressed') === 'true';
    var mild = $('[data-filter="mild"]').getAttribute('aria-pressed') === 'true';
    var excluded = $$('.chip--allergen[aria-pressed="true"]').map(function (b) { return b.dataset.allergen; });
    var active = veg || mild || excluded.length;
    var shown = 0;

    dishes.concat(sides).forEach(function (el) {
      var reasons = [];
      var list = (el.dataset.allergens || '').split(',').filter(Boolean);
      if (veg && !el.hasAttribute('data-veg')) reasons.push(T.notVeg);
      if (mild && el.hasAttribute('data-spicy')) reasons.push(T.spicy);
      var hit = excluded.filter(function (id) { return list.indexOf(id) !== -1; });
      if (hit.length) reasons.push(T.contains + hit.map(function (id) { return ALLERGENS[id].name.toLowerCase(); }).join(', '));
      var out = reasons.length > 0;
      el.classList.toggle('is-filtered', out);
      var warn = el.querySelector('.dish__warn');
      if (warn) warn.textContent = out ? '✕ ' + reasons.join(' · ') : '';
      if (!out) shown++;
    });
    countEl.textContent = active ? T.count(shown) : '';
  }
  $$('.filters .chip').forEach(function (chip) {
    chip.addEventListener('click', function () {
      chip.setAttribute('aria-pressed', String(chip.getAttribute('aria-pressed') !== 'true'));
      applyFilters();
    });
  });

  /* ---------- Images : illustration de secours si la photo ne charge pas ---------- */
  $$('.dish__media img').forEach(function (img) {
    var fail = function () { img.parentNode.classList.add('is-fallback'); };
    img.addEventListener('error', fail);
    if (img.complete && img.naturalWidth === 0) fail();
  });

  /* ---------- Révélation au scroll ---------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    // léger décalage en cascade dans une même grille
    $$('.reveal').forEach(function (el) {
      var siblings = el.parentNode ? $$(':scope > .reveal', el.parentNode) : [];
      var i = siblings.indexOf(el);
      if (i > 0) el.style.transitionDelay = Math.min(i, 6) * 70 + 'ms';
      io.observe(el);
    });
  } else {
    $$('.reveal').forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ---------- Onglets de la carte : section active ----------
     Le scrollspy se met en pause pendant les défilements déclenchés par un lien :
     sinon, recentrer la barre d'onglets en douceur annule (dans Chrome) le
     défilement fluide de la page, qui s'arrête en route. */
  var tabs = $$('.menu-tabs a');
  var menuSections = $$('.menu-section');
  var spyPaused = false, spyTimer = null;

  function setActiveTab(id) {
    tabs.forEach(function (t) {
      var on = t.getAttribute('href') === '#' + id;
      t.classList.toggle('is-active', on);
      if (on) {
        t.setAttribute('aria-current', 'true');
        var bar = t.parentNode;
        // défilement instantané : n'interrompt pas celui de la page
        bar.scrollLeft = t.offsetLeft - bar.clientWidth / 2 + t.clientWidth / 2;
      } else {
        t.removeAttribute('aria-current');
      }
    });
  }

  function currentSection() {
    var line = window.innerHeight * 0.45, found = null;
    menuSections.forEach(function (sec) {
      var r = sec.getBoundingClientRect();
      if (r.top <= line && r.bottom > line) found = sec.id;
    });
    return found;
  }

  var ticking = false;
  function onSpyScroll() {
    if (spyPaused || ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      ticking = false;
      setActiveTab(currentSection());
    });
  }

  function resumeSpy() {
    clearTimeout(spyTimer);
    window.removeEventListener('scrollend', resumeSpy);
    spyPaused = false;
    onSpyScroll();
  }

  function pauseSpy() {
    spyPaused = true;
    clearTimeout(spyTimer);
    if ('onscrollend' in window) window.addEventListener('scrollend', resumeSpy);
    spyTimer = setTimeout(resumeSpy, 1500); // filet de sécurité
  }

  // Tout lien interne (onglets, menu principal, boutons) met le scrollspy en pause
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a) return;
    pauseSpy();
    var id = a.getAttribute('href').slice(1);
    if (a.parentNode.classList.contains('menu-tabs')) setActiveTab(id);
  });

  window.addEventListener('scroll', onSpyScroll, { passive: true });

  /* ---------- Cœurs coréens (finger heart) ---------- */
  var heartPanel = $('#heart-panel');
  function popHearts(x, y) {
    if (motionOff()) return;
    for (var i = 0; i < 6; i++) {
      var h = document.createElement('span');
      h.className = 'floating-heart';
      h.textContent = '♥';
      h.style.left = (x - 10 + (Math.random() * 40 - 20)) + 'px';
      h.style.top = (y - 10) + 'px';
      h.style.setProperty('--dx', (Math.random() * 80 - 40) + 'px');
      h.style.setProperty('--r', (Math.random() * 60 - 30) + 'deg');
      h.style.animationDelay = (i * 60) + 'ms';
      h.style.color = ['#fff', '#f5a9c4', '#f7c948'][i % 3];
      heartPanel.appendChild(h);
      h.addEventListener('animationend', function () { this.remove(); });
    }
  }
  heartPanel.addEventListener('click', function (e) {
    var r = heartPanel.getBoundingClientRect();
    popHearts(e.clientX - r.left, e.clientY - r.top);
  });
  setTimeout(function () { popHearts(heartPanel.clientWidth / 2, heartPanel.clientHeight / 3); }, 1400);

  /* ---------- Démo bibimbap ---------- */
  var stage = $('#bowl-stage');
  var steps = $$('.step');
  var playBtn = $('#bowl-play');
  var timers = [];
  function setStep(n) {
    stage.classList.remove('step-1', 'step-2', 'is-mixed');
    if (n >= 1) stage.classList.add('step-1');
    if (n >= 2) stage.classList.add('step-2');
    if (n >= 3) stage.classList.add('is-mixed');
    steps.forEach(function (s) { s.classList.toggle('is-active', Number(s.dataset.step) === n); });
  }
  function play() {
    timers.forEach(clearTimeout);
    setStep(0);
    // force reflow pour relancer les animations
    void stage.offsetWidth;
    timers = [
      setTimeout(function () { setStep(1); }, 300),
      setTimeout(function () { setStep(2); }, 1500),
      setTimeout(function () { setStep(2); stage.classList.add('is-mixed'); steps.forEach(function (s) { s.classList.toggle('is-active', s.dataset.step === '3'); }); }, 2200)
    ];
    playBtn.textContent = T.replay;
  }
  playBtn.addEventListener('click', play);
  steps.forEach(function (s) {
    s.addEventListener('mouseenter', function () { if (!timers.length) setStep(Number(s.dataset.step)); });
  });
  if ('IntersectionObserver' in window && !motionOff()) {
    var autoPlay = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) { play(); autoPlay.disconnect(); }
    }, { threshold: 0.5 });
    autoPlay.observe(stage);
  }

  /* ---------- Easter egg : nurungji ----------
     Clic / tap / Entrée : ouvre et garde ouvert. Survol (souris) : ouvre tant que
     le pointeur reste sur le bol ou la bulle. Échap ou clic ailleurs : ferme. */
  var nuruBtn = $('#nurungji-btn');
  var nuruTip = $('#nurungji-tip');
  var nuruPinned = false;
  function setNurungji(open) {
    nuruTip.hidden = !open;
    nuruBtn.setAttribute('aria-expanded', String(open));
    stage.classList.toggle('show-crust', open);
    if (!open) nuruPinned = false;
  }
  nuruBtn.addEventListener('click', function () {
    var open = nuruTip.hidden || !nuruPinned;
    nuruPinned = open;
    setNurungji(open);
  });
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    stage.addEventListener('mouseenter', function () { if (nuruTip.hidden) setNurungji(true); });
    stage.addEventListener('mouseleave', function () { if (!nuruPinned) setNurungji(false); });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !nuruTip.hidden) {
      var inside = stage.contains(document.activeElement);
      setNurungji(false);
      if (inside) nuruBtn.focus();
    }
  });
  document.addEventListener('click', function (e) {
    if (!nuruTip.hidden && !stage.contains(e.target)) setNurungji(false);
  });

  /* ---------- Modale avant appel ----------
     Tous les liens tel: passent d'abord par la modale (sauf celui de la modale).
     Sans <dialog> natif ni JS, les liens appellent directement. */
  var callDialog = $('#call-dialog');
  var callInvoker = null;
  if (callDialog && typeof callDialog.showModal === 'function') {
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href^="tel:"]');
      if (!a || callDialog.contains(a)) return;
      e.preventDefault();
      callInvoker = a;
      callDialog.showModal();
      $('#call-dialog-confirm').focus();
    });
    $('#call-dialog-cancel').addEventListener('click', function () { callDialog.close(); });
    $('#call-dialog-confirm').addEventListener('click', function () {
      // laisse partir l'appel, puis ferme la modale
      setTimeout(function () { callDialog.close(); }, 300);
    });
    // clic sur le fond sombre = fermer
    callDialog.addEventListener('click', function (e) { if (e.target === callDialog) callDialog.close(); });
    callDialog.addEventListener('close', function () {
      // différé : le navigateur restaure lui-même un focus à la fermeture
      var el = callInvoker;
      callInvoker = null;
      setTimeout(function () { if (el && document.contains(el)) el.focus(); }, 0);
    });
  }

  /* ---------- Pétales d'hibiscus ---------- */
  (function () {
    var petals = $('#petals');
    for (var i = 0; i < 14; i++) {
      var p = document.createElement('span');
      p.className = 'petal';
      p.style.left = Math.random() * 100 + '%';
      p.style.animationDuration = (9 + Math.random() * 10) + 's';
      p.style.animationDelay = (-Math.random() * 18) + 's';
      p.style.setProperty('--drift', (Math.random() * 160 - 80) + 'px');
      var size = 8 + Math.random() * 10;
      p.style.width = p.style.height = size + 'px';
      petals.appendChild(p);
    }
  })();

  /* ---------- Mentions légales : ouverture via l'ancre #mentions-legales ---------- */
  var legal = document.getElementById('mentions-legales');
  function openLegalFromHash() {
    if (location.hash === '#mentions-legales') { legal.open = true; legal.scrollIntoView(); }
  }
  window.addEventListener('hashchange', openLegalFromHash);
  openLegalFromHash();

  /* ---------- État initial dépendant du scroll ----------
     Différé après le chargement : lire scrollY / getBoundingClientRect pendant
     l'exécution du script forcerait un calcul de mise en page anticipé
     (« forced reflow »). Utile seulement si la page s'ouvre déjà scrollée. */
  window.addEventListener('load', function () {
    requestAnimationFrame(function () { onScroll(); onSpyScroll(); });
  });

  /* ---------- Année ---------- */
  $('#year').textContent = new Date().getFullYear();

  /* =========================================================
     PWA : service worker, mise à jour, bannière d'installation
     ========================================================= */
  var ROOT = document.documentElement.getAttribute('data-root') || './';
  var isStandalone = window.matchMedia('(display-mode: standalone)').matches || navigator.standalone === true;

  /* ---------- Service worker + mise à jour ----------
     Une nouvelle version s'installe en arrière-plan puis attend : on propose
     de l'activer au lieu de recharger la page sans prévenir. */
  var updateToast = $('#update-toast');
  var userAskedUpdate = false;
  function offerUpdate(worker) {
    updateToast.innerHTML = '<p></p><button class="btn btn--yellow btn--small" type="button"></button>';
    updateToast.querySelector('p').textContent = T.updateMsg;
    var btn = updateToast.querySelector('button');
    btn.textContent = T.updateBtn;
    btn.addEventListener('click', function () {
      userAskedUpdate = true;
      btn.disabled = true;
      worker.postMessage({ type: 'SKIP_WAITING' });
    });
  }
  if ('serviceWorker' in navigator && location.protocol !== 'file:') {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register(ROOT + 'sw.js', { scope: ROOT }).then(function (reg) {
        if (reg.waiting && navigator.serviceWorker.controller) offerUpdate(reg.waiting);
        reg.addEventListener('updatefound', function () {
          var worker = reg.installing;
          if (!worker) return;
          worker.addEventListener('statechange', function () {
            // « installed » avec un contrôleur existant = mise à jour prête
            if (worker.state === 'installed' && navigator.serviceWorker.controller) offerUpdate(worker);
          });
        });
        // vérifie les mises à jour quand on revient sur l'onglet / l'app
        document.addEventListener('visibilitychange', function () {
          if (document.visibilityState === 'visible') reg.update().catch(function () {});
        });
      }).catch(function () {});
      navigator.serviceWorker.addEventListener('controllerchange', function () {
        if (userAskedUpdate) location.reload();
      });
    });
  }

  /* ---------- Bannière d'installation ----------
     Chrome / Edge / Android : invite native (beforeinstallprompt).
     iPhone / iPad (Safari) : explication « Partager > Sur l'écran d'accueil ».
     Affichée une fois arrivé à la fin de la carte ; « Plus tard » = 30 jours. */
  var banner = $('#install-banner');
  var DISMISS_KEY = 'yanji-install-dismissed';
  var deferredPrompt = null;
  var isIOS = /iphone|ipad|ipod/i.test(navigator.userAgent) ||
              (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var reachedMenuEnd = false;

  function recentlyDismissed() {
    try { return Date.now() - Number(localStorage.getItem(DISMISS_KEY) || 0) < 30 * 24 * 3600 * 1000; }
    catch (e) { return false; }
  }
  function canInstall() { return deferredPrompt || (isIOS && !isStandalone); }
  function showBanner() {
    if (!banner.hidden || isStandalone || recentlyDismissed() || !reachedMenuEnd || !canInstall()) return;
    var mode = deferredPrompt ? 'prompt' : 'ios';
    $$('[data-install]', banner).forEach(function (el) { el.hidden = el.getAttribute('data-install') !== mode; });
    banner.hidden = false;
    document.body.classList.add('has-install-banner');
  }
  function hideBanner(remember) {
    banner.hidden = true;
    document.body.classList.remove('has-install-banner');
    if (remember) { try { localStorage.setItem(DISMISS_KEY, String(Date.now())); } catch (e) {} }
  }

  window.addEventListener('beforeinstallprompt', function (e) {
    e.preventDefault(); // on garde l'invite pour le bon moment
    deferredPrompt = e;
    showBanner();
  });
  window.addEventListener('appinstalled', function () { deferredPrompt = null; hideBanner(false); });

  $('#install-accept').addEventListener('click', function () {
    if (!deferredPrompt) return;
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then(function (choice) {
      hideBanner(choice.outcome !== 'accepted');
      deferredPrompt = null;
    });
  });
  $('#install-dismiss').addEventListener('click', function () { hideBanner(true); });
  banner.addEventListener('keydown', function (e) { if (e.key === 'Escape') hideBanner(true); });

  if (!isStandalone && 'IntersectionObserver' in window) {
    var menuEnd = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) {
        reachedMenuEnd = true;
        menuEnd.disconnect();
        showBanner();
      }
    }, { threshold: 0.25 });
    menuEnd.observe($('#allergenes'));
  }
})();
