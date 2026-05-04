# Contenu de référence

Ce dossier contient le **contenu source** du site, en markdown, **avant migration dans WordPress**.

Objectif :
1. Garder un référentiel versionné (Git) du contenu — utile pour la traçabilité, les retours en arrière, les diffs éditoriaux.
2. Servir de base à un import automatique dans WordPress (script à venir : `scripts/import-content.php`).
3. Permettre à l'équipe rédac de travailler hors-ligne, en pull request, avant publication.

## Arborescence

```
content/
├─ pages/         → pages statiques (Accueil, Le Club, Le Parnasse, Mentions, etc.)
├─ equipes/       → fiches d'équipes (Green Team, Nîmoises, N1, N3, etc.)
├─ actus/         → archives d'actualités aspirées du site actuel
└─ partenaires/   → liste des sponsors par catégorie
```

## Workflow

1. **Phase initiale** : on copie-colle ces contenus à la main dans WordPress pour bootstrapper le site.
2. **Phase 2** : un script PHP wp-cli importera automatiquement chaque markdown vers le bon CPT.
3. **Phase 3** : la rédaction se fera directement dans WordPress (avec backup en markdown via plugin).
