# MNG icon font

> **Updated 2026-10-08:** reorganized to match the Figma "Icon Categories" page and checked against it glyph by glyph. First extracted 2026-10-08.

The production `icomoon` icon font, documented the way the design system documents it: the six categories, names and descriptions from the Figma **Icon Categories** frame (MNG Web Design System › Icons | 2026.08.28, node `1412:13`). **All MNG sites use the same icon font** (Karl, 2026-10-08). Figma is the source of truth; differences in production are in `design-vs-production.md` entry 10.

## Files

| File | What it is |
|---|---|
| `icomoon.ttf` | The exact production font (32,944 bytes), from the `@font-face` in ocregister.com's `boldcoastal.css` |
| `icomoon.woff`, `icomoon.woff2` | Web versions converted from the TTF with fontTools (same glyphs) |
| `icomoon.css` | `@font-face` plus one class per documented icon, named as in Figma (`icon-close`, `icon-menu7`, `icon-content-copy`…), each pointing at the design-correct glyph. Where production's class differs, a comment says so. |
| `icons.json` | The full map: category, Figma name, class, description, codepoint, production class and status for 171 icons; the known-missing list; production-only classes |
| `svg-missing/` | Figma artwork for the 12 icons that aren't in the font yet |
| `preview.html` | Every icon by category with its status, plus the known-missing icons |
| `preview.png` | Every glyph actually in the font, by codepoint (174) |

## Status of the 171 documented icons

- **162 match**: the production class has the same name and glyph.
- **4 named differently in production** (same glyph): `home` → `icon-home3`, `menu7` → `icon-hamburger`, `enlarge7` → `icon-enlarge`, "iTunes / Apple Music" → `icon-music5`.
- **3 production classes show the wrong glyph** (the right glyph is in the font): `grid2` → U+E932, `windows8` → U+E987, `book3` → U+E993.
- **2 have no production class** (the glyph is in the font): `content_copy` → U+E921, `ios_share` → U+E93A.

## Known missing from the font

From the Figma page's Pending Updates section: plus-circle, plus-circle2, minus-circle, minus-circle2, list, grid, crown, giving-hand, yield-filled, yield-outline (ADD); notification-outlines and notification-filled (CHANGE, replacing notification and notification2). Their Figma artwork is in `svg-missing/`.

## Not included

- Third-party vendor icons (cookies, weather, commenting) and the "Need to source/make/add" list (Obituary, Funeral Home, Find Your School): out of scope for this package.
- Payment marks (Visa, AmEx, Apple Pay…): kept out of the icon font on purpose (see `components/icons.md`).
- Production-only classes with no Figma entry: `icon-google-plus` (no glyph), `icon-mng-podcast1` (duplicate of android), `icon-users4` (duplicate of user4). Listed in `icons.json`.

## How it was made

The TTF was saved from the live OC Register page in Chrome (ocregister.com can't be fetched directly from Claude's sessions). Production class → codepoint pairs come from the theme CSS (`.icon-X::before { content: var(--icon-X) }`). Every Figma icon was rendered next to its production glyph to confirm the match. More history: `components/icons.md`.
