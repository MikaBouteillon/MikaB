# Roadmap projet — USAM Nîmes Gard

## Phase 1 — Site vitrine (en cours)

**Objectif :** un site moderne, performant, éditable par l'équipe non technique, en ligne sur `dev.usam-nimes.fr`.

- [x] Cadrage stack & identité visuelle
- [x] Charte graphique (palette, typo, ton)
- [x] Structure du repo
- [x] Logo de départ (à itérer avec un graphiste)
- [x] Squelette du thème WordPress
- [ ] Polices self-hostées dans `assets/fonts/`
- [ ] Templates dédiés équipes / joueurs / matchs
- [ ] Intégration complète des pages : Le Club, Équipes, École, Partenaires, Contact
- [ ] Page Le Parnasse (visite virtuelle, plan, accès)
- [ ] Formulaire de contact (Contact Form 7 + reCAPTCHA)
- [ ] Newsletter (Brevo / Mailchimp)
- [ ] SEO de base (Yoast, sitemap, OpenGraph, Schema.org SportsTeam)
- [ ] RGPD : bandeau cookies, mentions légales, politique de confidentialité
- [ ] Performance : Lighthouse > 90 sur toutes les pages
- [ ] Accessibilité : audit WCAG AA
- [ ] Mise en ligne `dev.usam-nimes.fr`
- [ ] Recette avec l'équipe USAM
- [ ] Migration prod sur `www.usam-nimes.fr`
- [ ] Redirection 301 depuis `usam-nimesgard.fr`

## Phase 2 — Billetterie intégrée

**Objectif :** reprendre la main sur la billetterie au lieu de pointer vers une plateforme tierce.

- [ ] Audit du système actuel (Mapado / Weezevent ?)
- [ ] Choix : Stripe direct OU plateforme spécialisée billetterie
- [ ] Plan de salle SVG interactif du Parnasse
- [ ] Gestion des abonnements saison (catégories, packs famille)
- [ ] Marketplace de revente entre abonnés
- [ ] App mobile staff pour scanner QR codes à l'entrée
- [ ] Tableau de bord ventes en temps réel

## Phase 3 — Automatisations club

**Objectif :** un back-office unifié qui fait tourner le club.

- [ ] CRM supporters (PostgreSQL via Supabase)
- [ ] Sync billetterie + boutique → CRM
- [ ] Email/SMS automation (J-7, J-1, J+1 match)
- [ ] Publication multi-canal automatique (compo → site + IG + FB + X)
- [ ] Pige automatique résultats LNH / FFHB
- [ ] Espace partenaires : reporting mensuel auto
- [ ] Gestion bénévoles (planning, badges, pointage)
- [ ] Inscriptions école de hand en ligne (paiement échelonné)

## Phase 4 — Extensions

- [ ] App mobile officielle (React Native)
- [ ] Programme fidélité "Green Citizens"
- [ ] Live streaming jeunes / féminines (YouTube)
- [ ] Studio contenu (podcast, mini-docs)
- [ ] Plateforme RSE Gard

---

## Priorités à confirmer avec le porteur

1. Faut-il commencer la phase 2 dès que la phase 1 est en ligne, ou attendre la saison suivante ?
2. La billetterie maison vs plateforme tierce → ROI à modéliser.
3. App mobile : besoin réel ou une bonne PWA suffit ?
