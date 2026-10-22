#!/usr/bin/env python3
"""Rebuild tokens/icons/icomoon.css and tokens/icons/preview.html from tokens/icons/icons.json.

icons.json is the source: edit it, then run `python3 scripts/icon-font/build.py` from the repo root.
"""
import html, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ICONS = ROOT / "tokens" / "icons"
d = json.loads((ICONS / "icons.json").read_text())

def cp(icon):
    return icon["codepoint"][2:].lower()

# ---- icomoon.css -------------------------------------------------------------
css = [
    "/* MNG icon font — one class per icon, named by its production class (Karl, 2026-10-22).",
    " * Font: production icomoon (identical on every MNG site), extracted 2026-10-08.",
    " * Generated from icons.json by scripts/icon-font/build.py. Don't edit by hand. */",
    "@font-face{font-family:'icomoon';src:url('icomoon.woff2') format('woff2'),url('icomoon.woff') format('woff'),url('icomoon.ttf') format('truetype');font-weight:normal;font-style:normal;font-display:block}",
    "[class^='icon-'],[class*=' icon-']{font-family:'icomoon'!important;speak:never;font-style:normal;font-weight:normal;font-variant:normal;text-transform:none;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}",
]
seen = set()
for cat in d["categories"]:
    css.append(f"\n/* {cat} */")
    for i in d["icons"]:
        if i["category"] != cat or i["class"] in seen:
            continue
        seen.add(i["class"])
        note = ""
        if i["status"] == "production-class-wrong-glyph":
            note = f"  /* production's {i['class']} shows the wrong glyph; this is the design glyph */"
        elif i["status"] == "no-production-class":
            note = "  /* no production class yet */"
        if i.get("layers"):  # multicolor mark: one span per layer
            css.append(f'.{i["class"]}{{position:relative;display:inline-block}}')
            for n, layer in enumerate(i["layers"], 1):
                shift = "" if n == 1 else ";margin-left:-1em"
                css.append(f'.{i["class"]} .path{n}::before{{content:"\\{layer["codepoint"][2:].lower()}";color:{layer["color"]}{shift}}}')
            continue
        selectors = ", ".join(f".{c}::before" for c in [i["class"]] + [a for a in i.get("aliases", [])])
        css.append(f'{selectors}{{content:"\\{cp(i)}"}}{note}')
(ICONS / "icomoon.css").write_text("\n".join(css) + "\n")

# ---- preview.html ------------------------------------------------------------
BLUE, RED, AMBER = "#0057FF", "#D91A1A", "#B36B00"

def source_line(i):
    if i.get("artworkSource") == "custom":
        return f'<b style="color:{BLUE}">Custom</b>'
    return f'<small>IcoMoon: {html.escape(i.get("icomoonName", i["name"]))}</small>'

def glyph_spans(i):
    return "".join(f'<span class="path{n}"></span>' for n in range(1, len(i.get("layers", [])) + 1))

def svg(path):
    return (ICONS / path).read_text().strip()

out = [
    '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MNG Icon Font</title>',
    '<link rel="stylesheet" href="icomoon.css"><style>',
    ":root{--fg:#141414;--muted:#5E5D5C;--line:#CCCAC7;--bg:#fff}",
    'body{font:14px/1.4 "Noto Sans",system-ui,sans-serif;margin:24px;color:var(--fg);background:var(--bg)}h1{font-size:22px}h2{font-size:17px;margin:28px 0 10px}',
    ".grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:8px}figure{margin:0;border:1px solid var(--line);border-radius:4px;padding:12px 6px;text-align:center}",
    ".g{font-size:32px;height:36px;display:flex;align-items:center;justify-content:center;margin-bottom:8px}.g svg{width:32px;height:32px}",
    "figcaption{font-size:12px;word-break:break-word}small{color:var(--muted)}em{color:var(--muted);font-style:normal;font-size:11px}b{font-size:11px}</style>",
    '<h1>MNG icon font</h1><p>Organized like the Figma "Icon Categories" page (MNG Web Design System, 1412:13). Every icon is named by its production class. '
    'Glyphs are the production <code>icomoon</code> font, the same on every MNG site. '
    f'Under each name: <small>IcoMoon: name</small> = original IcoMoon artwork and its name in IcoMoon; <b style="color:{BLUE}">Custom</b> = MNG artwork. '
    f'Badges: <b style="color:{RED}">wrong glyph</b> = production class shows the wrong icon, <b style="color:{AMBER}">no class</b> = glyph exists but production has no class, '
    f'<b style="color:{BLUE}">new artwork pending</b> = replaced in the next font build. Hover a tile for the note.</p>',
]
for cat in d["categories"]:
    out.append(f'<h2>{html.escape(cat)}</h2><div class="grid">')
    for i in (x for x in d["icons"] if x["category"] == cat):
        badges = []
        if i["status"] == "production-class-wrong-glyph":
            badges.append(f'<b style="color:{RED}">wrong glyph</b>')
        if i["status"] == "no-production-class":
            badges.append(f'<b style="color:{AMBER}">no class</b>')
        if i.get("pendingChange"):
            badges.append(f'<b style="color:{BLUE}">new artwork pending</b>')
        title = i.get("note") or (i.get("pendingChange") or {}).get("note", "")
        desc = f'<br><em>{html.escape(i["description"])}</em>' if i.get("description") else ""
        out.append(
            f'<figure title="{html.escape(title)}"><div class="g"><i class="{i["class"]}">{glyph_spans(i)}</i></div>'
            f'<figcaption>{html.escape(i["name"])}<br>{source_line(i)}<br><small>{i["class"]} {i["codepoint"]}</small>{desc}'
            + "".join("<br>" + b for b in badges) + "</figcaption></figure>")
    out.append("</div>")
nb = d["nextFontBuild"]
out.append(f'<h2>Next font build (not in production yet)</h2><p>{html.escape(nb["source"])} Artwork from <code>svg-missing/</code>.</p><div class="grid">')
for i in d["icons"]:
    if i.get("pendingChange"):
        pc = i["pendingChange"]
        out.append(f'<figure title="{html.escape(pc["note"])}"><div class="g">{svg(pc["artwork"])}</div><figcaption>{html.escape(i["name"])}<br>'
                   f'<b style="color:{BLUE}">Custom</b><br><small>{i["class"]} {i["codepoint"]}</small><br><em>New artwork, same class</em></figcaption></figure>')
for i in nb["add"]:
    out.append(f'<figure><div class="g">{svg(i["artwork"])}</div><figcaption>{html.escape(i["name"])}<br>{source_line(i)}<br>'
               f'<small>{i["class"]} {i["codepoint"]}</small><br><em>Add</em></figcaption></figure>')
out.append("</div></html>")
(ICONS / "preview.html").write_text("\n".join(out) + "\n")
print(f"icomoon.css: {len(seen)} classes; preview.html: {len(d['icons'])} icons + next build")
