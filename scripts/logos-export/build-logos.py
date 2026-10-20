#!/usr/bin/env python3
"""
Build the transparent SVG newspaper logos in logos/ from the Marketing logo
artwork (Illustrator .ai files, which are PDF-compatible).

Inputs
  --source   the 'Completed Market Logos' folder downloaded from Drive
             (https://drive.google.com/drive/folders/1luw8jc2lUoAHwbbOCokgacO_nzDLm7Vi).
             Only its 'Master Logos' sub-folder is read.
  --repo     the mng_web_ds repo root (default: two folders up from this script).
  sources.json (next to this script): which file and artboard each publication uses.

  figma-placeholders.json (next to this script): vector data of the 'FAKE NEWSPAPER LOGOS'
             placeholder set, read from Figma by extract-placeholders.js.

Outputs (all under <repo>/logos/)
  publications/<slug>/<slug>--horizontal--black.svg   black ink, transparent background
  publications/<slug>/<slug>--horizontal--white.svg   white ink, transparent background
  placeholder/<slug>/<slug>--<layout>--<black|white>.svg   fake logos for mock-ups
  logos.json                                          manifest (see logos/README.md)

How it works
  Every .ai file has two layers: 'Paste Board Elements' (the background box the
  designers place behind the logo) and 'Art' (the logo itself). The artboard is saved
  as a one-page PDF with only 'Art' switched on, converted with pdftocairo (which keeps
  Illustrator's clipping masks), any full-artboard rectangle is dropped, and every fill
  is set to currentColor; the root <svg color="..."> holds the ink colour (black or
  white). The viewBox is cropped tight to the visible ink, so there is no padding.

Requires: pdftocairo (poppler), pymupdf, cairosvg, Pillow.
Run:      python3 scripts/logos-export/build-logos.py --source "<path to Completed Market Logos>"
"""
import argparse, csv, html, io, json, os, re, subprocess, tempfile, unicodedata
from datetime import date

import cairosvg
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
INK = {"black": "#000000", "white": "#FFFFFF"}


def slugify(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return s


def fmt(v):
    s = f"{v:.3f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def isolate_art(src, page_no, tmp_pdf):
    """Save a one-page PDF of the artboard with only the 'Art' layer switched on."""
    doc = pymupdf.open(src)
    ocgs = doc.get_ocgs()
    on = [x for x, v in ocgs.items() if v["name"] == "Art"]
    off = [x for x, v in ocgs.items() if v["name"] != "Art"]
    if ocgs:
        doc.set_layer(-1, on=on, off=off)
    doc.select([page_no - 1])
    doc.save(tmp_pdf, garbage=3)
    page = pymupdf.open(tmp_pdf)[0]
    cols = set()
    for dr in page.get_drawings():
        if dr.get("fill") is not None and dr.get("layer") in ("Art", None):
            cols.add("#%02x%02x%02x" % tuple(round(c * 255) for c in dr["fill"]))
    return page.rect.width, page.rect.height, sorted(cols)


NUM = r"-?[0-9.]+"


def is_background(d, W, H):
    """A path that is just one rectangle covering (almost) the whole artboard."""
    if re.search(r"[CcQqAa]", d):
        return False
    nums = [float(n) for n in re.findall(NUM, d)]
    if len(nums) < 8 or len(nums) > 12:
        return False
    xs, ys = nums[0::2], nums[1::2]
    return (max(xs) - min(xs)) >= W * 0.97 and (max(ys) - min(ys)) >= H * 0.95


def cairo_svg(tmp_pdf, W, H, slug):
    """pdftocairo keeps Illustrator's clipping masks, which a raw path dump would lose."""
    raw = subprocess.run(["pdftocairo", "-svg", "-noshrink", "-nocenter", tmp_pdf, "-"], check=True, capture_output=True).stdout.decode()
    raw = re.sub(r"<\?xml[^>]*>\s*", "", raw)
    # drop background boxes (never inside <clipPath>, where a full-artboard rectangle is the clip)
    def drop_bg(m):
        d = re.search(r'\sd="([^"]*)"', m.group(0))
        return "" if (d and is_background(d.group(1), W, H)) else m.group(0)
    parts = re.split(r"(<clipPath\b.*?</clipPath>)", raw, flags=re.S)
    raw = "".join(p if p.startswith("<clipPath") else re.sub(r"<path\b[^>]*/>", drop_bg, p) for p in parts)
    # one ink colour, set on the root so a recolour is a single edit
    # (poppler writes colours as attributes or, in older versions, inside style="")
    raw = re.sub(r'\s(fill|stroke)="rgb\([^)]*\)"', lambda m: f' {m.group(1)}="currentColor"', raw)
    raw = re.sub(r'(fill|stroke):\s*rgb\([^)]*\)', lambda m: f'{m.group(1)}:currentColor', raw)
    raw = re.sub(r'\s(fill|stroke)-opacity="1"', "", raw)
    # unique ids so several logos can be inlined on one page
    raw = re.sub(r'id="([^"]+)"', lambda m: f'id="{slug}-{m.group(1)}"', raw)
    raw = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{slug}-{m.group(1)})', raw)
    raw = re.sub(r'xlink:href="#([^"]+)"', lambda m: f'xlink:href="#{slug}-{m.group(1)}"', raw)
    body = raw[raw.index(">", raw.index("<svg")) + 1: raw.rindex("</svg>")].strip()
    return body


def ink_bbox(body, W, H):
    """Tight bounds of the visible ink (after clipping), in artboard units."""
    k = min(8.0, 8000.0 / max(W, H))
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W*k}" height="{H*k}" color="#000">{body}</svg>'
    png = cairosvg.svg2png(bytestring=svg.encode())
    from PIL import Image
    im = Image.open(io.BytesIO(png)).convert("RGBA")
    box = im.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
    if not box:
        return None
    x0, y0, x1, y1 = box
    return (max(0, x0 / k), max(0, y0 / k), min(W, x1 / k), min(H, y1 / k))


def write_svg(path, body, bbox, ink, title):
    x0, y0, x1, y1 = bbox
    w, h = x1 - x0, y1 - y0
    title = html.escape(title, quote=True)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
           f'viewBox="{fmt(x0)} {fmt(y0)} {fmt(w)} {fmt(h)}" width="{fmt(w)}" height="{fmt(h)}" '
           f'color="{ink}" role="img" aria-label="{title}">\n<title>{title}</title>\n{body}\n</svg>\n')
    with open(path, "w") as f:
        f.write(svg)
    return round(w, 2), round(h, 2)


def build_placeholders(repo):
    """Fake logos for mock-ups, from the Figma vector data (no Illustrator source)."""
    src = os.path.join(HERE, "figma-placeholders.json")
    if not os.path.exists(src):
        return []
    data = json.load(open(src))
    out = []
    for slug, brand in data["brands"].items():
        entry = {"slug": slug, "name": brand["name"], "placeholder": True}
        for layout, v in brand["layouts"].items():
            b = [p["bounds"] for p in v["paths"]]
            bbox = (min(x[0] for x in b), min(x[1] for x in b), max(x[2] for x in b), max(x[3] for x in b))
            body = "\n".join(
                f'<path transform="translate({fmt(p["x"])} {fmt(p["y"])})" d="{vp["d"]}"'
                + (' fill-rule="evenodd"' if vp["w"] == "EVENODD" else "") + ' fill="currentColor"/>'
                for p in v["paths"] for vp in p["vp"])
            os.makedirs(os.path.join(repo, "logos", "placeholder", slug), exist_ok=True)
            files = {}
            for name, ink in INK.items():
                fn = f"{slug}--{layout}--{name}.svg"
                w, h = write_svg(os.path.join(repo, "logos", "placeholder", slug, fn), body, bbox, ink, brand["name"] + " (placeholder)")
                files[name] = f"placeholder/{slug}/{fn}"
            entry[layout] = {"files": files, "width": w, "height": h, "aspect_ratio": round(w / h, 4),
                             "source": f"Figma {data['file']} node {v['figma_node']} ({v['figma_frame']})"}
        out.append(entry)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--repo", default=os.path.abspath(os.path.join(HERE, "..", "..")))
    a = ap.parse_args()
    master = os.path.join(a.source, "Master Logos")
    cfg = json.load(open(os.path.join(HERE, "sources.json")))
    sites = {r["publication"]: r for r in csv.DictReader(open(os.path.join(a.repo, "tokens/colors/mng-colors-sites.csv"), encoding="utf-8"))}

    entries = [dict(e, in_color_tokens=True) for e in cfg["publications"]]
    used = {e["src"] for e in entries}
    # every other PageSuite file (sub-market weeklies that aren't in the color tokens)
    for folder in sorted(os.listdir(master)):
        fp = os.path.join(master, folder)
        if not os.path.isdir(fp):
            continue
        for fn in sorted(os.listdir(fp)):
            rel = f"{folder}/{fn}"
            if fn.endswith("_PageSuite.ai") and rel not in used:
                entries.append({"publication": folder, "src": rel, "page": 2, "in_color_tokens": False})

    outdir = os.path.join(a.repo, "logos", "publications")
    manifest, problems = [], []
    tmpdir = tempfile.mkdtemp(prefix="logos-")
    for e in entries:
        pub = e["publication"]
        slug = slugify(pub)
        tmp_pdf = os.path.join(tmpdir, slug + ".pdf")
        W, H, cols = isolate_art(os.path.join(master, e["src"]), e["page"], tmp_pdf)
        body = cairo_svg(tmp_pdf, W, H, slug)
        bbox = ink_bbox(body, W, H)
        if not bbox:
            problems.append(f"{pub}: no artwork on artboard {e['page']} of {e['src']}")
            continue
        os.makedirs(os.path.join(outdir, slug), exist_ok=True)
        files = {}
        for name, ink in INK.items():
            fn = f"{slug}--horizontal--{name}.svg"
            w, h = write_svg(os.path.join(outdir, slug, fn), body, bbox, ink, pub)
            files[name] = f"publications/{slug}/{fn}"
        site = sites.get(pub, {})
        manifest.append({
            "slug": slug,
            "publication": pub,
            "domain": site.get("domain") or None,
            "cluster": site.get("cluster") or None,
            "theme": site.get("theme") or None,
            "in_color_tokens": e["in_color_tokens"],
            "horizontal": {
                "files": files,
                "width": w, "height": h, "aspect_ratio": round(w / h, 4),
                "source": f"Master Logos/{e['src']}",
                "artboard": e["page"],
                "source_ink": sorted(cols),
            },
            **({"note": e["note"]} if e.get("note") else {}),
        })

    manifest.sort(key=lambda m: (not m["in_color_tokens"], m["publication"].lower()))
    out = {
        "_about": "Newspaper logo manifest. Built by scripts/logos-export/build-logos.py; see logos/README.md.",
        "generated": date.today().isoformat(),
        "variants": {"horizontal": ["black", "white"]},
        "placeholder_variants": {"layouts": ["horizontal", "stacked", "stacked-tall", "lettermark"], "colors": ["black", "white"]},
        "count": len(manifest),
        "in_color_tokens": sum(m["in_color_tokens"] for m in manifest),
        "missing": cfg["missing"],
        "logos": manifest,
        "placeholders": build_placeholders(a.repo),
    }
    with open(os.path.join(a.repo, "logos", "logos.json"), "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"{len(manifest)} logos ({out['in_color_tokens']} in color tokens), {len(cfg['missing'])} missing")
    for p in problems:
        print("PROBLEM:", p)


if __name__ == "__main__":
    main()
