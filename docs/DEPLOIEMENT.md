# Déploiement OVH

## Architecture cible

```
[Code thème]                       [Hébergement OVH Performance]
GitHub repo  ──── push main ───►   /www/wp-content/themes/usam/
                                   /www/wp-content/uploads/        (médias, jamais en git)
                                   /www/wp-config.php              (jamais en git)
```

- WordPress installé en racine du domaine (ou sous-domaine `dev.usam-nimes.fr` pour la recette).
- Le thème custom **est** le seul code qui transite par Git.
- Les uploads (médias) sont gérés en SFTP / via le back-office WordPress.

---

## Prérequis OVH

1. Souscrire un plan **OVH Hébergement Performance** (10/12€ HT / mois) — minimum 1.
   - PHP 8.2 ou 8.3
   - MySQL 8 ou MariaDB 10.x
   - SFTP + SSH
   - Espace disque : 250 Go (largement suffisant)
   - Mail pro inclus (10 boîtes)
2. Domaine `usam-nimes.fr` (ou autre) acheté chez OVH.
3. Sous-domaine `dev.usam-nimes.fr` créé (DNS chez OVH).
4. Certificat SSL Let's Encrypt activé (gratuit, en 1 clic dans le manager OVH).
5. Base de données MySQL créée pour WordPress (1 par environnement : `usamprod`, `usamdev`).

---

## Installation initiale

### 1. WordPress sur OVH

```bash
# Via SSH OVH
ssh utilisateur@ssh.cluster0XX.hosting.ovh.net
cd ~/www/dev/   # racine du sous-domaine dev
wget https://fr.wordpress.org/latest-fr_FR.tar.gz
tar xzf latest-fr_FR.tar.gz --strip-components=1
rm latest-fr_FR.tar.gz
```

Puis ouvrir `https://dev.usam-nimes.fr/` → assistant d'installation WP.

### 2. Déposer le thème

```bash
# Depuis ce repo en local, builder le CSS
cd wp-theme
npm install
npm run build

# Uploader en SFTP le dossier wp-theme renommé "usam"
# vers /www/dev/wp-content/themes/usam/
```

Activer le thème dans `wp-admin → Apparence → Thèmes`.

---

## Déploiement continu (CI/CD)

À mettre en place via GitHub Actions :

```yaml
# .github/workflows/deploy.yml (à créer)
name: Deploy theme to OVH
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: cd wp-theme && npm ci && npm run build
      - name: SFTP upload
        uses: SamKirkland/FTP-Deploy-Action@v4.3.5
        with:
          server: ftp.cluster0XX.hosting.ovh.net
          username: ${{ secrets.OVH_FTP_USER }}
          password: ${{ secrets.OVH_FTP_PASS }}
          local-dir: ./wp-theme/
          server-dir: ./www/dev/wp-content/themes/usam/
          exclude: |
            **/node_modules/**
            **/*.md
            **/package*.json
            **/tailwind.config.js
            **/assets/css/input.css
```

Secrets à configurer dans GitHub :
- `OVH_FTP_USER`
- `OVH_FTP_PASS`
- (plus tard) `OVH_FTP_USER_PROD` / `OVH_FTP_PASS_PROD`

---

## Stratégie d'environnements

| Env       | URL                       | Branche Git | Base de données |
| --------- | ------------------------- | ----------- | --------------- |
| Dev       | `dev.usam-nimes.fr`       | `claude/usam-nimes-website-Vlhoo` (puis `develop`) | `usamdev` |
| Recette   | `staging.usam-nimes.fr`   | `staging`   | `usamstaging`   |
| Prod      | `www.usam-nimes.fr`       | `main`      | `usamprod`      |

---

## Backups

- **Quotidien automatique** : OVH propose un add-on backup quotidien (~3€/mois). À activer.
- **Hebdo manuel** : export complet via UpdraftPlus → S3 / Backblaze (option).
- **Code** : déjà versionné sur GitHub.

---

## Monitoring

À mettre en place plus tard :
- **Uptime** : UptimeRobot (gratuit) avec alerte mail/Slack
- **Performance** : Lighthouse CI dans GitHub Actions
- **Sécurité** : Wordfence ou iThemes Security (plugin WP)
