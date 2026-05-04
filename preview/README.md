# Preview HTML — USAM Nîmes Gard

Maquettes statiques pour visualiser le rendu **immédiatement**, sans installer WordPress, PHP ou Node.

## Comment ouvrir

**Option 1 — Double-clic (le plus simple)**

Ouvre `preview/index.html` dans ton navigateur (Chrome, Firefox, Safari, Edge).
Pas de serveur à lancer, pas de build, ça marche en `file://`.

**Option 2 — Serveur local (recommandé pour tester sur ton téléphone)**

```bash
cd preview
python3 -m http.server 8080
# puis ouvre http://localhost:8080 dans ton navigateur
# pour ton téléphone : http://<ton-ip-locale>:8080
```

Ou avec Node :
```bash
cd preview
npx serve -p 8080
```

## Pages disponibles

| Fichier                          | Description                                              |
| -------------------------------- | -------------------------------------------------------- |
| `index.html`                     | Page d'accueil — hero, prochain match, équipes, actus, Le Parnasse, partenaires, newsletter |
| `le-club.html`                   | Page Le Club — histoire, palmarès, projet, contacts      |
| `equipe-pro-masculine.html`      | Effectif Green Team — 15 joueurs, calendrier court       |
| `actu-exemple.html`              | Détail d'une actualité (Bastien Lafosse signature)       |

## Tester le mobile

3 façons de simuler un mobile :

1. **DevTools navigateur** (F12 → bouton "Toggle device toolbar" → choisir iPhone, Pixel, etc.)
2. **Réduire la fenêtre** à 375px de large pour voir le responsive en live.
3. **Ouvrir sur ton vrai téléphone** via l'option 2 du serveur local + IP locale.

Points testés et fonctionnels en mobile :
- ✅ Menu hamburger avec drawer (slide depuis la droite)
- ✅ Touch targets ≥ 44px
- ✅ Typo qui s'adapte (clamp)
- ✅ Pas de scroll horizontal
- ✅ Le bandeau "Prochain match" se reformate en colonne
- ✅ Les grilles équipes/actus passent en 1 colonne sous 640px

## Stack utilisée pour la preview

- **Tailwind CSS** via CDN (script `cdn.tailwindcss.com`) — config injectée inline pour la palette USAM
- **Google Fonts** pour Anton, Sora et Inter
- **Vanilla JS** (~30 lignes) pour le menu mobile et le compteur match
- Logo USAM en **SVG inline** dans le header/footer

## Différences avec la version WordPress finale

Cette preview est **du HTML statique**. Le vrai site WordPress (dossier `wp-theme/`) :
- Auto-rempli depuis le back-office WordPress (CMS)
- Polices self-hostées (RGPD)
- Tailwind compilé en local (pas de CDN externe en prod)
- Custom Post Types pour joueurs, matchs, partenaires
- Compteur match alimenté par les données du back-office

## Limites connues

- Les images sont des placeholders (gradients colorés). Les vraies photos seront uploadées via WordPress.
- Le formulaire newsletter n'envoie rien (preview).
- Le menu de navigation pointe vers les 4 pages disponibles, les autres liens sont en `href="#"`.
