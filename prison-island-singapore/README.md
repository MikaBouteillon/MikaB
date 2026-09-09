# Prison Island Singapore — ESQ — Implantation des cellules

Implantation des cellules dans la *Game Area* (614,12 m²) du plan ESQ Singapour
(160 Orchard Road, PI. 37).

## Version retenue : v2 — 38 cellules aux surfaces de l'esquisse client

`PI_SINGAPORE_PLAN_38_Cells_v2.pdf`

Reprend **les 38 surfaces de cellules de l'esquisse client** (total 424,24 m²)
et les redistribue sur une trame de circulation vérifiée, en conservant tous les
poteaux existants.

| | |
|---|---|
| Game Area | 614,12 m² |
| Cellules | **38** |
| Surface utile cellules | 425,28 m² (**69,3 %**) |
| Écart max / esquisse client | **0,97 m²** (tolérance 1,00 m²) |
| Cellules de | 3,78 à 21,13 m² |
| Poteaux existants relevés | **19**, tous conservés et dégagés des circulations |

### Ce qui change par rapport à la v1

1. **Les poteaux ne sont plus effacés.** Les 19 carrés / rectangles noirs du fond
   de plan (0,30×0,50 à 1,80×1,94 m) sont relevés automatiquement dans le PDF
   source, puis :
   - **aucun ne tombe dans une circulation** (contrôle bloquant) ;
   - **aucun n'obstrue une baie de porte** — la position de porte est décalée le
     long du mur, voire reportée sur un autre côté, et si besoin l'ordre des
     cellules est permuté dans la bande ;
   - ils sont **redessinés par-dessus** les cellules, qui sont désormais en
     aplat 25 % (même teinte que la Game Area) et non plus opaques.
2. **Les surfaces sont les vôtres**, plus une trame régulière : de 3,78 m²
   (Einstein) à 21,13 m² (Tilt), avec la même répartition que votre esquisse.
3. L'affectation cellule → bande est optimisée (recuit simulé) pour coller aux
   surfaces visées ; 37 cellules sur 38 tombent à moins de 0,05 m² près.

### Organisation

Parcours linéaire de la porte **IN** (côté Briefing Room) à la porte **OUT**
(vers la Welcome Area), desservant aussi l'issue de secours ouest (Lift Lobby)
et la porte coupe-feu sud (AHU Room).

| Zone | Cellules |
|---|---|
| A — bloc nord | 24 |
| B — bande est | 7 |
| C — bloc sud | 7 |

Circulations : C1 et C2 est-ouest au nord, V1 nord-sud de liaison, C3 est-ouest
à l'est, CB nord-sud le long de la bande est, CC / CT / CS en zone sud.

## Variante : v1 — 41 cellules

`PI_SINGAPORE_PLAN_41_Cells.pdf` — trame plus régulière, cellules de 8,22 à
16,34 m², 415,21 m² utiles (67,6 %). Plus dense en nombre mais avec des cellules
plus petites et plus uniformes. Poteaux également conservés depuis la
correction.

## Contraintes tenues dans les deux versions

- Cellules **uniquement dans la zone en couleur** (Game Area). Rien dans la
  Welcome Area ni hors bail.
- **Circulations : 1,20 m de passage libre** — module 1,30 m d'axe à axe,
  cloisons 100 mm.
- Portes de cellule 0,90 m, débattement figuré.
- Poteaux existants conservés.

## Contrôles automatiques

`generate_plan_v2.py` échoue si l'un de ces points n'est pas tenu :

- chaque cellule est contenue dans l'emprise de la Game Area ;
- aucun recouvrement cellule/cellule ni cellule/circulation ;
- toute circulation ≥ 1,30 m d'axe à axe, soit **1,20 m de passage libre** ;
- **aucun poteau dans une circulation** ;
- le réseau de circulation est connexe (un seul tenant) ;
- chaque cellule ouvre par une porte de 0,90 m sur une circulation, **dégagée
  de tout poteau** ;
- chaque cellule est à moins de **1,00 m²** de la surface visée par l'esquisse
  client ;
- plus petite dimension utile ≥ 1,45 m.

```
$ python3 generate_plan_v2.py
Game Area          : 614.12 m2
Cellules           : 38
Poteaux releves    : 19 (tous conserves, hors circulations)
Ecart max / esquisse client : 0.97 m2 (tolerance 1.0 m2)
Controles geometriques : OK
Surface utile      : 425.28 m2 (69.3 % de la Game Area)
```

## Points à valider

- **Hauteurs sous plafond réduites.** Trame jaune H = 2,07 m : cellules
  **05 Shark Bay, 24 Cliffhanger, 38 The Hub**. Trame rouge H = 2,10 m sur une
  partie de la bande est. À arbitrer selon les jeux implantés.
- Huit cellules reçoivent un poteau en saillie (0,34 à 0,99 m², soit au plus
  11 % de la cellule) : The Nest, Devil's Island, WaterFall, Roof Top, Copy Cat,
  Source Code, Cliffhanger, Shipyard. Le poteau reste hors de la baie de porte.
- Une gaine technique 800×1000 subsiste en saillie dans la cellule sud-est.
- Distances de fuite et désenfumage à faire valider par le bureau de contrôle
  local (SCDF).

## Méthode

- Contour de la Game Area extrait vectoriellement du PDF source : l'aire
  calculée retombe exactement sur les 614,12 m² annoncés, ce qui valide
  l'échelle (1:200 sur A3, 1 pt = 0,0705556 m).
- Poteaux relevés par lecture des aplats noirs du fond de plan.
- Le fond de plan ESQ d'origine est conservé ; seuls les libellés du fond qui
  tombent désormais à l'intérieur d'une cellule (surface Game Area, hauteurs)
  sont masqués, l'information étant reprise dans le cartouche.

## Tableau des cellules (v2)

| N° | Cellule | Zone | Larg. (m) | Prof. (m) | Surface (m²) | Esquisse client | Écart |
|---:|---|---|---:|---:|---:|---:|---:|
| 01 | Riot | C – bloc sud | 4,35 | 2,92 | 12,73 | 12,75 | -0,02 |
| 02 | Pyramid | A – bloc nord | 3,10 | 4,05 | 12,53 | 12,56 | -0,03 |
| 03 | Maps | C – bloc sud | 2,13 | 2,92 | 6,24 | 6,25 | -0,01 |
| 04 | Submarine | B – bande est | 3,63 | 2,47 | 8,96 | 9,00 | -0,04 |
| 05 | Shark Bay | A – bloc nord | 4,09 | 4,20 | 17,16 | 17,17 | -0,01 |
| 06 | Flipper | B – bande est | 3,60 | 2,41 | 8,66 | 8,69 | -0,03 |
| 07 | The Docks | A – bloc nord | 4,37 | 4,05 | 17,67 | 17,71 | -0,04 |
| 08 | Lucky Lane | A – bloc nord | 1,52 | 2,50 | 3,80 | 3,53 | +0,27 |
| 09 | The Vault | C – bloc sud | 2,54 | 4,25 | 10,79 | 10,76 | +0,03 |
| 10 | Work Out | A – bloc nord | 3,70 | 4,40 | 16,27 | 16,18 | +0,09 |
| 11 | Penalty | C – bloc sud | 3,85 | 4,25 | 16,34 | 17,05 | -0,71 |
| 12 | Shipyard | C – bloc sud | 2,50 | 4,25 | 10,60 | 10,58 | +0,02 |
| 13 | The Bulgar | A – bloc nord | 2,83 | 3,40 | 9,63 | 9,63 | -0,00 |
| 14 | Laser Gun | A – bloc nord | 3,03 | 3,40 | 10,31 | 10,31 | -0,00 |
| 15 | Studio 21 | A – bloc nord | 5,86 | 3,40 | 19,94 | 19,94 | -0,00 |
| 16 | Catch | A – bloc nord | 2,36 | 2,20 | 5,20 | 4,46 | +0,74 |
| 17 | Prison | B – bande est | 3,60 | 3,10 | 11,14 | 11,18 | -0,04 |
| 18 | Flash Dance | A – bloc nord | 2,53 | 2,90 | 7,33 | 7,35 | -0,02 |
| 19 | Einstein | A – bloc nord | 1,80 | 2,10 | 3,78 | 3,52 | +0,26 |
| 20 | Roof Top | A – bloc nord | 6,07 | 2,90 | 17,60 | 17,65 | -0,05 |
| 21 | Dive | B – bande est | 3,60 | 1,70 | 6,12 | 6,15 | -0,03 |
| 22 | Basket | B – bande est | 3,60 | 2,97 | 10,69 | 10,74 | -0,05 |
| 23 | Tilt | A – bloc nord | 5,03 | 4,20 | 21,13 | 21,13 | -0,00 |
| 24 | Cliffhanger | A – bloc nord | 2,56 | 4,20 | 10,76 | 10,76 | -0,00 |
| 25 | The Nest | A – bloc nord | 4,07 | 4,20 | 17,08 | 17,09 | -0,01 |
| 26 | Color Blind | B – bande est | 3,63 | 2,84 | 10,31 | 10,36 | -0,05 |
| 27 | The Gate | A – bloc nord | 2,27 | 2,90 | 6,58 | 6,60 | -0,02 |
| 28 | Source Code | A – bloc nord | 1,59 | 4,40 | 6,98 | 6,94 | +0,04 |
| 29 | WaterFall | A – bloc nord | 4,45 | 4,20 | 18,69 | 18,69 | -0,00 |
| 30 | Hands On | C – bloc sud | 3,17 | 2,92 | 9,28 | 9,29 | -0,01 |
| 31 | Devil's Island | A – bloc nord | 4,95 | 4,05 | 20,04 | 20,08 | -0,04 |
| 32 | Wire | A – bloc nord | 1,88 | 3,40 | 6,40 | 6,40 | -0,00 |
| 33 | Tower | A – bloc nord | 1,77 | 4,20 | 7,42 | 7,42 | -0,00 |
| 34 | Smash and Grab | A – bloc nord | 2,74 | 2,90 | 7,96 | 7,98 | -0,02 |
| 35 | Jocker | A – bloc nord | 1,62 | 4,20 | 6,81 | 6,81 | -0,00 |
| 36 | Kettlebell | C – bloc sud | 2,70 | 4,20 | 11,35 | 11,47 | -0,12 |
| 37 | Copy Cat | B – bande est | 3,60 | 2,00 | 7,18 | 7,20 | -0,02 |
| 38 | The Hub | A – bloc nord | 5,53 | 2,50 | 13,83 | 12,86 | +0,97 |
| | **Total** | | | | **425,28** | **424,24** | **+1,04** |
