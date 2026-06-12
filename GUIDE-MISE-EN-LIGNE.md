# 🎾 Padel Performance Center — Guide de mise en ligne

Ton One Page est prêt. Il est dans le fichier **`index.html`** (un seul fichier, ultra simple à maintenir).

Voici **les 2 seules choses à faire** pour qu'il soit en ligne et qu'on puisse y payer la licence.

---

## ✅ Étape 1 — Mettre le site en ligne (gratuit, et ça dure)

Le site se met en ligne via **GitHub Pages** (hébergement gratuit et permanent — bien plus que 3 mois). La méthode la plus simple :

1. Va sur le dépôt GitHub `MikaBouteillon/MikaB`.
2. Clique sur **Settings** (Paramètres) → menu de gauche **Pages**.
3. Dans **Build and deployment → Source**, choisis **Deploy from a branch**.
4. Juste en dessous (**Branch**), sélectionne la branche
   **`claude/padel-performance-landing-3homgn`** et le dossier **`/ (root)`**, puis **Save**.
5. Attends 1-2 minutes : ta page est en ligne. ✅

➡️ L'adresse de ton site sera :
**https://mikabouteillon.github.io/MikaB/**

C'est ce lien que tu partages sur les réseaux sociaux. 🎯

> ℹ️ Il y a aussi un déploiement automatique prêt à l'emploi (`.github/workflows/deploy.yml`)
> si tu préfères la source **GitHub Actions** — mais la méthode « Deploy from a branch »
> ci-dessus est la plus simple et fonctionne parfaitement.

> 💡 Tu veux une adresse plus jolie (ex. `licence.padelperformancecenter.com`) ?
> C'est possible gratuitement dans **Settings → Pages → Custom domain**. Dis-le moi et je t'explique.

---

## ✅ Étape 2 — Activer le paiement de la licence

Pour encaisser les licences (21€ jeunes / 30€ adultes), le plus simple en France :

### Option recommandée : **HelloAsso** (100% gratuit pour les clubs/associations)
1. Crée un compte sur **helloasso.com** (gratuit, sans commission).
2. Crée une **« Adhésion »** ou un **« Paiement »** → un tarif **Licence Jeune 21€** et un tarif **Licence Adulte 30€** (tu peux faire un seul formulaire avec les 2 tarifs, ou deux liens séparés).
3. Récupère le **lien de paiement** de chaque tarif.

### Alternative : **Stripe Payment Links**
1. Compte sur **stripe.com** → **Payment Links** → crée un lien à 21€ et un à 30€.
2. Récupère les 2 liens.

### Puis : colle tes liens dans la page
Ouvre `index.html`, cherche le bloc **`CONFIG`** (tout en bas), et remplis :

```js
window.PPC_CONFIG = {
  licenceJeune:  "https://www.helloasso.com/.../licence-jeune",
  licenceAdulte: "https://www.helloasso.com/.../licence-adulte"
};
```

Sauvegarde → le site se met à jour tout seul. Les boutons « Prendre la licence » enverront directement vers le paiement. ✅

> Tant que les liens sont vides, les boutons affichent un message « inscriptions bientôt disponibles, contactez-nous » — donc rien n'est cassé en attendant.

---

## 🛠️ Ce que tu peux modifier facilement

Tout est dans `index.html` :
- **Les textes** : modifie directement dans la page (cherche le texte à changer).
- **Les prix** : cherche `22` et `26`.
- **Le téléphone** : cherche `06 87 46 07 04`.
- **Les liens de paiement** : bloc `CONFIG` en bas.

L'illustration du joueur (de dos, en plein smash, t-shirt « PADEL PERFORMANCE CENTER ») est dessinée en SVG directement dans la page : nette sur tous les écrans, aucun fichier image à gérer. Tu veux la remplacer plus tard par une vraie photo ? Dis-le moi.

---

## 📣 Pour la promo réseaux sociaux

- Lien à partager : **https://mikabouteillon.github.io/mikab/**
- La page est optimisée mobile et a un joli aperçu quand on partage le lien (titre + description).

Bon padel ! 🎾💚
