# Identité visuelle USAM Nîmes Gard — Refonte 2026

Direction artistique : **"Néo-green"**. On garde l'ADN vert historique du club mais on le passe en mode vif, électrique, moderne. L'objectif est d'avoir une identité qui claque autant sur un panneau LED dans Le Parnasse que sur un story Instagram.

---

## 1. Palette principale

| Rôle             | Nom         | HEX        | Usage                                       |
| ---------------- | ----------- | ---------- | ------------------------------------------- |
| Vert primaire    | Volt Green  | `#00E676`  | Logo, CTA principaux, surlignage, accents   |
| Vert profond    | Forest      | `#0B3D2E`  | Texte sur fond clair, fonds sombres         |
| Noir charbon    | Charcoal    | `#0A0A0A`  | Hero sombre, texte noir, fonds vidéo        |
| Blanc cassé     | Bone        | `#F5F5F0`  | Fond clair, contraste                       |
| Jaune accent    | Volt Yellow | `#E8FF59`  | CTA secondaire (billetterie), surlignage    |
| Gris UI         | Slate 200   | `#E2E8F0`  | Bordures, séparateurs, placeholders         |
| Gris UI foncé   | Slate 700   | `#334155`  | Texte secondaire, captions                  |

**Règles d'usage :**
- Le **Volt Green** ne doit **jamais** se retrouver à plat sur de grandes surfaces : on le réserve aux accents, traits, mots clés. C'est son rôle de couleur signal.
- Le couple **Charcoal + Volt Green** est le combo de référence pour le hero et les visuels match.
- Le **Volt Yellow** est strictement réservé aux CTA billetterie / urgents (ne pas en abuser).

---

## 2. Typographies

| Usage     | Police         | Poids utilisés      |
| --------- | -------------- | ------------------- |
| Display   | **Anton**      | Regular             |
| Titre H1-H3 | **Sora**     | 700, 800            |
| Body      | **Inter**      | 400, 500, 600       |
| Mono / data | **JetBrains Mono** | 500           |

Toutes en Google Fonts → self-hostées via `wp-theme/assets/fonts/` pour RGPD et perfo.

**Règles typographiques :**
- Les titres de matchs / scores / dates → **Anton** en majuscules, condensé, façon affiche sportive.
- Les noms de joueurs en fiche → **Sora 800** uppercase, espacement de lettres légèrement étiré.
- Le corps de texte → **Inter 16-18px**, line-height 1.6, jamais en blanc pur sur fond sombre (utiliser `#F5F5F0`).

---

## 3. Logo

Le logo actuel est conservé jusqu'à validation du nouveau. Direction proposée pour le nouveau logo :

- **Monogramme** : les 4 lettres `USAM` empilées ou imbriquées, géométrique, lecture immédiate.
- **Forme totem** : un blason simplifié — pas de fioritures, pas de ballon stylisé, pas de typographie cursive.
- **Versions** : monogramme seul / horizontal avec "Nîmes Gard" en sous-titre / icône carrée pour les réseaux.
- **Couleurs** : Volt Green sur Charcoal pour la version principale ; négatif pour fonds clairs ; mono blanc pour over-print sur photo.

Premier jet livré dans `design/logo-monogramme.svg` à itérer.

---

## 4. Iconographie

- Style **outline** ou **duotone**, jamais d'emoji ni d'icône colorée multicolore.
- Source : Lucide ou Phosphor (libres, cohérents).
- Trait constant 1.5px, coins légèrement arrondis (radius 2px).

---

## 5. Photographie & vidéo

- **Photos joueurs** : portraits sur fond Charcoal, lumière dure, direction "athlete portrait" (style NBA / Eurolig).
- **Photos match** : préférence pour les grands angles avec public visible (engagement) plutôt que les inserts de balle.
- **Couleur** : dérive très légère vers le vert dans les ombres si possible (LUT custom à fournir).
- **Bannir** : photos floues, fond blanc gym scolaire, compressions JPG visibles.

---

## 6. Ton de voix

- **Direct** : sujet → verbe → complément. Pas de jargon institutionnel.
- **Affirmatif** : on dit "On joue Nantes vendredi" pas "Nous aurons le plaisir de recevoir...".
- **Local** : on assume Nîmes, le Gard, l'Occitanie. On peut glisser une référence locale (la Romanité, le taureau, la garrigue) sans en faire une caricature.
- **Inclusif** : la section pro féminine a la **même typographie, la même charte, le même traitement éditorial** que la pro masculine. Pas de version "rose et fleurs".

---

## 7. Application web

Variables CSS définies dans `wp-theme/assets/css/input.css` :

```css
:root {
  --usam-volt: #00E676;
  --usam-forest: #0B3D2E;
  --usam-charcoal: #0A0A0A;
  --usam-bone: #F5F5F0;
  --usam-yellow: #E8FF59;
  --usam-slate-200: #E2E8F0;
  --usam-slate-700: #334155;
}
```

Mappées dans Tailwind via `tailwind.config.js` → utilisables comme `bg-usam-volt`, `text-usam-forest`, etc.

---

## 8. Do / Don't

| ✅ Do                                              | ❌ Don't                                       |
| -------------------------------------------------- | ---------------------------------------------- |
| Volt Green pour les CTA primaires                  | Volt Green sur tout le fond d'une page         |
| Charcoal + Volt Green sur hero                     | Vert + rouge (drapeau italien)                 |
| Anton uppercase pour les scores                    | Comic Sans, italiques, ombres portées          |
| Photos joueurs en portrait studio                  | Photos joueurs en gymnase amateur              |
| "On reçoit Nantes vendredi 21h"                    | "L'équipe aura le plaisir d'accueillir..."     |
