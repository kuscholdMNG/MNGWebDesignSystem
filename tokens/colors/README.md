# MNG Web Design System: Color Tokens (portable export)

> **2026-10-14:** the DTCG 2025.10 color tokens now live in `tokens/core/color.tokens.json` (primitives) and `tokens/themes/` (one file per theme, sub-theme and product, site overrides in `tokens/themes/sites/`, stacking in `mng.resolver.json`), with hex + color object + RGBA. Ready-to-use files are in `dist/`. This folder stays as the input for `scripts/build-tokens/make-tokens.py` (publications, sites, production audit) and for the CSV and decision log until step 5 of the export cleanup deletes it.

Generated 2026-10-01 from the MNG Web Design System Figma file (`jFHYqhZbJjvWQmDI4myCsd`): the Colors collection (`3749:16`, 20 modes) plus the Color Pallets | 2026.09.10 style guides. Covers **97 publications** and **23 themes / sub-themes**, including the three that don't fit Figma's 20-mode limit (The Baltimore Sun, Capital Gazette and, since 2026-10-15, Daily Herald).

| File | Use |
|---|---|
| `mng-colors.tokens.json` | **Source of truth.** W3C Design Tokens (DTCG) format. Works with Style Dictionary v4, Tokens Studio, Specify and Supernova. |
| `mng-colors.css` | CSS custom properties. Set `data-mng-site="domain"` (or `data-mng-theme="key"`) on `<html>`. |
| `mng-colors-sites.csv` | One row per publication: cluster, theme, sub-theme, resolved hex values, site overrides and the fixes Engineering needs to make. For Sheets and reviews. |
| `color-tokens-decision-log.md` | Why tokens were added, renamed, removed or excluded. |

## How a publication gets its colors

**Theme → sub-theme → site override.**

1. **Theme:** the shared WordPress theme file the site loads: Bold Coastal (`boldcoastal.css`), Modern Earthy (`modernearthy.css`) or Measured Vibrant (`measuredvibrant.css`).
2. **Sub-theme (optional):** a publication or group color ramp on top of the theme. Examples: Denver Post, Morning Call, NEPA-PMP (the `site-pmp` stylesheet on PMP sites, each NEPA site's own plugin stylesheet), 21C Michigan. Most come from the WordPress Customizer, scoped to `div#page`.
3. **Site override (optional):** single values set for one site, e.g. `subsite-custom` / `subsite-text`, or a **documented exception** such as Greeley Tribune's primary, light and dark. Exceptions are accepted differences, not mismatches: they're noted under the sub-theme's style guide in Figma, without red outlines, and need no fix.

Every site row in the JSON, CSS and CSV shows its theme and sub-theme.

## Structure (tokens.json)

- `color.gray / feedback / neutral / surface / tributes`: shared global colors.
- `color.theme.<key>`: 10 tokens per theme or sub-theme (`primary-lighter` … `tertiary`, plus `near-black`, `white`, `nav-text`, and `subsite-custom` where design defines it).
  - `$extensions.com.mng` holds `level` (theme / sub-theme), `parentTheme`, `loads` (theme files), `figmaMode` (`null` = not in Figma), `productionAudit` date, `mismatches` (the Figma red-dashed callouts, each with design value, production value and fix) and `sites`.
- `site.<domain-slug>`: each publication's tokens, as aliases to its theme / sub-theme, plus literal site overrides. Slugs replace dots with dashes (dots break DTCG alias paths).
  - `$extensions.com.mng` holds publication, cluster, theme, subTheme, `mismatchCount` (fixes Engineering needs to make), `fixesFrom` (where those fixes live) and `exceptions` (documented site differences that need no fix).

## Design vs. production

Token values are always the **design (should-be)** values. Production is never copied into tokens. When production differs, Figma marks the production row with a red-dashed outline and the gap is listed in **entry 21 of `production-vs-design-differences.md`** (project root: every fix grouped by theme / sub-theme, with the publications affected) and in the JSON/CSV.

- **Documented exceptions** (currently only Greeley Tribune) are part of the design, so their values are in the tokens and they have no red outline.
- **The Baltimore Sun** uses its documented Figma styles as is. No production comparison is tracked for it.

## Changes on 2026-10-15

- **New sub-theme: Daily Herald** (dailyherald.com), on Modern Earthy. Primary `#0072b4` (Karl); the rest of the ramp was extrapolated from it (see the decision log, §11). Not a Figma mode (20-mode limit): the spec is the "Daily Herald — Style Guide" section on the Color Pallets page. The site still runs on Everyware, so there is no production audit yet.

## Changes on 2026-10-01

- **NEPA joins PMP as one sub-theme, NEPA-PMP.** The 5 NEPA sites (Citizens' Voice, Times-Tribune, Wyoming County Examiner, Republican Herald, Standard-Speaker) load `modernearthy.css` plus their own site plugin, which sets the same colors on `body` as PMP. Verified live, along with matching type. They moved from plain Modern Earthy (4 fixes) to NEPA-PMP (2 fixes). The sub-theme key changed from `prairie-mountain-publishing` to `nepa-pmp` (CSS `data-mng-theme="nepa-pmp"`); the Figma mode and style guide are now named NEPA-PMP.
- **Disputed sites verified live:** Daily Press and New York Daily News run Measured Vibrant, GrowthSpotter runs Measured Vibrant with its own ramp, and The Morning Call runs Modern Earthy with its own override, all as in Figma. No sites are left waiting on a live check.

## Changes on 2026-09-30

- **`mng-colors-engineering-fixes.md` retired.** Its full fix list now lives in entry 21 of `production-vs-design-differences.md`, the single Engineering handoff doc.
- **Greeley Tribune's overrides are a documented exception, not a mismatch.** Its `div#page` values (primary `#536e7f`, light `#5b7b8b`, dark `#44687f`) are now its site tokens. The red outlines were removed in Figma, and the note sits under the PMP style guide. No Engineering fix for those three tokens.
- **Hartford Courant verified live (2026-09-25):** it runs **Measured Vibrant** (`measuredvibrant.css` + `site-tribune` style.min.css) with a `div#page` override. It's now a sub-theme of Measured Vibrant, and its production values match the Figma style guide.
- **The Baltimore Sun:** uses its documented Figma styles as is; the "needs a spec" follow-up was dropped.

## Changes on 2026-09-25

- **Greeley Tribune is no longer its own theme.** Its Figma mode became **Prairie Mountain Publishing**, and the Greeley Tribune style guide was removed. greeleytribune.com is a PMP site (see 2026-09-30 for its exception).
- **PMP now uses the Measured Vibrant should-be values** and is a Figma mode (it had lived only in the export). Production still differs on `primary-lighter` (not set, falls back to `#47b6ff`) and `tertiary` (`#303f9f`, should be `#eb5300`).
- Every publication now lists its theme, sub-theme and engineering fixes. Theme keys are unchanged, except `greeley-tribune` is gone.

## Rebuild

```
npx style-dictionary@4 build   # point `source` at mng-colors.tokens.json
```
