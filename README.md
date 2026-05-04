# USAM Nîmes Gard — Refonte du site officiel

Projet de refonte complète du site web de l'**USAM Nîmes Gard**, club professionnel de handball basé à Nîmes (Gard, 30), évoluant en Liqui Moly Starligue.

> Branche de dev : `claude/usam-nimes-website-Vlhoo`
> Domaine de dev visé : `dev.usam-nimes.fr`
> Domaine de prod actuel : `usam-nimesgard.fr`

---

## Stack technique

| Brique          | Choix                                    | Pourquoi                                                  |
| --------------- | ---------------------------------------- | --------------------------------------------------------- |
| CMS             | **WordPress 6.x**                        | Le plus simple à apprendre pour une équipe non-technique  |
| Thème           | **Custom (PHP + Tailwind CSS)**          | Refonte complète, 0 thème générique                       |
| Build CSS       | **Tailwind CLI**                         | Compilation locale, pas de Node en prod                   |
| Hébergement     | **OVH Performance** (mutualisé)          | RGPD, datacenter français, support FR, ~10€/mois          |
| Domaine         | OVH                                      | Tout au même endroit                                      |
| Déploiement     | **GitHub Action → SFTP OVH**             | Push sur `main` = déploiement auto                        |
| Versioning      | Git (ce repo)                            | Le code et les contenus de référence                      |

---

## Arborescence du repo

```
mikab/
├─ wp-theme/               # Thème WordPress custom (à uploader dans wp-content/themes/usam/)
│  ├─ style.css            # En-tête de thème WP
│  ├─ functions.php        # Hooks, enqueue assets, custom post types
│  ├─ index.php            # Fallback
│  ├─ header.php           # En-tête commune
│  ├─ footer.php           # Pied commun
│  ├─ front-page.php       # Page d'accueil
│  ├─ page.php             # Pages classiques
│  ├─ single.php           # Article de blog (actu)
│  ├─ archive.php          # Liste d'articles
│  ├─ template-parts/      # Composants réutilisables
│  ├─ templates/           # Templates de pages spécifiques (équipes, joueurs, etc.)
│  ├─ inc/                 # Code PHP modulaire (CPT, ACF, helpers)
│  ├─ assets/
│  │  ├─ css/              # Tailwind compilé
│  │  ├─ js/               # JS custom léger
│  │  └─ images/           # Images statiques (logo, icônes)
│  └─ tailwind.config.js   # Configuration Tailwind avec palette USAM
├─ wp-content-mu-plugins/  # Plugins maison (custom post types, helpers)
├─ design/                 # Charte graphique et logos
│  ├─ IDENTITE.md          # Référence palette + typo + ton
│  ├─ logo-monogramme.svg  # Logo principal (premier jet)
│  └─ logo-horizontal.svg  # Variante horizontale
├─ content/                # Contenu de référence (markdown)
│  ├─ pages/               # Pages statiques (à coller dans WP)
│  ├─ actus/               # Actualités aspirées du site actuel
│  ├─ equipes/             # Données d'équipes / joueurs
│  └─ partenaires/         # Liste des sponsors par catégorie
├─ docs/                   # Documentation pour l'équipe
│  ├─ CMS-GUIDE.md         # Guide WordPress pour les non-tech
│  ├─ DEPLOIEMENT.md       # Comment déployer sur OVH
│  └─ ROADMAP.md           # Phases du projet
├─ scripts/
│  └─ deploy-ovh.sh        # Script de push SFTP
└─ README.md               # Ce fichier
```

---

## Statut actuel

- [x] Recherche & cadrage
- [x] Choix de la stack
- [x] Identité visuelle (palette + typo)
- [x] Aspiration du contenu existant
- [x] Squelette du thème WordPress
- [ ] Intégration de la home complète
- [ ] Pages équipes (Pro M, Pro F, N1, N3, École)
- [ ] Custom Post Types (joueurs, matchs, sponsors)
- [ ] Connexion API LNH (calendrier / classement auto)
- [ ] Déploiement OVH
- [ ] Recette + go live

---

## Pour démarrer en local

```bash
# 1. Installer WordPress en local (LocalWP, MAMP, ou Docker)
# 2. Cloner ce repo dans wp-content/
git clone <repo> wp-content/themes/usam-tmp
# 3. Lier ce dossier au thème :
cp -r wp-theme wp-content/themes/usam
# 4. Compiler le CSS (Tailwind CLI)
cd wp-theme && npx tailwindcss -i ./assets/css/input.css -o ./assets/css/main.css --watch
# 5. Activer le thème "USAM" dans /wp-admin → Apparence → Thèmes
```

---

## Phases prévues

1. **Phase 1 — Vitrine (en cours)** : site public, contenu, design, déploiement OVH
2. **Phase 2 — Billetterie intégrée** : module Stripe + plan de salle Le Parnasse
3. **Phase 3 — Automatisations club** : CRM supporters, automation marketing, gestion bénévoles
4. **Phase 4 — App mobile + extensions** : selon ROI

Voir [docs/ROADMAP.md](docs/ROADMAP.md).
