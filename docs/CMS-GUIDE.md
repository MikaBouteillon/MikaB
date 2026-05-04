# Guide CMS — pour l'équipe USAM

Bienvenue. Ce guide t'apprend à publier sur le site **sans connaître une ligne de code**.

> Tu te connectes ici : `https://www.usam-nimesgard.fr/wp-admin`
> Identifiants : fournis par l'admin technique.

---

## Sommaire

1. [Connexion & sécurité](#1-connexion--sécurité)
2. [Publier une actualité](#2-publier-une-actualité)
3. [Ajouter un joueur](#3-ajouter-un-joueur)
4. [Créer un match](#4-créer-un-match)
5. [Gérer les partenaires](#5-gérer-les-partenaires)
6. [Modifier une page existante](#6-modifier-une-page-existante)
7. [Bonnes pratiques images](#7-bonnes-pratiques-images)
8. [Erreurs fréquentes](#8-erreurs-fréquentes)

---

## 1. Connexion & sécurité

- Mot de passe **obligatoirement** géré dans 1Password / Bitwarden.
- Active la **double authentification** (plugin déjà installé).
- **Jamais** de "admin" comme login.
- Si tu pars du club : préviens, on désactive ton compte.

---

## 2. Publier une actualité

1. Menu de gauche → **Articles → Ajouter**.
2. **Titre** : court et impactant. Pas de majuscules partout, on garde la casse normale (le thème met en CAPS automatiquement).
   - ✅ "Wesley Pardin élu meilleur gardien du mois"
   - ❌ "WESLEY PARDIN ÉLU MEILLEUR GARDIEN DU MOIS !!!"
3. **Contenu** : utilise les blocs (paragraphe, sous-titre, image, citation, vidéo).
4. **Image mise en avant** (colonne droite) : OBLIGATOIRE, c'est elle qui s'affiche en card sur la home.
   - Format : 1200×800px, JPG ou WebP, < 300 Ko.
   - Pas de texte gravé dans l'image (ça casse le responsive).
5. **Catégorie** : "Pro masculine", "Pro féminine", "Formation", "Club", "Communauté".
6. **Extrait** (colonne droite, panneau Extrait) : 25 mots max, c'est ce qui apparaît en aperçu.
7. Bouton **Publier** en haut à droite (ou "Programmer" pour planifier).

---

## 3. Ajouter un joueur

1. Menu de gauche → **Joueurs → Ajouter**.
2. **Titre** = nom complet du joueur (ex: "Wesley Pardin").
3. **Image mise en avant** = portrait studio (format 600×800px, fond Charcoal de préférence).
4. **Contenu** = bio courte (180 mots max).
5. **Équipe** (colonne droite) : coche "Green Team", "Nîmoises", "N1M"…
6. **Poste** : "Gardien", "Pivot", "Ailier", "Arrière", "Demi-centre".
7. **Extrait** : phrase d'accroche (sera utilisée sur la fiche).

---

## 4. Créer un match

1. Menu de gauche → **Matchs → Ajouter**.
2. **Titre** : `USAM Nîmes vs RC Nantes` (toujours USAM en premier si on est à domicile, en second si extérieur).
3. **Champs personnalisés** (en bas de l'écran) :
   - `usam_match_date` : date au format `2026-05-10` puis heure `2026-05-10 20:30`
   - `usam_match_adversaire` : "RC Nantes"
   - `usam_match_lieu` : "Le Parnasse" ou nom de la salle adverse
   - `usam_match_competition` : "Liqui Moly Starligue", "Coupe de France"…
   - `usam_match_equipe` : `green-team`, `nimoises`, `n1m`, `n3f`
   - `usam_match_billetterie_url` : lien complet vers la place sur la billetterie
   - Après match : `usam_match_score_usam` et `usam_match_score_adv`

> **Astuce** : un match futur affiche automatiquement le bandeau "Prochain match" sur la home.

---

## 5. Gérer les partenaires

1. **Partenaires → Ajouter**.
2. **Titre** = nom de l'entreprise.
3. **Image mise en avant** = logo PNG transparent ou SVG, format carré ou 3:2.
4. **Catégorie** : Institutionnels / Maillot / Officiels / Médias.
5. **Champ `usam_partenaire_url`** : URL du site du partenaire.

> Les logos s'affichent automatiquement sur la home (15 max) et sur la page Partenaires (tous).

---

## 6. Modifier une page existante

1. **Pages** → trouve la page → **Modifier**.
2. Tu peux changer le contenu sans toucher au design : le thème applique la mise en forme.
3. Bouton **Mettre à jour**.

⚠️ **Ne pas modifier les pages "Accueil" et "Le Parnasse"** sans prévenir l'équipe technique : elles utilisent des templates spécifiques.

---

## 7. Bonnes pratiques images

| Type d'image          | Dimension idéale | Poids max |
| --------------------- | ---------------- | --------- |
| Image mise en avant article | 1200×800        | 300 Ko   |
| Portrait joueur       | 600×800          | 200 Ko   |
| Logo partenaire       | 600×400 transparent | 80 Ko |
| Photo Le Parnasse / hero | 1920×1080      | 500 Ko   |

**Outils gratuits pour compresser** :
- [Squoosh](https://squoosh.app/) — drag & drop, sortie WebP
- [TinyPNG](https://tinypng.com/) — JPG / PNG batch

**Toujours remplir l'attribut Alt** (description courte de l'image, lue par les lecteurs d'écran et utile au SEO).

---

## 8. Erreurs fréquentes

| Symptôme                                  | Cause / solution                                                |
| ----------------------------------------- | --------------------------------------------------------------- |
| L'image n'apparaît pas sur la home        | "Image mise en avant" pas définie                               |
| Le match n'apparaît pas dans le bandeau   | Le slug d'équipe n'est pas `green-team` (vérifier les champs)   |
| Le titre est tout en majuscules           | C'est normal, le design applique l'uppercase automatiquement    |
| Le partenaire n'apparaît pas              | Catégorie non cochée                                            |
| "Erreur critique" en publiant             | Appeler l'équipe technique (admin@usam-nimes.fr)                |

---

## Aide

- **Contact technique** : (à définir)
- **Documentation WordPress officielle** : https://fr.wordpress.org/support/
