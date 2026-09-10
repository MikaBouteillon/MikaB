# Organigramme du Groupe — SVG généré (viewBox 1700 x 820)
NAVY="#101F3A"; ACC="#D9522B"; LINE="#AEB6C2"; MUTED="#6B7683"; BORDER="#CFD5DE"
C_PERSON=("#FFF4D6","#E2B54B"); C_HOLD=("#E4F3E7","#6DB97E"); C_TOP=(ACC,ACC); C_OFFICE=("#FBEAB4","#D9A400")
C_DEV=("#FDE4D3","#E07A30"); C_REG=("#F1E4F6","#B07CC6"); C_OPS=("#E6EFFA","#9FBBDF"); C_PROJ=("#FFFFFF","#7FA3D0")

out=[]
def rect(x,y,w,h,fill,stroke,sw=1.5,dash=None,rx=6):
    d=' stroke-dasharray="7 5"' if dash else ''
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
def text(x,y,s,size=14,weight=500,fill=NAVY,anchor="middle",ls=0):
    out.append(f'<text x="{x}" y="{y}" font-family="Inter, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{s}</text>')
def box(cx,cy,w,h,lines,col,sw=1.3,size=14,weight=500,color=NAVY,dash=None,sub=None):
    rect(cx-w/2,cy-h/2,w,h,col[0],col[1],sw,dash)
    n=len(lines); lh=size*1.25
    total=n*lh+(14 if sub else 0)
    y0=cy-total/2+size*0.85
    for i,l in enumerate(lines): text(cx,y0+i*lh,l,size,weight,color)
    if sub: text(cx,y0+n*lh+2,sub,11.5,500,("rgba(255,255,255,.8)" if color=="#fff" else MUTED))
def line(pts,arrow=True):
    d=" ".join(("M" if i==0 else "L")+f"{x},{y}" for i,(x,y) in enumerate(pts))
    m=' marker-end="url(#ah)"' if arrow else ''
    out.append(f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="1.6"{m}/>')
def pct(x,y,s,size=13):
    w=len(s)*7.2+12
    out.append(f'<rect x="{x-w/2}" y="{y-10}" width="{w}" height="20" rx="10" fill="#fff" stroke="{BORDER}" stroke-width="1"/>')
    text(x,y+4.5,s,size,600,NAVY)

out.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="'+LINE+'"/></marker></defs>')

# ---------- Fondateurs / holdings / SAS ENCORE ----------
CX=850
FX=[CX-440,CX,CX+440]
founders=[["Mikaël Bouteillon"],["Thibault d'Ayguesvives"],["Thibault Poncet"]]
holdings=[(["EURL TLK Holding"],"880 274 006 (FR)"),(["EURL DDT Holding"],"904 091 071 (FR)"),(["SARL Poncet Holding"],"799 344 353 (FR)")]
for i,x in enumerate(FX):
    box(x,24,230,48,founders[i],C_PERSON,sw=1.3,size=15,weight=600)
    line([(x,48),(x,78)]); pct(x+46,63,"100 %")
    box(x,106,230,60,holdings[i][0],C_HOLD,size=15,weight=600,sub=holdings[i][1])
SEY=222
box(CX,SEY,380,68,["SAS ENCORE"],C_TOP,size=19,weight=700,color="#fff",sub="988 864 278 (FR)")
line([(FX[0],136),(FX[0],164),(CX-120,164),(CX-120,188)]); pct(FX[0],178,"51 %")
line([(CX,136),(CX,188)]); pct(CX+46,162,"39 %")
line([(FX[2],136),(FX[2],164),(CX+120,164),(CX+120,188)]); pct(FX[2],178,"10 %")

# ---------- Bus principal ----------
BUS1=282
OFX=125; FRX=435; DEVX=1190
line([(CX,256),(CX,BUS1)],arrow=False)
line([(OFX,BUS1),(DEVX,BUS1)],arrow=False)
# ENCORE OFFICE
line([(OFX,BUS1),(OFX,314)]); pct(OFX+46,298,"100 %")
box(OFX,340,210,52,["ENCORE OFFICE"],C_OFFICE,sw=1.3,size=14.5,weight=700)
text(OFX,386,"Structure animatrice",11.5,500,MUTED); text(OFX,401,"et fonctions de siège",11.5,500,MUTED)
# FRANCE
FY0=314
line([(FRX,BUS1),(FRX,FY0)]); pct(FRX+46,298,"100 %")
rect(250,FY0,370,436,"#fff",BORDER,1.2,rx=8)
text(FRX,FY0+30,"SOCIÉTÉS D'EXPLOITATION FRANCE",12.5,700,ACC,ls=1.2)
fr_col1=[["Prison Island","Montpellier"],["Prison Island","Toulouse"],["Prison Island","Clermont Ferrand"],["Prison Island","Avignon"],["Prison Island","Orleans"],["Prison Island","Aubagne"],["Mini Mundo","Aubagne"]]
fr_col2=[["Alcatraz Adventure"],["Prison Island","Marseille"],["Prison Island","Saint Avertin"],["Prison Island","Valence"],["Expedition","Marseille"],["Prison Island","Paris 19"]]
for ci,col in enumerate([fr_col1,fr_col2]):
    for ri,l in enumerate(col):
        box([340,530][ci],FY0+72+ri*54,170,40,l,C_OPS,size=13.5)

# ---------- OUT 4 BLOOD DEVELOPPEMENT ----------
DEVY=340
line([(DEVX,BUS1),(DEVX,DEVY-34)]); pct(DEVX+46,298,"100 %")
box(DEVX,DEVY,360,68,["OUT 4 BLOOD DEVELOPPEMENT"],C_DEV,sw=1.6,size=15.5,weight=700)
COLS=[770,980,1190,1400,1610]; BW=170
BUS2=404; HY=448
line([(DEVX,DEVY+34),(DEVX,BUS2)],arrow=False); pct(DEVX+46,389,"100 %")
line([(COLS[0],BUS2),(COLS[-1],BUS2)],arrow=False)
regions=[None,["OUT 4 AUSTRALIA","PTY LTD"],["OUT 4 USA"],["OUT 4 UNITED","KINGDOM LIMITED"],["OUT 4 MEXICO"]]
subs=[
 [(["Prison Island","Berlin"],False),(["Prison Island","Stuttgart"],False),(["Prison Island","Frankfurt"],True),(["Prison Island","Barcelona"],True)],
 [(["Prison Island","Melbourne"],False),(["Prison Island","Brisbane"],False),(["Prison Island Perth"],False),(["Prison Gold Coast"],False),(["Speed Planet Brisbane"],False),(["Mini Mundo Melbourne"],False)],
 [(["PI Indianapolis"],False),(["PI Dallas"],False),(["PI New York"],False),(["PI Orlando"],False)],
 [(["Prison Island","London"],False),(["Prison Island","London 2"],False)],
 [(["Prison Island Mexico"],False)],
]
PITCH=52
for i,cx in enumerate(COLS):
    sx=cx-BW/2-18
    y_first=HY+26+34+20
    y_last=y_first+(len(subs[i])-1)*PITCH
    if regions[i]:
        line([(cx,BUS2),(cx,HY-26)])
        box(cx,HY,BW,52,regions[i],C_REG,sw=1.3,size=13.5,weight=700)
        if len(subs[i])>1:
            line([(cx,HY+26),(cx,HY+42),(sx,HY+42),(sx,y_last)],arrow=False)
            pct((cx+sx)/2,HY+42,"100 %")
        else:
            line([(cx,HY+26),(cx,y_first-20)]); pct(cx+46,HY+40,"100 %")
    else:
        text(cx-BW/2,HY-14,"EUROPE",11.5,700,ACC,anchor="start",ls=1.2)
        text(cx-BW/2,HY+2,"Détention directe",11.5,500,MUTED,anchor="start")
        line([(cx,BUS2),(cx,HY+42),(sx,HY+42),(sx,y_last)],arrow=False)
        pct((cx+sx)/2,HY+42,"100 %")
    for ri,(l,proj) in enumerate(subs[i]):
        cy=y_first+ri*PITCH
        if len(subs[i])>1 or not regions[i]: line([(sx,cy),(cx-BW/2,cy)],arrow=False)
        box(cx,cy,BW,40,l,(C_PROJ if proj else C_OPS),size=13.5,dash=proj)

# ---------- Légende (sous ENCORE OFFICE, hors du schéma) ----------
LX,LY=22,470
text(LX,LY-14,"LÉGENDE",11.5,700,ACC,anchor="start",ls=1.2)
items=[(C_PERSON,"Fondateur",False),(C_HOLD,"Holding personnelle",False),(C_TOP,"Holding de tête",False),(C_OFFICE,"Structure animatrice",False),
       (C_DEV,"Holding de développement",False),(C_REG,"Holding régionale",False),(C_OPS,"Société d'exploitation",False),(C_PROJ,"Société en cours de création",True)]
for k,(col,lab,dash) in enumerate(items):
    y=LY+k*28
    rect(LX,y,26,18,col[0],col[1],1.2,dash=dash,rx=4); text(LX+36,y+14,lab,12.5,500,MUTED,anchor="start")
text(LX,LY+8*28+10,"Pourcentages : quote-part",12,500,MUTED,anchor="start")
text(LX,LY+8*28+27,"de détention du capital",12,500,MUTED,anchor="start")

svg='<svg viewBox="0 0 1700 820" width="1700" height="820" xmlns="http://www.w3.org/2000/svg">'+"".join(out)+'</svg>'
open("orgchart.svg","w",encoding="utf-8").write(svg)
print("svg ok",len(svg))
