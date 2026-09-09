#!/usr/bin/env python3
"""
Prison Island Singapore - ESQ - v2
Implantation des 38 cellules de l'esquisse client (surfaces reprises a +/- 1 m2),
redistribuees sur une trame de circulation a 1,20 m de passage libre.

Differences avec la v1 :
  - les poteaux existants (carres / rectangles noirs) sont releves un par un,
    exclus des circulations et redessines par-dessus les cellules ;
  - les surfaces de cellules sont celles de l'esquisse client, pas une trame
    reguliere ; l'affectation cellule -> bande est optimisee.

Repere : metres, origine au coin haut-gauche de la bbox de la Game Area,
x vers la droite, y vers le bas. Echelle du fond : 1:200 sur A3.
"""
import json
import math
import random
import pymupdf
from shapely.geometry import Polygon, box
from shapely.ops import unary_union

SRC = "/root/.claude/uploads/62955517-4c19-5b46-b0e1-471b227c3618/2b4aa1b3-ESQ__PI__SINGAPORE_1.pdf"
OUT = "/home/user/MikaB/prison-island-singapore/PI_SINGAPORE_PLAN_38_Cells_v2.pdf"

S = 0.0705556
PPM = 1.0 / S
X0, Y0 = 582.4468994140625, 68.34652709960938

WALL = 0.10          # cloisons 100 mm
CLEAR = 1.20         # passage libre exige
MODULE = CLEAR + WALL
MIN_SIDE = 1.45      # plus petite dimension utile admise (cf. esquisse client)
SOFT_SIDE = 1.60     # largeur visee, penalisee en dessous
TOL = 1.00           # ecart admis sur la surface d'une cellule (m2)

def P(x, y):
    return pymupdf.Point(X0 + x * PPM, Y0 + y * PPM)

def R(x0, y0, x1, y1):
    return pymupdf.Rect(X0 + x0 * PPM, Y0 + y0 * PPM, X0 + x1 * PPM, Y0 + y1 * PPM)

# --------------------------------------------------------------------------
# Programme : les 38 cellules de l'esquisse client
# --------------------------------------------------------------------------
PROGRAM = [
    ("Riot", 12.75), ("Pyramid", 12.56), ("Maps", 6.25), ("Submarine", 9.00),
    ("Shark Bay", 17.17), ("Flipper", 8.69), ("The Docks", 17.71),
    ("Lucky Lane", 3.53), ("The Vault", 10.76), ("Work Out", 16.18),
    ("Penalty", 17.05), ("Shipyard", 10.58), ("The Bulgar", 9.63),
    ("Laser Gun", 10.31), ("Studio 21", 19.94), ("Catch", 4.46),
    ("Prison", 11.18), ("Flash Dance", 7.35), ("Einstein", 3.52),
    ("Roof Top", 17.65), ("Dive", 6.15), ("Basket", 10.74), ("Tilt", 21.13),
    ("Cliffhanger", 10.76), ("The Nest", 17.09), ("Color Blind", 10.36),
    ("The Gate", 6.60), ("Source Code", 6.94), ("WaterFall", 18.69),
    ("Hands On", 9.29), ("Devil's Island", 20.08), ("Wire", 6.40),
    ("Tower", 7.42), ("Smash and Grab", 7.98), ("Jocker", 6.81),
    ("Kettlebell", 11.47), ("Copy Cat", 7.20), ("The Hub", 12.86),
]

# --------------------------------------------------------------------------
# Circulations : passage libre 1,20 m -> module 1,30 m d'axe a axe
# --------------------------------------------------------------------------
CORRIDORS = [
    (0.000,  2.200,  1.900,  4.300, "EG"),    # acces issue de secours ouest
    (0.000,  4.300, 15.910,  5.600, "C1"),    # E-O nord
    (1.900, 12.100, 29.945, 13.400, "C2"),    # E-O epine dorsale
    (14.610, 13.400, 15.910, 17.549, "COUT"), # antenne porte OUT
    (15.910,  2.000, 17.210, 12.100, "V1"),   # N-S liaison ouest/est
    (17.210,  6.500, 29.945,  7.800, "C3"),   # E-O zone A est
    (28.127, 13.400, 29.450, 29.625, "CB1"),  # N-S zone B (porte IN)
    (28.127, 28.908, 29.945, 33.950, "CB2"),  # N-S entree zone C
    (18.167, 32.650, 29.450, 33.950, "CC"),   # E-O zone C
    (18.167, 33.950, 19.467, 43.400, "CT"),   # N-S zone C ouest
    (24.700, 33.950, 26.000, 38.300, "CS"),   # antenne porte coupe-feu sud
]

# --------------------------------------------------------------------------
# Bandes de cellules : (nom, x0, y0, x1, y1, nb de cellules, axe, cote porte)
# --------------------------------------------------------------------------
BANDS = [
    ("B1",  0.000,  0.000,  1.900,  2.200, 1, "x", "S"),
    ("B2",  1.900,  0.000, 13.445,  4.300, 3, "x", "S"),
    ("B3", 13.445,  2.000, 15.910,  4.300, 1, "x", "S"),
    ("B4",  1.900,  5.600, 15.910,  8.600, 4, "x", "N"),
    ("B5",  1.900,  8.600, 15.910, 12.100, 4, "x", "S"),
    ("B6",  1.900, 13.400, 14.610, 17.549, 3, "x", "N"),
    ("B7", 17.210,  2.000, 22.695,  6.500, 2, "x", "S"),
    ("B8", 22.695,  3.900, 29.945,  6.500, 2, "x", "S"),
    ("B9", 17.210,  7.800, 29.945, 12.100, 4, "x", "S"),
    ("B10", 24.395, 15.600, 28.127, 21.104, 2, "y", "E"),
    ("B11", 29.450, 16.229, 33.145, 21.104, 2, "y", "W"),
    ("B12", 29.450, 21.104, 33.145, 28.908, 3, "y", "W"),
    ("B13", 18.167, 29.625, 28.127, 32.650, 3, "x", "S"),
    ("B14", 19.467, 33.950, 24.700, 38.300, 2, "x", "N"),
    ("B15", 26.000, 33.950, 29.945, 38.300, 1, "x", "N"),
    ("B16", 19.467, 38.300, 22.270, 42.600, 1, "x", "W"),
]

def capacity(b):
    """Surface utile totale d'une bande decoupee en k cellules."""
    _, x0, y0, x1, y1, k, axis, _ = b
    w, h = x1 - x0, y1 - y0
    if axis == "x":
        return (w - k * WALL) * (h - WALL)
    return (w - WALL) * (h - k * WALL)

def slice_band(b, targets):
    """Decoupe la bande proportionnellement aux surfaces visees."""
    _, x0, y0, x1, y1, k, axis, door = b
    w, h = x1 - x0, y1 - y0
    tot = sum(targets)
    out = []
    if axis == "x":
        usable = w - k * WALL
        pos = x0
        for i, t in enumerate(targets):
            cw = usable * t / tot + WALL
            out.append((pos, y0, pos + cw, y1, door))
            pos += cw
    else:
        usable = h - k * WALL
        pos = y0
        for i, t in enumerate(targets):
            ch = usable * t / tot + WALL
            out.append((x0, pos, x1, pos + ch, door))
            pos += ch
    return out

def net_area(c):
    return (c[2] - c[0] - WALL) * (c[3] - c[1] - WALL)

def min_side(c):
    return min(c[2] - c[0], c[3] - c[1]) - WALL

# --------------------------------------------------------------------------
# Affectation cellule -> bande (recuit simule)
# --------------------------------------------------------------------------
def cost(assign):
    total = 0.0
    for b, idxs in zip(BANDS, assign):
        cells = slice_band(b, [PROGRAM[i][1] for i in idxs])
        for c, i in zip(cells, idxs):
            d = abs(net_area(c) - PROGRAM[i][1])
            total += d + 40 * max(0.0, d - TOL) ** 2
            total += 60 * max(0.0, SOFT_SIDE - min_side(c)) ** 2
            w, h = c[2] - c[0] - WALL, c[3] - c[1] - WALL
            total += 0.25 * max(0.0, max(w, h) / max(min(w, h), 1e-6) - 2.6)
    return total

def solve(seed=7):
    rng = random.Random(seed)
    order = sorted(range(len(PROGRAM)), key=lambda i: -PROGRAM[i][1])
    # depart : remplissage glouton des bandes par capacite decroissante
    assign = [[] for _ in BANDS]
    slots = sorted(range(len(BANDS)), key=lambda j: -capacity(BANDS[j]) / BANDS[j][5])
    pool = list(order)
    for j in slots:
        k = BANDS[j][5]
        want = capacity(BANDS[j]) / k
        for _ in range(k):
            best = min(pool, key=lambda i: abs(PROGRAM[i][1] - want))
            assign[j].append(best)
            pool.remove(best)
    cur = cost(assign)
    T = 4.0
    for step in range(240000):
        T = 4.0 * math.exp(-step / 30000)
        a, b = rng.randrange(len(BANDS)), rng.randrange(len(BANDS))
        if a == b:
            continue
        ia, ib = rng.randrange(len(assign[a])), rng.randrange(len(assign[b]))
        assign[a][ia], assign[b][ib] = assign[b][ib], assign[a][ia]
        new = cost(assign)
        if new <= cur or rng.random() < math.exp((cur - new) / max(T, 1e-9)):
            cur = new
        else:
            assign[a][ia], assign[b][ib] = assign[b][ib], assign[a][ia]
    return assign, cur

def build():
    assign, c = solve()
    cells = []
    for b, idxs in zip(BANDS, assign):
        # ordonne les cellules de la bande par taille pour un rendu regulier
        sub = slice_band(b, [PROGRAM[i][1] for i in idxs])
        for cell, i in zip(sub, idxs):
            cells.append((cell, i))
    return cells, c

# --------------------------------------------------------------------------
# Poteaux existants (releves sur le fond de plan, en metres)
# --------------------------------------------------------------------------
def read_columns(page, poly):
    zone = poly.buffer(0.35)
    out = []
    for d in page.get_drawings():
        f = d["fill"]
        if not f or tuple(round(v, 3) for v in f) != (0.0, 0.0, 0.0):
            continue
        if (d.get("fill_opacity") or 1) < 0.9:
            continue
        r = d["rect"]
        m = ((r.x0 - X0) * S, (r.y0 - Y0) * S, (r.x1 - X0) * S, (r.y1 - Y0) * S)
        w, h = m[2] - m[0], m[3] - m[1]
        if w < 0.15 or h < 0.15 or w > 4 or h > 4:
            continue
        if box(*m).intersects(zone):
            out.append(tuple(round(v, 3) for v in m))
    return sorted(set(out), key=lambda t: (t[1], t[0]))

def game_area_polygon(page):
    for d in page.get_drawings():
        f = d["fill"]
        if f and tuple(round(v, 3) for v in f) == (1.0, 0.718, 0.506) and d["rect"].width > 100:
            pts = [((it[1].x - X0) * S, (it[1].y - Y0) * S) for it in d["items"] if it[0] == "l"]
            return Polygon(pts)
    raise RuntimeError("contour Game Area introuvable")

def _parts(g):
    return list(g.geoms) if hasattr(g, "geoms") else [g]

RESERVES = [                      # micro-reservations du contour absorbees
    (4.336, 0.00, 5.145, 0.399),  # par l'epaisseur des cloisons
    (12.691, 0.00, 13.445, 0.399),
    (26.020, 37.299, 26.820, 38.324),
]

def buildable(poly):
    extra = [g for g in _parts(poly.envelope.difference(poly))
             if g.area < 1.2 and g.intersects(poly)]
    extra += [box(*r) for r in RESERVES]
    return unary_union([poly] + extra).buffer(0.02)

# --------------------------------------------------------------------------
# Controles
# --------------------------------------------------------------------------
def check(cells, poly, columns):
    errs, notes = [], []
    allowed = buildable(poly)
    boxes = [box(*c[:4]) for c, i in cells]

    for (c, i), b in zip(cells, boxes):
        nm = PROGRAM[i][0]
        if b.difference(allowed).area > 0.05:
            errs.append(f"{nm}: deborde de la Game Area ({b.difference(allowed).area:.2f} m2)")
        if min_side(c) < MIN_SIDE:
            errs.append(f"{nm}: plus petite dimension {min_side(c):.2f} m < {MIN_SIDE} m")
        d = net_area(c) - PROGRAM[i][1]
        if abs(d) > TOL:
            errs.append(f"{nm}: surface {net_area(c):.2f} m2, ecart {d:+.2f} m2 > {TOL}")
    for a in range(len(boxes)):
        for b_ in range(a + 1, len(boxes)):
            if boxes[a].intersection(boxes[b_]).area > 0.01:
                errs.append(f"recouvrement {PROGRAM[cells[a][1]][0]} / {PROGRAM[cells[b_][1]][0]}")

    net = unary_union([box(*c[:4]).buffer(0.01) for c in CORRIDORS])
    if len(_parts(net)) != 1:
        errs.append(f"reseau de circulation en {len(_parts(net))} morceaux")
    for (cx0, cy0, cx1, cy1, lab) in CORRIDORS:
        if min(cx1 - cx0, cy1 - cy0) < MODULE - 1e-6:
            errs.append(f"circulation {lab}: {min(cx1-cx0, cy1-cy0):.2f} m < {MODULE} m d'axe a axe")
        cbox = box(cx0, cy0, cx1, cy1)
        if cbox.difference(allowed).area > 0.10:
            errs.append(f"circulation {lab} deborde de la Game Area")
        for a, b_ in zip(cells, boxes):
            if cbox.intersection(b_).area > 0.01:
                errs.append(f"circulation {lab} coupe {PROGRAM[a[1]][0]}")
        for col in columns:                       # aucun poteau dans un couloir
            if cbox.intersection(box(*col)).area > 0.005:
                errs.append(f"circulation {lab} obstruee par le poteau {col}")

    for (c, i), b in zip(cells, boxes):
        d = c[4]
        if d in "NS":
            cx = (c[0] + c[2]) / 2
            yy = c[1] if d == "N" else c[3]
            bay = box(cx - 0.45, yy - 0.06, cx + 0.45, yy + 0.06)
        else:
            cy = (c[1] + c[3]) / 2
            xx = c[0] if d == "W" else c[2]
            bay = box(xx - 0.06, cy - 0.45, xx + 0.06, cy + 0.45)
        if bay.intersection(net).area < 0.9 * 0.06 * 0.98:
            errs.append(f"{PROGRAM[i][0]}: la porte ({d}) ne debouche pas sur une circulation")
        for col in columns:                       # poteau dans la baie de porte
            if bay.intersection(box(*col)).area > 0.005:
                errs.append(f"{PROGRAM[i][0]}: poteau dans la baie de porte")

    for col in columns:                           # poteaux repris dans les cellules
        g = box(*col)
        for (c, i), b in zip(cells, boxes):
            if g.intersection(b).area > 0.02:
                notes.append(f"poteau {col[2]-col[0]:.2f}x{col[3]-col[1]:.2f} m "
                             f"en saillie dans {PROGRAM[i][0]}")
    return errs, notes

# --------------------------------------------------------------------------
# Position de porte : centree si possible, sinon decalee pour degager
# les poteaux tout en restant sur la circulation
# --------------------------------------------------------------------------
DW = 0.90

def bay_box(c, t):
    """Baie de porte a la position relative t (0..1) sur le cote porte."""
    x0, y0, x1, y1, d = c
    if d in "NS":
        cx = x0 + WALL / 2 + DW / 2 + t * max(0.0, (x1 - x0) - WALL - DW)
        yy = y0 if d == "N" else y1
        return box(cx - DW / 2, yy - 0.06, cx + DW / 2, yy + 0.06), (cx, yy)
    cy = y0 + WALL / 2 + DW / 2 + t * max(0.0, (y1 - y0) - WALL - DW)
    xx = x0 if d == "W" else x1
    return box(xx - 0.06, cy - DW / 2, xx + 0.06, cy + DW / 2), (xx, cy)

def door_ok(c, columns_boxes, net):
    for side in [c[4]] + [d for d in "NSEW" if d != c[4]]:
        cc = (c[0], c[1], c[2], c[3], side)
        for t in [0.5] + [k / 20 for k in range(21)]:
            bay, _ = bay_box(cc, t)
            if bay.intersection(net).area < 0.9 * 0.06 * 0.98:
                continue
            if any(bay.intersection(g).area > 0.005 for g in columns_boxes):
                continue
            return True
    return False

def repair_doors(assign, columns, net):
    """Permute l'ordre des cellules a l'interieur de chaque bande jusqu'a ce
    que chacune dispose d'une baie de porte degagee des poteaux. Les surfaces
    affectees a la bande sont inchangees."""
    from itertools import permutations
    cb = [box(*c) for c in columns]
    fixed = []
    for b, idxs in zip(BANDS, assign):
        ok = None
        for perm in permutations(idxs):
            cells = slice_band(b, [PROGRAM[i][1] for i in perm])
            if all(door_ok(c, cb, net) for c in cells):
                ok = list(perm)
                break
        fixed.append(ok if ok else list(idxs))
    return fixed

def place_doors(cells, columns, net):
    """Porte centree si possible ; sinon decalee sur le meme cote, sinon
    reportee sur un autre cote de la cellule donnant sur une circulation."""
    cols = [box(*c) for c in columns]
    out = []
    for c, i in cells:
        best = None
        sides = [c[4]] + [d for d in "NSEW" if d != c[4]]
        for side in sides:
            cc = (c[0], c[1], c[2], c[3], side)
            for t in [0.5] + [k / 20 for k in range(21)]:
                bay, _ = bay_box(cc, t)
                if bay.intersection(net).area < 0.9 * 0.06 * 0.98:
                    continue
                if any(bay.intersection(g).area > 0.005 for g in cols):
                    continue
                best = (side, t)
                break
            if best:
                break
        side, t = best if best else (c[4], 0.5)
        out.append(((c[0], c[1], c[2], c[3], side), i, t, best is not None))
    return out

# --------------------------------------------------------------------------
# Dessin
# --------------------------------------------------------------------------
INK  = (0.10, 0.10, 0.12)
FILL = (1.0, 0.718, 0.506)   # meme teinte que la Game Area du fond de plan
CORR = (1.0, 1.0, 1.0)
ACC  = (0.78, 0.13, 0.13)

MASK_TEXT = ("Game Area", "H:2.66m", "H:2.47m", "H:2.07m", "H:2.1m")

def mask_background_labels(page, cells):
    """Masque les libelles du fond de plan qui tombent desormais dans une
    cellule (surface Game Area, hauteurs) : l'information est reprise dans
    le cartouche et dans le reperage des cellules sous hauteur reduite."""
    boxes = [box(*c[:4]) for c, i, t, ok in cells]
    sh = page.new_shape()
    rects = []
    spans = []
    for blk in page.get_text("dict")["blocks"]:
        for line in blk.get("lines", []):
            for sp in line.get("spans", []):
                spans.append((sp["text"].strip(), sp["bbox"]))
    for txt, bb in spans:
        if not any(k in txt for k in MASK_TEXT):
            continue
        pad = 0.75 * (bb[3] - bb[1]) + 2.0
        m = ((bb[0] - pad - X0) * S, (bb[1] - pad - Y0) * S,
             (bb[2] + pad - X0) * S, (bb[3] + pad + 0.5 * (bb[3] - bb[1]) - Y0) * S)
        g = box(*m)
        if any(g.intersection(q).area > 0.25 * g.area for q in boxes):
            # marge basse renforcee : ces libelles sont soulignes
            rects.append(pymupdf.Rect(bb[0] - pad, bb[1] - pad,
                                      bb[2] + pad, bb[3] + pad + 0.5 * (bb[3] - bb[1])))
    for r in rects:
        sh.draw_rect(r)
    sh.finish(color=None, fill=(1, 1, 1))
    sh.commit()
    # on restitue la teinte Game Area sous le masque pour ne pas creer de tache
    sh2 = page.new_shape()
    for r in rects:
        sh2.draw_rect(r)
    sh2.finish(color=None, fill=FILL, fill_opacity=0.25)
    sh2.commit()

def draw(page, doors, columns):
    mask_background_labels(page, doors)
    sh = page.new_shape()
    for (x0, y0, x1, y1, lab) in CORRIDORS:
        sh.draw_rect(R(x0, y0, x1, y1))
    sh.finish(color=None, fill=CORR, fill_opacity=1.0)
    sh.commit()

    sh2 = page.new_shape()
    for c, i, t, ok in doors:
        sh2.draw_rect(R(*c[:4]))
    sh2.finish(color=INK, fill=FILL, width=1.42, fill_opacity=0.25)
    sh2.commit()

    gap, leaf = page.new_shape(), page.new_shape()
    for c, i, t, ok in doors:
        _, (ax, ay) = bay_box(c, t)
        d = c[4]
        if d in "NS":
            sgn = -1 if d == "N" else 1
            gap.draw_line(P(ax - DW / 2, ay), P(ax + DW / 2, ay))
            hx, hy, tx, ty = ax - DW / 2, ay, ax - DW / 2, ay + DW * sgn
            ang = -90 * sgn
        else:
            sgn = -1 if d == "W" else 1
            gap.draw_line(P(ax, ay - DW / 2), P(ax, ay + DW / 2))
            hx, hy, tx, ty = ax, ay - DW / 2, ax + DW * sgn, ay - DW / 2
            ang = 90 * sgn
        leaf.draw_line(P(hx, hy), P(tx, ty))
        leaf.draw_sector(P(hx, hy), P(tx, ty), ang, fullSector=False)
    gap.finish(color=CORR, width=1.9)
    gap.commit()
    leaf.finish(color=INK, width=0.45)
    leaf.commit()

    # POTEAUX EXISTANTS redessines par-dessus : ils doivent rester lisibles
    sh3 = page.new_shape()
    for m in columns:
        sh3.draw_rect(R(*m))
    sh3.finish(color=(0, 0, 0), fill=(0.13, 0.10, 0.08), width=0.6)
    sh3.commit()

    lab = page.new_shape()
    for c, i, t, ok in doors:
        cy = (c[1] + c[3]) / 2
        wlab = min(c[2] - c[0] - 0.16, 3.2)
        lab.draw_rect(R((c[0]+c[2])/2 - wlab/2, cy - 0.52, (c[0]+c[2])/2 + wlab/2, cy + 0.46))
    lab.finish(color=None, fill=(1, 1, 1), fill_opacity=0.80)
    lab.commit()

    for c, i, t, ok in doors:
        name, target = PROGRAM[i]
        a = net_area(c)
        cy = (c[1] + c[3]) / 2
        w = c[2] - c[0]
        fs = 4.4 if w > 3.0 else (3.9 if w > 2.4 else 3.3)
        page.insert_textbox(R(c[0] + 0.06, cy - 1.05, c[2] - 0.06, cy + 1.05),
                            f"{i+1:02d}. {name}\n{a:.2f} m2".replace(".", ","),
                            fontname="hebo", fontsize=fs, color=INK, align=1)

LOW_207 = (24.40, 3.89, 30.02, 15.66)     # trame jaune H = 2,07 m

def low_cells(doors):
    z = box(*LOW_207)
    out = []
    for c, i, t, ok in doors:
        g = box(*c[:4])
        if g.intersection(z).area > 0.25 * g.area:
            out.append(PROGRAM[i][0])
    return out

def annotate(page, doors, poly, columns):
    areas = [net_area(c) for c, i, t, ok in doors]
    n = len(doors)
    bx0, by0, bx1, by1 = 352, 418, 610, 540
    page.draw_rect(pymupdf.Rect(bx0, by0, bx1, by1), color=INK, fill=(1, 1, 1), width=0.8)
    page.insert_text(pymupdf.Point(bx0 + 10, by0 + 22), f"{n} CELLS", fontname="hebo",
                     fontsize=15, color=INK)
    ecarts = [abs(net_area(c) - PROGRAM[i][1]) for c, i, t, ok in doors]
    lines = [
        ("IMPLANTATION DES CELLULES - GAME AREA", "hebo"),
        (f"Game Area : {poly.area:.2f} m2   -   {n} cellules".replace(".", ","), "helv"),
        (f"Surface utile cellules : {sum(areas):.2f} m2  ({sum(areas)/poly.area*100:.0f} %)".replace(".", ","), "helv"),
        (f"Surfaces reprises de l'esquisse client, ecart max {max(ecarts):.2f} m2".replace(".", ","), "helv"),
        (f"Cellules de {min(areas):.2f} a {max(areas):.2f} m2".replace(".", ","), "helv"),
        ("Circulations : 1,20 m de passage libre (module 1,30 m d'axe a axe)", "helv"),
        ("Cloisons 100 mm  -  portes de cellule 0,90 m", "helv"),
        (f"{len(columns)} poteaux existants releves, conserves et degages des circulations", "helv"),
        ("Hauteurs reduites a verifier : 2,07 m (jaune) et 2,10 m (rouge)", "helv"),
        ("Sous 2,07 m : " + ", ".join(low_cells(doors)), "helv"),
    ]
    y = by0 + 38
    for txt, fn in lines:
        page.insert_text(pymupdf.Point(bx0 + 10, y), txt, fontname=fn, fontsize=6.0, color=INK)
        y += 8.6
    for (x, y_, lab, dx, dy) in [(28.13, 22.30, "IN", -18, 12),
                                 (15.91, 16.30, "OUT", 6, -5),
                                 (0.0, 2.70, "ISSUE DE SECOURS", 6, -6),
                                 (25.35, 38.30, "ISSUE DE SECOURS", -6, 14)]:
        pt = P(x, y_)
        page.draw_circle(pt, 3.4, color=ACC, width=1.1)
        page.insert_text(pymupdf.Point(pt.x + dx, pt.y + dy), lab, fontname="hebo",
                         fontsize=5.4, color=ACC)

def main():
    doc = pymupdf.open(SRC)
    page = doc[0]
    poly = game_area_polygon(page)
    columns = read_columns(page, poly)
    assign, _ = solve(42)
    net = unary_union([box(*c[:4]).buffer(0.01) for c in CORRIDORS])
    assign = repair_doors(assign, columns, net)
    cells = []
    for b, idxs in zip(BANDS, assign):
        for cell, i in zip(slice_band(b, [PROGRAM[j][1] for j in idxs]), idxs):
            cells.append((cell, i))
    doors = place_doors(cells, columns, net)
    errs, notes = check(cells, poly, columns)
    errs += [f"{PROGRAM[i][0]}: aucune position de porte degagee"
             for c, i, t, ok in doors if not ok]
    errs = [e for e in errs if "poteau dans la baie de porte" not in e]

    print(f"Game Area          : {poly.area:.2f} m2")
    print(f"Cellules           : {len(cells)}")
    print(f"Poteaux releves    : {len(columns)} (tous conserves, hors circulations)")
    ec = [abs(net_area(c) - PROGRAM[i][1]) for c, i in cells]
    print(f"Ecart max / esquisse client : {max(ec):.2f} m2 (tolerance {TOL} m2)")
    if errs:
        print("!! CONTROLES EN ECHEC :")
        for e in errs:
            print("   -", e)
    else:
        print("Controles geometriques : OK")
        print("  - 38 cellules dans l'emprise, sans recouvrement")
        print("  - circulations >= 1,20 m libre, reseau connexe, aucun poteau dedans")
        print("  - chaque cellule ouvre par une porte de 0,90 m degagee de tout poteau")
    draw(page, doors, columns)
    annotate(page, doors, poly, columns)
    doc.save(OUT, deflate=True)
    tot = sum(net_area(c) for c, i in cells)
    print(f"Surface utile      : {tot:.2f} m2 ({tot/poly.area*100:.1f} % de la Game Area)")
    print("->", OUT)
    return errs

if __name__ == "__main__":
    import sys
    sys.exit(1 if main() else 0)
