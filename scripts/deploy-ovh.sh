#!/usr/bin/env bash
#
# Déploiement manuel du thème vers OVH via SFTP/lftp.
# Pour le déploiement automatique, voir docs/DEPLOIEMENT.md (GitHub Actions).
#
# Usage :
#   ENVFILE=.env.dev ./scripts/deploy-ovh.sh
#   ENVFILE=.env.prod ./scripts/deploy-ovh.sh
#
# Variables attendues dans le fichier .env :
#   OVH_HOST=ftp.cluster0XX.hosting.ovh.net
#   OVH_USER=...
#   OVH_PASS=...
#   OVH_REMOTE=/www/dev/wp-content/themes/usam

set -euo pipefail

ENVFILE="${ENVFILE:-.env.dev}"
if [[ ! -f "$ENVFILE" ]]; then
  echo "Fichier d'env introuvable : $ENVFILE" >&2
  exit 1
fi

# shellcheck disable=SC1090
source "$ENVFILE"

: "${OVH_HOST:?OVH_HOST manquant}"
: "${OVH_USER:?OVH_USER manquant}"
: "${OVH_PASS:?OVH_PASS manquant}"
: "${OVH_REMOTE:?OVH_REMOTE manquant}"

echo "→ Build CSS"
( cd wp-theme && npm ci && npm run build )

echo "→ Sync SFTP vers $OVH_HOST:$OVH_REMOTE"
lftp -u "$OVH_USER","$OVH_PASS" "sftp://$OVH_HOST" <<EOF
set sftp:auto-confirm yes
mirror --reverse --delete --verbose \
  --exclude-glob node_modules/ \
  --exclude-glob package*.json \
  --exclude-glob tailwind.config.js \
  --exclude-glob '*.md' \
  --exclude-glob 'assets/css/input.css' \
  wp-theme/ "$OVH_REMOTE"
bye
EOF

echo "✔ Déploiement terminé."
