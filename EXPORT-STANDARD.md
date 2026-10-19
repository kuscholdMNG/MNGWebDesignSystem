# MNG Web Design System — Export Standard

> **Adopted 2026-10-14** (drafted 2026-10-13; updated 2026-10-14: legacy exports are deleted when replaced, no archive; Fold 340 added to the MNG Device breakpoints; PNG previews stay in GitHub, no Git LFS; where pixel values are kept; Reader Dashboard is part of core; two breakpoint sets; Vite/package note). Every token and component export follows this file; the first build is in `tokens/core/`, `tokens/themes/`, `tokens/wordpress/` and `dist/` (pull request #2). The README's filing rules and the status doc's standing rules point here; if this file and another doc disagree, this file wins for anything about export formats.

## 1. What this covers

Every file that carries design values out of Figma and into code: tokens (color, type, spacing, radius, breakpoints and so on), component exports, and the ready-to-use files built from them for WordPress, React, Tailwind and other code bases.

Direction is **Figma → code**. We do not make files meant to be imported back into Figma.

## 2. Sources of truth

| Question | Source of truth |
|---|---|
| What a value *should* be | Figma (design). Tokens always carry design values, never production values. |
| A color's value | Its **hex** string. RGBA and the DTCG color object are calculated from the hex by the build script and must always match it. |
| Where a value comes from in production | `$extensions.com.mng.production` on the token (site, stylesheet, selector or CSS variable, date verified). |
| Where a value goes to in Figma | `$extensions.com.mng.figma` on the token (file, collection, variable, mode, and which components use it). |
| Production gaps | `production-vs-design-differences.md`. Tokens are never changed to match production. |
| Values that don't fit in Figma | Baltimore Sun and Capital Gazette (over Figma's 20-mode limit) live only in the token files. That is the one place the token file, not Figma, holds the design value. |

## 3. File format

- **Standard:** DTCG (Design Tokens Community Group) Format Module **2025.10**, the first stable version. Themes and site overrides follow the DTCG Resolver Module 2025.10.
- **File names:** `<topic>.tokens.json`, lowercase with hyphens (`color.tokens.json`, `typography-editorial.tokens.json`).
- **Every token has** `$type` (on the token or its group), `$value`, and `$description` where the purpose isn't obvious from the name.
- **Names:** nested groups, lowercase, hyphens inside a segment. Figma's `color/theme/primary` becomes the group path `color` › `theme` › `primary`, written `color.theme.primary` in references. Figma collection names (`Colors/`, `Type Primitives/`) are never part of a token name. Decimals use a hyphen: `font.size.16-5`.
- **References** (aliases) use `{group.token}`, e.g. `"$value": "{color.theme.primary}"`. A composite or component token always references the primitive instead of copying its value.
- **Custom data** goes only in `$extensions.com.mng`. Nothing else is added to `$value`.

### 3.1 Colors

Hex is the source of truth. Each color token carries three forms of the same color:

```json
"primary": {
  "$type": "color",
  "$value": {
    "colorSpace": "srgb",
    "components": [0, 0.4588, 0.502],
    "alpha": 1,
    "hex": "#007580"
  },
  "$extensions": {
    "com.mng": {
      "rgba": "rgba(0, 117, 128, 1)"
    }
  }
}
```

- `hex`: 6 digits, lowercase. **Source of truth.**
- `components`: red, green, blue on a 0–1 scale (hex ÷ 255), rounded to 4 decimals. Generated, never typed by hand.
- `alpha`: 0–1. `1` unless the design uses transparency.
- `rgba`: CSS form, generated from hex + alpha.
- When `alpha` is below 1, `$extensions.com.mng` also carries `hex8` (e.g. `#00000099` for black at 60%) for code bases that want 8-digit hex.

Example with transparency (the Event Card date bar, black at 60%):

```json
"date-bar-background": {
  "$type": "color",
  "$value": {
    "colorSpace": "srgb",
    "components": [0, 0, 0],
    "alpha": 0.6,
    "hex": "#000000"
  },
  "$extensions": {
    "com.mng": {
      "rgba": "rgba(0, 0, 0, 0.6)",
      "hex8": "#00000099"
    }
  }
}
```

A component token that only changes opacity references the base color and states the alpha in `$extensions.com.mng.alpha`; the build script resolves it to the final RGBA.

### 3.2 Dimensions (sizes, spacing, radius, breakpoints)

DTCG 2025.10 writes dimensions as objects:

```json
"200": { "$type": "dimension", "$value": { "value": 16, "unit": "px" } }
```

Design values are in `px`. The build adds `rem` (16px base) in the generated files.

### 3.3 Typography

Composite type tokens use `$type: typography` and reference primitives:

```json
"zone1-headline-mobile": {
  "$type": "typography",
  "$value": {
    "fontFamily": "{font.theme.heading-family}",
    "fontSize": "{font.size.25}",
    "fontWeight": "{font.weight.bold}",
    "lineHeight": 1.16,
    "letterSpacing": { "value": -0.03, "unit": "em" }
  },
  "$extensions": {
    "com.mng": {
      "lineHeightPx": 29,
      "figmaStyle": "Bold"
    }
  }
}
```

- **Line height:** DTCG stores it as a ratio (line height ÷ font size). Figma and our docs use px, so the px value is kept in `lineHeightPx`. The px value is the design value; the ratio is calculated from it.
- **Letter spacing:** stored in `em` (what production CSS uses). Figma shows it as a percent (−3% = −0.03em), kept in `letterSpacingFigma`.
- **Weight vs. style:** code uses `fontWeight` (number). Figma binds the font *style* (`Bold`, `SemiBold`) to avoid Display fonts, so the style name is kept in `figmaStyle`.

### 3.4 Where pixel values are kept

Pixels are the design unit everywhere (Figma's units are CSS pixels; we don't use points).

| Value | In the token (`$value`) | Also kept |
|---|---|---|
| Font size, spacing, radius, border width, breakpoints, ad sizes, container widths | px (`{ "value": 16, "unit": "px" }`) | `dist/`: px and rem |
| Line height | ratio (1.16) | `lineHeightPx` in `$extensions`; `dist/`: ratio and px |
| Letter spacing | em (−0.03) | `letterSpacingFigma` (−3%) in `$extensions`; `dist/`: em and px at the token's font size |
| Frame widths (340, 360, 768…) | not tokens | the component spec (`<slug>.md`) |

## 4. Metadata every token carries

`$extensions.com.mng` holds, where known:

```json
"com.mng": {
  "production": {
    "source": "boldcoastal.css",
    "selector": "body",
    "property": "--primary",
    "sites": ["ocregister.com", "denverpost.com"],
    "verified": "2026-08-03",
    "matches": true,
    "differencesEntry": 21
  },
  "figma": {
    "file": "MNG Web Design System",
    "collection": "Colors",
    "variable": "color/theme/primary",
    "mode": "BoldCoastal",
    "usedBy": ["Button Primary", "Button Linkstyle", "Event Card"]
  }
}
```

- `production`: where the value comes from in production. `matches: false` means production differs; the fix is in `production-vs-design-differences.md` (`differencesEntry`).
- `figma`: where the value goes to in Figma: the variable it lives in and the components that use it. The Figma file a value was first designed in isn't recorded.
- Tokens that exist in production but not in Figma yet get `"figma": null` and a note.

## 5. Layers and folders

Tokens and components are split into layers. **A layer may only reference layers above it in this list**; core never references WordPress.

| Layer | Folder | What's in it |
|---|---|---|
| Core (the main MNG Web Design System) | `tokens/core/` | Color primitives (gray, feedback, neutral, surface, tributes), type primitives (`font.family`, `font.size`, `font.weight`), spacing, radius, official breakpoints. Shared by every platform. **Reader Dashboard is part of core**: when it's ready, its tokens (Dashboard Typography, its breakpoints and so on) are added here under a `dashboard` group, not as a separate layer. |
| Themes | `tokens/themes/` | One file per theme (Bold Coastal, Measured Vibrant, Modern Earthy), sub-theme (Denver Post, NEPA-PMP, 21C Michigan…) and the site overrides, plus `mng.resolver.json` that says how they stack: theme → sub-theme → site. |
| WordPress | `tokens/wordpress/` | The WordPress Elements sub-system: editorial type styles (`Editorial/...`), theme type tokens (`font.theme.*`, eyebrow), layout and container widths, ad slot sizes, homepage block tokens, WordPress-specific breakpoints. |

Components follow the same split:

```
components/
  core/<slug>/          ← buttons, form fields, modals, icons, InLineMessage; Reader Dashboard components later
  wordpress/<slug>/     ← masthead, cards, homepage blocks, ad blocks, footer, breaking news
```

Non-token assets go in `assets/` (`assets/icons/`, `assets/logos/`). Generated files go in `dist/` (§8).

Placement follows **where the value is used in production**, not which Figma file it sits in. Example: the `Editorial/...` type styles live in the main Figma file but are WordPress-only, so they go in `tokens/wordpress/`.

## 6. Breakpoints

Two different things are both called breakpoints. They are kept apart:

- **Frame widths** (340, 360, 768, 1024, 1100, 1280): the widths Figma mock-ups are drawn at. They're documentation, recorded in component specs, **not tokens**.
- **Breakpoints:** the widths where a layout actually changes (CSS `min-width` boundaries). These are tokens (`$type: dimension`).

Breakpoints come in three tiers:

1. **Official.** Design values; like colors, an official breakpoint never changes to match production. There are two sets for now:

   | Set | Tokens | Values (min-width) | Used by | Future |
   |---|---|---|---|---|
   | **MNG Device breakpoints** (`tokens/core/`) | `breakpoint.fold`, `breakpoint.mobile`, `breakpoint.tablet`, `breakpoint.tablet-landscape`, `breakpoint.desktop` | 340, 360, 768, 1024, 1280. Fold (340) is the smallest supported width (Karl, 2026-10-14). | Reader Dashboard today; every product eventually | The one system-wide set |
   | **WordPress grid breakpoints** (`tokens/wordpress/`) | `breakpoint.wordpress-grid.xs`, `.s`, `.m`, `.l`, `.xl` | 320, 640, 800, 1040, 1280. The masthead switches to desktop at `l`. | WordPress themes, including Obituaries (from `_grid-variables.scss`) | Legacy; retired when WordPress moves to the Device set |

   The Device set matches the Figma screen widths one to one (Fold 340, Mobile 360, Tablet 768, Tablet horizontal 1024, Desktop 1280). Its token names deliberately differ from the WordPress grid names and from the Masthead's `Device` labels (`MD-TabletV (640–799px)` and so on), because those carry WordPress ranges. Each Device token records its Figma frame width in `$extensions.com.mng.figma.frameWidth`.
2. **Component breakpoints:** an intended one-off used by a single component goes in that component's `<slug>.tokens.json`, not in the system set.
3. **Production drift:** any other production breakpoint is logged in `production-vs-design-differences.md` with the official breakpoint it should snap to. Reader Dashboard must match the Device set (open questions: entry 30). Obituaries is part of the WordPress layer and must match the WordPress grid (drift: entry 31).

The full list of production breakpoints and how each is classified lives in `tokens/breakpoint-inventory.json` (built from the website repo and a CSS scan of the 6 review sites).

## 7. Component exports

Each component or assembly gets one folder: `components/<layer>/<slug>/`

| File | What it is |
|---|---|
| `<slug>.md` | The spec: purpose, anatomy, variants, states, sizes, behavior per breakpoint, accessibility, production references, known issues. |
| `<slug>.tokens.json` | DTCG component tokens that reference system tokens, e.g. `button.primary.background.hover` → `{color.theme.primary-light}`. Includes component-only breakpoints. |
| `<slug>.html` | HTML/CSS skeleton using the `dist/` CSS variables. |
| `previews/` | PNG previews, committed to GitHub as normal files (no Git LFS). Re-render and commit only the previews that changed. |

Each component folder's `.tokens.json` records the Figma component set it maps to (`$extensions.com.mng.figma.node`) and the production selector it matches (`$extensions.com.mng.production.selector`).

**Not allowed going forward:** Figma layer trees, raw Figma fills and strokes, Figma variable collection paths as keys (`Colors/color/gray/min`), or custom `schema` formats (`mng/tokens@1`, `mng-design-system/tokens@1`). Figma node IDs appear only inside `$extensions.com.mng.figma`.

## 8. Ready-to-use files (`dist/`)

Built from the DTCG files by `scripts/build-tokens/`. **Never edited by hand.** Rebuilt and committed with every token change.

| Folder | For | Contents |
|---|---|---|
| `dist/css/` | WordPress (classic), any web code | `core.css` (`:root`), one file per theme and sub-theme, `sites/<domain>.css` overrides scoped to `#page`. |
| `dist/scss/` | WordPress themes using Sass | The same values as Sass variables and maps. |
| `dist/js/` | React and other JS | ES module + TypeScript types (`tokens.js`, `tokens.d.ts`). |
| `dist/tailwind/` | Tailwind | v4 `@theme` CSS file and a v3 preset (`tailwind.preset.js`). |
| `dist/wordpress/` | WordPress block themes | `theme.json` fragments: color palette, font sizes, font families, spacing sizes and custom values, one per theme. |
| `dist/json/` | Anything else | Flat `name → value` JSON (hex, rgba, px). |

- `dist/` is also a package: a `package.json` at the repo top level with `exports`, so Vite, webpack or any Node build can install it straight from GitHub (`npm install github:kuscholdMNG/MNGWebDesignSystem`) and import `mng_web_design_system/css/core.css`, `.../js/tokens.js` or `.../tailwind/theme.css`. The Tailwind v4 file works with Tailwind's Vite plugin as is.
- CSS variable names: `--mng-` + the token path with hyphens (`--mng-color-theme-primary`, `--mng-font-size-16-5`, `--mng-spacing-200`).
- Colors are written as hex when alpha is 1, and as `rgba()` when it's below 1.
- Sizes are written in `px`, with `rem` versions where the format supports them.

## 9. Legacy exports

`figma-exports/` (the 2026-09 to 2026-10-09 exports) is legacy: not updated, and **deleted folder by folder** as each component gets a new export under `components/`. Old versions aren't kept, not even in an archive folder, while the formats are being settled; git history keeps them (Karl, 2026-10-14). The buttons export was deleted on 2026-10-14.

## 10. Checks before committing

`scripts/validate/` (to be built) runs before every commit and in GitHub on every push. It fails when:

- a `.tokens.json` file isn't valid DTCG 2025.10, or a reference doesn't resolve;
- a color's `components`, `rgba` or `hex8` don't match its hex;
- a layer references a layer below it (e.g. core → WordPress);
- `dist/` is out of date with the token files;
- a non-DTCG token JSON, `.DS_Store`, `__pycache__`, zip or copy-suffixed file (`file (1).md`) is added.

## 11. Changing values

Token value changes, new official breakpoints and changes to this standard go on a `review/...` branch with a pull request for Karl. Adding metadata, rebuilding `dist/` from unchanged values, or new legacy notes can go straight to `main`.
