# Design vs. Production — Engineering Handoff

**Purpose:** A running list of every place live production has been found diverging from the Figma design-system spec, or where something was explicitly flagged as needing engineering (or legal) attention. Figma is the source of truth for these systems; when production disagrees, the fix belongs here as an engineering item rather than being silently absorbed into design tokens. Each entry says where the drift is, what Figma says vs. what's live, and what engineering should do about it.

**Color fixes checklist (Google Sheet, one row per fix with a Done checkbox):** [MNG color fixes checklist](https://docs.google.com/spreadsheets/d/17oRvVmGWZgnfvKzupvgX7SEtA9b-uK6guqyufM4bxBk/edit). The same rows are in `tokens/colors/mng-colors-fixes.csv`.

**Contents**

- **Icons**
  - [1. Icon font — mismatches with the Figma icon page, dead and duplicate glyphs, and known missing icons](#1-icon-font--mismatches-with-the-figma-icon-page-dead-and-duplicate-glyphs-and-known-missing-icons)
- **Fonts and typography**
  - [2. Font fallbacks — Helvetica instead of the design stacks (all sites)](#2-font-fallbacks--helvetica-instead-of-the-design-stacks-all-sites)
  - [4. Reader Dashboard — Typography (2026-09-10)](#4-reader-dashboard--typography-2026-09-10)
  - [5. Upcoming Events (CitySpark widget) — font family](#5-upcoming-events-cityspark-widget--font-family)
  - [6. Article breadcrumbs — label font family and text color](#6-article-breadcrumbs--label-font-family-and-text-color)
- **Colors**
  - [7. Color Tokens — Universal Grays and Alert colors (all three themes)](#7-color-tokens--universal-grays-and-alert-colors-all-three-themes)
  - [8. Color Tokens — Endless Tributes (obituaries) palette](#8-color-tokens--endless-tributes-obituaries-palette)
  - [9. Color Tokens — theme and sub-theme color fixes (every publication)](#9-color-tokens--theme-and-sub-theme-color-fixes-every-publication)
  - [10. Component colors — Breaking News bar and Sponsored badge](#10-component-colors--breaking-news-bar-and-sponsored-badge)
- **Components, layout, ads and breakpoints**
  - [11. Buttons — Obituaries page CTA (Chicago Tribune, Denver Post)](#11-buttons--obituaries-page-cta-chicago-tribune-denver-post)
  - [12. Article Card / Teaser](#12-article-card--teaser)
  - [13. Reader Dashboard — Modal](#13-reader-dashboard--modal)
  - [14. Reader Dashboard — Disclosure](#14-reader-dashboard--disclosure)
  - [16. Containers, Images & Ad Units](#16-containers-images--ad-units)
  - [17. Navigation](#17-navigation)
  - [18. Ad Units — Homepage "Ad Blocks" slot after Blueconic/Most Popular is undersized (300×250 instead of 300×600)](#18-ad-units--homepage-ad-blocks-slot-after-blueconicmost-popular-is-undersized-300250-instead-of-300600)
  - [19. Masthead — Top-leaderboard ad slot renders at inconsistent sizes across page types](#19-masthead--top-leaderboard-ad-slot-renders-at-inconsistent-sizes-across-page-types)
  - [20. Masthead — Top nav bar overflows its container at the 1040–1279px (Tier 4) breakpoint](#20-masthead--top-nav-bar-overflows-its-container-at-the-10401279px-tier-4-breakpoint)
  - [21. Masthead — Article scrolled-state headline overflows behind the bookmark/share icons](#21-masthead--article-scrolled-state-headline-overflows-behind-the-bookmarkshare-icons)
  - [22. Masthead — Reader Dashboard shows the top nav-links row and "TRENDING:" bar, which the design explicitly excludes](#22-masthead--reader-dashboard-shows-the-top-nav-links-row-and-trending-bar-which-the-design-explicitly-excludes)
  - [23. Video carousel ("Videos from @OCRegister") — fixed-height iframe leaves ~200px of unused blank space at narrow (340–360px) widths](#23-video-carousel-videos-from-ocregister--fixed-height-iframe-leaves-200px-of-unused-blank-space-at-narrow-340360px-widths)
  - [24. Spacing — 10px and 14px values off the 4/8 grid](#24-spacing--10px-and-14px-values-off-the-48-grid)
  - [25. Radius — buttons are 4px; 5px on a button is drift](#25-radius--buttons-are-4px-5px-on-a-button-is-drift)
  - [26. Mobile adhesion — empty sticky bar shows at 1024px and up](#26-mobile-adhesion--empty-sticky-bar-shows-at-1024px-and-up)
  - [27. Blueconic Block (Most Popular) — list spacing and item headline](#27-blueconic-block-most-popular--list-spacing-and-item-headline)
  - [28. Reader Dashboard — breakpoints close to, but not on, the Figma screen widths (questions for DigiScrum)](#28-reader-dashboard--breakpoints-close-to-but-not-on-the-figma-screen-widths-questions-for-digiscrum)
  - [29. Obituaries — breakpoints that don't match the WordPress grid (for the CMS team)](#29-obituaries--breakpoints-that-dont-match-the-wordpress-grid-for-the-cms-team)
  - [30. Breakpoints off the official sets — WordPress themes, trust indicators, digisubs (all 6 sites)](#30-breakpoints-off-the-official-sets--wordpress-themes-trust-indicators-digisubs-all-6-sites)
- [Notes (reading live colors, removed entries)](#notes)

---

## 1. Icon font — mismatches with the Figma icon page, dead and duplicate glyphs, and known missing icons

**Found:** 2026-08-28 to 2026-08-31, icon font audit (`components/icons.md` §3, §5, §6). Added here 2026-09-25: `icons.md` said these were in this handoff, but they had never been logged.

**Figma spec (source of truth):** the `Icons` component set in the main MNG Web Design System file (node `4693:5`, 95 variants) and the documented icon list on its Icons page.

**Production (live icon font, checked on chicagotribune.com):**

| Item | What's wrong | Action |
|---|---|---|
| `google-plus` | Still in the live font. Google+ was shut down years ago, and the icon isn't documented. | Remove from the font. |
| `mng-podcast1` | Same codepoint (`e902`) as `android` — a font-build duplicate, not a separate icon. | Remove the alias. |
| `grid2` | Renders the same gift-box glyph as `gift2`, not a grid. The requested "grid" icon has not shipped. | Remove the alias; ship the real `grid` icon (artwork exists in Figma). |
| `notification`, `notification2` | New outline and filled alert artwork is designed in Figma to replace the IcoMoon glyphs. The class names stay: both are in use (Reader Dashboard inline-message headings, Save Article modal). *Updated 2026-10-22: this is new artwork under the existing names, not two new icons.* | Replace the glyphs at U+E94D (`notification`, outline) and U+E94E (`notification2`, filled); keep the classes. See 1.2. |


**Updated 2026-10-08:** re-checked glyph by glyph against the Figma **Icon Categories** frame (main file, Icons | 2026.08.28, node `1412:13`) using the font extracted from ocregister.com (`tokens/icons/`). **All MNG sites use the same icon font** (Karl, 2026-10-08), so these findings apply everywhere. Of the 171 documented icons, 162 match production by name and glyph. Third-party vendor icons and the "Need to source/make/add" list are out of scope.

### 1.1 Mismatches between the Figma page and the production font

| Figma name | Production | Action |
|---|---|---|
| `grid2` | `icon-grid2` shows the gift glyph (U+E930, same as `gift2`). The Figma grid2 artwork (9 dots) **is in the font** at U+E932, with no class. | Point `icon-grid2` at U+E932. (Supersedes the 2026-08 note above that the grid hasn't shipped: the 9-dot glyph is there, just not wired up. The square-tile `grid` in Pending Updates is a different icon; see 20.2.) |
| `windows8` | `icon-windows8` shows warning2 (U+E986). The Windows logo is in the font at U+E987, with no class. | Point `icon-windows8` at U+E987. |
| `book3` | `icon-book3` points at U+0065 (the letter "e"). The closed book is in the font at U+E993, with no class. | Point `icon-book3` at U+E993. |
| `content_copy` | No class. The glyph is in the font at U+E921. | Add `icon-content_copy` (or the agreed name) → U+E921. |
| `ios_share` | No class. The glyph is in the font at U+E93A. | Add `icon-ios_share` → U+E93A. |
| ~~`home`, `menu7`, `enlarge7`, "iTunes / Apple Music"~~ | **Resolved 2026-10-22 (Karl): production names win.** These are `icon-home3`, `icon-hamburger`, `icon-enlarge` and `icon-music5`; the design system now uses those names. | None. |
| *(none)* | `icon-google-plus` (no glyph), `icon-mng-podcast1` (= android) and `icon-users4` (= user4) have no Figma entry. `google-plus` and `mng-podcast1` are in the table above; `users4` was set aside by Karl 2026-08-31. U+E941 (a second padlock) is in the font with no class and no Figma entry. | Remove the dead classes; U+E941 can go in a font rebuild. |

### 1.2 Next font build (updated 2026-10-22)

Karl updated the MNG IcoMoon project and exported it on 2026-10-22 (188 icons). None of these is in the production font yet. Codepoints are in `tokens/icons/icons.json` (`nextFontBuild`); artwork is in `tokens/icons/svg-missing/`.

- **Add (17 new icons):** `plus-circle`, `plus-circle2`, `minus-circle`, `minus-circle2`, `list`, `grid` (square tiles), `crown`, `giving-hand`, `yield-filled`, `yield-outline`, `headphones`, `sort`, `sort2`, `sort-alpha-asc`, `sort-alpha-desc`, `filter3`, `filter4`.
- **New artwork, same class and codepoint:** `notification` (U+E94D, outline) and `notification2` (U+E94E, filled). Where they show today: `notification2` in the Reader Dashboard's inline-message headings (Saved Articles, Gifted Articles and Subscription pages; seen on Cañon City Daily Record 2026-10-21) and `notification` in the Save Article modal's "out of space" messages (`mng-digisubs` plugin CSS).
- **Keep production's class names.** The IcoMoon project was renamed to match production for `hamburger` (was `menu7`) and `enlarge` (was `enlarge7`). Two names in the export still differ from production: `Threads-square` (production `icon-threads`) and `users4` (production `icon-user4`). Keep the production classes when the font ships.

**Status:** Open.

---

## 2. Font fallbacks — Helvetica instead of the design stacks (all sites)

**Found:** 2026-10-14, computed `font-family` on all 6 review sites (ocregister, denverpost, chicagotribune, orlandosentinel, canoncitydailyrecord, mcall): nav labels, section headers, card headlines, excerpts, footer and obituaries. **Team:** CMS (WordPress themes).

**Design** (main file, Fonts page, Font Styles and Fallbacks `2768:1051`; tokens `font.family.noto-sans` / `font.family.noto-serif`, CSS `--mng-font-family-noto-sans` / `-serif`):

| Stack | Design (should be) | Production |
|---|---|---|
| Sans (`$body`) | `"Noto Sans", "Helvetica Neue", Arial, sans-serif` | `"Noto Sans", Helvetica, sans-serif` |
| Serif (`$heading`) | `"Noto Serif", Georgia, "Times New Roman", serif` | `"Noto Serif", Helvetica, serif` |

The same two stacks apply on every theme; each theme only chooses which one its headings and body use. Obituaries follow the site's theme.

**Fix:** in the theme font-family definitions, replace `Helvetica` with **Helvetica Neue** (then Arial) in the sans stack (Karl, 2026-10-14), and use Georgia, then Times New Roman, in the serif stack instead of Helvetica. The fallbacks only show when Noto doesn't load, so nothing changes visually when the web fonts work.

**Status:** Open.

---

## 4. Reader Dashboard — Typography (2026-09-10)

**Policy:** For anything specific to the Reader Dashboard, Figma is the source of truth — even where production currently differs. MNG Web Design System's `Dashboard/*` typography tokens (in the "Dashboard Typography" collection) are kept at their Figma-specified values; any place production has been found rendering something different is recorded here instead, for engineering to either fix in production or flag back to design if the production value should actually be adopted.

### 4.1 Page title size — `Dashboard/Titles/PageDesktop`

**Figma:** Noto Serif, **26px**, Bold (700) — matches Reader Dashboard v2.0's own Figma token (`Titles/Page (desktop, tabletH)`) exactly.

**Production:** canoncitydailyrecord.com/dashboard/ (desktop width) renders this title at **36px**, via a Tailwind `lg:text-4xl` breakpoint utility class overriding the base size.

**Action needed:** Reconcile production to the Figma-specified 26px, OR — if 36px is an intentional, approved change — get that confirmed with design so Figma can be updated to match and this item retired. Until then, MNG Web Design System's token stays at 26px per the policy above.

**Status:** Open.

### 4.2 Section Title weight — `Dashboard/Titles/SectionTitle`

**Figma:** Noto Sans, 18px, Bold (700).

**Production:** One live-measured instance showed weight 600 (Semi-Bold) instead of 700.

**Caveat (lower confidence than 2.1):** The measured instance may have been an admin/debug panel ("MNG Debugger" / "Entitlements JWT") rather than genuine reader-facing UI.

**Action needed:** Confirm on a real reader-facing Section Title instance whether it's 700 (matches Figma) or genuinely 600.

**Status:** Open.

### 4.3 `font/size/10` — unconfirmed in production

**Figma:** Defined at 10px in Reader Dashboard v2.0's Type Primitives, carried into MNG Web Design System.

**Production:** No confirmed live sighting during this audit (only canoncitydailyrecord.com/dashboard/ was checked).

**Action needed:** Low priority — confirm where (if anywhere) this size is actually used live.

**Status:** Open.

---

## 5. Upcoming Events (CitySpark widget) — font family

**Found:** 2026-10-07, ocregister.com (homepage `.csLayHolder` → `.cswidholder` iframe, CitySpark template).

**Figma spec (source of truth):** WordPress Elements `Upcoming Events Widget` matches production's layout, sizes, spacing and colors exactly (Karl, 2026-10-07), but sets all text in **Noto Sans**, like the rest of the design system.

**Production:** every text element in the widget is **Roboto Condensed**: the title "Upcoming Events" 400 20/22, the "See All Events" and "Add your event" buttons 400 12/15, the card dates 400 11, event names 700 13/14, venues 400 12/14, date-strip days 400 15/20 uppercase and dates 400 20/19.

**Fix:** change the CitySpark widget template's font to Noto Sans (same sizes and weights) on every site, with whoever manages the CitySpark account.

---

## 6. Article breadcrumbs — label font family and text color

**Found:** 2026-10-08, ocregister.com article page (`.breadcrumbs` › `.breadcrumb-type-wrapper > a`, e.g. "NEWS › ENVIRONMENT • News").

**Figma spec (source of truth):** WordPress Elements › Article Page › `Breadcrumbs` (`1110:19469`) matches production's sizes, spacing and colors (rebuilt 2026-10-08, Karl): crumbs Noto Sans 700 16/22 uppercase, the `arrow-right2` icon at 14px in `color/gray/500` with 5px on each side, and the label " • News" in Noto Sans 400 15.2/15.2 (`font/size/15-2`). All breadcrumb text (crumbs, bullet and label) is **`color/gray/min` (#141414)** (Karl, 2026-10-08).

**Production:**
- *Label font:* the label and its CSS-added " • " bullet have no font family set, so they render in **Helvetica** (inherited from the page default). The crumbs are Noto Sans.
- *Text color differs across sites:* breadcrumb text (crumbs, bullet and label) is **#000000** on OC Register, Chicago Tribune and Orlando Sentinel, but **Denver Post's crumbs use its theme red #8E1024**. So some sites let breadcrumbs take a theme / site-override color and others don't.
- *Separator arrow color differs across sites:* **#D7D6D2** on OC Register and Denver Post, **#C8C4C0** on Orlando Sentinel. Design uses `color/gray/500` (#CCCAC7), the closest gray token.
- mcall.com and canoncitydailyrecord.com weren't checked (Chrome isn't allowed on those domains).

**⚠ Decision needed: design AND dev teams together.** Should breadcrumb text be one neutral color on every site, or follow each site's theme / Customizer colors (as Denver Post's red does today)? Design's proposal (Karl, 2026-10-08): one neutral, `color/gray/min` (#141414), on every site whatever its theme or site override, so breadcrumbs don't take theme colors; the arrow is `color/gray/500` everywhere. Dev needs to confirm where Denver Post's red comes from (theme stylesheet or Customizer override) and what changing it affects. Record the agreed answer here.

**Fix:**
1. Set the label to Noto Sans (same 0.95em size, 400 weight) on every site. *Not blocked.*
2. *Pending the decision above:* set all breadcrumb text to the agreed color on every site (proposed `color/gray/min` #141414: from #000000 on most sites, and from #8E1024 on Denver Post).
3. *Pending the decision above:* set the separator arrow to one color on every site (proposed `color/gray/500` #CCCAC7, from #D7D6D2 / #C8C4C0).

**Status:** Open. Fix 1 is ready; fixes 2 and 3 wait on the design + dev decision.

---

## 7. Color Tokens — Universal Grays and Alert colors (all three themes)

**Figma spec (source of truth):** the Universal Grays (`color/gray/*`) and Alert colors (`color/feedback/*`) in the main file's Colors collection, shown in the **Grays & Alerts** block of the Bold Coastal, Modern Earthy and Measured Vibrant theme style guides on the Color Pallets page (production beside them, red-dashed where it differs). Requested again in ticket CI-14848.

**Production (all 6 review sites, checked live 2026-10-19):** Bold Coastal, Modern Earthy and Measured Vibrant ship the same legacy grays, black body text and no alert colors, so every theme needs the same fixes. NEPA-PMP runs modernearthy.css and gets the Modern Earthy fixes.

| Universal (design) | Production, all 3 themes | Fix |
|---|---|---|
| base text = `gray-min` `#141414` | `#000000`, hard-coded (×66 in boldcoastal.css and measuredvibrant.css, ×72 in modernearthy.css) | Change body text from `#000000` to `#141414`. |
| `gray-min` `#141414` | `#0a0908` (`$gray-min`, compiled in; no CSS variable): ×97 boldcoastal.css, ×40 measuredvibrant.css; modernearthy.css mixes `#0a0908` ×40 and `#141414` ×45 | Replace `#0a0908` with `#141414`. |
| `gray-100` `#393938` | `--site-branding-gray-100` `#38322a` | Change the value (`:root`). |
| `gray-200` `#5e5d5c` | `--site-branding-gray-200` `#5d5b5a` | Change the value (`:root`). |
| `gray-300` `#838280` | `--site-branding-gray-300` `#9d9a98` | Change the value (`:root`). |
| `gray-400` `#a7a6a3` | `--site-branding-gray-400` `#aaa7a4` | Change the value (`:root`). |
| `gray-500` `#cccac7` | `--site-branding-gray-500` `#d7d6d2` | Change the value (`:root`). |
| `gray-600` `#f1efeb` | `--site-branding-gray-600` `#f1efeb` | None (matches). |
| `gray-max` `#ffffff` | `#ffffff` | None (matches). |
| Alert low-success `#2e8000`, medium `#856a00`, high-error `#cc2b27` | Not defined in any theme file | Add all three to every theme. |

**Background:** the production grays are CRUX Style Library's older `grayRoot/100–600` scale. Design keeps `color/gray/*` as the source of truth; `grayRoot` isn't a token (Karl, 2026-09-10). The theme-specific Near Black / White neutrals (Bold Coastal `#0a0908`, Modern Earthy `#1a1a1a`, Measured Vibrant `#1f1e1c`) are separate theme tokens and keep their "Replace with gray-min" notes in Figma.

**Status:** Open. These rows are also in `tokens/colors/mng-colors-fixes.csv`.

---

## 8. Color Tokens — Endless Tributes (obituaries) palette

**Figma spec (source of truth):** the 9 `color/tributes/*` variables in the main file's Colors collection (same value in every mode, because obituary pages look the same on every site), shown in the Endless Tributes style guide on the Color Pallets page. Requested in ticket CI-14848.

| Token | Hex |
|---|---|
| primary-lighter | `#f15f87` |
| primary-light | `#c00c3d` |
| primary ("Scarlet") | `#8d092d` |
| primary-dark | `#770000` (rgb 119, 0, 0) |
| primary-darker | `#4d0000` |
| secondary ("Sage") | `#b3bc9c` |
| tertiary ("Brown") | `#3a252b` |
| tan | `#a39c8a` |
| tan-light | `#e8e6e2` |

**Production (obituaries pages on all 6 review sites, checked live 2026-10-19; identical on every site and unchanged since 2026-09-10):**

| Color | Live | Fix |
|---|---|---|
| primary `#8d092d` | Rendered, through the old widget variable `--primary-obit` | Keep the color; replace `--primary-obit` with the Endless Tributes primary. |
| primary-light `#c00c3d` | Hover state of the primary button, through `--primary-obit-light` | Keep the color; replace `--primary-obit-light` with the Endless Tributes primary-light. |
| primary-lighter `#f15f87` | Not in any stylesheet | Add it. |
| primary-dark `#770000` | Not in any stylesheet | Add it. |
| primary-darker `#4d0000` | Not in any stylesheet | Add it. |
| Sage `#b3bc9c` | Declared as `--quaternary-obit`, not used on the pages checked | Replace `--quaternary-obit` with the Endless Tributes secondary (Sage). |
| Brown `#3a252b` | Hard-coded on `.obits-homepage-*`, not on the pages checked | None. |
| tan `#a39c8a` | Hard-coded (search filter button) | None. |
| tan-light `#e8e6e2` | Renders `#ecede7` | Change to `#e8e6e2`. |
| `--secondary-obit` `#946c82`, `--tertiary-obit` `#227db4` | Declared at `:root`, not part of the palette | Remove. |

**Remove the old obituaries widget variables from the code** (Figma: Shared Platform Reference style guide, "Obituaries Widget Colors (--*-obit vars) - NEED TO REMOVE THESE FROM CODE"). All five are still declared at `:root` on every site: `--primary-obit`, `--primary-obit-light`, `--secondary-obit`, `--tertiary-obit`, `--quaternary-obit`. Delete them all; the three that carry palette colors (`--primary-obit`, `--primary-obit-light`, `--quaternary-obit`) are replaced by the Endless Tributes colors above (same values), and `--secondary-obit` and `--tertiary-obit` have no replacement.

**Beige `#ccc7bc` on obituary article pages:** not a palette color, still live on Denver Post obituary articles (rechecked 2026-10-19 on two articles): the "Click here to Send Flowers" banner (`.obit-tribute-wrapper`, black text), the guestbook "Post Your Message" button (`.guestbook-form-submit`), and the "Upcoming events" and "Sign Guestbook" buttons when they show. Set in `styleArticleObit.min.css`. **Fix:** replace it with tan-light `#e8e6e2` (Karl, 2026-10-19).

**Ticket CI-14848:** its Endless Tributes, gray and alert values match the design. A comment (2026-10-19) corrects its primary-dark label to `rgb(119, 0, 0)` and the deprecated "Modern Vibrant" theme name.

**Status:** Open. These rows are also in `tokens/colors/mng-colors-fixes.csv`.

---

## 9. Color Tokens — theme and sub-theme color fixes (every publication)

**Source:** the production columns of the Color Pallets style guides, audited 2026-08-03 (PMP 2026-09-24, Hartford Courant 2026-09-25, NEPA and the disputed Tribune sites 2026-10-01, The Mercury News, East Bay Times, Chicago Tribune and Cañon City 2026-10-19).

**Figma spec (source of truth):** each theme's or sub-theme's design spec column on the Color Pallets page, and the matching Colors collection mode. Every row in the tables below is a red-dashed callout in that theme's "in Production" column. Fix production; don't change the tokens.

**How to read this:** every publication in the cluster audit (97) has its own section, ordered **theme → cluster → sub-theme → site** (Karl, 2026-10-19), with its full list of fixes. Each theme opens with its theme-file fixes, which are fixed once in the theme stylesheet; a site's own table repeats them so each site reads on its own. To check fixes off, use `tokens/colors/mng-colors-fixes.csv` (one row per fix, empty `done` column; the gray / alert fixes from entry 7 and the obituaries fixes from entry 8 come first, then these per-site fixes in the same order). Breaking News bar and Sponsored badge colors: entry 10. The same data is in `tokens/colors/mng-colors-sites.csv` (`engineering_fixes`), one file per site in `tokens/sites/`, and `$extensions.com.mng.mismatches` in `tokens/colors/mng-colors.tokens.json`. Sections and the index are generated by `scripts/colors-docs/build-color-docs.py`.

**Where to read colors live:** themed variables on `document.querySelector('#page')`, not `:root` (the Customizer override is scoped to `#page`; see the method note at the end of this doc).

**Most common gaps:** `--primary-lighter` isn't set on most themes (the page falls back to a shared default), and Measured Vibrant, its sub-themes and NEPA-PMP all render `--tertiary` as `#303F9F` instead of their design values.

**Status:** Open.

<!-- BEGIN per-site color fixes (generated by scripts/colors-docs/build-color-docs.py; edit notes in scripts/colors-docs/notes.json) -->

### Bold Coastal

Loads: `boldcoastal.css`. Figma mode: BoldCoastal. Production audited 2026-08-03.

**Theme-file fixes** (fix once in the theme stylesheet; they apply to every site below unless a sub-theme or site sets its own value):

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#1799a5` | `MISSING` (not set) | Define --primary-lighter: #1799a5 (boldcoastal.css, body). It isn't set today. |
| `--tertiary` | `#f4a700` | `#00838f` (Theme default (body)) | Change --tertiary from #00838f to #f4a700 (boldcoastal.css, body). |

#### Bold Coastal — Baltimore cluster

##### Sub-theme: Capital Gazette

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: none (not a Figma mode). Production audited 2026-08-03.

**Capital Gazette** (capitalgazette.com) · sub-theme Capital Gazette · 3 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#3c6f95` | `#285f87` (div#page override) | Change --primary-lighter from #285f87 to #3c6f95 (Customizer, div#page). |
| `--primary-dark` | `#004171` | `#004e87` (div#page override) | Change --primary-dark from #004e87 to #004171 (Customizer, div#page). |
| `--primary-darker` | `#04365a` | `#014a52` (Theme default (inherited)) | Change --primary-darker from #014a52 to #04365a (Customizer, div#page). |

##### Sub-theme: The Baltimore Sun

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: none (not a Figma mode).

> Uses its documented Figma styles as is. No production comparison is tracked.

**The Baltimore Sun** (baltimoresun.com) · sub-theme The Baltimore Sun · 0 fixes

No fixes.

#### Bold Coastal — BANG cluster

##### Sub-theme: The Mercury News + East Bay Times

Loads: `boldcoastal.css + Customizer override (div#page)` on both sites. Figma mode: The Mercury News + East Bay Times (the two sites had identical design palettes and were combined into one mode and one style guide on 2026-10-19). Production audited 2026-08-03, each site separately; both Customizers rechecked live 2026-10-19.

Why the two sites differ (checked live 2026-10-19): both Customizers set the same 7 values except `--secondary`. East Bay Times sets `#eeff41`, the stock Modern Earthy / Measured Vibrant secondary, so it was copied in by mistake, not a brand choice (Karl, 2026-10-19). On these sites `--secondary` colors the breaking-news bar, the sponsored flag and poll links.

`--subsite-custom` is `#0097a7` in design since 2026-10-19 (Karl): it is the Bold Coastal value, and both sites already render it from `boldcoastal.css` (body), so there is no fix. It was blank in the old 2025 guide for these two sites.

**East Bay Times** (eastbaytimes.com) · sub-theme The Mercury News + East Bay Times · 1 fix

| Token | Design | Production | Fix |
|---|---|---|---|
| `--secondary` | `#ffc518` | `#eeff41` (Customizer (div#page)) | Change --secondary from #eeff41 to #ffc518 (Customizer, div#page). East Bay Times only; The Mercury News already matches. Rechecked live 2026-10-19: the East Bay Times Customizer sets #eeff41 explicitly, the stock Modern Earthy / Measured Vibrant secondary, copied in by mistake (Karl, 2026-10-19). |

**The Mercury News** (mercurynews.com) · sub-theme The Mercury News + East Bay Times · 0 fixes

No fixes.

#### Bold Coastal — Denver cluster

##### Sub-theme: Denver Post

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: DenverPost. Production audited 2026-08-03.

**The Denver Post** (denverpost.com) · sub-theme Denver Post · 3 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#c81632` | `#af1628` | Change --primary-lighter from #af1628 to #c81632 (Customizer, div#page). |
| `--primary-light` | `#af1628` | `#c81632` | Change --primary-light from #c81632 to #af1628 (Customizer, div#page). |
| `--tertiary` | `#ffc518` | `#a13b1e` | Change --tertiary from #a13b1e to #ffc518 (Customizer, div#page). |

#### Bold Coastal — SCNG cluster

**Orange County Register** (ocregister.com) · theme Bold Coastal · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#1799a5` | `MISSING` (not set) | Define --primary-lighter: #1799a5 (boldcoastal.css, body). It isn't set today. |
| `--tertiary` | `#f4a700` | `#00838f` (Theme default (body)) | Change --tertiary from #00838f to #f4a700 (boldcoastal.css, body). |

**Torrance Daily Breeze** (dailybreeze.com) · theme Bold Coastal · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#1799a5` | `MISSING` (not set) | Define --primary-lighter: #1799a5 (boldcoastal.css, body). It isn't set today. |
| `--tertiary` | `#f4a700` | `#00838f` (Theme default (body)) | Change --tertiary from #00838f to #f4a700 (boldcoastal.css, body). |

#### Bold Coastal — Sonoma cluster

##### Sub-theme: Petaluma Argus-Courier

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: Petaluma Argus-Courier. Production audited 2026-08-03.

**Petaluma Argus-Courier** (petalumanews.com) · sub-theme Petaluma Argus-Courier · 1 fix

| Token | Design | Production | Fix |
|---|---|---|---|
| `--secondary` | `#ffea00` | `MISSING` (not set) | Define --secondary: #ffea00 (Customizer, div#page). It isn't set today. |

##### Sub-theme: The Press Democrat

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: The Press Democrat. Production audited 2026-08-03.

`--subsite-custom` `#eeeeee` is the sub-theme's own design value since 2026-10-19 (Karl): it overrides the Bold Coastal `#0097a7` and matches production, so there is no fix.

**Sonoma County Gazette** (sonomacountygazette.com) · sub-theme The Press Democrat · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--secondary` | `#ffea00` | `MISSING` (not set) | Define --secondary: #ffea00 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#006fb7` | `#d10f14` (div#page override) | Change --tertiary from #d10f14 to #006fb7 (Customizer, div#page). |

**The Press Democrat** (pressdemocrat.com) · sub-theme The Press Democrat · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--secondary` | `#ffea00` | `MISSING` (not set) | Define --secondary: #ffea00 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#006fb7` | `#d10f14` (div#page override) | Change --tertiary from #d10f14 to #006fb7 (Customizer, div#page). |

##### Sub-theme: The Sonoma Index-Tribune

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: The Sonoma Index-Tribune. Production audited 2026-08-03.

**The Sonoma Index-Tribune** (sonomanews.com) · sub-theme The Sonoma Index-Tribune · 1 fix

| Token | Design | Production | Fix |
|---|---|---|---|
| `--secondary` | `#ffea00` | `MISSING` (not set) | Define --secondary: #ffea00 (Customizer, div#page). It isn't set today. |

#### Bold Coastal — St. Paul cluster

##### Sub-theme: St. Paul Pioneer Press

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: St. Paul Pioneer Press. Production audited 2026-08-03.

`--subsite-custom` `#ffffff` is the sub-theme's own design value since 2026-10-19 (Karl): it overrides the Bold Coastal `#0097a7` and matches production, so there is no fix.

**St. Paul Pioneer Press** (twincities.com) · sub-theme St. Paul Pioneer Press · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#0187e0` | `MISSING` (not set) | Define --primary-lighter: #0187e0 (Customizer, div#page). It isn't set today. |
| `--primary-darker` | `#005892` | `MISSING` (not set) | Define --primary-darker: #005892 (Customizer, div#page). It isn't set today. |
| `--secondary` | `#ffea00` | `MISSING` (not set) | Define --secondary: #ffea00 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#f4a700` | `MISSING` (not set) | Define --tertiary: #f4a700 (Customizer, div#page). It isn't set today. |

### Modern Earthy

Loads: `modernearthy.css`. Figma mode: ModernEarthy. Production audited 2026-08-03.

**Theme-file fixes** (fix once in the theme stylesheet; they apply to every site below unless a sub-theme or site sets its own value):

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

#### Modern Earthy — 21C Michigan cluster

##### Sub-theme: 21C Michigan Sites (Combined)

Loads: `modernearthy.css + Customizer override (div#page), identical on all 4 sites`. Figma mode: 21C Michigan Sites (Combined). Production audited 2026-08-03.

**Daily Oakland Press** (theoaklandpress.com) · sub-theme 21C Michigan Sites (Combined) · 3 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#3e7cb2` | `MISSING` (not set) | Define --primary-lighter: #3e7cb2 (Customizer, div#page). It isn't set today. |
| `--primary-dark` | `#32476c` | `#3a527a` (div#page override) | Change --primary-dark from #3a527a to #32476c (Customizer, div#page). |
| `--primary-darker` | `#2c3b55` | `#003d66` (Theme default (inherited)) | Change --primary-darker from #003d66 to #2c3b55 (Customizer, div#page). |

**Macomb Daily** (macombdaily.com) · sub-theme 21C Michigan Sites (Combined) · 3 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#3e7cb2` | `MISSING` (not set) | Define --primary-lighter: #3e7cb2 (Customizer, div#page). It isn't set today. |
| `--primary-dark` | `#32476c` | `#3a527a` (div#page override) | Change --primary-dark from #3a527a to #32476c (Customizer, div#page). |
| `--primary-darker` | `#2c3b55` | `#003d66` (Theme default (inherited)) | Change --primary-darker from #003d66 to #2c3b55 (Customizer, div#page). |

**Mount Pleasant Morning Sun** (themorningsun.com) · sub-theme 21C Michigan Sites (Combined) · 3 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#3e7cb2` | `MISSING` (not set) | Define --primary-lighter: #3e7cb2 (Customizer, div#page). It isn't set today. |
| `--primary-dark` | `#32476c` | `#3a527a` (div#page override) | Change --primary-dark from #3a527a to #32476c (Customizer, div#page). |
| `--primary-darker` | `#2c3b55` | `#003d66` (Theme default (inherited)) | Change --primary-darker from #003d66 to #2c3b55 (Customizer, div#page). |

**The News-Herald (Southgate)** (thenewsherald.com) · sub-theme 21C Michigan Sites (Combined) · 3 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#3e7cb2` | `MISSING` (not set) | Define --primary-lighter: #3e7cb2 (Customizer, div#page). It isn't set today. |
| `--primary-dark` | `#32476c` | `#3a527a` (div#page override) | Change --primary-dark from #3a527a to #32476c (Customizer, div#page). |
| `--primary-darker` | `#2c3b55` | `#003d66` (Theme default (inherited)) | Change --primary-darker from #003d66 to #2c3b55 (Customizer, div#page). |

#### Modern Earthy — 21C New York cluster

**Kingston Daily Freeman** (dailyfreeman.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Oneida Daily Dispatch** (oneidadispatch.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Saratogian** (saratogian.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**The Troy Record** (troyrecord.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

#### Modern Earthy — 21C Ohio cluster

**Lake County News-Herald** (news-herald.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Lorain Morning Journal** (morningjournal.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

#### Modern Earthy — 21C Pennsylvania cluster

**Delaware County Times** (delcotimes.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Main Line Media News** (mainlinemedianews.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Norristown Times Herald** (timesherald.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Reading Eagle** (readingeagle.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**The Lansdale Reporter** (thereporteronline.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**The Pottstown Mercury** (pottsmerc.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Trentonian** (trentonian.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**West Chester Daily Local** (dailylocal.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

#### Modern Earthy — BANG cluster

**Silicon Valley** (siliconvalley.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

#### Modern Earthy — Boston cluster

**Nashoba Valley Voice** (nashobavalleyvoice.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

##### Sub-theme: Boston Herald

Loads: `modernearthy.css + Customizer override (div#page)`. Figma mode: Boston Herald. Production audited 2026-08-03.

**Boston Herald** (bostonherald.com) · sub-theme Boston Herald · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#3c81c7` | `MISSING` (not set) | Define --primary-lighter: #3c81c7 (Customizer, div#page). It isn't set today. |
| `--primary-darker` | `#0f496f` | `MISSING` (not set) | Define --primary-darker: #0f496f (Customizer, div#page). It isn't set today. |
| `--secondary` | `#eeff41` | `MISSING` (not set) | Define --secondary: #eeff41 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#ff5722` | `MISSING` (not set) | Define --tertiary: #ff5722 (Customizer, div#page). It isn't set today. |

#### Modern Earthy — Colorado Weeklies cluster

##### Sub-theme: NEPA-PMP

Loads: `modernearthy.css + color override on body: site-pmp style.min.css (PMP sites) or each NEPA site's own site plugin (site-citizensvoice, site-thetimes-tribune, site-wcexaminer, site-republicanherald, site-standardspeaker), identical values`. Figma mode: NEPA-PMP. Production audited 2026-10-01.

> One color sub-theme for two groups: the 19 PMP sites (shared site-pmp stylesheet) and the 5 NEPA sites (each site's own plugin stylesheet). Verified live 2026-10-01: NEPA sets the same six variables on body with identical values, and renders the same type as PMP.

Greeley Tribune's `div#page` override of `--primary`, `--primary-light` and `--primary-dark` is a documented exception (Karl, 2026-09-30): it's noted under the NEPA-PMP style guide without red outlines and needs no fix.

**Colorado Daily** (coloradodaily.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Julesburg Advocate** (julesburgadvocate.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Lamar Ledger** (lamarledger.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

#### Modern Earthy — Fitch cluster

**Lowell Sun** (lowellsun.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Sentinel & Enterprise (Fitchburg)** (sentinelandenterprise.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

#### Modern Earthy — NEPA cluster

##### Sub-theme: NEPA-PMP

Sub-theme notes: see its first cluster above.

**Republican Herald (Pottsville)** (republicanherald.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Scranton Times-Tribune** (thetimes-tribune.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Standard-Speaker (Hazleton)** (standardspeaker.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**The Citizens' Voice (Wilkes-Barre)** (citizensvoice.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Wyoming County Examiner** (wcexaminer.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

#### Modern Earthy — PMP cluster

##### Sub-theme: NEPA-PMP

Sub-theme notes: see its first cluster above.

**Boulder Daily Camera** (dailycamera.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Greeley Tribune** (greeleytribune.com) · sub-theme NEPA-PMP · 2 fixes

Documented exception (no fix): `--primary` `#536e7f`, `--primary-light` `#5b7b8b`, `--primary-dark` `#44687f`.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Longmont Times-Call** (timescall.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Loveland Reporter-Herald** (reporterherald.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

#### Modern Earthy — PMP Weeklies cluster

##### Sub-theme: NEPA-PMP

Sub-theme notes: see its first cluster above.

**Akron News-Reporter** (akronnewsreporter.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**BoCoPreps** (bocopreps.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Broomfield Enterprise** (broomfieldenterprise.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Brush News-Tribune** (brushnewstribune.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Buffzone** (buffzone.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Cañon City Daily Record** (canoncitydailyrecord.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Colorado Hometown Weekly** (coloradohometownweekly.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Estes Park Trail-Gazette** (eptrail.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Fort Morgan Times** (fortmorgantimes.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**South Platte Sentinel** (southplattesentinel.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Sterling Journal-Advocate** (journal-advocate.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**The Burlington Record** (burlington-record.com) · sub-theme NEPA-PMP · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

#### Modern Earthy — SCNG cluster

**Excelsior California** (excelsiorcalifornia.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**LA Daily News** (dailynews.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Pasadena Star-News** (pasadenastarnews.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Press Enterprise (Riverside)** (pressenterprise.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**San Bernardino Sun** (sbsun.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**San Gabriel Valley Tribune** (sgvtribune.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Whittier Daily News** (whittierdailynews.com) · theme Modern Earthy · 4 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` (not set) | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` (not set) | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

#### Modern Earthy — Tribune cluster

##### Sub-theme: Daily Herald

New palette, added 2026-10-15 (Karl). Planned delivery: `modernearthy.css + Customizer override (div#page)`. Figma mode: Daily Herald (since 2026-10-19). The spec is that mode, the "Daily Herald — Style Guide" section on the Color Pallets page and `tokens/themes/daily-herald.tokens.json`.

No fixes yet: dailyherald.com still runs on Everyware (verified 2026-09-24), so there is no production column to compare. When it moves to Modern Earthy, set all ten values in the Customizer (`div#page`): `--primary-lighter` `#3b97dc`, `--primary-light` `#087abe`, `--primary` `#0072b4`, `--primary-dark` `#0066a2`, `--primary-darker` `#0e598b`, `--secondary` `#eeff41`, `--tertiary` `#ff5722` (`--near-black`, `--white` and `--nav-text` use the Modern Earthy defaults `#1a1a1a` / `#fafafa` / `#1a1a1a`). Then audit it like the other sub-themes.

**Daily Herald** (dailyherald.com) · sub-theme Daily Herald · 0 fixes

No fixes.

##### Sub-theme: Morning Call

Loads: `modernearthy.css + Customizer override (div#page)`. Figma mode: Morning Call. Production audited 2026-08-03.

Production's `--primary` (`#014b78`) is the design's `primary-dark`: the Customizer ramp looks shifted one step. Fix it as listed (design is the source of truth).

**The Morning Call** (mcall.com) · sub-theme Morning Call · 6 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#5399c4` | `MISSING` (not set) | Define --primary-lighter: #5399c4 (Customizer, div#page). It isn't set today. |
| `--primary-light` | `#27719f` | `#337ca9` (div#page override) | Change --primary-light from #337ca9 to #27719f (Customizer, div#page). |
| `--primary` | `#166291` | `#014b78` (div#page override) | Change --primary from #014b78 to #166291 (Customizer, div#page). |
| `--primary-darker` | `#00385a` | `MISSING` (not set) | Define --primary-darker: #00385a (Customizer, div#page). It isn't set today. |
| `--secondary` | `#eeff41` | `MISSING` (not set) | Define --secondary: #eeff41 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#ff5722` | `MISSING` (not set) | Define --tertiary: #ff5722 (Customizer, div#page). It isn't set today. |

### Measured Vibrant

Loads: `measuredvibrant.css`. Figma mode: MeasuredVibrant. Production audited 2026-08-03.

**Theme-file fixes** (fix once in the theme stylesheet; they apply to every site below unless a sub-theme or site sets its own value):

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

#### Measured Vibrant — BANG cluster

**Marin Independent Journal** (marinij.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

#### Measured Vibrant — Norcal cluster

**Chico Enterprise-Record** (chicoer.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Eureka Times-Standard** (times-standard.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Lake County Record-Bee** (record-bee.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Monterey Herald** (montereyherald.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Oroville Mercury-Register** (orovillemr.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Red Bluff Daily News** (redbluffdailynews.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Santa Cruz Sentinel** (santacruzsentinel.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Ukiah Daily Journal** (ukiahdailyjournal.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Vacaville Reporter** (thereporter.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Vallejo Times-Herald** (timesheraldonline.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Woodland Daily Democrat** (dailydemocrat.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

#### Measured Vibrant — Norcal Weeklies cluster

**Fort Bragg Advocate-News** (advocate-news.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Paradise Post** (paradisepost.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**The Mendocino Beacon** (mendocinobeacon.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**The Willits News** (willitsnews.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

#### Measured Vibrant — SCNG cluster

**Inland Valley Daily Bulletin** (dailybulletin.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Long Beach Press-Telegram** (presstelegram.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Redlands Daily Facts** (redlandsdailyfacts.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**San Diego Union-Tribune** (sandiegouniontribune.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

#### Measured Vibrant — Tribune cluster

**Daily Press** (dailypress.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**New York Daily News** (nydailynews.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**The Virginian-Pilot** (pilotonline.com) · theme Measured Vibrant · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

##### Sub-theme: Chicago Tribune

Loads: `measuredvibrant.css (Measured Vibrant values; own Figma mode)`. Figma mode: Chicago Tribune.

> No style guide of its own; audited under Measured Vibrant, whose production callouts apply.

**Chicago Tribune** (chicagotribune.com) · sub-theme Chicago Tribune · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

##### Sub-theme: GrowthSpotter

Loads: `measuredvibrant.css + Customizer override (div#page)`. Figma mode: GrowthSpotter. Production audited 2026-08-03.

**GrowthSpotter** (growthspotter.com) · sub-theme GrowthSpotter · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#529950` | `MISSING` (not set) | Define --primary-lighter: #529950 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#e7632a` | `#303f9f` (Theme default (inherited)) | Change --tertiary from #303f9f to #e7632a (Customizer, div#page). |

##### Sub-theme: Hartford Courant

Loads: `measuredvibrant.css + site-tribune style.min.css + Customizer override (div#page)`. Figma mode: Hartford Courant. Production audited 2026-09-25.

> Verified live 2026-09-25: loads measuredvibrant.css + site-tribune style.min.css, with a div#page Customizer override (primary, light and dark all #2b7ea5). Production matches the Figma production column.

**Hartford Courant** (courant.com) · sub-theme Hartford Courant · 6 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#5796bd` | `MISSING` (not set) | Define --primary-lighter: #5796bd (Customizer, div#page). It isn't set today. |
| `--primary` | `#166d95` | `#2b7ea5` (div#page override) | Change --primary from #2b7ea5 to #166d95 (Customizer, div#page). |
| `--primary-dark` | `#084e6f` | `#2b7ea5` (same as --primary (div#page)) | Change --primary-dark from #2b7ea5 to #084e6f (Customizer, div#page). |
| `--primary-darker` | `#171e44` | `MISSING` (not set) | Define --primary-darker: #171e44 (Customizer, div#page). It isn't set today. |
| `--secondary` | `#eeff41` | `MISSING` (not set) | Define --secondary: #eeff41 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#6a54ca` | `MISSING` (not set) | Define --tertiary: #6a54ca (Customizer, div#page). It isn't set today. |

##### Sub-theme: Orlando Sentinel

Loads: `measuredvibrant.css + Customizer override (div#page)`. Figma mode: Orlando Sentinel. Production audited 2026-08-03.

**Orlando Sentinel** (orlandosentinel.com) · sub-theme Orlando Sentinel · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#5c95dd` | `MISSING` (not set) | Define --primary-lighter: #5c95dd (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#48a395` | `#303f9f` (Theme default (inherited)) | Change --tertiary from #303f9f to #48a395 (Customizer, div#page). |

##### Sub-theme: South Florida Sun Sentinel

Loads: `measuredvibrant.css + Customizer override (div#page)`. Figma mode: South Florida Sun Sentinel. Production audited 2026-08-03.

`--subsite-custom` `#000000` is the sub-theme's own design value since 2026-10-19 (Karl); Measured Vibrant has none. It matches production, so there is no fix.

**South Florida Sun Sentinel** (sun-sentinel.com) · sub-theme South Florida Sun Sentinel · 2 fixes

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#4a92af` | `MISSING` (not set) | Define --primary-lighter: #4a92af (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#ab9500` | `#303f9f` (Theme default (inherited)) | Change --tertiary from #303f9f to #ab9500 (Customizer, div#page). |

### Not on MNG themes

#### Not on MNG themes — Sonoma cluster

**Sonoma Magazine** (sonomamag.com): Not on MNG WordPress themes (verified 2026-09-24): no MNG theme tokens.

<!-- END per-site color fixes -->

### Index: every publication

Ordered theme > cluster > sub-theme > site, as above.

| Theme | Cluster | Sub-theme | Publication | Domain | Fixes |
|---|---|---|---|---|---|
| Bold Coastal | Baltimore | Capital Gazette | Capital Gazette | capitalgazette.com | 3 |
| Bold Coastal | Baltimore | The Baltimore Sun | The Baltimore Sun | baltimoresun.com | 0 |
| Bold Coastal | BANG | The Mercury News + East Bay Times | East Bay Times | eastbaytimes.com | 1 |
| Bold Coastal | BANG | The Mercury News + East Bay Times | The Mercury News | mercurynews.com | 0 |
| Bold Coastal | Denver | Denver Post | The Denver Post | denverpost.com | 3 |
| Bold Coastal | SCNG | — | Orange County Register | ocregister.com | 2 |
| Bold Coastal | SCNG | — | Torrance Daily Breeze | dailybreeze.com | 2 |
| Bold Coastal | Sonoma | Petaluma Argus-Courier | Petaluma Argus-Courier | petalumanews.com | 1 |
| Bold Coastal | Sonoma | The Press Democrat | Sonoma County Gazette | sonomacountygazette.com | 2 |
| Bold Coastal | Sonoma | The Press Democrat | The Press Democrat | pressdemocrat.com | 2 |
| Bold Coastal | Sonoma | The Sonoma Index-Tribune | The Sonoma Index-Tribune | sonomanews.com | 1 |
| Bold Coastal | St. Paul | St. Paul Pioneer Press | St. Paul Pioneer Press | twincities.com | 4 |
| Modern Earthy | 21C Michigan | 21C Michigan Sites (Combined) | Daily Oakland Press | theoaklandpress.com | 3 |
| Modern Earthy | 21C Michigan | 21C Michigan Sites (Combined) | Macomb Daily | macombdaily.com | 3 |
| Modern Earthy | 21C Michigan | 21C Michigan Sites (Combined) | Mount Pleasant Morning Sun | themorningsun.com | 3 |
| Modern Earthy | 21C Michigan | 21C Michigan Sites (Combined) | The News-Herald (Southgate) | thenewsherald.com | 3 |
| Modern Earthy | 21C New York | — | Kingston Daily Freeman | dailyfreeman.com | 4 |
| Modern Earthy | 21C New York | — | Oneida Daily Dispatch | oneidadispatch.com | 4 |
| Modern Earthy | 21C New York | — | Saratogian | saratogian.com | 4 |
| Modern Earthy | 21C New York | — | The Troy Record | troyrecord.com | 4 |
| Modern Earthy | 21C Ohio | — | Lake County News-Herald | news-herald.com | 4 |
| Modern Earthy | 21C Ohio | — | Lorain Morning Journal | morningjournal.com | 4 |
| Modern Earthy | 21C Pennsylvania | — | Delaware County Times | delcotimes.com | 4 |
| Modern Earthy | 21C Pennsylvania | — | Main Line Media News | mainlinemedianews.com | 4 |
| Modern Earthy | 21C Pennsylvania | — | Norristown Times Herald | timesherald.com | 4 |
| Modern Earthy | 21C Pennsylvania | — | Reading Eagle | readingeagle.com | 4 |
| Modern Earthy | 21C Pennsylvania | — | The Lansdale Reporter | thereporteronline.com | 4 |
| Modern Earthy | 21C Pennsylvania | — | The Pottstown Mercury | pottsmerc.com | 4 |
| Modern Earthy | 21C Pennsylvania | — | Trentonian | trentonian.com | 4 |
| Modern Earthy | 21C Pennsylvania | — | West Chester Daily Local | dailylocal.com | 4 |
| Modern Earthy | BANG | — | Silicon Valley | siliconvalley.com | 4 |
| Modern Earthy | Boston | — | Nashoba Valley Voice | nashobavalleyvoice.com | 4 |
| Modern Earthy | Boston | Boston Herald | Boston Herald | bostonherald.com | 4 |
| Modern Earthy | Colorado Weeklies | NEPA-PMP | Colorado Daily | coloradodaily.com | 2 |
| Modern Earthy | Colorado Weeklies | NEPA-PMP | Julesburg Advocate | julesburgadvocate.com | 2 |
| Modern Earthy | Colorado Weeklies | NEPA-PMP | Lamar Ledger | lamarledger.com | 2 |
| Modern Earthy | Fitch | — | Lowell Sun | lowellsun.com | 4 |
| Modern Earthy | Fitch | — | Sentinel & Enterprise (Fitchburg) | sentinelandenterprise.com | 4 |
| Modern Earthy | NEPA | NEPA-PMP | Republican Herald (Pottsville) | republicanherald.com | 2 |
| Modern Earthy | NEPA | NEPA-PMP | Scranton Times-Tribune | thetimes-tribune.com | 2 |
| Modern Earthy | NEPA | NEPA-PMP | Standard-Speaker (Hazleton) | standardspeaker.com | 2 |
| Modern Earthy | NEPA | NEPA-PMP | The Citizens' Voice (Wilkes-Barre) | citizensvoice.com | 2 |
| Modern Earthy | NEPA | NEPA-PMP | Wyoming County Examiner | wcexaminer.com | 2 |
| Modern Earthy | PMP | NEPA-PMP | Boulder Daily Camera | dailycamera.com | 2 |
| Modern Earthy | PMP | NEPA-PMP | Greeley Tribune | greeleytribune.com | 2 |
| Modern Earthy | PMP | NEPA-PMP | Longmont Times-Call | timescall.com | 2 |
| Modern Earthy | PMP | NEPA-PMP | Loveland Reporter-Herald | reporterherald.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | Akron News-Reporter | akronnewsreporter.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | BoCoPreps | bocopreps.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | Broomfield Enterprise | broomfieldenterprise.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | Brush News-Tribune | brushnewstribune.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | Buffzone | buffzone.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | Cañon City Daily Record | canoncitydailyrecord.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | Colorado Hometown Weekly | coloradohometownweekly.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | Estes Park Trail-Gazette | eptrail.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | Fort Morgan Times | fortmorgantimes.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | South Platte Sentinel | southplattesentinel.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | Sterling Journal-Advocate | journal-advocate.com | 2 |
| Modern Earthy | PMP Weeklies | NEPA-PMP | The Burlington Record | burlington-record.com | 2 |
| Modern Earthy | SCNG | — | Excelsior California | excelsiorcalifornia.com | 4 |
| Modern Earthy | SCNG | — | LA Daily News | dailynews.com | 4 |
| Modern Earthy | SCNG | — | Pasadena Star-News | pasadenastarnews.com | 4 |
| Modern Earthy | SCNG | — | Press Enterprise (Riverside) | pressenterprise.com | 4 |
| Modern Earthy | SCNG | — | San Bernardino Sun | sbsun.com | 4 |
| Modern Earthy | SCNG | — | San Gabriel Valley Tribune | sgvtribune.com | 4 |
| Modern Earthy | SCNG | — | Whittier Daily News | whittierdailynews.com | 4 |
| Modern Earthy | Tribune | Daily Herald | Daily Herald | dailyherald.com | 0 |
| Modern Earthy | Tribune | Morning Call | The Morning Call | mcall.com | 6 |
| Measured Vibrant | BANG | — | Marin Independent Journal | marinij.com | 2 |
| Measured Vibrant | Norcal | — | Chico Enterprise-Record | chicoer.com | 2 |
| Measured Vibrant | Norcal | — | Eureka Times-Standard | times-standard.com | 2 |
| Measured Vibrant | Norcal | — | Lake County Record-Bee | record-bee.com | 2 |
| Measured Vibrant | Norcal | — | Monterey Herald | montereyherald.com | 2 |
| Measured Vibrant | Norcal | — | Oroville Mercury-Register | orovillemr.com | 2 |
| Measured Vibrant | Norcal | — | Red Bluff Daily News | redbluffdailynews.com | 2 |
| Measured Vibrant | Norcal | — | Santa Cruz Sentinel | santacruzsentinel.com | 2 |
| Measured Vibrant | Norcal | — | Ukiah Daily Journal | ukiahdailyjournal.com | 2 |
| Measured Vibrant | Norcal | — | Vacaville Reporter | thereporter.com | 2 |
| Measured Vibrant | Norcal | — | Vallejo Times-Herald | timesheraldonline.com | 2 |
| Measured Vibrant | Norcal | — | Woodland Daily Democrat | dailydemocrat.com | 2 |
| Measured Vibrant | Norcal Weeklies | — | Fort Bragg Advocate-News | advocate-news.com | 2 |
| Measured Vibrant | Norcal Weeklies | — | Paradise Post | paradisepost.com | 2 |
| Measured Vibrant | Norcal Weeklies | — | The Mendocino Beacon | mendocinobeacon.com | 2 |
| Measured Vibrant | Norcal Weeklies | — | The Willits News | willitsnews.com | 2 |
| Measured Vibrant | SCNG | — | Inland Valley Daily Bulletin | dailybulletin.com | 2 |
| Measured Vibrant | SCNG | — | Long Beach Press-Telegram | presstelegram.com | 2 |
| Measured Vibrant | SCNG | — | Redlands Daily Facts | redlandsdailyfacts.com | 2 |
| Measured Vibrant | SCNG | — | San Diego Union-Tribune | sandiegouniontribune.com | 2 |
| Measured Vibrant | Tribune | — | Daily Press | dailypress.com | 2 |
| Measured Vibrant | Tribune | — | New York Daily News | nydailynews.com | 2 |
| Measured Vibrant | Tribune | — | The Virginian-Pilot | pilotonline.com | 2 |
| Measured Vibrant | Tribune | Chicago Tribune | Chicago Tribune | chicagotribune.com | 2 |
| Measured Vibrant | Tribune | GrowthSpotter | GrowthSpotter | growthspotter.com | 2 |
| Measured Vibrant | Tribune | Hartford Courant | Hartford Courant | courant.com | 6 |
| Measured Vibrant | Tribune | Orlando Sentinel | Orlando Sentinel | orlandosentinel.com | 2 |
| Measured Vibrant | Tribune | South Florida Sun Sentinel | South Florida Sun Sentinel | sun-sentinel.com | 2 |
| — | Sonoma | — | Sonoma Magazine | sonomamag.com | — |

---

## 10. Component colors — Breaking News bar and Sponsored badge

### 10.1 Breaking News bar — Denver Post uses primary-lighter instead of secondary

**Found:** 2026-10-02, live check of the six review sites (theme CSS read on `#page`; no breaking bar was active, so the color was read from the site's own `.breaking-bar` rule).

**Figma spec (source of truth):** the Breaking News Banner (WordPress Elements, `506:5632`) background is `color/theme/secondary` and its text is `color/theme/near-black` (bound 2026-10-02).

**Production:**

| Site | `.breaking-bar` background | Text | Token |
|---|---|---|---|
| ocregister.com | #FFEA00 | #0A0908 | secondary |
| chicagotribune.com | #EEFF41 | #1F1E1C | secondary |
| orlandosentinel.com | #EEFF41 | #1F1E1C | secondary |
| canoncitydailyrecord.com | #EEFF41 | #141414 | secondary |
| mcall.com | #EEFF41 | #141414 | secondary |
| **denverpost.com** | **#AF1628** | #0A0908 | **primary-lighter** (Denver Post override) |

**Open question (Karl):** keep Denver Post's red bar as a documented Denver Post exception, or have Engineering align it to `secondary` (`#003459`, navy, on Denver Post). Until decided, Figma stays on `secondary`.

**Status:** Open, waiting on that decision.

### 10.2 Sponsored content badge — needs to be fixed in production

**Found:** 2026-10-02, live check of the six review sites (homepage, Latest Headlines and article lists).

**Figma spec (source of truth):** the "Sponsored content" badge (WordPress Elements, Article Status Badge `Type=Sponsored`, `3344:63995`, and its instances in Latest Headlines, Top Zone and TopZone Article Card) stays **#7D161E with white text** (Karl, 2026-10-02). It is intentionally not bound to a theme token for now: none of the theme roles works on every site (white text fails contrast on the yellow `secondary` themes, and `tertiary` passes on only 9 of 22 themes).

**Production:** the live badge is the Nativo native-ad label (inline style set by the vendor template), not a theme class, and it doesn't match the design anywhere checked.

| Site | Live label background | Design | Match |
|---|---|---|---|
| denverpost.com | #003459 (navy, white text) | #7D161E | ❌ |
| ocregister.com | #0097A7 | #7D161E | ❌ |
| chicagotribune.com, orlandosentinel.com, canoncitydailyrecord.com, mcall.com | no Nativo sponsored unit on the homepage checked | #7D161E | not checked |

**Fix:** update the Nativo sponsored-label template on every site to the design badge (#7D161E background, white `gray/max` text, Noto Sans), with Ad Ops. Re-check the other four sites when a sponsored unit is running.

**Note:** the theme's own `.sponsored-content .sponsored-flag` (a different element) uses `primary-light` with white text, and `secondary` with dark text on images.

**Status:** Open.

---

## 11. Buttons — Obituaries page CTA (Chicago Tribune, Denver Post)

**Found:** 2026-09-01, during the buttons audit.

**Figma spec:** Button Primary (main file, ***Buttons page), Default size — padding 16px vertical + 20px horizontal, 14px text.

**Production:** The live `.subscribe-button` CTA (249×44, confirmed identical on Chicago Tribune and Denver Post, also appears on regular article pages — a general paywall CTA, not obituary-specific) renders with padding 14px/10px instead of 16px/20px, and font-size 15px instead of 14px. Radius and per-masthead fill color already match Figma.

**Decision (Karl, 2026-09-01):** This is not a new button size/variant — it should simply carry Button Primary's existing Default styling. Production needs to be brought in line with Figma's padding and font-size values above; no new Figma token or variant should be created for it.

**Status:** Open.

---

## 12. Article Card / Teaser

### 12.1 Denver Post — Section Highlight shows 4 headline items instead of 3

**Found:** Article Card / Teaser audit.

**Figma / platform norm:** Every pilot site (Chicago Tribune, OC Register, Orlando Sentinel, Greeley Tribune, mcall.com) shows exactly 3 headline items in the Section Highlight module.

**Production:** Denver Post shows 4 — and this isn't theme-scoped, since OC Register shares Denver Post's Bold Coastal theme but still shows 3.

**Action needed:** Confirm whether this is a deliberate per-site editorial choice or a real inconsistency worth fixing.

**Status:** Open — not yet root-caused.

### 12.2 Section title color and underline don't match Figma on any of the 6 review sites

**Found:** Article Card / Teaser audit.

**Figma spec:** Section Highlight / "Latest Headlines" title: text color `color/gray/100`, with a 2px underline in the site's own `--primary`. Size, weight and family come from the per-theme eyebrow tokens: Bold Coastal 20px / 400 / Noto Sans, Measured Vibrant 17px / 700 / Noto Sans, Modern Earthy 21px / 400 / Noto Serif (`tokens/typography/typography-decision-log.md`, decision 6). Production already matches these sizes.

**Production:** the text color is wrong on all 6 sites. The underline is missing on Chicago Tribune, Orlando Sentinel, OC Register and Denver Post; only the two Modern Earthy sites have it.

**Fix:** set the title color to `color/gray/100` and add the 2px `--primary` underline on every theme.

**Status:** Open. Ready for Engineering.

### 12.3 Responsive layout rules vary by container context (not fully mapped)

**Found:** Article Card / Teaser audit, §5 Open Item 8.

**Detail:** `feature-medium` and `headline-only` responsive (`flex-direction`) rules change depending on the parent container class (e.g. `.landing-four-up-hybrid`, `.landing-three-one`, `.slow .feature-top` each carry their own breakpoint overrides for the same classes). This overlaps with the upcoming Containers component and hasn't been fully mapped — flagging so it isn't mistaken for one universal rule.

**Status:** Open / informational — needs a dedicated mapping pass.

### 12.4 Excerpt/dek color needs re-verification (minor)

**Detail:** The dek/excerpt color (~`#484642`, sampled from Chicago Tribune) was derived via an rgb→hex rounding pass that wasn't double-checked the way other colors in the doc were.

**Status:** Open — low priority, worth a re-check before treating as final.

---

## 13. Reader Dashboard — Modal

**Figma source:** "ModalsCenter" library component, Reader Dashboard v2.0. **Live source:** East Bay Times preprod, account-verification flow.

### 13.1 Card border mismatch

Figma's ModalsCenter has a 1px `color/gray/300` border on the card; the live card was recorded relying on shadow only, with no border distinguished. Both may be true (a subtle border could be present but visually indistinguishable from the shadow) — not resolved either way.

**Status:** Open.

### 13.2 Backdrop opacity mismatch

Live backdrop is 45% black; the Figma-modeled value is 50% black — close, and not even built into the component as a literal property either way.

**Status:** Open — low priority.

### 13.3 Fixed 444px width, narrow-viewport behavior untested

The modal card is a fixed 444px, not fluid/responsive. Behavior at narrow viewports has not been tested.

**Status:** Open.

### 13.4 Password "Update" flow is unstyled design debt

Clicking "Update" for password doesn't open a modal — it navigates to a separate, essentially unstyled page (`/reset-password/`: Arial font, square corners, plain black button border, default gray input border) that matches none of the design system.

**Action needed:** This is design debt to flag, not a pattern worth capturing faithfully — needs a real design pass, not a Figma-matching exercise.

**Status:** Open.

### 13.5 Destructive-action modals unexplored

Only the account-verification modal was captured live. Other triggers (e.g. canceling a subscription) were deliberately not explored to avoid triggering irreversible account actions, so their modal spec is unconfirmed.

**Status:** Open — needs a human to click through and report back rather than automated exploration.

---

## 14. Reader Dashboard — Disclosure

### 14.1 Two competing disclosure/accordion patterns need reconciliation

Production's live Reader Dashboard (e.g. chicagotribune.com/user-tools/dashboard) uses a chevron/icon-based accordion pattern, different from the simpler text-link toggle documented from preprod (the pattern actually built in Figma). The chevron pattern is currently out of scope because that surface is being replaced — but if it survives the replacement, the two patterns will need to be reconciled into one.

**Status:** Open — contingent on what survives the Reader Dashboard replacement.

### 14.2 Coverage and behavior gaps

Only one instance of the disclosure pattern (Login Methods on Profile) was found and tested; other tabs (Subscription, Benefits, etc.) weren't checked for additional instances. Whether expand/collapse is animated or instant was never confirmed.

**Status:** Open.

---

## 16. Containers, Images & Ad Units

### 16.1 `object-fit: fill` on card images — distortion risk

Both hero and feature-medium images use `object-fit: fill` with no `aspect-ratio` set, meaning images are stretched to exactly fill their container rather than cropped-to-fill (`cover`). Distortion is currently minimal because sampled images happen to be close to the container's aspect ratio, but an editor uploading an off-ratio image would visibly stretch/squash it.

**Action needed:** Confirm with engineering whether `fill` is intentional or should be `cover`, since this is a live distortion risk on any off-ratio upload.

**Status:** Open.

### 16.2 Main content container width — Chicago Tribune vs. Denver Post

Chicago Tribune's `main` container measures 1260px at a 1280px viewport; Denver Post measures 1245px at the same viewport — a real 15px difference, not explained by Denver Post running a different theme (it doesn't — confirmed both load real shared theme stylesheets with their own Customizer overrides, same pattern as every other site).

**Status:** Open — not root-caused; could be a scrollbar-width artifact of that specific page load rather than a genuine CSS difference.

### 16.3 Orlando Sentinel — ad slots register lazily on mobile homepage

On Orlando Sentinel's mobile homepage, only the `mobile_adhesion` slot registered with Google Publisher Tag at initial load; the other 10 ad containers exist in the DOM but didn't register in `getSlots()` even after scrolling most of the page and waiting. This looks like Freestar (Orlando Sentinel's header-bidding wrapper, different from the other 5 pilot sites) registering slots lazily/progressively rather than upfront.

**Action needed:** Confirm with engineering whether this is expected Freestar behavior or worth a longer dwell-time re-check.

**Status:** Open.

### 16.4 No visible ad-disclosure label

No "Advertisement"/"Sponsored" text label or `aria-label` was found near any ad container on any of the 6 pilot sites — only Google's own AdChoices icon (rendered inside the ad iframe itself, not site-authored markup).

**Action needed:** Confirm with engineering/legal whether the absence of an explicit disclosure label at the container level is intentional, since AdChoices alone is a weaker disclosure than what many other publishers use.

**Status:** Open — legal/compliance relevance.

---

## 17. Navigation

### 17.1 Obituaries page — hamburger + "All Sections" both visible at desktop width

**Figma / platform rule:** On the homepage, the hamburger icon is only visible at ≤1039px.

**Production:** On the Obituaries page, at a comfortably-desktop viewport, both the hamburger icon and the "All Sections" button are visible simultaneously — confirmed on all 6 pilot sites (Chicago Tribune, Denver Post, OC Register, Orlando Sentinel, Greeley Tribune, mcall.com), including at a 1728px viewport.

**Action needed:** Still not explained — genuinely flagged to engineering to confirm whether this is intentional for the Obituaries template or a bug.

**Status:** Open.

### 17.2 Cross-site avatar inconsistency for the same logged-in account

Cross-site SSO is confirmed working (same session carries from one site to another with no re-login). But for the identical account, Denver Post rendered an actual photo avatar while Orlando Sentinel rendered a generated initials badge ("PA").

**Action needed:** Confirm whether this is a per-site fallback difference (e.g. photo failed to load/sync on one site) or a real bug.

**Status:** Open — not root-caused.

### 17.3 Reader Dashboard's own breakpoint convention differs from the marketing site's

The Reader Dashboard treats 1024×768 and 1280×960 as "menu always visible," a 1024px breakpoint — different from the audited 1039px rule on the main marketing-site nav. Since the Dashboard is a distinct web app from the shared marketing-site theme, this may be a legitimately different, real breakpoint rather than a conflict.

**Status:** Informational / low priority — flagged for awareness, not treated as an error.

### 17.4 Hidden duplicate nav `<li>` artifacts

On some categories (confirmed on Sports), the individual sub-section links (e.g. Chicago Bears, Bulls, Blackhawks, Cubs, White Sox) exist twice: once in the real working sub-menu, and again as `class="hidden"` top-level `<li>` siblings directly in the nav — apparent unused WordPress nav-menu artifacts.

**Status:** Open — worth a cleanup pass, low risk/low priority.

### 17.5 Device-class first-paint timing (Denver Post, mcall.com)

A device-signal CSS class is added client-side (confirmed not server-side) slightly later on Denver Post and mcall.com than the other 4 sites — likely real device detection working correctly, just applied a beat slower on those two.

**Action needed:** Worth asking engineering whether any component's CSS actually depends on this class being present at first paint. If nothing does, this needs no action.

**Status:** Open — low priority, likely closable with a single confirmation.

---

## 18. Ad Units — Homepage "Ad Blocks" slot after Blueconic/Most Popular is undersized (300×250 instead of 300×600)

**Found:** 2026-09-14, during the five-width (340/360/768/1024/1280) homepage production-parity audit.

**Figma action taken:** Per Karl's instruction, this ad instance was updated in Figma to the production-accurate `Cube 1 RRail ATF 300x600` block at every width where it appears (Mobile 340/360, and the new 768/Tablet build), replacing the previous `Cube Article 300x250` placeholder — specifically so the Figma mockups now make this gap visible rather than quietly matching the undersized code.

**Figma spec (now, post-fix):** `Cube 1 RRail ATF 300x600` — matches the size production is actually observed serving.

**Production:** Live GPT ad-slot scanning (`iframe[id^="google_ads_iframe"]` DOM query, cross-referenced against scroll position) on ocregister.com found this slot — `cube2_rrail_mid` — rendering at 300×600 at both mobile (340/360) and tablet (768) widths, at every width checked.

**Action needed:** Confirm whether the live implementation for this ad slot is intentionally 300×250 somewhere in code (unlikely, given production itself serves 300×600 into it) or whether this was simply never corrected after being built against an earlier/incorrect spec. Since Figma now shows the corrected 300×600 size, any remaining 300×250 assumption in the live templates should be treated as the bug to fix, not Figma.

**Status:** Open.

---

## 19. Masthead — Top-leaderboard ad slot renders at inconsistent sizes across page types

**Found:** 2026-09-15, during the Masthead breakpoint audit (`breakpoint-audit.md`), 375px (mobile) pass, comparing OC Register live production against the `Masthead` component set (WordPress Elements → Menus and Parts).

**Figma spec (as of this finding, before the Figma fix below):** The `Masthead` component's `Default`-state ad placement was inconsistent across `Page` variants — Home showed an ad box labeled "Top Leaderboard 320x100," while Section Front and Article showed no ad at all beneath the masthead.

**Production:** The same ad position (`div-gpt-ad-top_leaderboard`, directly below the masthead) renders at different sizes depending on page type, confirmed live at 375px width:

| Page | Live ad size |
|---|---|
| Home | 320×50 |
| Section Front (`/news/`) | 320×100 |
| Article | 320×50 |

**Decision (Karl, 2026-09-15):** This needs to be fixed in production so the top-leaderboard ad slot displays consistently. Figma has been updated (see below) to show the ad on all three page types at their live-measured sizes, so the intended placement is now visible as a reference for engineering.

**Figma action taken:** Added/corrected the ad placeholder on all three `Default`-state Page variants of the `Masthead` component (SM-Mobile tier): Home corrected to `Top Leaderboard 320x50` (was mislabeled 320x100), Section Front now shows `Top Leaderboard 320x100`, Article now shows `Top Leaderboard 320x50` — each matching what production actually serves at that page type.

**Action needed:** Engineering to reconcile the production-side inconsistency — confirm whether the top-leaderboard slot is intended to serve a uniform ad size across Home/Section Front/Article, and align production accordingly.

**Status:** Open.

---

## 20. Masthead — Top nav bar overflows its container at the 1040–1279px (Tier 4) breakpoint

**Found:** 2026-09-15, during the Masthead breakpoint audit (`breakpoint-audit.md`), XL-Desktop tier, comparing Chicago Tribune live production (one of the standing 6-site review list) against the `Masthead` component set (WordPress Elements → Menus and Parts).

**Production:** At 1040px width — the real breakpoint where the header switches to the full desktop nav — Chicago Tribune's top nav row (`.nav-primary`, 11 items: Business, Entertainment, Education, Immigration, Opinion, Politics, Sports, Suburbs, Chicago Magazine, Obituaries, BestReviews) does not fit within its container. The row's actual rendered width (1100.8px) is wider than its wrapper (973.75px). Because the page sets `overflow-x: hidden` on `<body>`, the row doesn't scroll into view — it's centered on the container and the overflow is simply clipped, cutting the first and last items off mid-word on both the left and right edges. No responsive fallback (smaller font, reduced spacing, wrapping, or item overflow menu) kicks in at this width.

Cross-checked against the standing 6-site list: Chicago Tribune and Orlando Sentinel both carry 11 top-nav items (the most of the 6 sites checked — OC Register 8, Denver Post 9, The Morning Call 10, Greeley Tribune 7), so this is the realistic worst case for how many items the nav needs to support, not an edge case.

**Figma spec (before this fix):** The `Masthead` component's top nav row was sized to fit neatly within its 1040px-wide container at whatever item count each page variant happened to have (7–10 items), with no representation of what happens once a site's real item count exceeds what the row can hold.

**Decision (Karl, 2026-09-15):** Build the Figma component to match production's actual (broken) treatment rather than hide the problem — the nav bar should visibly overflow and clip the same way Chicago Tribune's does, so the gap is obvious to anyone reviewing the component, and flag it here for engineering to fix in production.

**Figma action taken:** Brought all three `Default`-state Page variants (Home, Section Front, Article) of the XL-Desktop `Masthead` component up to 11 top-nav items each (added placeholder items to match Chicago Tribune's count), left the nav row at its natural/uncompressed content width (no longer force-fit to the container), and set the row's parent container to clip content at the component's 1040px bounds. The result: the nav row is centered and overflows past both edges, with the first and last items cut off mid-word — matching Chicago Tribune's live behavior.

**Action needed:** Engineering to add real responsive handling for the top nav at the 1040–1279px tier when the site's item count is high enough to overflow — options include a smaller font/tighter spacing at this tier, wrapping to a second line, or an overflow ("More") menu for items past what fits. Whatever the fix, it needs to apply platform-wide, not just to Chicago Tribune, since Orlando Sentinel hits the same 11-item count and any other site could grow into it.

**Addendum (2026-09-22):** The clipping isn't fully resolved even at the widest Desktop tier — while fixing an unrelated Masthead side-margin bug at 1024/1100 (WordPress Elements → Homepage, the homepage template audit §3.58, since retired), the same fixed-width `Top Nav` row (1322px) was found still clipped by ~21px per side at the full 1280px Desktop width, versus ~118.5px per side at 1100px. So this isn't strictly a "1040–1279px tier" problem that clears up at Desktop — it's a continuum that only becomes fully invisible somewhere above 1322px of available nav width. Doesn't change the action needed above, just widens the affected range engineering should account for.

**Status:** Open.

---

## 21. Masthead — Article scrolled-state headline overflows behind the bookmark/share icons

**Found:** 2026-09-15, during the Ad-Free Masthead audit (`breakpoint-audit.md`), 1100px pass, Article page, scrolled state, logged into an ad-free account.

**Production:** In the scrolled masthead on an article page, the breadcrumb + headline (`.article-title`, e.g. "National Politics | Judge blocks Kennedy Center board from putting…") renders at its full natural width based on the actual headline's length. The bookmark/save icon (`.saveArticleButton`) sits at a fixed horizontal position in the same row that does not account for how long the rendered headline actually is. For a headline long enough — this one included — the tail end of the headline text renders directly underneath the bookmark icon instead of stopping short of it, so the last few characters are visually obscured rather than cleanly truncated with an ellipsis.

Confirmed via DOM inspection at 1100px: the headline's own bounding box spans x 462–847px; the bookmark icon sits at x 778–809px — a 69px overlap.

**Also confirmed at 1040px** (2026-09-15, same Ad-Free audit pass, same article): the overlap is worse at this narrower width — headline box spans x 430–815px, bookmark icon sits at x 720–751px, a 95px overlap. Visually, the bookmark icon now sits directly on top of a word in the headline rather than just clipping the tail end.

**Also checked at 1728px** (2026-09-15, same audit pass, same article, Karl's full screen width): no overlap at all — the headline's container (`.entry-title`) correctly sizes down and its text box's right edge (x 1185px) sits 241px clear of the share widget's left edge (x 1426px).

**Root cause identified — this is a narrow-viewport layout bug, not a headline-length coincidence:**

| Width | Overlap |
|---|---|
| 1040px | 95px (worst) |
| 1100px | 69px |
| 1728px | none — 241px clearance |

The headline's flex/width allocation fails to shrink correctly relative to the fixed-width share-icon widget below some threshold between 1100px and 1728px — narrower windows make it worse, not better, which is the opposite of what a simple text-truncation gap would produce. This isn't tied to ad-free/logged-in state specifically — it would happen for any sufficiently long headline at a narrow-enough width regardless of login state — but was caught during the ad-free audit pass.

**Figma spec:** Not reproduced. Figma's Article `Scrolled` variant uses a fixed placeholder headline ("Roughly forty characters of the article t...") short enough that it doesn't hit this edge case, so the component itself doesn't currently demonstrate the bug. Unlike the Tier 4 top-nav overflow (entry #20, a systemic issue reproducible with any content at that width), this one only shows up in the narrower part of the desktop range, so it wasn't rebuilt into the static mock — it's flagged here for engineering instead.

**Action needed:** Give the headline element a max-width (or text-overflow: ellipsis truncation) tied to the actual available space before the bookmark/share-icon cluster at all desktop widths, not just the wider end of the range — the current layout only holds up above ~1700px.

**Status:** Open.

---

## 22. Masthead — Reader Dashboard shows the top nav-links row and "TRENDING:" bar, which the design explicitly excludes

**Found:** 2026-09-15, during the Reader Dashboard masthead audit (`breakpoint-audit.md`), on canoncitydailyrecord.com/dashboard/, logged in as a subscriber, at 1100px and 1040px (both above the masthead's 1039px desktop-nav threshold).

**Production:** At desktop widths, the Reader Dashboard's masthead renders the full top nav-links row (News / Local News / Sports / Things to Do / Opinion / Obituaries / Marketplace / On the Record / BestReviews) and a "TRENDING:" bar (e.g. "Fremont County Nonprofit Guide 2026," "Royal Gorge Living") above the breadcrumb and page content — the same two rows Home's masthead shows at this tier.

**Figma spec:** The `Masthead` component's `Device=XL-Desktop, Page=Dashboard` variant (`456:2715`, and the equivalent `Scrolled` variant `456:2840`) does **not** include a nav-links row or trending bar — it's just the top utility row (hamburger/All Sections, avatar, search) plus the weather/date/logo row, at 144px total versus Home's 497px 4-row structure.

**Decision (Karl, 2026-09-15):** Figma is correct — the Reader Dashboard should **not** display the trending bar or top navigation. What production shows at canoncitydailyrecord.com/dashboard/ is the bug, not a Figma gap. No Figma changes made.

**Action needed:** Engineering to suppress the nav-links row and "TRENDING:" bar on the Reader Dashboard page template at desktop widths, so it matches the intentionally-minimal masthead Figma already models.

**Note:** confirmed only on canoncitydailyrecord.com (the one site used for this phase, per Karl's direction) — not cross-checked against the other 5 repertoire sites.

**Status:** Open.

---

## 23. Video carousel ("Videos from @OCRegister") — fixed-height iframe leaves ~200px of unused blank space at narrow (340–360px) widths

**Found:** 2026-09-16, during a systematic 340px/360px breakpoint sweep across all homepage components (per Karl — checking widths narrower than any explicit CSS breakpoint, since 640px is the first real tier boundary). Verified twice: once via a narrowed real desktop Chrome window, and again via true mobile device emulation (Pixel 9 UA, touch-enabled, no desktop scrollbar) at both 340px and 360px, on ocregister.com.

**Production:** The `.dfm-page-middle-flex-container` block (a single Flourish-hosted `<iframe src="https://flo.uri.sh/visualisation/21363813/embed" title="Video from @OCRegister">`) renders at a fixed height of 490px at both 340px and 360px viewport widths. At these widths the visible content inside the iframe — header ("Videos from @OCRegister"), subtitle, the row of video tiles, and the horizontal scroll-indicator bar — only fills roughly the top 260–265px of that height, leaving about 200px of blank white space below the scroll indicator before the next section (Photos) begins. Confirmed identically at both 340px and 360px, and identically whether tested via a narrowed desktop window or true mobile emulation, so this isn't a testing-methodology artifact — it's a real rendering behavior at these widths.

**Figma spec:** The `Videos from OCRegister Carousel` component (built 2026-09-16, see the homepage template audit section 3.35, since retired) sizes its outer frame to HUG its actual content height at every placed width — header + subtitle + tile row + scroll indicator, with no trailing blank space. It does not reproduce this gap, since the gap appears to be a property of the live Flourish embed's own fixed iframe height, not something the surrounding page template's CSS controls (no dedicated `@media` rules were found for `.dfm-page-middle-flex-container` itself in this or the earlier 3.2x-era investigation).

**Action needed:** Since the iframe height is most likely set via the Flourish visualisation's own embed configuration rather than page-template CSS, this is probably a Flourish-settings fix rather than a template fix — either make the embed size its iframe responsively to actual content height at narrow widths, or set a shorter fixed height specifically for the sub-640px range. Flagging for whoever owns the Flourish embed configuration to confirm whether that's adjustable there.

**Status:** Open.

---

## 24. Spacing — 10px and 14px values off the 4/8 grid

**Found:** 2026-10-01, while creating the spacing tokens. Measured live on chicagotribune.com (homepage, 1728px viewport, every visible element's padding, margin and gap).

**Figma spec (source of truth):** spacing follows the 4/8 grid. The main file's "Spacing & Radius" collection has `spacing/050` 4, `spacing/100` 8, `spacing/150` 12, `spacing/200` 16, `spacing/250` 20, `spacing/300` 24.

**Decision (Karl, 2026-10-01):** 10px and 14px are production drift, not design values. They are not tokens; production should move to the nearest grid value.

**Production:**

| Where | Live value | Fix |
|---|---|---|
| `.subscribe-button` (header, footer and article paywall CTA) | padding 14px / 10px | Use Button Primary Default: 16px / 20px (`spacing/200` / `spacing/250`). Same fix as entry 11. |
| Main content wrapper (left/right page gutter) | padding 0 10px | Use `spacing/100` (8px) or `spacing/150` (12px); confirm with design which one. |
| `ul.footer-menus`, `div.colophon` | padding 0 10px | Same as the page gutter. |

**Context:** on that page 10px appears 17 times. The grid values are far more common (16px 79, 12px 46, 32px 36, 8px 34, 4px 28). Other off-grid values also appear (15px 38, 17px 20, 19px 17, 3px 28) and should be reviewed in a later pass.

**Engineering patch (ready to apply):**

```css
/* 24a. Subscribe CTA = Button Primary Default (also closes entry 11) */
.subscribe-button {
  padding: 16px 20px;   /* was 14px 10px; spacing/200 vertical, spacing/250 horizontal */
  font-size: 14px;      /* was 15px */
}

/* 24b. Page gutter. GUTTER = 8px (spacing/100) or 12px (spacing/150), pending Karl */
.main-content-wrapper,   /* placeholder: the wrapper with padding: 0 10px today */
ul.footer-menus,
div.colophon {
  padding-left: GUTTER;  /* was 10px */
  padding-right: GUTTER; /* was 10px */
}
```

Check after the change: the subscribe CTA keeps its 44px min height and its fill color per masthead, and the header, body and footer edges still line up with each other.

**Status:** Open. 24a is ready for Engineering. 24b needs one design decision first (8px or 12px).

---

## 25. Radius — buttons are 4px; 5px on a button is drift

**Found:** 2026-10-01. Live check of chicagotribune.com and ocregister.com (homepage and article) and denverpost.com (homepage): every button uses 4px (Subscribe Now, newsletter Sign Up buttons). Figma's Button Primary, Secondary, Tertiary and Linkstyle were already 4px.

**Decision (Karl, 2026-10-01):** button radius is 4px across the board (`radius/sm`). In Figma, Action Button, Button Action and Button ActionMenu were changed from 5px to 4px, and every button shape is now bound to `radius/sm`. `radius/utility` (5px) stays, for containers only (Karl, 2026-10-01).

**Production:**

| Where | Live value | Fix |
|---|---|---|
| Search submit button (`.search-button`, masthead search form; see `components/navigation.md`) | border-radius 5px | Use 4px (`radius/sm`). |
| Account dropdown panel (masthead; see `components/navigation.md`) | border-radius 0 0 5px 5px | No fix. It's a container, so 5px (`radius/utility`) is correct. |

**Containers keep 5px (`radius/utility`):** InLineMessage containers, ModalsCenter parts, Form Field shapes, check boxes, the status badge and the account dropdown. In Figma their 5px corners are bound to `radius/utility`.

**Engineering patch (ready to apply):**

```css
/* 25a. Masthead search submit = button radius */
.search-button {
  border-radius: 4px;   /* was 5px; radius/sm */
}
/* Leave the account dropdown at 0 0 5px 5px (radius/utility, container). */
```

**Status:** Open. Ready for Engineering.

---

## 26. Mobile adhesion — empty sticky bar shows at 1024px and up

**Found:** 2026-10-02, ocregister.com at a 1024px window (homepage and article page).

**Figma spec (source of truth):** `mobile_adhesion` exists only below 1024px — Ad Blocks `Mobile Adhesion 320x50` / `300x50` on mobile and `Mobile Adhesion 728x90` at tablet (768). The 1024, 1100 and 1280 templates have no adhesion unit (the 1024 floating anchor was removed 2026-10-02).

**Production:** at 1024px the `#mobile-adhesion` container is still fixed to the bottom of the viewport (1024×90, with its Close button), but the GPT slot has no valid size at that width (`getSizes(1024)` returns an empty list), so no ad can ever load. Readers see an empty bar.

**Fix:** hide the `#mobile-adhesion` container (and its Close button) at the same breakpoint where the slot's size mapping goes empty (≥1024px), or remove the container from the DOM at desktop widths. Check the other five review sites.

---

## 27. Blueconic Block (Most Popular) — list spacing and item headline

**Found:** 2026-10-07, ocregister.com at 360, 768, 1024, 1100 and 1280px (homepage "Most Popular", `.dfm-most-popular-flex-container` inside `landing-three-one` → `.three-one-left`).

**Figma spec (source of truth):** WordPress Elements `Blueconic Block (Most Popular)` (`3352:20526`) with `Most Popular List Item` (`3352:24171`) kept at **44px** tall per item. The space between items is added in the block (column auto-layout gap), not in the item.

### 27.1 Item spacing and column gaps

Production stacks the items with no gap. Each row is 60px tall for a one-line headline and 77px for two lines. Design keeps the item at 44px and adds the difference as the gap between items, so a one-line row lands on production's 60px.

| Width | Columns (production) | Design column gap | Design item gap |
|---|---|---|---|
| 360 (Mobile) | 1 × 340 | — | 16 (`spacing/200`) |
| 768 (Tablet) | 2 × 365 | 19 | 16 (`spacing/200`) |
| 1024 | 2 × 288 (every headline wraps to 2 lines) | 19 | 11 (fits the 77px two-line row) |
| 1100 | 2 × 360 | 21 | 16 (`spacing/200`) |
| 1280 | 2 × 459 | 22 | 16 (`spacing/200`) |

### 27.2 Spacing values with no token — remove in a future pass

The gaps of **11, 19, 21 and 22** px come from production's fluid layout and are kept in Figma as plain numbers on purpose. There are no tokens for them, and none should be created. When engineering moves these blocks onto the spacing scale (4 / 8 / 12 / 16 / 20 / 24), replace them: 11 → 12 (`spacing/150`), 19 / 21 → 20 (`spacing/250`), 22 → 24 (`spacing/300`) or 20, and update the Figma gaps to match. 16 and 20 are already bound to `spacing/200` / `spacing/250`.

### 27.3 Item headline type

| | Production (all widths) | Design (`Most Popular List Item`) |
|---|---|---|
| Headline | Noto Serif **600**, 16px / **17.07px** | Noto Serif **Bold (700)**, 16px / **auto (~22px)** |

One-line items are unaffected (the 44px height holds), but every extra line adds about 5px more in design than in production. Two-line rows are 66px plus the gap in design versus 77px in production, and three-line rows grow further apart. **Decision (Karl, 2026-10-07): keep the Figma item as is** — 44px tall, Noto Serif Bold 16 / auto. This is a known difference, not a Figma bug; production should move to the design's type if it's ever aligned.

---

## 28. Reader Dashboard — breakpoints close to, but not on, the Figma screen widths (questions for DigiScrum)

**Found:** 2026-10-14, in the Reader Dashboard source (`plugins/mng-digital-subscriber-widgets/reader-dashboard-src/`, Karl's local copy of the website repo dated 2026-05-08) and its built CSS. **Team:** DigiScrum. *Live check still to do: confirm the current production build matches this copy.*

**Design (source of truth):** Reader Dashboard v2.0 is designed at 5 screen widths: Fold 340, Mobile 360, Tablet (vertical) 768, Tablet (horizontal) 1024, Desktop 1280. These are the MNG Device breakpoints (min-widths 360 / 768 / 1024 / 1280; Fold is everything below 360).

**Production:** 768 (`md`, `min-[768px]`), 1024 (`lg`, `window.innerWidth >= 1024`) and 1280 (`xl`) match. Four values don't, and they are too close to the design widths to be accidents, so **this entry asks why before asking for a fix** (Karl, 2026-10-14). The repo copy has no git history or code comments explaining them; the likely reasons below are inferred.

| Production value | Where it's used | Likely reason | Question for DigiScrum |
|---|---|---|---|
| `min-[361px]` | text field size and height, inline form box padding, menu width (344px), page margins, display-name form (`text-field.tsx`, `inline-form-box.tsx`, `reader-dashboard.tsx`, `update-display-name.tsx`) | "Wider than 360": 360 is the most common Android phone width and Figma's largest phone frame. The compact phone styles apply at 360 and below; the roomier ones start at 361. Figma has no design between 361 and 767, so the team picked where the roomier layout starts. | Is 361 meant as "wider than the 360 Mobile frame"? Should the roomier styles start at 360 (Figma's Mobile) or stay at 361? |
| `min-[413px]` | "No articles saved" empty state alignment (`no-articles-saved.tsx`) | "Wider than 412": 412 is a common large-Android width. Likely a fix for a wrap seen on a specific phone. | Was this a fix for a specific device? Could it use 360 or 768 instead? |
| `sm` 640 (40rem) | logout status width (`logout-status.tsx`, `sm:w-fit`) and Tailwind's `.container` | Tailwind's default `sm` screen, left in place (the team didn't set its own screens). | Was 640 chosen, or is it Tailwind's default? Could it be 768? |
| `2xl` 1536 (96rem) | Tailwind's `.container` max width only; no `container` class found in the dashboard source | Tailwind's default `2xl` screen, generated automatically. | Can it be removed? |

**Next step:** ask DigiScrum the questions above. Depending on the answers, each value becomes part of the Device set (if a new screen width is really needed, Figma gets a matching frame first), a documented component breakpoint, or a fix. Our generated Tailwind screens (`dist/tailwind/`) can replace Tailwind's defaults so `sm` / `2xl` disappear.

**Status:** Open — waiting on DigiScrum's answers.

---

## 29. Obituaries — breakpoints that don't match the WordPress grid (for the CMS team)

**Found:** 2026-10-14, in the Obituaries styles (`assets/client/scss/layouts/scng/components/features/_obits.scss` in the WordPress themes, Karl's local repo copy dated 2026-05-08) and the 2026-09-15 live audit of the Obituaries pages (`components/breakpoint-audit.md`). **Team:** CMS. *Live check still to do.*

**Design (Karl, 2026-10-14):** Obituaries is built on the WordPress theme grid (it uses the theme's `ai-breakpoint()` mixin), so it belongs to the WordPress layer and follows the **WordPress grid breakpoints**: `xs` 320, `s` 640, `m` 800, `l` 1040, `xl` 1280 (min-widths; written as max-widths 639 / 799 / 1039 / 1279). Values that don't match the grid are drift for the CMS team to correct in the future.

**Production:**

| Production breakpoint | Where it's used | Matches the WordPress grid? | Snap to |
|---|---|---|---|
| `ai-breakpoint` `s` / `m` / `l` (640 / 800 / 1040) | spacing and layout | Yes | none |
| ≥1040px (`65em`) / ≤1039px (`64.9375em`) | horizontal layout / 2-column upper bound | Yes (`l`) | none |
| 800px (`50em`) | filter panel padding when open | Yes (`m`) | none |
| ≤624px (`39em`, and a raw `624px` rule) / ≥625px (`39.0625em`) | 1-column layout and search form stacking / 2-column start | No | 640 (`s`) |
| ≥1300px (`81.25em`) / ≤1299px (`81.1875em`) | listing and "stop scaling" | No | 1280 (`xl`) |
| 1000px (`62.5rem`) | top and bottom leaderboard ad placement | No | 1040 (`l`) |
| 625–734 / 735–1299px | photo gallery widget (likely shared, not obituary-only) | No | 640 / 800 / 1280 |

**Fix (future, CMS team):** move each non-matching rule to the grid breakpoint in the right-hand column. The gallery widget and the 1000px ad rule may be shared with other pages; confirm before changing them. The Masthead's Obituaries search widget (624) is part of this fix.

**Status:** Open (future).

---

## 30. Breakpoints off the official sets — WordPress themes, trust indicators, digisubs (all 6 sites)

**Found:** 2026-10-14, live CSS scan of the homepage, an article and the obituaries page on all 6 review sites (`tokens/breakpoint-inventory.json`, built by `scripts/breakpoint-inventory/`). Every value below was found on all 6 sites (the three theme stylesheets share their media queries). **Teams:** CMS, DigiScrum. **Updated 2026-10-14** with Karl's decisions.

**Design:** two official sets (EXPORT-STANDARD.md section 6). WordPress code follows the **WordPress grid** (min-widths 320 / 640 / 800 / 1040 / 1280; max-widths 639 / 799 / 1039 / 1279). Everything else, including the digisubs plugin and app (Karl, 2026-10-14), follows the **MNG Device breakpoints** (min-widths 340 / 360 / 768 / 1024 / 1280; max-widths 339 / 359 / 767 / 1023 / 1279). Of the 56 values kept in the inventory, 13 are official, 34 are drift (below) and 9 are component breakpoints. Left out: third-party code (paywall, cookie consent, ad vendors), the WordPress admin bar, and the digisubs modal, spoof banner, push prompt, share box and employee debugger (not documented, Karl), and the special investigative header template (see below).

**Production (drift) and fix:** move each rule to the official breakpoint in the right-hand column. The Sports Radar template and the promotion widget follow the WordPress grid (Karl, 2026-10-14). "Off by one" rules (`max-width: 340 / 360 / 800 / 1024 / 1040 / 1280`) overlap the official boundary by 1px and should be one less. The Obituaries values (624 / 625, 1299 / 1300) and the photo gallery (734 / 735) are also in entry 29.

**WordPress themes** (team: CMS; snap to the WordPress grid):

| Production | Where | Snap to |
|---|---|---|
| `(max-width: 405px)` | Sports Radar page template (#content.sports-radar-content; local template styling embedded Sportradar data widgets). | `(max-width: 639px)` (WordPress grid s) |
| `(max-width: 500px)` | Sports Radar page template. | `(max-width: 639px)` (WordPress grid s) |
| `(max-width: 535px)` | Sports Radar page template. | `(max-width: 639px)` (WordPress grid s) |
| `(max-width: 624px)` | Obituaries 1-column layout (entry 29). | `(max-width: 639px)` (WordPress grid s) |
| `(min-width: 625px)` | Obituaries 2-column start (entry 29). | `(min-width: 640px)` (WordPress grid s) |
| `(max-width: 700px)` | Promotion widget (.promotion-widget, homepage promo tiles, e.g. Chicago Tribune Fun and Games / Tribune Store). | `(max-width: 639px)` (WordPress grid s) |
| `(max-width: 734px)` | Photo gallery widget (.gallery-container; also entry 29). Fix (Karl). | `(max-width: 799px)` (WordPress grid m) |
| `(min-width: 735px)` | Photo gallery widget (also entry 29). Fix (Karl). | `(min-width: 800px)` (WordPress grid m) |
| `(max-width: 800px)` | Off by one: (max-width: 800px) overlaps m; should be 799 (#featured-flex-landing-three). | `(max-width: 799px)` (WordPress grid m) |
| `(max-width: 900px)` | Promotion widget title. | `(max-width: 799px)` (WordPress grid m) |
| `(max-width: 930px)` | Footer cookie notice button (Karl: fix to 1039). | `(max-width: 1039px)` (WordPress grid l) |
| `(max-width: 960px)` | Sports Radar page template. | `(max-width: 1039px)` (WordPress grid l) |
| `(max-width: 1280px)` | Off by one: (max-width: 1280px) overlaps xl; should be 1279 (.custom-dfm-section.dark-layout). | `(max-width: 1279px)` (WordPress grid xl) |
| `(max-width: 1299px)` | Obituaries listing (entry 29). | `(max-width: 1279px)` (WordPress grid xl) |
| `(min-width: 1300px)` | Obituaries "stop scaling" (entry 29). | `(min-width: 1280px)` (WordPress grid xl) |

**dfm-trust-indicators plugin** (team: CMS; snap to the WordPress grid):

| Production | Where | Snap to |
|---|---|---|
| `(max-width: 1040px)` | Off by one: (max-width: 1040px) overlaps l; should be 1039 (trust-indicator footer links). | `(max-width: 1039px)` (WordPress grid l) |

**mng-digisubs plugin (account menu, regwall, sign-in, modals)** (team: DigiScrum; snap to the MNG Device set):

| Production | Where | Snap to |
|---|---|---|
| `(max-width: 340px)` | Off by one: (max-width: 340px) overlaps fold; should be 339. | `(max-width: 339px)` (MNG Device fold) |
| `(max-width: 450px)` | Digisubs modals, paywall container, regwall form, save-article and nickname modals, account dropdown (37 rules). | `(max-width: 359px)` (MNG Device mobile) |
| `(max-width: 550px)` | Regwall (:root:not(:has(#server-regwall))). | `(max-width: 359px)` (MNG Device mobile) |
| `(max-width: 576px)` | Digisubs content (.sspw-content). | `(max-width: 767px)` (MNG Device tablet) |
| `(max-width: 600px)` | Shared with the theme. Digisubs change-username modal: snap to Device tablet. Theme article bottom share buttons (.article-bottom-share): snap to WordPress grid s. | `(max-width: 767px)` (MNG Device tablet) / `(max-width: 639px)` (WordPress grid s) |
| `(max-width: 770px)` | Account dropdown menu. | `(max-width: 767px)` (MNG Device tablet) |
| `(max-width: 820px)` | Account dropdown menu. | `(max-width: 767px)` (MNG Device tablet) |
| `(max-width: 1024px)` | Off by one for the Device set (should be 1023); the theme rule (#dfm-digisubs-menu) should use grid l (1039). | `(max-width: 1023px)` (MNG Device tablet-landscape) |

**Digisubs app, plugins.mngdigisubs.com (Bootstrap 5 defaults)** (team: DigiScrum; snap to the MNG Device set):

| Production | Where | Snap to |
|---|---|---|
| `(max-width: 360px)` | Off by one: (max-width: 360px) overlaps mobile; should be 359. | `(max-width: 359px)` (MNG Device mobile) |
| `(max-width: 400px)` | Sign-in modal. | `(max-width: 359px)` (MNG Device mobile) |
| `(max-width: 575.98px)` | Bootstrap sm-down. | `(max-width: 767px)` (MNG Device tablet) |
| `(min-width: 576px)` | Bootstrap sm container. | `(min-width: 768px)` (MNG Device tablet) |
| `(max-width: 991.98px)` | Bootstrap lg-down. | `(max-width: 1023px)` (MNG Device tablet-landscape) |
| `(min-width: 992px)` | Bootstrap lg container. | `(min-width: 1024px)` (MNG Device tablet-landscape) |
| `(max-width: 1199.98px)` | Bootstrap xl-down. | `(max-width: 1279px)` (MNG Device desktop) |
| `(min-width: 1200px)` | Bootstrap xl container. | `(min-width: 1280px)` (MNG Device desktop) |
| `(max-width: 1399.98px)` | Bootstrap xxl-down: no official breakpoint above 1280. | `(max-width: 1279px)` (MNG Device desktop) |
| `(min-width: 1400px)` | Bootstrap xxl container: no official breakpoint above 1280. | `(min-width: 1280px)` (MNG Device desktop) |

**Not drift: component breakpoints (keep their own values, Karl):** the Masthead nav icons on very small phones (`max-width: 335px`, `350px`) and the ad rules: top leaderboard (`min-width: 300 / 750 / 1000px`), header banners, the top leaderboard ad container under the masthead (`max-width: 750px`), and the mobile adhesion ad (`max-width: 480 / 1000 / 1025px`). They go in the Masthead and Ad Blocks component tokens (WordPress layer).

**Left out for now:** the special investigative header template (`max-width: 730 / 1150px`, plus 500 / 600 / 750 / 900 / 1024 it shares with other rules). It wasn't found on a live page of the 6 sites. **To do:** find it in production when more article pages are added to WordPress Elements, then classify its breakpoints (Karl, 2026-10-14).

**Status:** Open.

---

## Notes

**Reading live colors:** read themed CSS variables such as `--primary` on `document.querySelector('#page')`, not on `document.documentElement`. The WordPress Customizer's per-site override is scoped to `#page`, so reading at `:root` only shows the theme default.

**Removed entries:** 3 (headline tiers, resolved in design 2026-09-24) and 15 (Reader Dashboard hand-built copies, retired 2026-09-25) were resolved and removed on 2026-10-20; see git history. Their numbers aren't reused, so links to the other entries still work.
