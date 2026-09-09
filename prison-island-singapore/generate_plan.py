#!/usr/bin/env python3
"""
Prison Island Singapore - ESQ
Implantation des cellules dans la Game Area (614,12 m2).

Le fond de plan ESQ d'origine est conserve; les cellules, les circulations
et les cotations sont dessinees par-dessus.

Repere de travail : metres, origine au coin haut-gauche de la bounding box
de la Game Area, x vers la droite, y vers le bas.
Echelle du fond de plan : 1:200 sur A3  ->  1 pt PDF = 0,0705556 m
"""
import math
import pymupdf
from shapely.geometry import Polygon, box

SRC = "/root/.claude/uploads/62955517-4c19-5b46-b0e1-471b227c3618/2b4aa1b3-ESQ__PI__SINGAPORE_1.pdf"
OUT = "/home/user/MikaB/prison-island-singapore/PI_SINGAPORE_PLAN_41_Cells.pdf"

S = 0.0705556                 # metres par point PDF
PPM = 1.0 / S                 # points PDF par metre (14,1732)
X0, Y0 = 582.4468994140625, 68.34652709960938   # origine du repere (pt PDF)

WALL = 0.10                   # epaisseur des cloisons (m)
CLEAR = 1.20                  # passage libre exige en circulation (m)
MODULE = CLEAR + WALL         # 1,30 m d'axe a axe de cloison

def P(x, y):
    """metres -> points PDF"""
    return pymupdf.Point(X0 + x * PPM, Y0 + y * PPM)

def R(x0, y0, x1, y1):
    return pymupdf.Rect(X0 + x0 * PPM, Y0 + y0 * PPM, X0 + x1 * PPM, Y0 + y1 * PPM)

# --------------------------------------------------------------------------
# 1. Contour exact de la Game Area (extrait du PDF source)
# --------------------------------------------------------------------------
def game_area_polygon(page):
    for d in page.get_drawings():
        f = d["fill"]
        if f and tuple(round(v, 3) for v in f) == (1.0, 0.718, 0.506) and d["rect"].width > 100:
            pts = [((it[1].x - X0) * S, (it[1].y - Y0) * S) for it in d["items"] if it[0] == "l"]
            return Polygon(pts)
    raise RuntimeError("contour Game Area introuvable")

def read_columns(page, poly):
    """Poteaux existants (carres / rectangles noirs) du fond de plan."""
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
        if 0.15 < w < 4 and 0.15 < h < 4 and box(*m).intersects(zone):
            out.append(tuple(round(v, 3) for v in m))
    return sorted(set(out), key=lambda t: (t[1], t[0]))

# --------------------------------------------------------------------------
# 2. Noms de cellules Prison Island (nomenclature des plans de reference)
# --------------------------------------------------------------------------
NAMES = [
    "Slippery Slope", "Riot", "Basket", "Catch", "Colorblind", "Penalty", "Tilt",
    "Lucky Lane", "Inca", "Green Mile", "Music", "The Hub", "Shark Bay",
    "Cell Block North", "Work Out", "Boiler Room", "Maps", "Devils Island",
    "Ventilation", "Roof Top", "Gates", "Pyramid", "The Burglar", "Hitman",
    "The Nest", "Laser Gun", "KettleBell", "Studio 21", "Butchers Lane",
    "Waterfall", "Joker", "Wire", "Visitors", "Source Code", "The Docks",
    "The Prison", "Hands On", "Tower", "Submarine", "Cliffhanger", "Dive",
    "Einstein", "Copy Cat", "The Vault", "Smash & Grab",
]

# --------------------------------------------------------------------------
# 3. Trame : circulations (modules d'axe a axe) et files de cellules
# --------------------------------------------------------------------------
# --- Zone A ouest : x 1,90 -> 15,91 ; y 0 -> 17,549 -----------------------
AW_X0, AW_X1 = 1.90, 15.91
# --- Zone A est   : x 15,91 -> 29,945 ; y 2,00/3,90 -> 12,10 --------------
V1_X0, V1_X1 = 15.91, 17.21          # circulation verticale de liaison
# --- Zone B (bande est) ---------------------------------------------------
CB_X0, CB_X1 = 28.127, 29.527        # circulation verticale principale
# --- Zone C (bloc sud) ----------------------------------------------------
CT_X0, CT_X1 = 18.167, 19.467        # circulation verticale ouest

CORRIDORS = [
    # (x0, y0, x1, y1, libelle)
    (0.00,  3.60, 15.91,  4.90, "C1"),      # E-O nord
    (0.00,  2.20,  1.90,  3.60, "SI"),      # acces issue de secours ouest
    (13.445, 2.00, 15.91, 3.60, "C1b"),     # elargissement sous l'escalier S8
    (1.90, 12.10, 29.945, 13.40, "C2"),     # E-O centrale (epine dorsale)
    (14.61, 13.40, 15.91, 17.549, "COUT"),  # antenne vers la porte OUT
    (V1_X0, 2.00, V1_X1, 12.10, "V1"),      # N-S de liaison A-ouest / A-est
    (17.21,  6.85, 29.945, 8.15, "C3"),     # E-O zone A est
    (CB_X0, 13.40, CB_X1, 33.95, "CB"),     # N-S zone B -> zone C (porte IN)
    (18.167, 32.65, 29.437, 33.95, "CC"),   # E-O zone C
    (CT_X0, 33.95, CT_X1, 43.40, "CT"),     # N-S zone C ouest (vers la queue)
    (24.70, 33.95, 26.00, 38.30, "CS"),     # antenne vers la porte coupe-feu sud
]

def strip(x0, y0, x1, y1, n, door, axis="x"):
    """Decoupe une bande en n cellules egales. door = N/S/E/W."""
    out = []
    for i in range(n):
        if axis == "x":
            a = x0 + (x1 - x0) * i / n
            b = x0 + (x1 - x0) * (i + 1) / n
            out.append((a, y0, b, y1, door))
        else:
            a = y0 + (y1 - y0) * i / n
            b = y0 + (y1 - y0) * (i + 1) / n
            out.append((x0, a, x1, b, door))
    return out

CELLS = []
# ---- ZONE A OUEST --------------------------------------------------------
CELLS += strip(AW_X0,  0.00, 13.445, 3.60, 4, "S")            # R1
CELLS += strip(AW_X0,  4.90, AW_X1,  8.60, 5, "N")            # R2
CELLS += strip(AW_X0,  8.60, AW_X1, 12.10, 5, "S")            # R3
CELLS += strip(AW_X0, 13.40, 14.61, 17.549, 4, "N")           # R4
# ---- ZONE A EST ----------------------------------------------------------
CELLS += strip(V1_X1,  2.00, 22.695, 6.85, 2, "S")            # nord-ouest
CELLS += strip(22.695, 3.90, 29.945, 6.85, 2, "S")            # nord-est
CELLS += strip(V1_X1,  8.15, 29.945, 12.10, 5, "S")           # sud
# ---- ZONE B --------------------------------------------------------------
CELLS += strip(24.395, 15.59, CB_X0, 21.104, 2, "E", axis="y")
CELLS += strip(CB_X1, 16.229, 33.145, 21.104, 2, "W", axis="y")
CELLS += strip(CB_X1, 21.104, 33.145, 28.908, 3, "W", axis="y")
# ---- ZONE C --------------------------------------------------------------
CELLS += strip(18.167, 29.625, CB_X0, 32.65, 3, "S")          # file nord
CELLS += strip(CT_X1, 33.95, 24.70, 38.30, 2, "N")            # file sud ouest
CELLS += strip(26.00, 33.95, 29.945, 38.30, 1, "N")           # file sud est
CELLS += strip(CT_X1, 38.30, 22.27, 42.60, 1, "W")            # queue sud

# --------------------------------------------------------------------------
# 4. Controles geometriques
# --------------------------------------------------------------------------
# Micro-reservations du contour (poteaux de facade 800x400 et gaine technique
# 800x1000 au droit de la porte coupe-feu sud) : elles sont absorbees dans
# l'epaisseur des cloisons / restent en saillie dans la cellule.
RESERVES = [
    (4.336, 0.00, 5.145, 0.399),
    (12.691, 0.00, 13.445, 0.399),
    (26.020, 37.299, 26.820, 38.324),
]

def buildable(poly):
    """Game Area + micro-reservations absorbees par les cloisons de cellule."""
    from shapely.ops import unary_union
    extra = [g for g in _parts(poly.envelope.difference(poly))
             if g.area < 1.2 and g.intersects(poly)]
    extra += [box(*r) for r in RESERVES]
    return unary_union([poly] + extra).buffer(0.02)

def _parts(g):
    return list(g.geoms) if hasattr(g, "geoms") else [g]

def check(poly):
    poly = buildable(poly)
    errs = []
    boxes = []
    for i, (x0, y0, x1, y1, d) in enumerate(CELLS):
        b = box(x0, y0, x1, y1)
        boxes.append(b)
        if b.difference(poly).area > 0.05:
            errs.append(f"cellule {i+1} deborde de la Game Area "
                        f"({b.difference(poly).area:.2f} m2)")
        if min(x1 - x0, y1 - y0) - WALL < 2.30:
            errs.append(f"cellule {i+1} trop etroite ({min(x1-x0, y1-y0)-WALL:.2f} m)")
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            if boxes[i].intersection(boxes[j]).area > 0.01:
                errs.append(f"recouvrement cellules {i+1}/{j+1}")
    # reseau de circulation : connexite
    from shapely.ops import unary_union
    net = unary_union([box(*c[:4]).buffer(0.01) for c in CORRIDORS])
    if len(_parts(net)) != 1:
        errs.append(f"reseau de circulation en {len(_parts(net))} morceaux non relies")
    # chaque cellule doit ouvrir sur une circulation (baie de 0,90 m)
    for i, (x0, y0, x1, y1, d) in enumerate(CELLS):
        if d in "NS":
            cx = (x0 + x1) / 2
            yy = y0 if d == "N" else y1
            bay = box(cx - 0.45, yy - 0.06, cx + 0.45, yy + 0.06)
        else:
            cy = (y0 + y1) / 2
            xx = x0 if d == "W" else x1
            bay = box(xx - 0.06, cy - 0.45, xx + 0.06, cy + 0.45)
        if bay.intersection(net).area < 0.9 * 0.06:
            errs.append(f"cellule {i+1} : la porte ({d}) ne debouche pas sur une circulation")
    for (cx0, cy0, cx1, cy1, lab) in CORRIDORS:
        if min(cx1 - cx0, cy1 - cy0) < MODULE - 1e-6:
            errs.append(f"circulation {lab} < {MODULE} m d'axe a axe")
        c = box(cx0, cy0, cx1, cy1)
        for i, b in enumerate(boxes):
            if c.intersection(b).area > 0.01:
                errs.append(f"circulation {lab} coupe la cellule {i+1}")
        if c.difference(poly).area > 0.10:
            errs.append(f"circulation {lab} deborde de la Game Area")
    return errs

# --------------------------------------------------------------------------
# 5. Dessin
# --------------------------------------------------------------------------
INK   = (0.10, 0.10, 0.12)
FILL  = (1.0, 0.718, 0.506)     # meme teinte que la Game Area du fond de plan
CORR  = (1.0, 1.0, 1.0)
ACC   = (0.78, 0.13, 0.13)

def draw(page, poly):
    # --- circulations : fond blanc pour degager le cheminement --------------
    sh = page.new_shape()
    for (x0, y0, x1, y1, lab) in CORRIDORS:
        sh.draw_rect(R(x0, y0, x1, y1))
    sh.finish(color=None, fill=CORR, fill_opacity=1.0)
    sh.commit()

    # --- cellules -----------------------------------------------------------
    sh2 = page.new_shape()
    for (x0, y0, x1, y1, d) in CELLS:
        sh2.draw_rect(R(x0, y0, x1, y1))
    sh2.finish(color=INK, fill=FILL, width=1.42, fill_opacity=0.25)  # 1,42 pt = cloison 100 mm
    sh2.commit()

    # --- portes : baie de 0,90 m, vantail + arc de debattement ------------
    DW = 0.90
    gap = page.new_shape()
    leaf = page.new_shape()
    for (x0, y0, x1, y1, d) in CELLS:
        if d in "NS":
            cx = (x0 + x1) / 2
            y = y0 if d == "N" else y1
            sgn = -1 if d == "N" else 1
            hx, hy = cx - DW / 2, y                 # gond
            tx, ty = hx, y + DW * sgn               # extremite du vantail
            gap.draw_line(P(cx - DW / 2, y), P(cx + DW / 2, y))
            ang = -90 * sgn
        else:
            cy = (y0 + y1) / 2
            x = x0 if d == "W" else x1
            sgn = -1 if d == "W" else 1
            hx, hy = x, cy - DW / 2
            tx, ty = x + DW * sgn, hy
            gap.draw_line(P(x, cy - DW / 2), P(x, cy + DW / 2))
            ang = 90 * sgn
        leaf.draw_line(P(hx, hy), P(tx, ty))
        leaf.draw_sector(P(hx, hy), P(tx, ty), ang, fullSector=False)
    gap.finish(color=CORR, width=1.9)               # efface la cloison au droit de la baie
    gap.commit()
    leaf.finish(color=INK, width=0.45)
    leaf.commit()

    # --- POTEAUX EXISTANTS redessines par-dessus : ils doivent rester lisibles
    shc = page.new_shape()
    for m in read_columns(page, poly):
        shc.draw_rect(R(*m))
    shc.finish(color=(0, 0, 0), fill=(0.13, 0.10, 0.08), width=0.6)
    shc.commit()


    # --- textes -------------------------------------------------------------
    for i, (x0, y0, x1, y1, d) in enumerate(CELLS):
        net = (x1 - x0 - WALL) * (y1 - y0 - WALL)
        cy = (y0 + y1) / 2
        w = x1 - x0
        fs = 4.4 if w > 3.0 else (3.9 if w > 2.6 else 3.4)
        page.insert_textbox(R(x0 + 0.06, cy - 1.05, x1 - 0.06, cy + 1.05),
                            f"{i+1:02d}. {NAMES[i % len(NAMES)]}\n{net:.2f} m2".replace(".", ","),
                            fontname="hebo", fontsize=fs, color=INK, align=1)
    return sum((x1 - x0 - WALL) * (y1 - y0 - WALL) for x0, y0, x1, y1, d in CELLS)

def annotate(page, n, net, poly):
    areas = [(a[2] - a[0] - WALL) * (a[3] - a[1] - WALL) for a in CELLS]
    bx0, by0, bx1, by1 = 352, 424, 604, 534
    page.draw_rect(pymupdf.Rect(bx0, by0, bx1, by1), color=INK, fill=(1, 1, 1), width=0.8)
    page.insert_text(pymupdf.Point(bx0 + 10, by0 + 22), f"{n} CELLS", fontname="hebo",
                     fontsize=15, color=INK)
    lines = [
        ("IMPLANTATION DES CELLULES - GAME AREA", "hebo"),
        (f"Game Area : 614,12 m2   -   {n} cellules", "helv"),
        (f"Surface utile cellules : {net:.2f} m2  ({net/poly.area*100:.0f} %)".replace(".", ","), "helv"),
        (f"Cellule moyenne {net/n:.2f} m2  (mini {min(areas):.2f} / maxi {max(areas):.2f})".replace(".", ","), "helv"),
        ("Circulations : 1,20 m de passage libre (module 1,30 m d'axe a axe)", "helv"),
        ("Cloisons 100 mm  -  portes de cellule 0,90 m", "helv"),
        ("Poteaux existants 900x900 conserves, integres aux cloisons/cellules", "helv"),
        ("Hauteurs reduites a verifier : 2,07 m (jaune) et 2,10 m (rouge)", "helv"),
    ]
    y = by0 + 38
    for txt, fn in lines:
        page.insert_text(pymupdf.Point(bx0 + 10, y), txt, fontname=fn, fontsize=6.0, color=INK)
        y += 8.6
    # reperes du parcours
    for (x, y_, lab, dx, dy) in [(28.13, 22.30, "IN", 6, 3),
                                 (15.91, 16.30, "OUT", 6, -5),
                                 (0.0, 2.70, "ISSUE DE SECOURS", 6, -6),
                                 (25.35, 38.30, "ISSUE DE SECOURS", 6, 12)]:
        pt = P(x, y_)
        page.draw_circle(pt, 3.4, color=ACC, width=1.1)
        page.insert_text(pymupdf.Point(pt.x + dx, pt.y + dy), lab, fontname="hebo",
                         fontsize=5.4, color=ACC)

def main():
    doc = pymupdf.open(SRC)
    page = doc[0]
    poly = game_area_polygon(page)
    errs = check(poly)
    print(f"Game Area : {poly.area:.2f} m2")
    print(f"Cellules  : {len(CELLS)}")
    if errs:
        print("!! CONTROLES EN ECHEC :")
        for e in errs:
            print("   -", e)
    else:
        print("Controles geometriques : OK")
        print("  - 41 cellules dans l'emprise de la Game Area, sans recouvrement")
        print("  - circulations >= 1,20 m de passage libre, reseau connexe")
        print("  - chaque cellule ouvre par une porte de 0,90 m sur une circulation")
    net = draw(page, poly)
    annotate(page, len(CELLS), net, poly)
    doc.save(OUT, deflate=True)
    print(f"Surface utile cellules : {net:.2f} m2 "
          f"({net/poly.area*100:.1f} % de la Game Area)")
    print(f"Moyenne : {net/len(CELLS):.2f} m2/cellule")
    print("->", OUT)
    return errs

if __name__ == "__main__":
    import sys
    sys.exit(1 if main() else 0)
