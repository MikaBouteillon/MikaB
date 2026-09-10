# Organigramme du Groupe — SVG généré (viewBox 1700 x 830)
import base64
NAVY="#101F3A"; ACC="#D9522B"; LINE="#AEB6C2"; MUTED="#6B7683"; BORDER="#CFD5DE"
# palette (teintes sobres inspirées de l'original)
C_PERSON=("#FFF4D6","#E2B54B")   # fondateurs : ambre
C_HOLD=("#E4F3E7","#6DB97E")     # holdings personnelles : vert
C_TOP=(ACC,ACC)                  # SAS ENCORE : orange marque, texte blanc
C_OFFICE=("#FBEAB4","#D9A400")   # ENCORE OFFICE : jaune
C_DEV=("#FDE4D3","#E07A30")      # OUT 4 BLOOD DEVELOPPEMENT : orange clair
C_REG=("#F1E4F6","#B07CC6")      # holdings régionales : violet
C_OPS=("#E6EFFA","#9FBBDF")      # sociétés d'exploitation : bleu clair
C_PROJ=("#FFFFFF","#7FA3D0")     # en création : pointillés

def flag_data(cc):
    return "data:image/png;base64,"+base64.b64encode(open(f"assets/flags/{cc}.png","rb").read()).decode()
FLAGS={cc:flag_data(cc) for cc in ["fr","de","gb","es","au","us","mx"]}

out=[]
def rect(x,y,w,h,fill,stroke,sw=1.5,dash=None,rx=6):
    d=' stroke-dasharray="7 5"' if dash else ''
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
def text(x,y,s,size=14,weight=500,fill=NAVY,anchor="middle",ls=0):
    out.append(f'<text x="{x}" y="{y}" font-family="Inter, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{s}</text>')
def flag(x,y,cc,w=22,h=15):
    out.append(f'<clipPath id="c{len(out)}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2.5"/></clipPath>')
    out.append(f'<image href="{FLAGS[cc]}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#c{len(out)-1})"/>')
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2.5" fill="none" stroke="rgba(16,31,58,.18)" stroke-width="1"/>')
def box(cx,cy,w,h,lines,col,sw=1.3,size=14,weight=500,color=NAVY,dash=None,sub=None,fl=None):
    rect(cx-w/2,cy-h/2,w,h,col[0],col[1],sw,dash)
    n=len(lines); lh=size*1.25
    total=n*lh+(14 if sub else 0)
    y0=cy-total/2+size*0.85
    tx=cx+(12 if fl else 0)
    for i,l in enumerate(lines): text(tx,y0+i*lh,l,size,weight,color)
    if sub: text(tx,y0+n*lh+2,sub,11.5,500,("rgba(255,255,255,.8)" if color=="#fff" else MUTED))
    if fl: flag(cx-w/2+10,cy-7.5,fl)
def line(pts,arrow=True):
    d=" ".join(("M" if i==0 else "L")+f"{x},{y}" for i,(x,y) in enumerate(pts))
    out.append(f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="1.6"{" marker-end=url(#ah)" if arrow else ""}/>'.replace("marker-end=url(#ah)",'marker-end="url(#ah)"'))
def pct(x,y,s,size=13):
    w=len(s)*7.2+12
    out.append(f'<rect x="{x-w/2}" y="{y-10}" width="{w}" height="20" rx="10" fill="#fff" stroke="{BORDER}" stroke-width="1"/>')
    text(x,y+4.5,s,size,600,NAVY)

out.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="'+LINE+'"/></marker></defs>')

# ---------- Fondateurs / holdings / SAS ENCORE (centré, pleine largeur) ----------
CX=850
FX=[CX-440,CX,CX+440]
founders=[["Mikaël Bouteillon"],["Thibault d'Ayguesvives"],["Thibault Poncet"]]
holdings=[(["EURL TLK Holding"],"880 274 006 (FR)"),(["EURL DDT Holding"],"904 091 071 (FR)"),(["SARL Poncet Holding"],"799 344 353 (FR)")]
shares=["51 %","39 %","10 %"]
for i,x in enumerate(FX):
    box(x,24,230,48,founders[i],C_PERSON,sw=1.3,size=15,weight=600)
    line([(x,48),(x,78)]); pct(x+44,63,"100 %")
    box(x,106,230,60,holdings[i][0],C_HOLD,size=15,weight=600,sub=holdings[i][1])
SEY=220
box(CX,SEY,380,68,["SAS ENCORE"],C_TOP,size=19,weight=700,color="#fff",sub="988 864 278 (FR)")
line([(FX[0],136),(FX[0],162),(CX-120,162),(CX-120,186)]); pct(FX[0],176,"51 %")
line([(CX,136),(CX,186)]); pct(CX+44,160,"39 %")
line([(FX[2],136),(FX[2],162),(CX+120,162),(CX+120,186)]); pct(FX[2],176,"10 %")

# ---------- Bus principal ----------
BUS1=278
OFX=120; FRX=435; DEVX=1200
line([(CX,254),(CX,BUS1)],arrow=False)
line([(OFX,BUS1),(DEVX,BUS1)],arrow=False)
# ENCORE OFFICE
line([(OFX,BUS1),(OFX,312)]); pct(OFX+44,295,"100 %")
box(OFX,338,210,52,["ENCORE OFFICE"],C_OFFICE,sw=1.3,size=14.5,weight=700)
text(OFX,384,"Structure animatrice",11.5,500,MUTED); text(OFX,399,"et fonctions de siège",11.5,500,MUTED)
# FRANCE
FY0=312
line([(FRX,BUS1),(FRX,FY0)]); pct(FRX+44,295,"100 %")
rect(250,FY0,370,424,"#fff",BORDER,1.2,rx=8)
flag(268,FY0+18,"fr"); text(298,FY0+30,"SOCIÉTÉS D'EXPLOITATION — FRANCE",12.5,700,ACC,anchor="start",ls=1.2)
fr_col1=[["Prison Island","Montpellier"],["Prison Island","Toulouse"],["Prison Island","Clermont Ferrand"],["Prison Island","Avignon"],["Prison Island","Orleans"],["Prison Island","Aubagne"],["Mini Mundo","Aubagne"]]
fr_col2=[["Alcatraz Adventure"],["Prison Island","Marseille"],["Prison Island","Saint Avertin"],["Prison Island","Valence"],["Expedition","Marseille"],["Prison Island","Paris 19"]]
for ci,col in enumerate([fr_col1,fr_col2]):
    for ri,l in enumerate(col):
        box([335,525][ci],FY0+70+ri*52,172,42,l,C_OPS,size=13.5)
# OUT 4 BLOOD DEVELOPPEMENT
DEVY=342
line([(DEVX,BUS1),(DEVX,DEVY-34)]); pct(DEVX+44,295,"100 %")
box(DEVX,DEVY,360,68,["OUT 4 BLOOD DEVELOPPEMENT"],C_DEV,sw=1.6,size=15.5,weight=700)
COLS=[795,995,1195,1395,1595]
BUS2=404; HY=446
line([(DEVX,DEVY+34),(DEVX,BUS2)],arrow=False); pct(DEVX+44,390,"100 %")
line([(COLS[0],BUS2),(COLS[-1],BUS2)],arrow=False)
regions=[None,(["OUT 4 AUSTRALIA","PTY LTD"],"au"),(["OUT 4 USA"],"us"),(["OUT 4 UNITED","KINGDOM LIMITED"],"gb"),(["OUT 4 MEXICO"],"mx")]
subs=[
 [(["Prison Island","Berlin"],False,"de"),(["Prison Island","Stuttgart"],False,"de"),(["Prison Island","Frankfurt"],True,"de"),(["Prison Island","Barcelona"],True,"es")],
 [(["Prison Island","Melbourne"],False,None),(["Prison Island","Brisbane"],False,None),(["Prison Island Perth"],False,None),(["Prison Gold Coast"],False,None),(["Speed Planet Brisbane"],False,None),(["Mini Mundo Melbourne"],False,None)],
 [(["PI Indianapolis"],False,None),(["PI Dallas"],False,None),(["PI New York"],False,None),(["PI Orlando"],False,None)],
 [(["Prison Island","London"],False,None),(["Prison Island","London 2"],False,None)],
 [(["Prison Island Mexico"],False,None)],
]
for i,cx in enumerate(COLS):
    sx=cx-92-14
    y_first=HY+26+34+21
    y_last=y_first+(len(subs[i])-1)*52
    if regions[i]:
        line([(cx,BUS2),(cx,HY-26)])
        box(cx,HY,184,52,regions[i][0],C_REG,sw=1.3,size=13.5,weight=700,fl=regions[i][1])
        if len(subs[i])>1:
            line([(cx,HY+26),(cx,HY+40),(sx,HY+40),(sx,y_last)],arrow=False)
        pct(cx+50,HY+40,"100 %")
    else:
        flag(cx-92,HY-30,"de"); flag(cx-92+27,HY-30,"es")
        text(cx-92+58,HY-18,"EUROPE",11.5,700,ACC,anchor="start",ls=1.2)
        text(cx-92,HY-2,"Détention directe",11.5,500,MUTED,anchor="start")
        line([(cx,BUS2),(cx,HY-40),(sx,HY-40),(sx,y_last)],arrow=False)
        pct(cx+50,HY+18,"100 %")
    for ri,(l,proj,fl) in enumerate(subs[i]):
        cy=y_first+ri*52
        if len(subs[i])>1 or not regions[i]: line([(sx,cy),(cx-92,cy)])
        else: line([(cx,HY+26),(cx,cy-21)])
        box(cx,cy,184,42,l,(C_PROJ if proj else C_OPS),size=13.5,dash=proj,fl=fl)

# ---------- Légende ----------
LX,LY=1275,660
text(LX,LY-14,"LÉGENDE",11.5,700,ACC,anchor="start",ls=1.2)
items=[(C_PERSON,"Fondateur",False),(C_HOLD,"Holding personnelle",False),(C_TOP,"Holding de tête",False),(C_OFFICE,"Structure animatrice",False),
       (C_DEV,"Holding de développement",False),(C_REG,"Holding régionale",False),(C_OPS,"Société d'exploitation",False),(C_PROJ,"Société en cours de création",True)]
for k,(col,lab,dash) in enumerate(items):
    x=LX+(k%2)*205; y=LY+(k//2)*28
    rect(x,y,26,18,col[0],col[1],1.2,dash=dash,rx=4); text(x+36,y+14,lab,12.5,500,MUTED,anchor="start")
text(LX,LY+124,"Pourcentages : quote-part de détention du capital",12,500,MUTED,anchor="start")

svg='<svg viewBox="0 0 1700 812" width="1700" height="812" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'+"".join(out)+'</svg>'
open("orgchart.svg","w",encoding="utf-8").write(svg)
print("svg ok",len(svg))
