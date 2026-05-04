/**
 * USAM Nîmes Gard — JS principal.
 * Léger volontairement : on évite tout framework côté front.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Toggle menu mobile
  const trigger = document.querySelector('[data-usam-mobile-toggle]');
  const nav = document.querySelector('header nav');
  if (trigger && nav) {
    trigger.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('!block');
      trigger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }
});
