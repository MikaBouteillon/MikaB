# SAS ENCORE — version française du deck

Régénère `SAS_ENCORE_2026_FR.pdf` à partir du PDF anglais d'origine :
le texte est retiré page par page puis réécrit en français aux mêmes
coordonnées, avec la même police (DM Sans), les mêmes tailles, couleurs
et interlettrages. Images, fonds et éléments vectoriels sont conservés
tels quels.

## Prérequis

```
pip install pymupdf
```

Les fichiers DM Sans (300/400/500/700 + italiques 300/400) doivent être
placés dans `fonts/`, nommés `DMSans-<poids>-<normal|italic>.ttf`
(récupérables sur Google Fonts).

## Utilisation

```
python build.py SAS_ENCORE_2026_FR.pdf
```

- `engine.py` : moteur de mise en page (césure, alignement, interlettrage,
  ajustement automatique de la taille si un bloc déborde).
- `content.py` : tout le contenu français, bloc par bloc, positionné sur
  la maquette d'origine.
