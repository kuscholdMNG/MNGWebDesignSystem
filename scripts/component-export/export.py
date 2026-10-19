#!/usr/bin/env python3
"""MNG Web Design System: shared component exporter (EXPORT-STANDARD.md section 7).

Usage (from the repo top):
  python3 scripts/component-export/export.py <raw_dir> [slug ...]

Inputs
  <raw_dir>/specs-*.json      Figma dumps from extract.js (MODE 'specs'): {"fileKey", "fileName", "results": [...]}
  <raw_dir>/previews-*.json   Figma dumps from extract.js (MODE 'previews'): {"out": {nodeId: base64 PNG}}
  scripts/component-export/registry.json   which components to export, their layer and hand-checked text
  tokens/core, tokens/themes, tokens/wordpress                system tokens the component tokens reference
Outputs (one folder per component, replaced on every run)
  components/<layer>/<slug>/<slug>.md           spec: purpose, Figma links, properties, variants, anatomy, tokens,
                                                 breakpoints, accessibility, usage, production, known issues
  components/<layer>/<slug>/<slug>.tokens.json  DTCG 2025.10 component tokens that reference system tokens
  components/<layer>/<slug>/<slug>.html         HTML/CSS skeleton of every variant, using the dist/ CSS variables
  components/<layer>/<slug>/previews/*.png      variant previews @2x and the documentation frame @0.5x
  components/index.json                         every exported component
Component tokens are derived from the Figma layers: a value bound to a Figma variable becomes a reference to the
system token ({color.theme.primary}); an unbound value is written as a literal and listed under Known issues.
Values that are the same in every variant go under "base"; values that change are keyed by the variant property
that explains them (e.g. "state-hover"). Stdlib only.
"""
import base64, glob, html, json, os, re, shutil, sys
from collections import Counter, OrderedDict, defaultdict
from itertools import combinations

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
DATE = os.environ.get('EXPORT_DATE', '2026-10-14')
STANDARD = 'EXPORT-STANDARD.md'

def load(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)

def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def fmt(x):
    if isinstance(x, float):
        x = round(x, 3)
        return str(int(x)) if x == int(x) else str(x)
    return str(x)

def url(fk, nid):
    return 'https://www.figma.com/design/%s/?node-id=%s' % (fk, nid.replace(':', '-'))

# ---------- system tokens ----------
def flatten(doc, layer, out, path=()):
    for k, v in doc.items():
        if k.startswith('$') or not isinstance(v, dict):
            continue
        if '$value' in v:
            out['.'.join(path + (k,))] = (layer, v)
        else:
            flatten(v, layer, out, path + (k,))

SYSTEM = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'tokens/core/*.tokens.json'))):
    flatten(load(f), 'core', SYSTEM)
for f in sorted(glob.glob(os.path.join(ROOT, 'tokens/themes/*.tokens.json'))):
    flatten(load(f), 'themes', SYSTEM)
for f in sorted(glob.glob(os.path.join(ROOT, 'tokens/wordpress/**/*.tokens.json'), recursive=True)):
    flatten(load(f), 'wordpress', SYSTEM)
LAYER_RANK = {'core': 0, 'themes': 1, 'wordpress': 2}

def css_var(path):
    return '--mng-' + path.replace('.', '-')

def figma_ref(v):
    """Figma variable 'Collection/name/path' -> DTCG token path, or None if it has no single system token."""
    if not v or '/' not in v:
        return None
    col, name = v.split('/', 1)
    p = name.split('/')
    if col == 'Type Primitives' and p[:2] == ['font', 'style']:
        p = ['font', 'weight', p[2]]
    if col == 'Typography Theme' and p[-1] == 'eyebrow-style':
        p[-1] = 'eyebrow-weight'
    if col == 'Typeography Tokens' and p[0] == 'Shared':
        p = [slug(x) for x in p]
    path = '.'.join(p)
    return path if path in SYSTEM else None

WEIGHT = {'Thin': 100, 'ExtraLight': 200, 'Light': 300, 'Regular': 400, 'Medium': 500, 'SemiBold': 600, 'Bold': 700, 'ExtraBold': 800, 'Black': 900}

def color_value(hexs, alpha=1):
    h = hexs.lower()
    rgb = [int(h[i:i + 2], 16) for i in (1, 3, 5)]
    v = {'colorSpace': 'srgb', 'components': [round(c / 255, 4) for c in rgb], 'alpha': alpha, 'hex': h}
    return v, 'rgba(%d, %d, %d, %s)' % (rgb[0], rgb[1], rgb[2], fmt(float(alpha)))

# ---------- reading Figma layers ----------
def visible_walk(n, path, fn, root=True):
    if n.get('hidden'):
        return
    p = path + ([] if root else [slug(n['name']) or 'layer'])
    fn(n, p or ['root'])
    for c in n.get('children', []) or []:
        visible_walk(c, p, fn, False)

def props_of(n):
    """(prop, $type, value, figma variable or None) for one layer."""
    out = []
    vars_ = n.get('vars') or {}
    def paint(ps):
        if not ps or ps == 'mixed':
            return None
        p = ps[0]
        if p.get('type') != 'SOLID':
            return None
        return p
    if n['type'] == 'TEXT':
        st = n['styles'][0]
        sv = st.get('vars') or vars_
        c = paint(st.get('color'))
        if c:
            out.append(('color', 'color', (c['hex'], c.get('opacity', 1)), c.get('variable')))
        out.append(('font-family', 'fontFamily', st['font'], sv.get('fontFamily')))
        out.append(('font-size', 'dimension', st['size'], sv.get('fontSize')))
        out.append(('font-weight', 'fontWeight', WEIGHT.get(st['style'].replace(' Italic', '').replace('Italic', 'Regular'), 400), sv.get('fontStyle') or sv.get('fontWeight')))
        if st['lineHeight'] != 'auto':
            out.append(('line-height', 'dimension', float(st['lineHeight'].rstrip('px%')), sv.get('lineHeight')))
        ls = float(st['letterSpacing'].rstrip('px%'))
        if ls:
            out.append(('letter-spacing', 'dimension', ls, sv.get('letterSpacing')))
        return out
    if n['type'] == 'INSTANCE':
        out.append(('width', 'dimension', n['w'], vars_.get('width')))
        out.append(('height', 'dimension', n['h'], vars_.get('height')))
        c = paint(n.get('iconFill'))
        if c:
            out.append(('icon-color', 'color', (c['hex'], c.get('opacity', 1)), c.get('variable')))
        return out
    f = paint(n.get('fills'))
    if f:
        out.append(('background', 'color', (f['hex'], f.get('opacity', 1)), f.get('variable')))
    s = paint(n.get('strokes'))
    if s:
        out.append(('border-color', 'color', (s['hex'], s.get('opacity', 1)), s.get('variable')))
        w = n.get('strokeWeight')
        if isinstance(w, list):
            for side, ww in zip(('top', 'right', 'bottom', 'left'), w):
                if ww:
                    out.append(('border-%s-width' % side, 'dimension', ww, None))
        else:
            out.append(('border-width', 'dimension', w, vars_.get('strokeWeight')))
        out.append(('border-style', 'strokeStyle', 'dashed' if n.get('dash') else 'solid', None))
    r = n.get('radius')
    if r is not None and not isinstance(r, list):
        out.append(('border-radius', 'dimension', r, vars_.get('topLeftRadius')))
    l = n.get('layout')
    if l:
        for side, val, key in zip(('top', 'right', 'bottom', 'left'), l['pad'], ('paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft')):
            if val or key in vars_:
                out.append(('padding-' + side, 'dimension', val, vars_.get(key)))
        kids = [c for c in n.get('children', []) or [] if not c.get('hidden') and not c.get('absolute')]
        if len(kids) > 1 and (l['gap'] or 'itemSpacing' in vars_):
            out.append(('gap', 'dimension', l['gap'], vars_.get('itemSpacing')))
    if n.get('minH'):
        out.append(('min-height', 'dimension', n['minH'], vars_.get('minHeight')))
    sz = n.get('sizing') or {}
    if sz.get('h') == 'FIXED' and not n.get('absolute'):
        out.append(('width', 'dimension', n['w'], vars_.get('width')))
    if sz.get('v') == 'FIXED' and not n.get('absolute'):
        out.append(('height', 'dimension', n['h'], vars_.get('height')))
    if n.get('opacity') is not None:
        out.append(('opacity', 'number', n['opacity'], vars_.get('opacity')))
    return out

def token_for(ptype, value, figvar, issues, where, layer):
    """DTCG token for one value: a reference when bound and valid, else a literal."""
    ref = figma_ref(figvar)
    tok = {'$type': ptype}
    ext = {}
    if ref:
        rl = SYSTEM[ref][0]
        if LAYER_RANK[rl] > LAYER_RANK['themes'] and layer == 'core':
            issues.append('**Layer:** %s binds `%s` (WordPress layer) in a core component; written as a literal.' % (where, figvar))
            ref = None
    if ref:
        tok['$value'] = '{%s}' % ref
        ext['figma'] = {'variable': figvar}
    else:
        if ptype == 'color':
            v, rgba = color_value(*value)
            tok['$value'] = v
            ext['rgba'] = rgba
        elif ptype == 'dimension':
            tok['$value'] = {'value': round(float(value), 3) if not float(value).is_integer() else int(value), 'unit': 'px'}
        elif ptype == 'fontFamily':
            tok['$value'] = value
        else:
            tok['$value'] = value
        if figvar:
            ext['figma'] = {'variable': figvar, 'note': 'Bound in Figma, but no single system token matches; literal value.'}
        elif ptype in ('color', 'fontFamily', 'fontWeight') or where.split(' ')[-1] in ('font-size', 'border-radius', 'gap') or 'padding' in where:
            ext['unbound'] = True
    if ext:
        tok['$extensions'] = {'com.mng': ext}
    return tok

def collapse(variants, keys, values):
    """values: {variant_index: value_json}. Returns [(selector_tuple, [variant indexes])] for the smallest
    set of variant properties that explains the value."""
    present = sorted(values)
    for size in range(0, len(keys) + 1):
        for S in combinations(keys, size):
            groups = defaultdict(list)
            ok = True
            seen = {}
            for i in present:
                k = tuple(variants[i]['variantProperties'][p] for p in S)
                if k in seen and seen[k] != values[i]:
                    ok = False
                    break
                seen[k] = values[i]
                groups[k].append(i)
            if not ok:
                continue
            if size == 0 and len(present) < len(variants):
                # present in only some variants: name the property value that marks them, if there is one;
                # otherwise the value is the same wherever the layer appears, so it is a base value
                for p in keys:
                    vals = {variants[i]['variantProperties'][p] for i in present}
                    others = {variants[i]['variantProperties'][p] for i in range(len(variants)) if i not in values}
                    if len(vals) == 1 and not (vals & others):
                        return [((p,), tuple(vals), present)]
            return [(S, k, idx) for k, idx in groups.items()]
    return [(tuple(keys), tuple(variants[i]['variantProperties'][p] for p in keys), [i]) for i in present]

def selector_name(S, k):
    if not S:
        return 'base'
    return '.'.join('%s-%s' % (slug(p), slug(v)) for p, v in zip(S, k))

# ---------- HTML skeleton ----------
def css_paint(p):
    ref = figma_ref(p.get('variable'))
    col = p['hex'] if p.get('opacity', 1) == 1 else 'rgba(%s, %s)' % (', '.join(str(int(p['hex'][i:i + 2], 16)) for i in (1, 3, 5)), fmt(p['opacity']))
    return 'var(%s, %s)' % (css_var(ref), col) if ref else col

def css_dim(val, var):
    ref = figma_ref(var)
    return 'var(%s, %spx)' % (css_var(ref), fmt(val)) if ref else '%spx' % fmt(val)

def node_css(n, parent):
    css = []
    v = n.get('vars') or {}
    l = n.get('layout')
    if l:
        css.append('display:flex')
        css.append('flex-direction:' + ('row' if l['dir'] == 'HORIZONTAL' else 'column'))
        css.append('gap:' + css_dim(l['gap'], v.get('itemSpacing')))
        css.append('padding:' + ' '.join(css_dim(x, v.get(k)) for x, k in zip(l['pad'], ('paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft'))))
        m = {'MIN': 'flex-start', 'CENTER': 'center', 'MAX': 'flex-end', 'SPACE_BETWEEN': 'space-between', 'BASELINE': 'baseline'}
        css.append('justify-content:' + m.get(l['main'], 'flex-start'))
        css.append('align-items:' + m.get(l['cross'], 'flex-start'))
    pl = parent.get('layout') if parent else None
    s = n.get('sizing') or {}
    if n.get('absolute'):
        css.append('position:absolute')
        c = n.get('constraints') or {}
        if c.get('horizontal') == 'STRETCH' and parent:
            css.append('left:%spx;right:%spx' % (fmt(n['x']), fmt(parent['w'] - n['x'] - n['w'])))
        else:
            css.append('left:%spx;width:%spx' % (fmt(n.get('x', 0)), fmt(n['w'])))
        if c.get('vertical') == 'STRETCH' and parent:
            css.append('top:%spx;bottom:%spx' % (fmt(n['y']), fmt(parent['h'] - n['y'] - n['h'])))
        else:
            css.append('top:%spx;height:%spx' % (fmt(n.get('y', 0)), fmt(n['h'])))
    elif not parent:
        # variant root: hug its content, or keep its Figma width when fixed / fill
        css.append('width:max-content' if s.get('h') == 'HUG' else 'width:%spx' % fmt(n['w']))
        if s.get('h') == 'HUG':
            # hugs its content but never overflows its container; a Figma max width becomes the CSS max width
            css.append('max-width:%s' % (('min(%spx, 100%%)' % fmt(n['maxW'])) if n.get('maxW') else '100%'))
        if s.get('v') == 'FIXED':
            css.append('height:%spx' % fmt(n['h']))
    else:
        horiz_main = pl and pl['dir'] == 'HORIZONTAL'
        for axis, dim in (('h', 'width'), ('v', 'height')):
            mode = s.get(axis)
            main = (axis == 'h') == bool(horiz_main)
            if mode == 'FIXED' or (n['type'] == 'INSTANCE' and mode == 'HUG'):
                css.append('%s:%spx' % (dim, fmt(n['w'] if axis == 'h' else n['h'])))
                if pl and main:
                    css.append('flex-shrink:0')
            elif mode == 'FILL' and pl:
                css.append('flex:1 1 0;min-width:0' if main else 'align-self:stretch')
    if n.get('minH'):
        css.append('min-height:' + css_dim(n['minH'], v.get('minHeight')))
    r = n.get('radius')
    if r is not None:
        css.append('border-radius:' + (' '.join(fmt(x) + 'px' for x in r) if isinstance(r, list) else css_dim(r, v.get('topLeftRadius'))))
    fills = n.get('fills')
    if fills and fills != 'mixed' and n['type'] not in ('TEXT', 'INSTANCE') and fills[0]['type'] == 'SOLID':
        css.append('background:' + css_paint(fills[0]))
    st = n.get('strokes')
    if st and st != 'mixed' and st[0]['type'] == 'SOLID':
        col = css_paint(st[0]); w = n.get('strokeWeight'); al = n.get('strokeAlign')
        style = 'dashed' if n.get('dash') else 'solid'
        if isinstance(w, list):
            for side, ww in zip(('top', 'right', 'bottom', 'left'), w):
                if ww:
                    css.append('border-%s:%spx %s %s' % (side, fmt(ww), style, col))
        elif al == 'OUTSIDE':
            css.append('box-shadow:0 0 0 %spx %s' % (fmt(w), col))
        elif al == 'INSIDE' and style == 'solid':
            css.append('box-shadow:inset 0 0 0 %spx %s' % (fmt(w), col))
        else:
            css.append('border:%spx %s %s' % (fmt(w), style, col))
    if n.get('clip'):
        css.append('overflow:hidden')
    if any(c.get('absolute') for c in n.get('children', []) or []):
        css.append('position:relative')
    if n['type'] == 'TEXT':
        stl = n['styles'][0]; sv = stl.get('vars') or v
        fam = figma_ref(sv.get('fontFamily'))
        famcss = 'var(%s)' % css_var(fam) if fam else "'%s', sans-serif" % stl['font']
        wt = figma_ref(sv.get('fontStyle'))
        wtcss = 'var(%s)' % css_var(wt) if wt else str(WEIGHT.get(stl['style'], 400))
        lh = 'normal' if stl['lineHeight'] == 'auto' else stl['lineHeight']
        css.append('font-family:%s;font-size:%s;font-weight:%s;line-height:%s' % (famcss, css_dim(stl['size'], sv.get('fontSize')), wtcss, lh))
        if stl.get('color'):
            css.append('color:' + css_paint(stl['color'][0]))
        css.append('text-align:' + n['align'].lower())
        if n.get('autoResize') == 'WIDTH_AND_HEIGHT':
            css.append('white-space:nowrap')
        case = {'UPPER': 'uppercase', 'LOWER': 'lowercase', 'TITLE': 'capitalize'}.get(stl.get('case'))
        if case:
            css.append('text-transform:' + case)
        if stl.get('decoration') == 'UNDERLINE':
            css.append('text-decoration:underline')
    return ';'.join(css)

ICON_GLYPH = {'close': '✕', 'new-tab': '↗', 'content_copy': '⧉', 'floppy-disk': '💾', 'user-plus': '+'}

def node_html(n, cslug, parent=None, ind=4):
    pad = ' ' * ind
    hid = ' hidden' if n.get('hidden') else ''
    c = 'mng-%s__%s' % (cslug, slug(n['name']) or 'layer')
    st = node_css(n, parent)
    if n['type'] == 'TEXT':
        return '%s<span class="%s" data-layer="%s" style="%s"%s>%s</span>' % (pad, c, html.escape(n['name']), st, hid, html.escape(n['text']))
    if n['type'] == 'INSTANCE':
        var = ', '.join('%s=%s' % kv for kv in (n.get('variant') or {}).items())
        g = ICON_GLYPH.get((n.get('variant') or {}).get('Name', ''), '◻')
        ic = n.get('iconFill')
        color = ';color:' + css_paint(ic[0]) if ic and ic != 'mixed' else ''
        return ('%s<!-- instance of %s (%s), Figma node %s -->\n%s<span class="mng-instance %s" data-component="%s" data-variant="%s" aria-hidden="true" style="%s;display:inline-flex;align-items:center;justify-content:center;font-size:%spx%s"%s>%s</span>'
                % (pad, n.get('component'), var, n.get('mainId'), pad, c, html.escape(n.get('component') or ''), html.escape(var), st, fmt(n['h']), color, hid, g))
    kids = '\n'.join(node_html(k, cslug, n, ind + 2) for k in n.get('children', []) or [])
    aria = ' aria-hidden="true"' if n['name'] == 'Focus Ring' else ''
    if kids:
        return '%s<div class="%s" data-layer="%s" style="%s"%s%s>\n%s\n%s</div>' % (pad, c, html.escape(n['name']), st, hid, aria, kids, pad)
    return '%s<div class="%s" data-layer="%s" style="%s"%s%s></div>' % (pad, c, html.escape(n['name']), st, hid, aria)

# ---------- spec helpers ----------
def anatomy(n, depth=0, maxd=6):
    if depth > maxd:
        return []
    bits = ['%s×%s' % (fmt(n['w']), fmt(n['h']))]
    if n.get('layout'):
        l = n['layout']
        bits.append('%s, gap %s, padding %s' % (l['dir'].lower(), fmt(l['gap']), '/'.join(fmt(x) for x in l['pad'])))
    if n.get('sizing'):
        bits.append('%s×%s' % (n['sizing']['h'].lower(), n['sizing']['v'].lower()))
    if n.get('absolute'):
        bits.append('absolute')
    if n['type'] == 'TEXT':
        st = n['styles'][0]
        bits.append('"%s", %s %s %spx' % (n['text'][:40], st['font'], st['style'], fmt(st['size'])))
    if n['type'] == 'INSTANCE':
        bits.append('instance of %s (%s)' % (n.get('component'), ', '.join('%s=%s' % kv for kv in (n.get('variant') or {}).items())))
    if n.get('hidden'):
        bits.append('**hidden**')
    lines = ['%s- **%s** `%s`: %s' % ('  ' * depth, n['name'], n['type'], ', '.join(bits))]
    if n['type'] != 'INSTANCE':
        for c in n.get('children', []) or []:
            lines += anatomy(c, depth + 1, maxd)
    return lines

def token_rows(tree, prefix=()):
    for k, v in tree.items():
        if k.startswith('$'):
            continue
        if isinstance(v, dict) and '$value' in v:
            yield prefix + (k,), v
        elif isinstance(v, dict):
            yield from token_rows(v, prefix + (k,))

def show_value(t):
    v = t['$value']
    if isinstance(v, str) and v.startswith('{'):
        return '`%s`' % v
    if isinstance(v, dict) and 'hex' in v:
        return '%s%s' % (v['hex'], '' if v.get('alpha', 1) == 1 else ' @ %s' % fmt(v['alpha']))
    if isinstance(v, dict) and 'unit' in v:
        return '%s%s' % (fmt(v['value']), v['unit'])
    return str(v)

# ---------- main ----------
def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    raw = sys.argv[1]
    only = set(sys.argv[2:])
    reg = load(os.path.join(HERE, 'registry.json'))
    sets, fileinfo = {}, {}
    for f in sorted(glob.glob(os.path.join(raw, 'specs-*.json'))):
        d = load(f)
        for r in d['results']:
            sets[r['set']['id']] = r
            fileinfo[r['set']['id']] = (d['fileKey'], d['fileName'])
    pngs = {}
    for f in sorted(glob.glob(os.path.join(raw, 'previews-*.json'))):
        pngs.update(load(f)['out'])
    order_vals = reg.get('valueOrder', {})
    order_props = reg.get('propertyOrder', [])
    index = []
    all_issues = 0
    for comp in reg['components']:
        if only and comp['slug'] not in only:
            continue
        r = sets.get(comp['node'])
        if not r:
            print('skip %s: no Figma dump for %s' % (comp['slug'], comp['node']))
            continue
        fk, fname = fileinfo[comp['node']]
        s = r['set']
        cs = comp['slug']
        layer = comp['layer']
        keys = sorted(s['properties'], key=lambda k: (order_props.index(k) if k in order_props else 99, k))
        def vsort(v):
            vp = v['variantProperties']
            return tuple((order_vals[k].index(vp[k]) if k in order_vals and vp[k] in order_vals[k] else s['properties'][k]['options'].index(vp[k])) for k in keys)
        variants = sorted(s['variants'], key=vsort)
        for v in variants:
            v['_label'] = ' / '.join(v['variantProperties'][k] for k in keys) or s['name']
            v['_slug'] = '-'.join(slug(v['variantProperties'][k]) for k in keys) or 'default'
        out = os.path.join(ROOT, 'components', layer, cs)
        if os.path.isdir(out):
            shutil.rmtree(out)
        os.makedirs(os.path.join(out, 'previews'))
        issues = list(comp.get('knownIssues') or [])
        auto_issues = []

        # previews
        for v in variants:
            fn = '%s--%s.png' % (cs, v['_slug'])
            if v['id'] in pngs:
                open(os.path.join(out, 'previews', fn), 'wb').write(base64.b64decode(pngs[v['id']]))
                v['_preview'] = 'previews/' + fn
        docfn = None
        if r.get('doc') and r['doc']['id'] in pngs:
            docfn = '%s--documentation.png' % cs
            open(os.path.join(out, 'previews', docfn), 'wb').write(base64.b64decode(pngs[r['doc']['id']]))

        # component tokens
        data = defaultdict(dict)
        types = {}
        figvars = defaultdict(dict)
        for i, v in enumerate(variants):
            def grab(n, path, i=i):
                for prop, ptype, val, fv in props_of(n):
                    key = (tuple(path), prop)
                    data[key][i] = json.dumps([val, fv])
                    types[key] = ptype
            visible_walk(v, [], grab)
        tokens = OrderedDict()
        unbound = []
        for key in sorted(data, key=lambda k: (k[0], k[1])):
            path, prop = key
            for S, kv, idx in collapse(variants, keys, data[key]):
                val, fv = json.loads(data[key][idx[0]])
                if isinstance(val, list):
                    val = tuple(val)
                where = '`%s` %s %s' % (selector_name(S, kv), '.'.join(path), prop)
                tok = token_for(types[key], val, fv, auto_issues, where, layer)
                if tok.get('$extensions', {}).get('com.mng', {}).get('unbound'):
                    unbound.append('%s = %s' % (where, show_value(tok)))
                node = tokens.setdefault(selector_name(S, kv), OrderedDict())
                for seg in path:
                    node = node.setdefault(seg, OrderedDict())
                node[prop] = tok
        tok_doc = OrderedDict([
            ('$description', '%s component tokens. Generated by scripts/component-export/export.py from Figma (%s, %s); never edit by hand. '
                             '"base" holds values shared by every variant; other groups are keyed by the variant property that changes the value.'
                             % (comp['name'], fname, s['id'])),
            ('$extensions', {'com.mng': {'figma': {'file': fname, 'fileKey': fk, 'node': s['id'], 'componentSet': s['name'], 'page': r['page']['name']},
                                          'production': comp.get('production'), 'layer': layer, 'exported': DATE}}),
            (cs, tokens)])
        with open(os.path.join(out, cs + '.tokens.json'), 'w', encoding='utf-8') as f:
            json.dump(tok_doc, f, indent=2, ensure_ascii=False)
            f.write('\n')

        # usage and dependencies
        total = sum(v['usage']['total'] for v in variants)
        built_into, pages, deps, icons = Counter(), Counter(), Counter(), Counter()
        nested = 0
        for v in variants:
            for k, c in v['usage']['inComponents'].items():
                built_into[k.split('/')[0]] += c
            for k, c in v['usage']['other'].items():
                pages[k.split(' > ')[0]] += c
            nested += v['usage']['nested']
            def dep(n, path):
                if n['type'] == 'INSTANCE':
                    deps[n.get('component')] += 1
                    if n.get('component') == 'Icons':
                        icons[(n.get('variant') or {}).get('Name')] += 1
            visible_walk(v, [], dep)
        zero = [v['_label'] for v in variants if v['usage']['total'] == 0]
        if unbound:
            auto_issues.append('**Values not bound to a token** (literal in the component tokens): ' + '; '.join(unbound[:12]) + ('; and %d more' % (len(unbound) - 12) if len(unbound) > 12 else '') + '.')
        # Variants with 0 instances are fine (Karl, 2026-10-14): the counts are in the Variants table, not Known issues.
        fonts = set()
        for v in variants:
            visible_walk(v, [], lambda n, p: fonts.update(st['font'] for st in n.get('styles', [])) if n['type'] == 'TEXT' else None)
        if fonts - {'Noto Sans', 'Noto Serif'}:
            auto_issues.append('**Fonts outside Noto Sans / Noto Serif:** ' + ', '.join(sorted(fonts - {'Noto Sans', 'Noto Serif'})) + '.')
        issues += auto_issues
        all_issues += len(issues)

        # markdown
        default = variants[0]
        bps = s['properties'].get('Breakpoint', {}).get('options')
        rel = os.path.relpath(ROOT, out)
        md = ['---',
              'name: %s' % comp['name'], 'slug: %s' % cs, 'layer: %s' % layer, 'figma_file: %s' % fk, 'figma_set: "%s"' % s['name'],
              'figma_node: "%s"' % s['id'], 'component_key: %s' % s['key'], 'variants: %d' % len(variants),
              'tokens: %s.tokens.json' % cs, 'skeleton: %s.html' % cs, 'exported: %s' % DATE, '---', '',
              '# %s' % comp['name'], '', '> %s' % comp['description'], '',
              '## Figma', '',
              '- File: **%s** (`%s`), page **%s**' % (fname, fk, r['page']['name']),
              '- Component set: [`%s` · %s](%s) · key `%s`' % (s['name'], s['id'], url(fk, s['id']), s['key'])]
        if r.get('doc'):
            md.append('- Documentation frame: [%s](%s)%s' % (r['doc']['name'], url(fk, r['doc']['id']), ' · overview: [previews/%s](previews/%s)' % (docfn, docfn) if docfn else ''))
        md += ['', '## Properties', '']
        if keys:
            md += ['| Property | Default | Options |', '|---|---|---|']
            for k in keys:
                p = s['properties'][k]
                md.append('| %s | %s | %s |' % (k, p['default'], ', '.join(sorted(p['options'], key=lambda x: order_vals.get(k, p['options']).index(x) if x in order_vals.get(k, p['options']) else 99))))
        else:
            md.append('No variant properties (single component).')
        md += ['', '## Variants', '', '| Variant | Size | Node | Instances | Preview |', '|---|---|---|---|---|']
        for v in variants:
            md.append('| `%s` | %s×%s | [%s](%s) | %d | %s |' % (v['_label'], fmt(v['w']), fmt(v['h']), v['id'], url(fk, v['id']), v['usage']['total'],
                                                             '![](%s)' % v['_preview'] if v.get('_preview') else '—'))
        md += ['', '## Anatomy', '', 'Default variant `%s` (hidden layers marked):' % default['_label'], ''] + anatomy(default)
        focus = next((v for v in variants if v['variantProperties'].get('State') == 'InFocus'), None)
        if focus:
            md += ['', 'InFocus variant `%s`:' % focus['_label'], ''] + anatomy(focus)
        md += ['', '## Component tokens', '',
               'From `%s.tokens.json`. References point at system tokens (`tokens/core/`, `tokens/themes/`); the CSS variable is `--mng-` + the token path. '
               'A literal value means the Figma layer isn\'t bound to a token.' % cs, '',
               '| Token | Value |', '|---|---|']
        for path, t in token_rows(tokens):
            md.append('| `%s.%s` | %s |' % (cs, '.'.join(path), show_value(t)))
        md += ['', '## Behavior and breakpoints', '', comp.get('breakpoints') or 'No Breakpoint property: one size at every width.', '']
        md += ['- %s' % x for x in comp.get('rules') or []]
        md += ['', '## Accessibility', '',
               '- Keyboard focus: the `InFocus` variant shows the focus ring (see Behavior). Never remove the focus indicator.' if focus else '- No InFocus state in Figma.',
               '- Text color on its background must meet WCAG AA contrast (4.5:1 for text under 18px) in every theme; theme colors change per site.',
               '- Icons inside a labelled control are decorative (`aria-hidden`); an icon-only control needs an accessible name (`aria-label`).', '',
               '## Where it is used', '',
               'Scope: instances in the Figma file **%s** only (other files that use the library are not counted). Total: **%d**.' % (fname, total), '']
        if built_into:
            md.append('Inside components: ' + ', '.join('%s ×%d' % kv for kv in built_into.most_common()) + '.')
        if pages:
            md.append('Placed on pages: ' + ', '.join('%s ×%d' % kv for kv in pages.most_common()) + '.')
        if nested:
            md.append('%d instances are nested inside other instances.' % nested)
        md += ['', '**Built from:** ' + (', '.join('%s ×%d' % kv for kv in deps.most_common()) if deps else 'no nested components.')]
        if icons:
            md.append('Icon variants: ' + ', '.join('`%s` ×%d' % kv for kv in icons.most_common()) + '.')
        prod = comp.get('production')
        md += ['', '## Production', '']
        if prod:
            md += ['- %s: `%s`' % (k, v) for k, v in prod.items()]
        else:
            md.append('No production selector recorded yet. Production gaps go in `design-vs-production.md`.')
        md += ['', '## Known issues', '']
        md += ['%d. %s' % (i + 1, x) for i, x in enumerate(issues)] if issues else ['None open.']
        md += ['', '## Files', '',
               '- `%s.tokens.json`: component tokens (DTCG 2025.10).' % cs,
               '- `%s.html`: HTML/CSS skeleton of every variant, using the `dist/` CSS variables (open it in a browser).' % cs,
               '- `previews/`: PNG of every variant @2x%s.' % (' and the documentation frame' if docfn else ''),
               '', '*Generated %s by `scripts/component-export/export.py` (%s section 7). Edit the text in `scripts/component-export/registry.json`, not here.*' % (DATE, STANDARD)]
        with open(os.path.join(out, cs + '.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(md) + '\n')

        # html
        secs = []
        for v in variants:
            secs.append('<section class="mng-variant" data-variant="%s">\n  <h2>%s <small>%s×%s · <a href="%s">Figma %s</a></small></h2>\n  <div class="mng-variant__stage">\n%s\n  </div>\n</section>'
                        % (html.escape(v['_label']), html.escape(v['_label']), fmt(v['w']), fmt(v['h']), url(fk, v['id']), v['id'], node_html(v, cs)))
        page = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(name)s: skeleton</title>
<!-- Generated %(date)s by scripts/component-export/export.py from Figma %(file)s (%(fk)s), set %(sid)s. Structure and tokens only; rules are in %(slug)s.md. -->
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700&family=Noto+Serif:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="%(rel)s/dist/css/core.css">
<link rel="stylesheet" href="%(rel)s/dist/css/themes/bold-coastal.css">
<style>
  [hidden]{display:none!important}
  *{box-sizing:border-box}
  body{font-family:var(--mng-font-family-noto-sans);margin:24px;background:#fff;color:#141414}
  h1{font-size:20px;margin:0 0 4px} .mng-intro{margin:0 0 24px;color:#5e5d5c;font-size:14px}
  .mng-variant{margin:0 0 24px} .mng-variant h2{font-size:13px;font-weight:600;margin:0 0 8px} .mng-variant h2 small{font-weight:400;color:#838280}
  .mng-variant__stage{padding:16px;border:1px dashed #cccac7;display:inline-block;min-width:120px}
</style></head>
<body>
<h1>%(name)s</h1>
<p class="mng-intro">Every variant of the Figma set <code>%(set)s</code>. Theme: Bold Coastal (swap the theme stylesheet to preview another theme). Icons are placeholders.</p>
%(secs)s
</body></html>
''' % {'name': html.escape(comp['name']), 'date': DATE, 'file': fname, 'fk': fk, 'sid': s['id'], 'slug': cs, 'rel': rel,
       'set': html.escape(s['name']), 'secs': '\n'.join(secs)}
        with open(os.path.join(out, cs + '.html'), 'w', encoding='utf-8') as f:
            f.write(page)

        index.append(OrderedDict([('slug', cs), ('name', comp['name']), ('group', comp.get('group')), ('layer', layer),
                                  ('path', 'components/%s/%s/' % (layer, cs)), ('figma', {'fileKey': fk, 'node': s['id'], 'set': s['name']}),
                                  ('variants', len(variants)), ('instances', total), ('knownIssues', len(issues)), ('exported', DATE)]))
        print('%-22s %2d variants, %3d tokens, %d issues -> components/%s/%s/' % (cs, len(variants), sum(1 for _ in token_rows(tokens)), len(issues), layer, cs))

    # index (merge with components already exported in earlier runs)
    ip = os.path.join(ROOT, 'components', 'index.json')
    old = load(ip)['components'] if os.path.exists(ip) else []
    done = {c['slug'] for c in index}
    merged = [c for c in old if c['slug'] not in done] + index
    merged.sort(key=lambda c: (c['layer'], c.get('group') or '', c['slug']))
    with open(ip, 'w', encoding='utf-8') as f:
        json.dump({'$description': 'Components exported by scripts/component-export/export.py (EXPORT-STANDARD.md section 7). Never edit by hand.',
                   'components': merged}, f, indent=2, ensure_ascii=False)
        f.write('\n')

if __name__ == '__main__':
    main()
