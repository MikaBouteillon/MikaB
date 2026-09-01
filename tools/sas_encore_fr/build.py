# -*- coding: utf-8 -*-
import pymupdf, sys
from engine import strip_text, render
from content import PAGES

SRC = '/root/.claude/uploads/9136c525-50b7-55c8-a2b8-c05db2453e93/5e7a54ed-SAS_ENCORE_2026_EN2_1.pdf'
OUT = sys.argv[1] if len(sys.argv) > 1 else 'SAS_ENCORE_2026_FR.pdf'

doc = pymupdf.open(SRC)
for i, page in enumerate(doc):
    strip_text(page)
    for blk in PAGES[i]:
        render(page, blk)

doc.set_metadata({'title': 'SAS ENCORE', 'author': '', 'subject': '',
                  'keywords': '', 'creator': '', 'producer': ''})
doc.save(OUT, garbage=4, deflate=True)
print('written', OUT)
