// USAM Nîmes Gard — preview shared JS
// Le JS du splash est inline dans chaque page (à la fin du <body>)
// pour être robuste aux caches CDN.
(function () {
  // Mobile menu toggle
  const trigger = document.querySelector('[data-mobile-toggle]');
  const drawer  = document.querySelector('[data-mobile-drawer]');
  const close   = document.querySelector('[data-mobile-close]');

  if (trigger && drawer) {
    const open = () => {
      drawer.classList.add('open');
      drawer.setAttribute('aria-hidden', 'false');
      document.body.classList.add('no-scroll');
    };
    const shut = () => {
      drawer.classList.remove('open');
      drawer.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('no-scroll');
    };
    trigger.addEventListener('click', open);
    close && close.addEventListener('click', shut);
    drawer.addEventListener('click', (e) => {
      if (e.target === drawer) shut();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') shut();
    });
  }

  // Compteur live pour le prochain match (si bandeau présent)
  const matchEl = document.querySelector('[data-match-countdown]');
  if (matchEl) {
    const target = new Date(matchEl.dataset.matchCountdown).getTime();
    const tick = () => {
      const diff = target - Date.now();
      if (diff <= 0) { matchEl.textContent = "C'est l'heure !"; return; }
      const d = Math.floor(diff / 86400000);
      const h = Math.floor((diff / 3600000) % 24);
      const m = Math.floor((diff / 60000) % 60);
      matchEl.textContent = `${d}j ${h}h ${m}min`;
    };
    tick(); setInterval(tick, 60000);
  }
})();
