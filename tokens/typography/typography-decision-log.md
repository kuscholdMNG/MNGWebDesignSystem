# Typography Decision Log

> **Rewritten 2026-09-24.** Simplified from `font-token-audit.md` (Sept 9–10, 2026). The original ran as a session diary and later sections reversed earlier ones. This version keeps only the final outcome of each decision.
> - Current token values: `typography-tokens.md` (this folder).
> - Known Figma-vs-production gaps: `design-vs-production.md` (MNGWebDesignSystem folder).

## Background

On 2026-09-09 the typography tokens in the Figma files were compared against each other and against live production:
- **CRUX Style Library**: full scale, but with a single global serif/sans pairing, no line height or letter spacing, several stale values and some unused steps.
- **MNG Web Design System file (then "UI Style Guide")**: closest to production and the only one that was theme-aware.

Sites checked live: ocregister.com, denverpost.com, chicagotribune.com, orlandosentinel.com, canoncitydailyrecord.com, mcall.com.

## Decisions

1. **One source of truth.** The MNG Web Design System file owns all typography tokens. Karl, 2026-09-09.
2. **CRUX Style Library is never edited.** It stays as read-only reference. That includes its unconfirmed weights (100/200/300/800/900), its unused 32px `3xl`, its stale `headlineH2` weight (400; production is 500) and its fallback-stack mismatch. Standing rule from Karl, 2026-09-10.
3. **Button label sizes** are `Shared/Buttons/Utility|Small|Medium|Large/Size` → 12 / 13 / 14 / 19px, measured live.
4. **Headings follow the theme.** `Editorial/Titles/Display`, `Title`, `Subtitle` and `SectionHeader` use `font/theme/heading-family`, so Modern Earthy correctly gets sans headings and serif body. Subtitle (the deck) is treated as a heading.
5. **Editorial body copy is 16.5px** (`font/size/16-5`), confirmed live on all 6 sites. `font/size/16` is kept for Reader Dashboard only.
6. **Eyebrows are per theme.** There is no single eyebrow size (an earlier "standardize on 20px" decision never shipped). The size, weight and family tokens are:

   | Theme | Size | Weight | Family | Confirmed on |
   |---|---|---|---|---|
   | Bold Coastal | 20px | 400 | Noto Sans | ocregister.com, denverpost.com |
   | Measured Vibrant | 17px | 700 | Noto Sans | chicagotribune.com, orlandosentinel.com |
   | Modern Earthy | 21px | 400 | Noto Serif | mcall.com, canoncitydailyrecord.com |

   The eyebrow family is independent of the heading family (Modern Earthy headings are sans, its eyebrow is serif).
7. **40px is the section-front H1**, e.g. the "Sports" heading on a category page (`class="section-header"`, confirmed on ocregister.com and chicagotribune.com). It is not a kicker label; kickers are 16px/700/uppercase. Added as `Editorial/Titles/SectionHeader`.
8. **New editorial tokens from live checks (2026-09-10, all 6 sites):**
   - `Editorial/Navigation/PrimaryLabel`: Noto Sans / 15px / 600.
   - `Editorial/ModuleHeader`: heading family / 20px / 600.
   - `Editorial/Footer/Copyright`: Noto Sans / 12px / 400.
   - The 30px/600 homepage `h2` is screen-reader-only, so it is not a token.
9. **Reader Dashboard gets its own collection.** "Dashboard Typography" has 14 composites (44 variables). It isn't theme-aware and uses flat Noto Sans / Noto Serif. For Reader Dashboard, **Figma is the source of truth even where production differs**, so `Dashboard/Titles/PageDesktop` is 26px, matching Reader Dashboard v2.0's Figma. Production gaps go to `design-vs-production.md`, not into the tokens.
10. **Near-integer measurements are rounded** to the nearest primitive: ~12.48 → 12, ~14.06 → 14, ~19.2 → 19.
11. **Leftovers left alone:** the legacy `AccuweatherTemp` text style (weather widget only) and a generic, non-Noto type scale on the Fonts page (Frame 56). The latter looks like starter-kit content and is safe to archive if you want.

## Added 2026-09-24

- **Prairie Mountain Publishing sites** (19) load `modernearthy.css`, so they use Modern Earthy typography. Their PMP override changes colors only. Cañon City Daily Record is one of them, which is why it matched Modern Earthy exactly.

- **New styles from a 7-site live check** (ocregister, denverpost, chicagotribune, orlandosentinel, canoncitydailyrecord, mcall, greeleytribune):
  - Card tiers, headline list, related headline and body copy are now Editorial styles. See `typography-tokens.md`.
  - Size, weight, line height and letter spacing were identical on every site, including Modern Earthy.
- **Small headlines get their own per-theme family** (Karl): `font/theme/small-headline-family` = Bold Coastal Sans, Modern Earthy Sans, Measured Vibrant Serif. It's used by CardQuaternary (19px) and HeadlineList (15px).
- **The lead story has two styles** (Karl):
  - `Editorial/Titles/Title` (top of page): 32.8 / -0.87.
  - `Editorial/Titles/TitleMedia` (media block): 33 / -1.16.
  - Title's old averaged -1.0 letter spacing was replaced.

## Still open

- Most tokens aren't yet bound to real text layers in the file. They're a reference catalog for now.
- `font/size/24` has only one uncertain editorial sighting (kept for Reader Dashboard).
- The Fonts page's "Typescale" reference table (node `2946:1136`, Frame 23) still shows Display Headline at 29px; the token is 36px. The table also has a "SECTION HEADER 1COL" row at 21px/400, which matches the Modern Earthy eyebrow.
