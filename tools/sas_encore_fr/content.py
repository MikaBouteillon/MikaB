# -*- coding: utf-8 -*-
"""Contenu français du deck SAS ENCORE (blocs positionnés sur la maquette d'origine)."""

W, LIME, OR = '#ffffff', '#c9ff55', '#eb5e28'
P1, P2, P3 = '#b9cbdd', '#d6e2ef', '#c0d0e2'
MUT, MUT2, MUT3 = '#9cb0c6', '#8fa5bc', '#7a8fa6'
CAP, FOOT, LIGHT, QUOTE = '#5b738d', '#4a6079', '#c7d6e6', '#e4edf6'

EYE = dict(y=53.25, x=57.0, size=9.75, style='b', color=LIME, ls=1.8)
H1LS = -0.035


def footer(num):
    return [
        dict(x=57.0, y=511.5, size=9.0, style='m', color=FOOT, ls=1.438,
             text='SAS ENCORE — MAKE IT NOW GROUP'),
        dict(x=800.0, y=511.5, w=101.8, align='r', size=9.0, style='m',
             color=FOOT, ls=1.438, text=num),
    ]


def eyebrow(t):
    d = dict(EYE)
    d['text'] = t
    return d


PAGES = []

# ---------------------------------------------------------------- page 1
PAGES.append([
    dict(x=57.0, y=182.25, size=72.0, style='b', color=W, ls_em=-0.0407,
         text='SAS ENCORE', w=846, maxlines=1),
    dict(x=57.0, y=218.25, size=15.0, style='m', color=OR, ls=4.231,
         text='MAKE IT NOW GROUP  ·  DEPUIS 2014'),
    dict(x=57.0, y=270.0, size=25.5, style='b', color=W, ls_em=H1LS,
         w=500, maxlines=1, text='Des mètres carrés vides.'),
    dict(x=57.0, y=300.75, size=25.5, style='b', color=LIME, ls_em=H1LS,
         w=500, maxlines=1, text='Des lieux qui font le plein.'),
    dict(x=57.0, y=333.75, size=13.5, style='l', color=P1, lh=19.5, w=470,
         maxlines=3,
         text='Entre les deux : un concept, un chantier et une équipe. '
              'Nous faisons les trois nous-mêmes, avec nos propres capitaux.'),
    # statistiques
    dict(x=57.0, y=419.25, size=30.0, style='b', color=LIME, ls_em=-0.038, text='40+'),
    dict(x=57.0, y=437.25, size=9.0, style='r', color=MUT, ls=0.538, text='SITES'),
    dict(x=150.75, y=419.25, size=30.0, style='b', color=LIME, ls_em=-0.038, text='14'),
    dict(x=150.75, y=437.25, size=9.0, style='r', color=MUT, ls=0.538, text='PAYS'),
    dict(x=245.25, y=419.25, size=30.0, style='b', color=LIME, ls_em=-0.038, text='500+'),
    dict(x=245.25, y=437.25, size=9.0, style='r', color=MUT, ls=0.538, text='PERSONNES'),
    dict(x=357.75, y=419.25, size=30.0, style='b', color=LIME, ls_em=-0.038, text='40 M€'),
    dict(x=357.75, y=437.25, size=9.0, style='r', color=MUT, ls=0.538,
         text='CHIFFRE D’AFFAIRES 2026'),
    dict(x=600.0, y=474.75, w=303.0, align='r', size=10.5, style='r', color=MUT,
         text='Mikaël Bouteillon  ·  Thibaut Poncet  ·  Thibault d’Ayguesvives'),
    dict(x=800.0, y=494.25, w=101.3, align='r', size=10.5, style='r', color=FOOT,
         ls=2.0, text='2026'),
])

# ---------------------------------------------------------------- page 2
PAGES.append([
    eyebrow('QUI NOUS SOMMES'),
    dict(x=57.0, y=103.5, size=42.0, style='b', color=W, ls_em=H1LS, w=846,
         maxlines=1, text='Trois fondateurs.'),
    dict(x=57.0, y=145.5, size=42.0, ls_em=H1LS, w=846, maxlines=1,
         runs=[('Une ', 'b', W), ('machine opérationnelle', 'b', OR), ('.', 'b', W)]),
    dict(x=57.0, y=389.25, size=9.38, style='i', color=CAP,
         text='Mikaël, Thibaut & Thibault — associés fondateurs'),
    dict(x=378.0, y=195.0, size=14.62, lh=22.5, w=525, maxlines=5, ymax=283.0,
         runs=[('Un groupe détenu par ses fondateurs qui ', 'l', P2),
               ('lance, construit et exploite', 'b', W),
               (' des activités à forte valeur en France et à l’international — '
                'loisirs, sport, événementiel, hôtellerie, immobilier et sourcing. '
                'Nous ne franchisons pas notre croissance : nous détenons les concepts, '
                'la construction et les opérations.', 'l', P2)]),
] + [
    dict(x=x, y=y, size=25.5, style='b', color=OR, ls_em=-0.032, text=n)
    for (x, y, n) in [(390.75, 328.5, '40+'), (568.99, 328.5, '14'), (747.25, 328.5, '40+'),
                      (390.75, 412.5, '500+'), (568.99, 412.5, '12'), (747.25, 412.5, '40 M€')]
] + [
    dict(x=x, y=y, size=9.0, style='r', color=MUT, w=155, maxlines=1, text=t)
    for (x, y, t) in [(390.75, 347.25, 'Sites'), (568.99, 347.25, 'Pays · 4 continents'),
                      (747.25, 347.25, 'Sociétés du groupe'), (390.75, 431.25, 'Collaborateurs'),
                      (568.99, 431.25, 'Métiers'), (747.25, 431.25, 'Chiffre d’affaires 2026')]
] + [
    dict(x=393.75, y=479.25, size=12.38, style='m', color=W, w=500, maxlines=1,
         text='Diversifier les activités. Perfectionner l’exécution.'),
    dict(x=393.75, y=497.25, size=12.38, style='l', color=MUT, w=500, maxlines=1,
         text='C’est toute la stratégie.'),
] + footer('02'))

# ---------------------------------------------------------------- page 3
TL1 = [
    (57.0, '2010', 'Découverte du CrossFit aux États-Unis — le déclic.'),
    (226.2, '2014', 'Ouverture de CrossFit Nîmes ; première diversification dans la restauration.'),
    (395.39, '2016', 'Naissance de The Affiliates Battle — aujourd’hui un rendez-vous majeur du calendrier CrossFit.'),
    (564.6, '2019', 'Prison Island Montpellier : le cœur de métier du groupe démarre.'),
    (733.79, '2020–21', 'Trois ouvertures malgré le COVID. Thibault d’Ayguesvives devient troisième associé.'),
]
TL2 = [
    (57.0, '2023', 'Trois nouveaux Prison Island. Partenariat avec Decathlon.'),
    (268.5, '2024', 'Partenariat Fever. Ouverture de Bushido Academy et d’Alcatraz Adventure.'),
    (480.0, '2025', 'Déploiement international : Berlin, Londres, Brisbane, Melbourne, Braga.'),
    (691.5, '2026', '40+ sites dans 14 pays. Nouveaux concepts : Speed Planet, Minimundo.'),
]
p3 = [
    eyebrow('NOTRE PARCOURS'),
    dict(x=57.0, y=103.5, size=42.0, style='b', color=W, ls_em=H1LS, w=846,
         maxlines=1, text='Nous avons appris sur un site.'),
    dict(x=57.0, y=145.5, size=42.0, ls_em=H1LS, w=846, maxlines=1,
         runs=[('Nous l’avons répété ', 'b', W), ('40+ fois', 'b', LIME), ('.', 'b', W)]),
]
for x, yr, tx in TL1:
    p3.append(dict(x=x, y=218.25, size=15.0, style='b', color=OR, ls_em=-0.027, text=yr))
    p3.append(dict(x=x, y=237.75, size=9.75, style='l', color=P3, lh=13.9,
                   w=155 if x < 700 else 169, maxlines=4, text=tx))
for x, yr, tx in TL2:
    p3.append(dict(x=x, y=335.25, size=15.0, style='b', color=OR, ls_em=-0.027, text=yr))
    p3.append(dict(x=x, y=354.75, size=9.75, style='l', color=P3, lh=14.25,
                   w=198 if x < 690 else 211, maxlines=5, text=tx))
p3.append(dict(x=57.0, y=467.25, size=11.25, w=846, maxlines=1,
               runs=[('Chaque ouverture finance et documente la suivante. ', 'l', MUT),
                     ('Seize ans, zéro fermeture.', 'm', W)]))
PAGES.append(p3 + footer('03'))

# ---------------------------------------------------------------- page 4
CARDS4 = [
    (69.75, 296.25, 'Centres de loisirs', 'Jeux d’action indoor & divertissement familial'),
    (355.75, 296.25, 'Clubs de sport', 'CrossFit, Hyrox, padel, arts martiaux'),
    (641.74, 296.25, 'Événements sportifs', 'Compétitions à grande échelle et formats sous licence'),
    (69.75, 461.25, 'Immobilier & aménagement', 'Nous concevons et aménageons nos propres sites'),
    (355.75, 461.25, 'Restauration', 'Une cuisine saine, dans nos sites et au-delà'),
    (641.74, 461.25, 'Import & export', 'Sourcing direct depuis la Chine pour chaque projet'),
]
p4 = [
    eyebrow('CE QUE NOUS FAISONS'),
    dict(x=57.0, y=103.5, size=42.0, style='b', color=W, ls_em=H1LS, w=846,
         maxlines=1, text='Six métiers.'),
    dict(x=57.0, y=145.5, size=42.0, ls_em=H1LS, w=846, maxlines=1,
         runs=[('Une ', 'b', W), ('méthode', 'b', OR), ('.', 'b', W)]),
]
for x, y, t, s in CARDS4:
    p4.append(dict(x=x, y=y, size=12.75, style='b', color=W, ls_em=-0.029,
                   w=248, maxlines=1, text=t))
    p4.append(dict(x=x, y=y + 16.5, size=9.38, style='l', color=MUT,
                   w=250, maxlines=1, text=s))
PAGES.append(p4 + footer('04'))

# ---------------------------------------------------------------- page 5
CARDS5 = [
    (67.5, 213.75, 'CrossFit Nîmes', 'Box emblématique · France'),
    (352.75, 213.75, 'Hyrox Nîmes', 'Centre d’entraînement officiel'),
    (637.99, 213.75, 'Padel Performance Center', 'Padel extérieur haut de gamme'),
    (67.5, 335.25, 'Bushido Academy', 'Club de MMA & sports de combat'),
    (352.75, 335.25, 'The Affiliates Battle', 'Compétition CrossFit majeure'),
    (637.99, 335.25, 'Pure Taste', 'Bar à salades & cuisine saine'),
    (67.5, 456.75, 'Back From Holidays Contest', 'Compétition CrossFit amateur'),
    (352.75, 456.75, 'Alcatraz Adventure', 'Complexe de loisirs indoor'),
    (637.99, 456.75, 'Expedition Marseille', 'Jeu d’action indoor coopératif'),
]
p5 = [
    eyebrow('PORTFOLIO'),
    dict(x=57.0, y=103.5, size=42.0, ls_em=H1LS, w=545, maxlines=1,
         runs=[('Des preuves, pas des ', 'b', W), ('promesses', 'b', LIME), ('.', 'b', W)]),
    dict(x=610.0, y=85.5, w=293.0, align='r', size=10.5, lh=15.75, maxlines=3,
         ymax=101.25,
         runs=[('Prison Island', 'b', W),
               (' est notre marque phare — un jeu d’action indoor coopératif '
                'désormais présent dans ', 'l', MUT),
               ('14 pays', 'b', OR), ('.', 'l', MUT)]),
]
for x, y, t, s in CARDS5:
    p5.append(dict(x=x, y=y, size=10.5, style='b', color=W, w=252, maxlines=1, text=t))
    p5.append(dict(x=x, y=y + 12.75, size=8.62, style='l', color=MUT, w=252,
                   maxlines=1, text=s))
PAGES.append(p5 + footer('05'))

# ---------------------------------------------------------------- page 6
REG = [
    (72.75, 346.5, 'EUROPE', '25', [
        ('France', '13', 'Nîmes · Montpellier · Marseille · Marguerittes · Avignon · Grenoble · '
                         'Clermont-Ferrand · Orléans · Tours · Toulouse · Valence · '
                         'Paris La Villette · Paris Bercy', 243.75, 257.25, 3),
        ('Allemagne', '5', 'Berlin · Stuttgart · Francfort · Munich · Hambourg', 306.0, 319.5, 1),
        ('Royaume-Uni', '2', 'Londres · Londres #2', 343.5, 357.0, 1),
        ('Italie', '2', 'Rome · Milan', 380.25, 393.75, 1),
        ('Pays-Bas · Espagne · Portugal', '3', 'Amsterdam · Barcelone · Braga', 417.75, 431.25, 1),
    ]),
    (389.53, 648.8, 'AMÉRIQUES', '24', [
        ('États-Unis', '21', 'New Jersey · Boston · Philadelphie · Washington DC · Charlotte · '
                             'Atlanta · Orlando · Tampa · Miami · Nashville · Columbus · Chicago · '
                             'Indianapolis · Austin · San Antonio · Denver · Portland · '
                             'San Francisco · Los Angeles · San Diego · Honolulu', 243.75, 257.25, 4),
        ('Mexique · Brésil · Chili', '3', 'Mexico · São Paulo · Santiago', 318.75, 332.25, 1),
    ]),
    (691.77, 887.2, 'ASIE-PACIFIQUE', '6', [
        ('Australie', '4', 'Perth · Brisbane · Gold Coast · Melbourne', 243.75, 257.25, 1),
        ('Japon · Singapour', '2', 'Tokyo · Singapour', 281.25, 294.75, 1),
    ]),
]
p6 = [
    eyebrow('IMPLANTATIONS'),
    dict(x=57.0, y=103.5, size=42.0, style='b', color=W, ls_em=H1LS, w=846,
         maxlines=1, text='La France comme base.'),
    dict(x=57.0, y=145.5, size=42.0, ls_em=H1LS, w=650, maxlines=1,
         runs=[('Le monde comme ', 'b', W), ('terrain de jeu', 'b', OR), ('.', 'b', W)]),
    dict(x=700.0, y=109.5, w=203.0, align='r', size=11.25, style='b', color=W,
         maxlines=1, text='14 pays · 4 continents.'),
    dict(x=700.0, y=126.0, w=203.0, align='r', size=11.25, style='l', color=MUT,
         lh=17.0, maxlines=3,
         text='Sites en exploitation, ouvertures engagées et pipeline 2027.'),
    dict(x=85.5, y=484.5, size=9.38, style='li', color=MUT3, w=700, maxlines=1,
         text='Les chiffres incluent les sites en exploitation, les ouvertures engagées '
              'et le pipeline 2027.'),
]
for xl, xr, name, num, rows in REG:
    p6.append(dict(x=xl, y=208.5, size=11.25, style='b', color=LIME, ls=0.42, text=name))
    p6.append(dict(x=xr - 120, y=208.5, w=120, align='r', size=22.5, style='b',
                   color=W, ls_em=-0.045, text=num))
    for cname, cnum, cities, y1, y2, nl in rows:
        p6.append(dict(x=xl, y=y1, size=10.12, maxlines=1, w=xr - xl,
                       runs=[(cname, 'b', W), ('\x00gap:6.0', 'b', W),
                             (cnum, 'b', OR, 9.0)]))
        p6.append(dict(x=xl, y=y2, size=8.62, style='l', color=MUT2, lh=12.6,
                       w=xr - xl, maxlines=nl + 1, text=cities))
PAGES.append(p6 + footer('06'))

# ---------------------------------------------------------------- page 7
CARDS7 = [
    (72.75, 'Speed Planet',
     'Parc de toboggans indoor géant, conçu pour la vitesse et les sensations — '
     'ouvert toute l’année, pensé pour les familles et les groupes.'),
    (358.75, 'Minimundo',
     'Ville de jeux de rôle indoor à l’échelle des enfants : des zones thématiques '
     'et immersives qui récompensent la curiosité et l’imagination.'),
    (644.74, 'W Campus',
     'Plateforme de formation en ligne pour nos managers et nos équipes, bientôt '
     'installée dans un campus physique dédié de 200 m².'),
]
p7 = [
    eyebrow('PIPELINE 2026'),
    dict(x=57.0, y=103.5, size=42.0, ls_em=H1LS, w=846, maxlines=1,
         runs=[('Ce que nous ', 'b', W), ('construisons ensuite', 'b', OR), ('.', 'b', W)]),
    dict(x=74.25, y=448.5, size=9.75, style='b', color=LIME, ls=1.8,
         text='PROCHAINES VILLES'),
    dict(x=232.0, y=449.25, size=11.62, style='m', color=QUOTE, w=655, maxlines=1,
         text='Gold Coast  ·  Indianapolis  ·  Paris  ·  et d’autres Prison Island '
              'en Europe, en Australie et aux États-Unis'),
]
for x, t, s in CARDS7:
    p7.append(dict(x=x, y=341.25, size=15.75, style='b', color=W, ls_em=-0.015,
                   w=246, maxlines=1, text=t))
    p7.append(dict(x=x, y=363.0, size=10.12, style='l', color=MUT, lh=15.0,
                   w=246, maxlines=4, text=s))
PAGES.append(p7 + footer('07'))

# ---------------------------------------------------------------- page 8
CARDS8 = [
    (75.75, 'Tout en interne',
     'Un siège dans le Sud de la France et plus de 500 collaborateurs dans le groupe. '
     'Design, construction, marketing, finance et opérations sont internes — '
     'la qualité n’est jamais sous-traitée.'),
    (361.75, 'Maîtrise de la chaîne',
     'Nous sourçons et importons nos équipements et structures directement depuis la '
     'Chine, avec des accords exclusifs avec les fabricants. D’où notre maîtrise des '
     'coûts, des délais et de la qualité sur chaque site.'),
    (647.74, 'La vitesse comme stratégie',
     'Nous testons, ajustons et avançons vite sur le terrain plutôt que d’attendre le '
     'moment parfait — avec la discipline qui garde les sites bien tenus et les '
     'engagements tenus.'),
]
p8 = [
    eyebrow('LE MODÈLE'),
    dict(x=57.0, y=103.5, size=42.0, ls_em=H1LS, w=846, maxlines=1,
         runs=[('Opérateur, pas ', 'b', W), ('intermédiaire', 'b', LIME), ('.', 'b', W)]),
    dict(x=71.25, y=336.0, size=28.5, style='b', color=OR, ls_em=-0.030, text='40+'),
    dict(x=71.25, y=354.0, size=8.62, style='r', color=MUT, text='Sociétés'),
    dict(x=214.25, y=336.0, size=28.5, style='b', color=OR, ls_em=-0.030, text='500+'),
    dict(x=214.25, y=354.0, size=8.62, style='r', color=MUT, text='Collaborateurs'),
    dict(x=57.0, y=466.5, size=10.88, lh=13.5, w=846, maxlines=2,
         runs=[('Concept, construction, ouverture et exploitation — ', 'l', MUT),
               ('une même équipe porte un site de bout en bout.', 'm', W),
               (' C’est ainsi que nous ouvrons vite, tenons nos marges et gardons '
                'le même standard à Nîmes, Berlin ou Brisbane.', 'l', MUT)]),
]
for x, t, s in CARDS8:
    p8.append(dict(x=x, y=183.0, size=17.25, style='b', color=W, ls_em=-0.035,
                   w=242, maxlines=1, text=t))
    p8.append(dict(x=x, y=207.0, size=10.5, style='l', color=MUT, lh=16.5,
                   w=242, maxlines=5, text=s))
PAGES.append(p8 + footer('08'))

# ---------------------------------------------------------------- page 9
PAGES.append([
    eyebrow('PARTENAIRES & FINANCEMENT'),
    dict(x=57.0, y=103.5, size=42.0, style='b', color=W, ls_em=H1LS, w=846,
         maxlines=1, text='Soutenus par ceux'),
    dict(x=57.0, y=145.5, size=42.0, ls_em=H1LS, w=846, maxlines=1,
         runs=[('qui ', 'b', W), ('construisent', 'b', OR), ('.', 'b', W)]),
    dict(x=57.0, y=180.75, size=12.75, style='l', color=MUT, lh=19.5, w=620,
         maxlines=2,
         text='Banques, institutions et opérateurs qui ont financé, ouvert et développé '
              'des sites avec nous — de notre première box à Nîmes à nos premiers '
              'établissements à l’étranger.'),
    dict(x=57.0, y=441.75, w=846, align='c', size=16.5, style='li', color=QUOTE,
         maxlines=1,
         text='« Nous ne finançons pas une idée. Nous ouvrons un site, '
              'nous l’exploitons, et nous regardons les chiffres. »'),
    dict(x=57.0, y=468.0, w=846, align='c', size=9.0, style='b', color=OR,
         ls_ref=('MIKAËL BOUTEILLON — PRESIDENT', 201.3),
         text='MIKAËL BOUTEILLON — PRÉSIDENT'),
] + footer('09'))

# ---------------------------------------------------------------- page 10
PAGES.append([
    dict(x=57.0, y=193.5, size=48.0, style='b', color=W, ls_em=-0.040, w=846,
         maxlines=1, text='Construisons le'),
    dict(x=57.0, y=240.75, size=48.0, style='b', color=W, ls_em=-0.040, w=846,
         maxlines=1, text='prochain ensemble.'),
    dict(x=57.0, y=290.25, size=9.0, style='b', color=LIME,
         ls_ref=('CONTACT', 54.4), text='CONTACT'),
    dict(x=57.0, y=318.0, size=15.75, style='b', color=W, ls_em=-0.015,
         text='Mikaël Bouteillon'),
    dict(x=57.0, y=335.25, size=9.75, style='b', color=OR,
         ls_ref=('PRESIDENT', 61.9), text='PRÉSIDENT'),
    dict(x=57.0, y=360.0, size=12.0, style='l', color=LIGHT, text='+33 6 47 73 87 33'),
    dict(x=57.0, y=381.0, size=12.0, style='l', color=LIGHT, text='management@makeitnow.live'),
    dict(x=57.0, y=402.0, size=12.0, style='l', color=LIGHT, text='makeitnow.live'),
    dict(x=273.0, y=290.25, size=9.0, style='b', color=LIME,
         ls_ref=('HEAD OFFICE', 76.5), text='SIÈGE SOCIAL'),
    dict(x=273.0, y=316.5, size=12.0, style='l', color=LIGHT,
         text='SAS ENCORE — Make It Now Group'),
    dict(x=273.0, y=337.5, size=12.0, style='l', color=LIGHT,
         text='105 rue Claude Nicolas Ledoux'),
    dict(x=273.0, y=358.5, size=12.0, style='l', color=LIGHT,
         text='30900 Nîmes — France'),
])
