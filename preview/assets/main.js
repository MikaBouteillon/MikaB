// USAM Nîmes Gard — preview shared JS
(function () {
  // Splash d'arrivée
  const splash = document.querySelector('[data-splash]');
  if (splash) {
    const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const seen   = sessionStorage.getItem('usam-splash-seen') === '1';

    if (reduce || seen) {
      splash.remove();
    } else {
      document.body.classList.add('no-scroll');

      const dismiss = () => {
        if (splash.classList.contains('gone')) return;
        splash.classList.add('gone');
        document.body.classList.remove('no-scroll');
        sessionStorage.setItem('usam-splash-seen', '1');
        setTimeout(() => splash.remove(), 700);
      };

      const auto = setTimeout(dismiss, 2600);
      splash.addEventListener('click', () => { clearTimeout(auto); dismiss(); });
      splash.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ' || e.key === 'Escape') {
          clearTimeout(auto); dismiss();
        }
      });
    }
  }

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
