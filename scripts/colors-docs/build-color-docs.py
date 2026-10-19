#!/usr/bin/env python3
"""Rebuild the per-site color documents from tokens/colors/mng-colors.tokens.json.

Every publication in the cluster audit (97) is listed on its own, ordered
theme -> cluster -> sub-theme -> site (Karl, 2026-10-19).

Writes:
  - tokens/colors/mng-colors-sites.csv   (rows re-ordered; cluster, resolved values, fixes per site)
  - tokens/colors/mng-colors.css         (one block per theme/sub-theme for reference + one block per site)
  - tokens/colors/mng-colors-fixes.csv   one row per fix (a checklist for engineering, with a blank `done` column)
  - design-vs-production.md  entry 9, between the BEGIN/END per-site markers
Inputs: tokens/colors/mng-colors.tokens.json, scripts/colors-docs/notes.json (hand notes per theme/sub-theme).
Run from the repo root: python3 scripts/colors-docs/build-color-docs.py
"""
import csv, io, json, re, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
J = json.load(open(os.path.join(ROOT, 'tokens/colors/mng-colors.tokens.json')))
NOTES = json.load(open(os.path.join(ROOT, 'scripts/colors-docs/notes.json')))
TH, SI = J['color']['theme'], J['site']
TOK = ['primary-lighter', 'primary-light', 'primary', 'primary-dark', 'primary-darker', 'secondary', 'tertiary',
       'near-black', 'white', 'nav-text', 'subsite-custom', 'subsite-text']
THEME_ORDER = ['Bold Coastal', 'Modern Earthy', 'Measured Vibrant']
slug = lambda n: re.sub(r'[^a-z0-9]+', '-', n.lower()).strip('-')
key_by_name = {v['$extensions']['com.mng']['name']: k for k, v in TH.items()}
REF = re.compile(r'^\{color\.theme\.([^.]+)\.([^}]+)\}$')

def theme_val(tk, name):
    """Value of a token on a theme/sub-theme, cascading to its parent theme."""
    while tk:
        if name in TH[tk]:
            return TH[tk][name]['$value'], tk
        parent = TH[tk]['$extensions']['com.mng'].get('parentTheme')
        tk = key_by_name.get(parent) if parent else None
    return None, None

def site_values(sk):
    s = SI[sk]; m = s['$extensions']['com.mng']
    src = m.get('tokenSource', '').split('.')[-1] or None
    out = {}
    for t in TOK:
        if t in s:
            v = s[t]['$value']; r = REF.match(v)
            if r:
                val, frm = theme_val(r.group(1), r.group(2)); out[t] = (val, frm)
            else:
                out[t] = (v, 'site')
        elif src:
            val, frm = theme_val(src, t)
            if val: out[t] = (val, frm)
    return out

def fixes(sk):
    m = SI[sk]['$extensions']['com.mng']; fk = (m.get('fixesFrom') or '').split('.')[-1]
    if not fk: return []
    dom = m['domain']
    return [x for x in TH[fk]['$extensions']['com.mng'].get('mismatches', []) if not x.get('sites') or dom in x['sites']]

sites = []
for sk, s in SI.items():
    if sk.startswith('$'): continue
    m = s['$extensions']['com.mng']
    sites.append({'key': sk, 'pub': m['publication'], 'dom': m['domain'], 'cluster': m.get('cluster', '').strip(),
                  'theme': m.get('theme'), 'sub': m.get('subTheme'), 'note': m.get('note'), 'm': m})
def order(x):
    t = THEME_ORDER.index(x['theme']) if x['theme'] in THEME_ORDER else 9
    return (t, x['cluster'].lower(), 0 if not x['sub'] else 1, (x['sub'] or '').lower(), x['pub'].lower())
sites.sort(key=order)
for x in sites:
    if x['m'].get('mismatchCount') is not None and len(fixes(x['key'])) != x['m']['mismatchCount']:
        raise SystemExit('fix count mismatch for %s: %d vs %d' % (x['dom'], len(fixes(x['key'])), x['m']['mismatchCount']))

# ---------- CSV ----------
p = os.path.join(ROOT, 'tokens/colors/mng-colors-sites.csv')
rows = list(csv.DictReader(io.StringIO(open(p).read()))); fields = list(rows[0].keys())
by_dom = {r['domain']: r for r in rows}
outrows = []
for x in sites:
    r = by_dom[x['dom']]; r['cluster'] = x['cluster']
    fx = fixes(x['key']); r['mismatch_count'] = str(len(fx)) if x['theme'] else r['mismatch_count']
    if x['theme']:
        r['engineering_fixes'] = '; '.join('%s: %s -> %s' % (f['token'], f['production'], f['design']) for f in fx)
        vals = site_values(x['key'])
        for t in TOK: r[t] = vals.get(t, ('', ''))[0] or ''
    outrows.append(r)
o = io.StringIO(); w = csv.DictWriter(o, fields, lineterminator='\n'); w.writeheader(); w.writerows(outrows)
open(p, 'w').write(o.getvalue())

# ---------- fixes checklist ----------
# One row per thing engineering has to change. The easy wins come first: the gray / alert fixes for each theme file
# (entry 7) and the obituaries fixes (entry 8). Then the per-site color fixes (entry 9), ordered theme > cluster >
# sub-theme > site: theme-file rows first in each theme (fix once), then each site's rows (theme-file fixes repeated so
# a site can be checked off on its own).
GRAY_ALERT = [  # design-vs-production entry 7, audited 2026-10-19; identical on all three themes
    ('--text (body)', '#000000', '#141414', 'Change body text from #000000 to gray-min #141414.'),
    ('gray-min', '#0a0908', '#141414', 'Replace hard-coded $gray-min #0a0908 with #141414.'),
    ('--site-branding-gray-100', '#38322a', '#393938', 'Change --site-branding-gray-100 to #393938 (:root).'),
    ('--site-branding-gray-200', '#5d5b5a', '#5e5d5c', 'Change --site-branding-gray-200 to #5e5d5c (:root).'),
    ('--site-branding-gray-300', '#9d9a98', '#838280', 'Change --site-branding-gray-300 to #838280 (:root).'),
    ('--site-branding-gray-400', '#aaa7a4', '#a7a6a3', 'Change --site-branding-gray-400 to #a7a6a3 (:root).'),
    ('--site-branding-gray-500', '#d7d6d2', '#cccac7', 'Change --site-branding-gray-500 to #cccac7 (:root).'),
    ('alert low-success', 'MISSING', '#2e8000', 'Add the low-success alert color #2e8000.'),
    ('alert medium', 'MISSING', '#856a00', 'Add the medium alert color #856a00.'),
    ('alert high-error', 'MISSING', '#cc2b27', 'Add the high-error alert color #cc2b27.'),
]
THEME_CSS = {'Bold Coastal': 'boldcoastal.css', 'Modern Earthy': 'modernearthy.css', 'Measured Vibrant': 'measuredvibrant.css'}
OBITS = [  # design-vs-production entry 8 (rechecked 2026-10-19); obituaries look the same on every site
    ('primary-lighter (tributes)', 'MISSING', '#f15f87', 'Add Endless Tributes primary-lighter #f15f87.'),
    ('primary-dark (tributes)', 'MISSING', '#770000', 'Add Endless Tributes primary-dark #770000 (rgb 119, 0, 0).'),
    ('primary-darker (tributes)', 'MISSING', '#4d0000', 'Add Endless Tributes primary-darker #4d0000.'),
    ('tan-light (tributes)', '#ecede7', '#e8e6e2', 'Change tan-light from #ecede7 to #e8e6e2.'),
    ('--secondary-obit', '#946c82', 'remove', 'Remove --secondary-obit (not part of the Endless Tributes palette).'),
    ('--tertiary-obit', '#227db4', 'remove', 'Remove --tertiary-obit (not part of the Endless Tributes palette).'),
    ('beige #ccc7bc (article pages)', '#ccc7bc', '#e8e6e2', 'Replace #ccc7bc with tan-light #e8e6e2 on the Send Flowers banner (.obit-tribute-wrapper), the guestbook submit button and the Upcoming events / Sign Guestbook buttons (styleArticleObit.min.css).'),
]
def where(fix):
    m = re.search(r'\(([^()]*(?:\.css|Customizer)[^()]*)\)', fix)
    return m.group(1) if m else ''
FX = ['theme', 'cluster', 'sub_theme', 'publication', 'domain', 'token', 'production_value', 'design_value',
      'where_to_fix', 'scope', 'fix', 'differences_entry', 'done']
fixrows = []
for t in ['Bold Coastal', 'Modern Earthy', 'Measured Vibrant']:
    for tok, prod, des, fix in GRAY_ALERT:
        fixrows.append([t, '(all clusters)', '', '(theme file)', '(all %s sites)' % t, tok, prod, des,
                        THEME_CSS[t], 'theme file: fix once', fix, '7', ''])
for tok, prod, des, fix in OBITS:
    fixrows.append(['Endless Tributes', '(all clusters)', '', '(obituaries)', '(every site)', tok, prod, des,
                    'obituaries widget CSS', 'platform: fix once', fix, '8', ''])
cur_theme = None
for x in sites:
    if x['theme'] != cur_theme:
        cur_theme = x['theme']
        if x['theme'] in THEME_CSS:
            tk = key_by_name[x['theme']]
            for f in TH[tk]['$extensions']['com.mng'].get('mismatches', []):
                fixrows.append([x['theme'], '(all clusters)', '', '(theme file)', '(all %s sites)' % x['theme'], '--' + f['token'],
                                f['production'], f['design'], where(f['fix']), 'theme file: fix once', f['fix'], '9', ''])
    if not x['theme']:
        continue
    tk = key_by_name[x['theme']]
    theme_tokens = {f['token'] for f in TH[tk]['$extensions']['com.mng'].get('mismatches', [])}
    src = (x['m'].get('fixesFrom') or '').split('.')[-1]
    for f in fixes(x['key']):
        shared = src == tk or (f['token'] in theme_tokens and x['theme'] in THEME_CSS and THEME_CSS[x['theme']] in f['fix'])
        scope = 'theme file (also listed above)' if shared else ('this site only' if f.get('sites') else
                ('sub-theme: ' + x['sub'] if x['sub'] else 'this site'))
        fixrows.append([x['theme'], x['cluster'], x['sub'] or '', x['pub'], x['dom'], '--' + f['token'], f['production'],
                        f['design'], where(f['fix']), scope, f['fix'], '9', ''])
o = io.StringIO(); w = csv.writer(o, lineterminator='\n'); w.writerow(FX); w.writerows(fixrows)
open(os.path.join(ROOT, 'tokens/colors/mng-colors-fixes.csv'), 'w').write(o.getvalue())

# ---------- CSS ----------
L = ['/* MNG Web Design System — color tokens (design spec values). Generated by scripts/colors-docs/build-color-docs.py',
     '   from tokens/colors/mng-colors.tokens.json; do not edit by hand. Every publication has its own block, ordered',
     '   theme > cluster > sub-theme > site. Engineering fixes: design-vs-production.md entry 9. */', '']
L.append('/* ===== Themes and sub-themes (reference: [data-mng-theme]) ===== */')
for tk, t in TH.items():
    m = t['$extensions']['com.mng']
    decl = ['  --%s: %s;' % (n, theme_val(tk, n)[0]) for n in TOK if theme_val(tk, n)[0] and (n in t or m.get('parentTheme'))]
    L.append('/* %s (%s%s) */' % (m['name'], m['level'], ', on ' + m['parentTheme'] if m.get('parentTheme') else ''))
    L.append('[data-mng-theme="%s"] {' % tk); L += decl; L.append('}'); L.append('')
L.append('/* ===== Publications, one block each (theme > cluster > sub-theme > site) ===== */')
cur = (None, None, None)
for x in sites:
    if x['theme'] != cur[0]: L.append(''); L.append('/* ==== %s ==== */' % (x['theme'] or 'Not on MNG themes'))
    if (x['theme'], x['cluster']) != cur[:2]: L.append('/* --- Cluster: %s --- */' % x['cluster'])
    if (x['theme'], x['cluster'], x['sub']) != cur and x['sub']: L.append('/* Sub-theme: %s */' % x['sub'])
    cur = (x['theme'], x['cluster'], x['sub'])
    if not x['theme']:
        L.append('/* %s (%s): %s */' % (x['pub'], x['dom'], x['note'])); continue
    vals = site_values(x['key']); fx = fixes(x['key'])
    L.append('[data-mng-site="%s"] { /* %s · %d engineering fix%s */' % (x['dom'], x['pub'], len(fx), '' if len(fx) == 1 else 'es'))
    for t in TOK:
        if t in vals:
            v, frm = vals[t]
            L.append('  --%s: %s;%s' % (t, v, ' /* site override */' if frm == 'site' else ''))
    L.append('}')
open(os.path.join(ROOT, 'tokens/colors/mng-colors.css'), 'w').write('\n'.join(L) + '\n')

# ---------- entry 9 ----------
def fix_table(fx):
    if not fx: return ['No fixes.']
    out = ['| Token | Design | Production | Fix |', '|---|---|---|---|']
    for f in fx:
        prod = '`%s`' % f['production'] + (' (%s)' % f['productionSource'] if f.get('productionSource') else '')
        out.append('| `--%s` | `%s` | %s | %s |' % (f['token'], f['design'], prod, f['fix']))
    return out
def notes_for(name, level):
    n = NOTES.get(name) or {}
    out = []
    if n.get('loads'): out += ['Loads: %s' % n['loads'], '']
    if n.get('notes'): out += [n['notes'], '']
    return out
M = ['<!-- BEGIN per-site color fixes (generated by scripts/colors-docs/build-color-docs.py; edit notes in scripts/colors-docs/notes.json) -->', '']
seen_sub = set()
cur = (None, None, None)
for x in sites:
    if x['theme'] != cur[0]:
        tname = x['theme'] or 'Not on MNG themes'
        M += ['### %s' % tname, '']
        if x['theme']:
            tk = key_by_name[x['theme']]
            M += notes_for(x['theme'], 'theme')
            M += ['**Theme-file fixes** (fix once in the theme stylesheet; they apply to every site below unless a sub-theme or site sets its own value):', '']
            M += fix_table(TH[tk]['$extensions']['com.mng'].get('mismatches', [])) + ['']
    if (x['theme'], x['cluster']) != cur[:2]:
        M += ['#### %s — %s cluster' % (x['theme'] or 'Not on MNG themes', x['cluster']), '']
    if x['sub'] and (x['theme'], x['cluster'], x['sub']) != cur:
        M += ['##### Sub-theme: %s' % x['sub'], '']
        M += notes_for(x['sub'], 'sub-theme') if x['sub'] not in seen_sub else ['Sub-theme notes: see its first cluster above.', '']
        seen_sub.add(x['sub'])
    cur = (x['theme'], x['cluster'], x['sub'])
    fx = fixes(x['key'])
    head = '**%s** (%s)' % (x['pub'], x['dom'])
    if not x['theme']:
        M += [head + ': ' + (x['note'] or ''), '']; continue
    M += [head + ' · ' + (x['sub'] and 'sub-theme %s' % x['sub'] or 'theme %s' % x['theme']) + ' · %d fix%s' % (len(fx), '' if len(fx) == 1 else 'es'), '']
    if x['m'].get('exceptions'):
        M += ['Documented exception (no fix): ' + ', '.join('`--%s` `%s`' % (e['token'], e['siteValue']) for e in x['m']['exceptions']) + '.', '']
    M += fix_table(fx) + ['']
M += ['<!-- END per-site color fixes -->']
p = os.path.join(ROOT, 'design-vs-production.md'); s = open(p).read()
a = s.index('<!-- BEGIN per-site color fixes'); b = s.index('<!-- END per-site color fixes -->') + len('<!-- END per-site color fixes -->')
s = s[:a] + '\n'.join(M) + s[b:]
# index table, same order
a = s.index('### Index: every publication'); b = s.index('\n## ', a + 1)
I = ['### Index: every publication', '', 'Ordered theme > cluster > sub-theme > site, as above.', '',
     '| Theme | Cluster | Sub-theme | Publication | Domain | Fixes |', '|---|---|---|---|---|---|']
for x in sites:
    I.append('| %s | %s | %s | %s | %s | %s |' % (x['theme'] or '—', x['cluster'], x['sub'] or '—', x['pub'], x['dom'],
                                                  len(fixes(x['key'])) if x['theme'] else '—'))
s = s[:a] + '\n'.join(I) + '\n\n---\n' + s[b:]
open(p, 'w').write(s)
print('sites:', len(sites), '| fix rows:', len(fixrows))
