#!/usr/bin/env python3
"""MNG Web Design System: build tokens/breakpoint-inventory.json (EXPORT-STANDARD.md section 6).

Inputs
  scripts/breakpoint-inventory/scans/<domain>.json   live CSS scans of the 6 review sites (scan.js), 2026-10-14.
                                                      ocregister.com is the full list; the other files list only
                                                      the differences from it ("b" = extra, "absent" = missing).
  CLASSIFY below                                      who owns each value and what it should snap to (hand-checked).
  REPO_SOURCES below                                  breakpoints found in the website repo copy (2026-05-08), from
                                                      status open item 11 and design-vs-production entries 31 and 32.
Output
  tokens/breakpoint-inventory.json

Tiers (EXPORT-STANDARD.md section 6): official (MNG Device or WordPress grid), component (an intended one-off,
goes in that component's tokens), drift (logged in design-vs-production.md with what to snap to),
to-confirm (waiting for Karl), plus third-party, wordpress-admin and not-documented values, which are
left out of the output (Karl, 2026-10-14).

Run from the repo top: python3 scripts/breakpoint-inventory/build-inventory.py      Stdlib only.
"""
import glob, json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SCANS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scans')
BASE = 'ocregister.com'

DEVICE = {'fold': 340, 'mobile': 360, 'tablet': 768, 'tablet-landscape': 1024, 'desktop': 1280}
GRID = {'xs': 320, 's': 640, 'm': 800, 'l': 1040, 'xl': 1280}

def bp(set_name, key, kind):
    """Human form of a boundary, e.g. 'WordPress grid s: min-width 640 / max-width 639'."""
    v = (DEVICE if set_name == 'device' else GRID)[key]
    label = ('MNG Device ' if set_name == 'device' else 'WordPress grid ') + key
    return {'set': set_name, 'token': ('breakpoint.%s' % key) if set_name == 'device' else ('breakpoint.wordpress-grid.%s' % key),
            'query': '(min-width: %dpx)' % v if kind == 'min' else '(max-width: %dpx)' % (v - 1), 'label': label}

THEME = 'WordPress theme (boldcoastal / measuredvibrant / modernearthy CSS)'
DIGI = 'mng-digisubs (MNG subscriptions: account menu, regwall, sign-in; follows the MNG Device set, Karl 2026-10-14)'
DIGI_APP = 'plugins.mngdigisubs.com (MNG digisubs app, Bootstrap 5 default grid; follows the MNG Device set)'
TRUST = 'dfm-trust-indicators plugin (MNG)'
ADS = 'WordPress theme ad rules (dfp-ad, mobile adhesion)'
MG2 = 'Mg2 Connext paywall (third party, engage.<site>)'
OSANO = 'Osano cookie consent (third party, inline)'
KARGO = 'Kargo ads (third party, inline)'
HTL = 'HTL ad bidder (third party, htlbid.com)'
WPADMIN = 'WordPress admin bar (logged-in editors only)'

# key: (owners, tier, snap_to or None, note)
G, D = 'wordpress-grid', 'device'
CLASSIFY = {
    '>0': ([HTL], 'third-party', None, ''),
    '>300': ([ADS], 'component', None, 'Ad Blocks component breakpoint: ad rules keep their own values (Karl, 2026-10-14). Top leaderboard ad (.dfp-ad.dfp-top_leaderboard).'),
    '>320': ([THEME], 'official', bp('grid', 'xs', 'min'), ''),
    '<320': ([KARGO], 'third-party', None, ''),
    '<335': ([THEME], 'component', None, 'Masthead (WordPress): nav search icon on very small phones. Component breakpoint for the Masthead (Karl, 2026-10-14).'),
    '<340': ([DIGI, DIGI_APP], 'drift', bp('device', 'fold', 'max'), 'Off by one: (max-width: 340px) overlaps fold; should be 339.'),
    '<344': ([DIGI], 'not-documented', None, 'Not documented (Karl, 2026-10-14): digisubs modal, spoof banner, push prompt, share box or employee debugger.'),
    '<350': ([THEME], 'component', None, 'Masthead (WordPress): nav hamburger icon on very small phones. Component breakpoint for the Masthead (Karl, 2026-10-14).'),
    '<360': ([DIGI_APP], 'drift', bp('device', 'mobile', 'max'), 'Off by one: (max-width: 360px) overlaps mobile; should be 359.'),
    '>360': ([DIGI], 'official', bp('device', 'mobile', 'min'), 'Regwall button.'),
    '>376': ([OSANO], 'third-party', None, ''),
    '<380': ([DIGI], 'not-documented', None, 'Not documented (Karl, 2026-10-14): digisubs modal, spoof banner, push prompt, share box or employee debugger.'),
    '<400': ([DIGI_APP], 'drift', bp('device', 'mobile', 'max'), 'Sign-in modal.'),
    '<405': ([THEME], 'drift', bp('grid', 's', 'max'), 'Sports Radar page template (#content.sports-radar-content; local template styling embedded Sportradar data widgets): follows the WordPress grid (Karl, 2026-10-14).'),
    '<420': ([MG2], 'third-party', None, ''),
    '<430': ([DIGI], 'not-documented', None, 'Not documented (Karl, 2026-10-14): digisubs modal, spoof banner, push prompt, share box or employee debugger.'),
    '>431': ([DIGI], 'not-documented', None, 'Not documented (Karl, 2026-10-14): digisubs modal, spoof banner, push prompt, share box or employee debugger.'),
    '<432': ([MG2], 'third-party', None, ''),
    '<450': ([DIGI], 'drift', bp('device', 'mobile', 'max'), 'Digisubs modals, paywall container, regwall form, save-article and nickname modals, account dropdown (37 rules).'),
    '>450': ([DIGI], 'not-documented', None, 'Not documented (Karl, 2026-10-14): digisubs modal, spoof banner, push prompt, share box or employee debugger.'),
    '<467': ([MG2], 'third-party', None, ''),
    '<480': ([ADS], 'component', None, 'Ad Blocks component breakpoint: ad rules keep their own values (Karl, 2026-10-14). Mobile adhesion ad (#mobile-adhesion).'),
    '<500': ([THEME], 'drift', bp('grid', 's', 'max'), 'Sports Radar page template (#content.sports-radar-content; local template styling embedded Sportradar data widgets): follows the WordPress grid (Karl, 2026-10-14).'),
    '<535': ([THEME], 'drift', bp('grid', 's', 'max'), 'Sports Radar page template (#content.sports-radar-content; local template styling embedded Sportradar data widgets): follows the WordPress grid (Karl, 2026-10-14).'),
    '<550': ([DIGI], 'drift', bp('device', 'mobile', 'max'), 'Regwall (:root:not(:has(#server-regwall))).'),
    '<575.98': ([DIGI_APP], 'drift', bp('device', 'tablet', 'max'), 'Bootstrap sm-down.'),
    '<576': ([DIGI, MG2], 'drift', bp('device', 'tablet', 'max'), 'Digisubs content (.sspw-content).'),
    '>576': ([DIGI_APP], 'drift', bp('device', 'tablet', 'min'), 'Bootstrap sm container.'),
    '<600': ([THEME, DIGI], 'drift', bp('grid', 's', 'max'), 'Theme: article bottom share buttons (.article-bottom-share), snap to grid s (639). Digisubs: change-username modal, snap to Device tablet (767). (The share box rule here is not documented.)'),
    '>600': ([WPADMIN], 'wordpress-admin', None, 'body.admin-bar.'),
    '<624': ([THEME], 'drift', bp('grid', 's', 'max'), 'Obituaries 1-column layout (entry 32).'),
    '>625': ([THEME], 'drift', bp('grid', 's', 'min'), 'Obituaries 2-column start (entry 32).'),
    '<639': ([THEME], 'official', bp('grid', 's', 'max'), ''),
    '>640': ([THEME], 'official', bp('grid', 's', 'min'), ''),
    '<700': ([THEME], 'drift', bp('grid', 's', 'max'), 'Promotion widget (.promotion-widget, homepage promo tiles): follows the WordPress grid (Karl, 2026-10-14).'),
    '<720': ([MG2], 'third-party', None, ''),
    '<730': ([THEME], 'not-documented', None, 'Special investigative header template: left out for now (Karl, 2026-10-14).'),
    '<734': ([THEME], 'drift', bp('grid', 'm', 'max'), 'Photo gallery widget (.gallery-container; also entry 32). Fix (Karl).'),
    '>735': ([THEME], 'drift', bp('grid', 'm', 'min'), 'Photo gallery widget (also entry 32). Fix (Karl).'),
    '<750': ([ADS, THEME], 'component', None, 'Ad Blocks component breakpoint: ad rules keep their own values (Karl, 2026-10-14). Header banners (.header-banners): the top leaderboard ad container under the masthead. The special investigative header also uses 750.'),
    '>750': ([ADS], 'component', None, 'Ad Blocks component breakpoint: ad rules keep their own values (Karl, 2026-10-14). Top leaderboard ad.'),
    '<767': ([MG2], 'third-party', None, ''),
    '<767.98': ([DIGI_APP], 'official', bp('device', 'tablet', 'max'), 'Bootstrap md-down: the same boundary as MNG Device tablet (below 768).'),
    '<768': ([MG2], 'third-party', None, ''),
    '>768': ([DIGI, DIGI_APP, MG2, OSANO], 'official', bp('device', 'tablet', 'min'), 'Digisubs rules match MNG Device tablet.'),
    '<770': ([DIGI], 'drift', bp('device', 'tablet', 'max'), 'Account dropdown menu.'),
    '<783': ([WPADMIN], 'wordpress-admin', None, ''),
    '>783': ([WPADMIN], 'wordpress-admin', None, ''),
    '<799': ([THEME], 'official', bp('grid', 'm', 'max'), ''),
    '<800': ([THEME, MG2], 'drift', bp('grid', 'm', 'max'), 'Off by one: (max-width: 800px) overlaps m; should be 799 (#featured-flex-landing-three).'),
    '>800': ([THEME], 'official', bp('grid', 'm', 'min'), ''),
    '<820': ([DIGI], 'drift', bp('device', 'tablet', 'max'), 'Account dropdown menu.'),
    '<900': ([THEME], 'drift', bp('grid', 'm', 'max'), 'Promotion widget title: follows the WordPress grid (Karl). Sports Radar also uses an 800-900 range.'),
    '<930': ([THEME], 'drift', bp('grid', 'l', 'max'), 'Footer cookie notice button (Karl: fix to 1039).'),
    '<960': ([THEME], 'drift', bp('grid', 'l', 'max'), 'Sports Radar page template (#content.sports-radar-content; local template styling embedded Sportradar data widgets): follows the WordPress grid (Karl, 2026-10-14).'),
    '<971': ([MG2], 'third-party', None, ''),
    '>972': ([MG2], 'third-party', None, ''),
    '<979': ([MG2], 'third-party', None, ''),
    '<991': ([MG2], 'third-party', None, ''),
    '<991.98': ([DIGI_APP], 'drift', bp('device', 'tablet-landscape', 'max'), 'Bootstrap lg-down.'),
    '<992': ([MG2], 'third-party', None, ''),
    '>992': ([DIGI_APP, MG2], 'drift', bp('device', 'tablet-landscape', 'min'), 'Bootstrap lg container.'),
    '<1000': ([ADS], 'component', None, 'Ad Blocks component breakpoint: ad rules keep their own values (Karl, 2026-10-14). Mobile adhesion ad.'),
    '>1000': ([ADS], 'component', None, 'Ad Blocks component breakpoint: ad rules keep their own values (Karl, 2026-10-14). Top and bottom leaderboard ad placement.'),
    '<1024': ([DIGI, THEME, MG2], 'drift', bp('device', 'tablet-landscape', 'max'), 'Off by one for the Device set (should be 1023); the theme rule (#dfm-digisubs-menu) should use grid l (1039).'),
    '>1024': ([DIGI], 'official', bp('device', 'tablet-landscape', 'min'), 'Digisubs card line.'),
    '<1025': ([ADS], 'component', None, 'Ad Blocks component breakpoint: ad rules keep their own values (Karl, 2026-10-14). Mobile adhesion ad.'),
    '<1039': ([THEME, DIGI, TRUST], 'official', bp('grid', 'l', 'max'), 'The masthead switches to desktop here.'),
    '<1040': ([TRUST, THEME], 'drift', bp('grid', 'l', 'max'), 'Off by one: (max-width: 1040px) overlaps l; should be 1039 (trust-indicator footer links).'),
    '>1040': ([THEME], 'official', bp('grid', 'l', 'min'), ''),
    '<1064': ([MG2], 'third-party', None, ''),
    '<1150': ([THEME], 'not-documented', None, 'Special investigative header template: left out for now (Karl, 2026-10-14).'),
    '<1199': ([MG2], 'third-party', None, ''),
    '<1199.98': ([DIGI_APP], 'drift', bp('device', 'desktop', 'max'), 'Bootstrap xl-down.'),
    '<1200': ([OSANO, MG2], 'third-party', None, ''),
    '>1200': ([DIGI_APP, MG2], 'drift', bp('device', 'desktop', 'min'), 'Bootstrap xl container.'),
    '<1279': ([THEME], 'official', bp('grid', 'xl', 'max'), ''),
    '<1280': ([THEME], 'drift', bp('grid', 'xl', 'max'), 'Off by one: (max-width: 1280px) overlaps xl; should be 1279 (.custom-dfm-section.dark-layout).'),
    '>1280': ([THEME, DIGI], 'official', bp('grid', 'xl', 'min'), 'Also MNG Device desktop (1280).'),
    '>1281': ([MG2], 'third-party', None, ''),
    '<1299': ([THEME], 'drift', bp('grid', 'xl', 'max'), 'Obituaries listing (entry 32).'),
    '>1300': ([THEME], 'drift', bp('grid', 'xl', 'min'), 'Obituaries "stop scaling" (entry 32).'),
    '<1399.98': ([DIGI_APP], 'drift', bp('device', 'desktop', 'max'), 'Bootstrap xxl-down: no official breakpoint above 1280.'),
    '>1400': ([DIGI_APP], 'drift', bp('device', 'desktop', 'min'), 'Bootstrap xxl container: no official breakpoint above 1280.'),
    '<599': ([WPADMIN], 'wordpress-admin', None, 'Admin bar notes.'),
    '<782': ([WPADMIN], 'wordpress-admin', None, 'Admin bar (only when an editor is logged in).'),
    '>782': ([WPADMIN], 'wordpress-admin', None, ''),
    '>900': ([WPADMIN], 'wordpress-admin', None, 'Admin bar notes.'),
    '>960': ([WPADMIN], 'wordpress-admin', None, 'Admin bar notes.'),
}

REPO_SOURCES = [
    {'source': 'assets/client/scss/common-base/layout/_grid-variables.scss (WordPress themes)',
     'values': [320, 640, 800, 1040, 1280], 'tier': 'official', 'set': 'wordpress-grid',
     'note': 'The WordPress grid ($columns-map, ai-breakpoint() mixin, written in em). The masthead switches at l (1040).'},
    {'source': 'plugins/mng-digital-subscriber-widgets/reader-dashboard-src (Reader Dashboard, Tailwind v4)',
     'values': [640, 768, 1024, 1280, 1536], 'tier': 'drift', 'set': 'device',
     'note': 'Tailwind defaults sm/md/lg/xl/2xl; the layout switches at 1024 and 1280. 640 and 1536 are not Device values. Production-vs-design entry 31 (questions for DigiScrum).'},
    {'source': 'Reader Dashboard built CSS', 'values': [361, 413], 'tier': 'drift', 'set': 'device',
     'note': 'Source not traced yet; close to Device mobile (360). Entry 31.'},
    {'source': 'assets/client/scss/layouts/scng/components/features/_obits.scss (Obituaries)',
     'values': [624, 625, 734, 735, 1000, 1299, 1300], 'tier': 'drift', 'set': 'wordpress-grid',
     'note': 'Obituaries off-grid values; also seen live. Entry 32 (CMS team).'},
    {'source': 'Spotlight template (WordPress themes)', 'values': [624, 734, 735, 1299, 1300], 'tier': 'drift',
     'set': 'wordpress-grid', 'note': 'Same off-grid values as Obituaries (shared gallery and listing rules).'},
]

def load_scans():
    scans = {}
    for p in sorted(glob.glob(os.path.join(SCANS, '*.json'))):
        with open(p, encoding='utf-8') as f:
            d = json.load(f)
        scans[d['site']] = d
    return scans

def main():
    scans = load_scans()
    base = scans[BASE]
    base_keys = {e[0]: e for e in base['b']}
    values = {}
    for site, d in scans.items():
        if site == BASE:
            keys = set(base_keys)
            extra = {}
        else:
            keys = set(base_keys) - set(d.get('absent', []))
            extra = {e[0]: e for e in d['b']}
            keys |= set(extra)
        for k in keys:
            e = base_keys.get(k) or extra[k]
            v = values.setdefault(k, {'uses': e[1], 'sheets': list(e[2]), 'sample': e[3], 'sites': []})
            v['sites'].append(site)
            for s in e[2]:
                if s not in v['sheets']:
                    v['sheets'].append(s)
    missing = sorted(set(values) - set(CLASSIFY))
    if missing:
        raise SystemExit('classify these first: %s' % missing)
    rows = []
    for k, v in values.items():
        owners, tier, snap, note = CLASSIFY[k]
        kind = 'min' if k[0] == '>' else 'max'
        px = float(k[1:])
        px = int(px) if px == int(px) else px
        third = (MG2, OSANO, KARGO, HTL, WPADMIN)
        ours = [o for o in owners if o not in third] or owners
        sheets = [x for x in v['sheets'] if not x.startswith('3P:') or 'mngdigisubs' in x]
        sample = v['sample'] if not any(t in v['sample'] for t in ('osano', 'Mg2', 'kargo', 'htlad')) else None
        row = {'query': '(%s-width: %spx)' % (kind, px), 'kind': kind, 'px': px, 'tier': tier, 'owners': ours,
               'sites': sorted(v['sites']), 'rules': v['uses'], 'stylesheets': sheets or v['sheets'], 'sampleSelector': sample}
        if snap:
            row['official' if tier == 'official' else ('snapToIfDrift' if tier == 'to-confirm' else 'snapTo')] = snap
        if note:
            row['note'] = note
        rows.append(row)
    excluded = {t: sum(1 for r in rows if r['tier'] == t) for t in ('third-party', 'wordpress-admin')}
    rows = [r for r in rows if r['tier'] not in excluded and r['tier'] != 'not-documented']  # not ours / not documented (Karl, 2026-10-14)
    rows.sort(key=lambda r: (r['px'], r['kind']))
    counts = {}
    for r in rows:
        if r['tier'] in ('third-party', 'wordpress-admin', 'not-documented'):
            continue
        counts[r['tier']] = counts.get(r['tier'], 0) + 1
    out = {
        '$description': 'Every width breakpoint found in MNG production code, classified as official, component or drift '
                        '(EXPORT-STANDARD.md section 6); third-party and WordPress admin-bar values are left out. Built by scripts/breakpoint-inventory/'
                        'build-inventory.py; never edit by hand. Drift is logged in design-vs-production.md '
                        '(entries 31, 32, 33) with the official breakpoint to snap to.',
        'scanned': '2026-10-14',
        'method': 'Live CSS scan (scan.js) of every loaded stylesheet, @media width conditions only, on the homepage, an '
                  'article and the obituaries page of each review site, at a 1728px-wide window (media rules are read '
                  'from the CSS, so the window width does not matter). Cross-origin sheets were fetched; the HTL ad '
                  'bidder sheet was blocked on most sites. em/rem converted at 16px. JavaScript breakpoints '
                  '(matchMedia, window.innerWidth) are not included.',
        'officialSets': {
            'device': {'tokens': 'tokens/core/breakpoint.tokens.json', 'minWidths': DEVICE},
            'wordpress-grid': {'tokens': 'tokens/wordpress/breakpoint.tokens.json', 'minWidths': GRID},
        },
        'sites': {s: {'pages': d['pages'], 'blockedStylesheets': d.get('blocked', [])} for s, d in scans.items()},
        'summary': counts,
        'excluded': {'thirdParty': excluded['third-party'], 'wordpressAdminBar': excluded['wordpress-admin'],
                     'digisubsNotDocumented': ['digisubs modal (max 344)', 'spoof banner (max 380)', 'push prompt (max 430)',
                                               'article share box (min 431)', 'employee debugger (min 450)'],
                     'specialInvestigativeHeader': 'Left out for now (max-width 730 / 1150, plus shared 500 / 600 / 750 / 900 / 1024). Not found on a live page of the 6 sites; find it in production when more article pages are added to WordPress Elements (Karl, 2026-10-14).',
                     'note': 'Third-party breakpoints (Mg2 Connext paywall, Osano, Kargo, HTL ad bidder) and the WordPress '
                             'admin bar (logged-in editors only) are not ours, so they are left out (Karl, 2026-10-14).'},
        'production': rows,
        'websiteRepo': {'copy': '~/Documents/digital-first-media-master-built COPY 20260508 (read-only, 2026-05-08)',
                        'found': REPO_SOURCES},
    }
    p = os.path.join(ROOT, 'tokens', 'breakpoint-inventory.json')
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print('breakpoint inventory: %d values %s' % (len(rows), counts))

if __name__ == '__main__':
    main()
