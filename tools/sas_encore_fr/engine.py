# -*- coding: utf-8 -*-
"""Moteur de remplacement de texte dans le PDF SAS ENCORE."""
import pymupdf

FONTFILE = {
    'b':  'fonts/DMSans-700-normal.ttf',
    'm':  'fonts/DMSans-500-normal.ttf',
    'r':  'fonts/DMSans-400-normal.ttf',
    'l':  'fonts/DMSans-300-normal.ttf',
    'i':  'fonts/DMSans-400-italic.ttf',
    'li': 'fonts/DMSans-300-italic.ttf',
}
FONTNAME = {k: 'dm' + k for k in FONTFILE}
FONT = {k: pymupdf.Font(fontfile=v) for k, v in FONTFILE.items()}

GAP = '\x00gap:'


def rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def chunk_width(text, style, size, ls):
    if text.startswith(GAP):
        return float(text[len(GAP):])
    return FONT[style].text_length(text, fontsize=size) + ls * len(text)


def draw_chunk(page, x, y, text, style, size, color, ls):
    if text.startswith(GAP):
        return x + float(text[len(GAP):])
    kw = dict(fontsize=size, fontname=FONTNAME[style], fontfile=FONTFILE[style],
              color=rgb(color))
    if ls == 0:
        page.insert_text((x, y), text, **kw)
        return x + FONT[style].text_length(text, fontsize=size)
    for ch in text:
        page.insert_text((x, y), ch, **kw)
        x += FONT[style].text_length(ch, fontsize=size) + ls
    return x


def build_words(runs, base_size):
    """runs -> liste de mots ; un mot = [(texte, style, couleur, taille), ...]"""
    words, cur, pending = [], [], 0
    for run in runs:
        text, style, color = run[0], run[1], run[2]
        size = run[3] if len(run) > 3 and run[3] else base_size
        if text.startswith(GAP):
            cur.append((text, style, color, size))
            continue
        parts = text.split(' ')
        for k, part in enumerate(parts):
            if k > 0:
                pending += 1
            if part == '':
                continue
            if pending:
                if cur:
                    words.append(cur)
                cur = []
                # les espaces multiples de la maquette d'origine sont conservés
                extra = pending - 1
                if extra:
                    sw = FONT[style].text_length(' ', fontsize=size) * extra
                    cur.append((GAP + repr(sw), style, color, size))
                pending = 0
            cur.append((part, style, color, size))
    if cur:
        words.append(cur)
    return words


def wrap(words, maxw, ls, scale=1.0):
    lines, cur, curw = [], [], 0.0
    for w in words:
        ww = sum(chunk_width(t, s, sz * scale, ls * scale) for t, s, c, sz in w)
        sp = FONT[w[0][1]].text_length(' ', fontsize=w[0][3] * scale) + ls * scale
        add = ww if not cur else ww + sp
        if cur and curw + add > maxw + 0.6:
            lines.append(cur)
            cur, curw = [w], ww
        else:
            cur.append(w)
            curw += add
    if cur:
        lines.append(cur)
    return lines


def render(page, blk):
    x = blk['x']
    y = blk['y']
    size = blk['size']
    maxw = blk.get('w', 2000)
    align = blk.get('align', 'l')
    lh = blk.get('lh', size * 1.35)
    maxlines = blk.get('maxlines')
    color = blk.get('color', '#ffffff')
    style = blk.get('style', 'l')
    runs = blk.get('runs') or [(blk['text'], style, color)]
    ls = blk.get('ls', 0.0)
    if 'ls_em' in blk:
        ls = blk['ls_em'] * size
    if 'ls_ref' in blk:
        ref, tgt = blk['ls_ref']
        ls = (tgt - FONT[runs[0][1]].text_length(ref, fontsize=size)) / max(1, len(ref) - 1)

    words = build_words(runs, size)
    scale = 1.0
    lines = wrap(words, maxw, ls, scale)
    if maxlines:
        while len(lines) > maxlines and scale > 0.78:
            scale -= 0.02
            lines = wrap(words, maxw, ls, scale)

    n = len(lines)
    ymax = blk.get('ymax')
    y0 = y
    if ymax is not None:
        y0 = min(y, ymax - (n - 1) * lh)

    for i, line in enumerate(lines):
        chunks = []
        for j, w in enumerate(line):
            if j > 0:
                st = line[j - 1][-1][1]
                sz = line[j - 1][-1][3] * scale
                chunks.append((' ', st, line[j - 1][-1][2], sz))
            for t, s, c, sz in w:
                chunks.append((t, s, c, sz * scale))
        total = sum(chunk_width(t, s, sz, ls * scale) for t, s, c, sz in chunks)
        if align == 'r':
            cx = x + maxw - total
        elif align == 'c':
            cx = x + (maxw - total) / 2
        else:
            cx = x
        cy = y0 + i * lh
        for t, s, c, sz in chunks:
            cx = draw_chunk(page, cx, cy, t, s, sz, c, ls * scale)


def strip_text(page):
    for b in page.get_text('dict')['blocks']:
        if b['type'] != 0:
            continue
        for l in b['lines']:
            for s in l['spans']:
                r = pymupdf.Rect(s['bbox'])
                r.y0 -= 1.5
                r.y1 += 1.5
                r.x0 -= 1.0
                r.x1 += 1.5
                page.add_redact_annot(r)
    page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                          graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                          text=pymupdf.PDF_REDACT_TEXT_REMOVE)
