# Generates the group org chart as inline SVG (viewBox 1700 x 840)
NAVY="#101F3A"; ACC="#D9522B"; LINE="#AEB6C2"; PANEL="#F4F5F7"; BORDER="#CFD5DE"; MUTED="#6B7683"; TINT="#E9EDF3"
out=[]
def rect(x,y,w,h,fill,stroke,sw=1.5,dash=None,rx=6):
    d=f' stroke-dasharray="7 5"' if dash else ''
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
def text(x,y,s,size=14,weight=500,fill=NAVY,anchor="middle",family="Inter",ls=0):
    out.append(f'<text x="{x}" y="{y}" font-family="{family}, Inter, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{s}</text>')
def box(cx,cy,w,h,lines,fill=PANEL,stroke=BORDER,sw=1.2,size=14,weight=500,color=NAVY,dash=None,sub=None):
    rect(cx-w/2,cy-h/2,w,h,fill,stroke,sw,dash)
    n=len(lines); lh=size*1.25
    total=n*lh + (14 if sub else 0)
    y0=cy - total/2 + size*0.85
    for i,l in enumerate(lines):
        text(cx,y0+i*lh,l,size,weight,color)
    if sub:
        text(cx,y0+n*lh+2,sub,11.5,500,("rgba(255,255,255,.75)" if color=="#fff" else MUTED))
def line(pts,arrow=True):
    d=" ".join(("M" if i==0 else "L")+f"{x},{y}" for i,(x,y) in enumerate(pts))
    m=' marker-end="url(#ah)"' if arrow else ''
    out.append(f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="1.6"{m}/>')
def pct(x,y,s,size=13):
    w=len(s)*7.2+12
    out.append(f'<rect x="{x-w/2}" y="{y-10}" width="{w}" height="20" rx="10" fill="#fff" stroke="{BORDER}" stroke-width="1"/>')
    text(x,y+4.5,s,size,600,NAVY)

out.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="'+LINE+'"/></marker></defs>')

# ---------- Top: founders / holdings / SAS ENCORE ----------
FX=[120,340,560]
founders=[["Mikaël Bouteillon"],["Thibault d'Ayguesvives"],["Thibault Poncet"]]
holdings=[(["EURL TLK Holding"],"880 274 006 (FR)"),(["EURL DDT Holding"],"904 091 071 (FR)"),(["SARL Poncet Holding"],"799 344 353 (FR)")]
shares=["51 %","39 %","10 %"]
for i,x in enumerate(FX):
    box(x,24,200,48,founders[i],fill="#fff",stroke=NAVY,sw=1.4,size=14.5,weight=600)
    line([(x,48),(x,88)])
    pct(x+40,68,"100 %")
    box(x,118,200,60,holdings[i][0],fill=TINT,stroke=BORDER,size=14.5,weight=600,sub=holdings[i][1])
# SAS ENCORE
SEX,SEY=340,250
box(SEX,SEY,320,68,["SAS ENCORE"],fill=NAVY,stroke=NAVY,size=18,weight=700,color="#fff",sub="988 864 278 (FR)")
# holdings -> SAS ENCORE
line([(120,148),(120,190),(250,190),(250,216)])
line([(340,148),(340,216)])
line([(560,148),(560,190),(430,190),(430,216)])
pct(120,205,"51 %"); pct(340+42,182,"39 %"); pct(560,205,"10 %")

# ---------- Left: ENCORE OFFICE + France ----------
line([(180,284),(120,284),(120,352)]); pct(120,318,"100 %")
box(120,378,200,52,["ENCORE OFFICE"],fill="#fff",stroke=NAVY,sw=1.6,size=14.5,weight=700)
text(120,424,"Structure animatrice et fonctions de siège",11.5,500,MUTED)
# France container
FXc=[335,525]; FY0=350
rect(250,FY0,370,424,"#fff",BORDER,1.2,rx=8)
line([(340,284),(340,FY0)]); pct(340+42,318,"100 %")
text(435,FY0+30,"SOCIÉTÉS D'EXPLOITATION — FRANCE",12.5,700,ACC,ls=1.2)
fr_col1=[["Prison Island","Montpellier"],["Prison Island","Toulouse"],["Prison Island","Clermont Ferrand"],["Prison Island","Avignon"],["Prison Island","Orleans"],["Prison Island","Aubagne"],["Mini Mundo","Aubagne"]]
fr_col2=[["Alcatraz Adventure"],["Prison Island","Marseille"],["Prison Island","Saint Avertin"],["Prison Island","Valence"],["Expedition","Marseille"],["Prison Island","Paris 19"]]
for ci,col in enumerate([fr_col1,fr_col2]):
    for ri,l in enumerate(col):
        box(FXc[ci],FY0+70+ri*52,172,42,l,size=13.5,weight=500)

# ---------- Right: OUT 4 BLOOD DEVELOPPEMENT ----------
OX,OY=930,250
line([(500,250),(760,250)]); pct(630,250,"100 %")
box(OX,OY,340,68,["OUT 4 BLOOD DEVELOPPEMENT"],fill="#fff",stroke=NAVY,sw=1.8,size=15,weight=700)
# bus
COLS=[795,995,1195,1395,1595]
BUSY=330
line([(OX,284),(OX,BUSY)],arrow=False)
line([(COLS[0],BUSY),(COLS[-1],BUSY)],arrow=False)
pct(OX+52,308,"100 %")
HY=372
regions=[None,["OUT 4 AUSTRALIA","PTY LTD"],["OUT 4 USA"],["OUT 4 UNITED","KINGDOM LIMITED"],["OUT 4 MEXICO"]]
subs=[
 [(["Prison Island","Berlin"],False),(["Prison Island","Stuttgart"],False),(["Prison Island","Frankfurt"],True),(["Prison Island","Barcelona"],True)],
 [(["Prison Island","Melbourne"],False),(["Prison Island","Brisbane"],False),(["Prison Island Perth"],False),(["Prison Gold Coast"],False),(["Speed Planet Brisbane"],False),(["Mini Mundo Melbourne"],False)],
 [(["PI Indianapolis"],False),(["PI Dallas"],False),(["PI New York"],False),(["PI Orlando"],False)],
 [(["Prison Island","London"],False),(["Prison Island","London 2"],False)],
 [(["Prison Island Mexico"],False)],
]
for i,cx in enumerate(COLS):
    if regions[i]:
        line([(cx,BUSY),(cx,HY-26)])
        box(cx,HY,184,52,regions[i],fill="#fff",stroke=NAVY,sw=1.4,size=13.5,weight=700)
        # vertical spine from header to subs
        y_first=HY+26+34+21
        y_last=y_first+(len(subs[i])-1)*52
        sx=cx-92-14
        line([(cx,HY+26),(cx,HY+40),(sx,HY+40),(sx,y_last)],arrow=False) if len(subs[i])>1 else None
        pct(cx+50,HY+40,"100 %") 
        for ri,(l,proj) in enumerate(subs[i]):
            cy=y_first+ri*52
            if len(subs[i])>1: line([(sx,cy),(cx-92,cy)])
            else: line([(cx,HY+26),(cx,cy-21)])
            box(cx,cy,184,42,l,size=13.5,weight=500,fill=("#fff" if proj else PANEL),stroke=(NAVY if proj else BORDER),sw=(1.2 if proj else 1.2),dash=proj)
    else:
        # direct European subsidiaries hanging from the bus
        text(cx-92,HY-16,"EUROPE",11.5,700,ACC,anchor="start",ls=1.2); text(cx-92,HY-1,"Détention directe",11.5,500,MUTED,anchor="start")
        sx=cx-92-14
        y_first=HY+26+34+21
        y_last=y_first+(len(subs[i])-1)*52
        line([(cx,BUSY),(cx,HY-24),(sx,HY-24)],arrow=False)
        line([(sx,HY-24),(sx,y_last)],arrow=False)
        pct(cx+50,HY+12,"100 %")
        for ri,(l,proj) in enumerate(subs[i]):
            cy=y_first+ri*52
            line([(sx,cy),(cx-92,cy)])
            box(cx,cy,184,42,l,size=13.5,weight=500,fill=("#fff" if proj else PANEL),stroke=(NAVY if proj else BORDER),dash=proj)

# ---------- Legend ----------
LX,LY=1490,600
text(LX,LY-14,"LÉGENDE",11.5,700,ACC,anchor="start",ls=1.2)
rect(LX,LY,26,18,PANEL,BORDER,1.2,rx=4); text(LX+36,LY+14,"Société en activité",12.5,500,MUTED,anchor="start")
rect(LX,LY+30,26,18,"#fff",NAVY,1.2,dash=True,rx=4); text(LX+36,LY+44,"Société en cours de création",12.5,500,MUTED,anchor="start")
rect(LX,LY+60,26,18,"#fff",NAVY,1.4,rx=4); text(LX+36,LY+74,"Holding / structure de tête",12.5,500,MUTED,anchor="start")
text(LX,LY+108,"Pourcentages : quote-part",12,500,MUTED,anchor="start"); text(LX,LY+126,"de détention du capital",12,500,MUTED,anchor="start")

svg='<svg viewBox="0 0 1700 800" width="1700" height="800" xmlns="http://www.w3.org/2000/svg">'+"".join(out)+'</svg>'
open("orgchart.svg","w",encoding="utf-8").write(svg)
print("svg ok", len(svg))
