# Prison Island Singapore — ESQ — Implantation des cellules

Implantation de **41 cellules** dans la *Game Area* (614,12 m²) du plan ESQ
Singapour (160 Orchard Road, PI. 37), en reprenant les principes des plans
Prison Island existants (Paris, New York, Francfort, Milan, Orlando, Nashville,
Mexico, Indianapolis).

## Livrable

| Fichier | Contenu |
|---|---|
| `PI_SINGAPORE_PLAN_41_Cells.pdf` | Plan ESQ d'origine + implantation des cellules (A3, 1:200) |
| `PI_SINGAPORE_PLAN_41_Cells.png` | Aperçu raster du plan |
| `generate_plan.py` | Script de génération et de contrôle géométrique |

## Contraintes respectées

- **Cellules uniquement dans la zone en couleur** (Game Area, 614,12 m²). Aucune
  cellule dans la Welcome Area, ni dans les emprises hors bail.
- **Circulations : 1,20 m de passage libre** — module de 1,30 m d'axe à axe de
  cloison, cloisons de 100 mm.
- Portes de cellule de 0,90 m, débattement figuré.
- Poteaux existants 900×900 conservés : la trame des cellules est calée sur les
  files de poteaux (entraxes 8,40 m × 8,60 m), les poteaux étant absorbés dans
  les cloisons de refend ou laissés en saillie dans la cellule.
- Accès conservés : porte **IN** (côté Briefing Room), porte **OUT** (vers la
  Welcome Area), issue de secours ouest (Lift Lobby) et porte coupe-feu sud
  (AHU Room).

## Chiffres clés

| | |
|---|---|
| Game Area | 614,12 m² |
| Cellules | **41** |
| Surface utile cellules | 415,21 m² (67,6 %) |
| Circulations + réserves | 198,91 m² (32,4 %) |
| Cellule moyenne | 10,13 m² |
| Mini / maxi | 8,22 m² / 16,34 m² |

À titre de comparaison, les plans de référence tournent autour de 16 à 19 m² de
Game Area par cellule (Nashville : 777 m² / 45 cellules ; Mexico : 859 m² /
45 cellules ; Indianapolis : 865 m² / 47 cellules au RDC). Ici le ratio est de
15,0 m²/cellule : la densité est plus élevée parce que le briefing, le stockage
et le local serveur de Singapour sont situés **hors** Game Area (dans la Welcome
Area), contrairement aux plans de référence où ils sont comptés dedans.

## Organisation

Le parcours est linéaire, de la porte IN à la porte OUT :

1. **Zone B — bande est** (cellules 28 à 34) : entrée par la porte IN, circulation
   verticale principale desservant 2 cellules à l'ouest et 5 à l'est.
2. **Zone C — bloc sud** (cellules 35 à 41) : desservie par une circulation
   est-ouest centrale et une antenne verticale vers la queue sud ; antenne
   dédiée vers la porte coupe-feu de l'AHU Room.
3. **Zone A — bloc nord** (cellules 01 à 27) : deux circulations est-ouest
   (C1 au nord, C2 en épine dorsale) reliées par une circulation verticale ;
   files de cellules dos à dos entre les deux. Sortie par la porte OUT, issue de
   secours à l'ouest.

## Points à valider

- **Hauteurs sous plafond réduites** : la trame jaune (H = 2,07 m, cellules 21,
  22, 26, 27) et la trame rouge (H = 2,10 m) sont incluses dans la Game Area
  mais restent basses ; à confirmer avec l'exploitant selon les jeux implantés.
  Le reste est à 2,66 m / 2,47 m.
- Distances de fuite et désenfumage à faire valider par le bureau de contrôle
  local (SCDF) — le réseau de circulation dessert les quatre issues existantes.
- Une gaine technique de 800×1000 subsiste en saillie dans la cellule 40, et des
  poteaux 900×900 en saillie dans quelques cellules (repérables sur le fond de
  plan).

## Contrôles automatiques

`generate_plan.py` vérifie et échoue si l'un des points n'est pas tenu :

- chaque cellule est contenue dans l'emprise de la Game Area ;
- aucun recouvrement entre cellules, ni entre cellule et circulation ;
- toute circulation ≥ 1,30 m d'axe à axe (soit 1,20 m libre) ;
- le réseau de circulation est connexe (un seul tenant) ;
- chaque cellule ouvre par une porte de 0,90 m sur une circulation.

```
$ python3 generate_plan.py
Game Area : 614.12 m2
Cellules  : 41
Controles geometriques : OK
Surface utile cellules : 415.21 m2 (67.6 % de la Game Area)
```

## Tableau des cellules

| N° | Cellule | Zone | Larg. (m) | Prof. (m) | Surface (m²) |
|---:|---|---|---:|---:|---:|
| 01 | Slippery Slope | A - Bloc nord (ouest) | 2,79 | 3,50 | 9,75 |
| 02 | Riot | A - Bloc nord (ouest) | 2,79 | 3,50 | 9,75 |
| 03 | Basket | A - Bloc nord (ouest) | 2,79 | 3,50 | 9,75 |
| 04 | Catch | A - Bloc nord (ouest) | 2,79 | 3,50 | 9,75 |
| 05 | Colorblind | A - Bloc nord (ouest) | 2,70 | 3,60 | 9,73 |
| 06 | Penalty | A - Bloc nord (ouest) | 2,70 | 3,60 | 9,73 |
| 07 | Tilt | A - Bloc nord (ouest) | 2,70 | 3,60 | 9,73 |
| 08 | Lucky Lane | A - Bloc nord (ouest) | 2,70 | 3,60 | 9,73 |
| 09 | Inca | A - Bloc nord (ouest) | 2,70 | 3,60 | 9,73 |
| 10 | Green Mile | A - Bloc nord (ouest) | 2,70 | 3,40 | 9,19 |
| 11 | Music | A - Bloc nord (ouest) | 2,70 | 3,40 | 9,19 |
| 12 | The Hub | A - Bloc nord (ouest) | 2,70 | 3,40 | 9,19 |
| 13 | Shark Bay | A - Bloc nord (ouest) | 2,70 | 3,40 | 9,19 |
| 14 | Cell Block North | A - Bloc nord (ouest) | 2,70 | 3,40 | 9,19 |
| 15 | Work Out | A - Bloc nord (ouest) | 3,08 | 4,05 | 12,46 |
| 16 | Boiler Room | A - Bloc nord (ouest) | 3,08 | 4,05 | 12,46 |
| 17 | Maps | A - Bloc nord (ouest) | 3,08 | 4,05 | 12,46 |
| 18 | Devils Island | A - Bloc nord (ouest) | 3,08 | 4,05 | 12,46 |
| 19 | Ventilation | A - Bloc nord (est) | 2,64 | 4,75 | 12,55 |
| 20 | Roof Top | A - Bloc nord (est) | 2,64 | 4,75 | 12,55 |
| 21 | Gates | A - Bloc nord (est) | 3,52 | 2,85 | 10,05 |
| 22 | Pyramid | A - Bloc nord (est) | 3,52 | 2,85 | 10,05 |
| 23 | The Burglar | A - Bloc nord (est) | 2,45 | 3,85 | 9,42 |
| 24 | Hitman | A - Bloc nord (est) | 2,45 | 3,85 | 9,42 |
| 25 | The Nest | A - Bloc nord (est) | 2,45 | 3,85 | 9,42 |
| 26 | Laser Gun | A - Bloc nord (est) | 2,45 | 3,85 | 9,42 |
| 27 | KettleBell | A - Bloc nord (est) | 2,45 | 3,85 | 9,42 |
| 28 | Studio 21 | B - Bande est | 3,63 | 2,66 | 9,65 |
| 29 | Butchers Lane | B - Bande est | 3,63 | 2,66 | 9,65 |
| 30 | Waterfall | B - Bande est | 3,52 | 2,34 | 8,22 |
| 31 | Joker | B - Bande est | 3,52 | 2,34 | 8,22 |
| 32 | Wire | B - Bande est | 3,52 | 2,50 | 8,80 |
| 33 | Visitors | B - Bande est | 3,52 | 2,50 | 8,80 |
| 34 | Source Code | B - Bande est | 3,52 | 2,50 | 8,80 |
| 35 | The Docks | C - Bloc sud | 3,22 | 2,92 | 9,42 |
| 36 | The Prison | C - Bloc sud | 3,22 | 2,92 | 9,42 |
| 37 | Hands On | C - Bloc sud | 3,22 | 2,92 | 9,42 |
| 38 | Tower | C - Bloc sud | 2,52 | 4,25 | 10,70 |
| 39 | Submarine | C - Bloc sud | 2,52 | 4,25 | 10,70 |
| 40 | Cliffhanger | C - Bloc sud | 3,85 | 4,25 | 16,34 |
| 41 | Dive | C - Bloc sud | 2,70 | 4,20 | 11,35 |
| | **Total** | | | | **415,21** |
