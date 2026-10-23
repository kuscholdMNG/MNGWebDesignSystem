# For You → MNG DS components: status and handoff

> **Updated 2026-10-23** for the import re-test (still hanging; workaround found for every variable the atoms need), the timestamp decision (13px, Karl), and the three card atoms in WordPress Elements ▸ Article Parts (Kicker and Author done; Timestamp waiting on the clock icon). Moved into the repo from the "For You Tab MVP" project the same day.

## Goal

Find every element on the **For You tab** of the v3 prototype that isn't in the MNG design files yet. Build each missing element as a Figma component, using DS variables only. When they're approved, publish them through the MNG Web DS / WordPress Elements libraries.

## Sources

| Source | Location |
|---|---|
| v3 prototype (source of truth for the For You design) | `~/Github/for_you_tab_mvp/claude-design-v3/Main.dc.html`. Canvas: https://claude.ai/artifact/9ZnuwkmmUmwmyPmg15nJBj |
| MNG Web Design System (Figma) | file key `jFHYqhZbJjvWQmDI4myCsd` |
| WordPress Elements (Figma) | file key `b1iZxkFwtAYq9rElmnCAzd` |
| DS repo: tokens, Figma exports for Claude, component specs | `~/Github/mng_web_ds`. See `figma-exports/mng-design-system-export/` (README + `index.json`), `components/*.md` and `tokens/icons/icons.json`. Status log: `MNG-Web-Design-System-Status.md`; production gaps: `design-vs-production.md` |
| Production tabs reference | https://staging.dailylocal.com/world-cup/ |

How the Figma files are connected: Figma Desktop with the Desktop Bridge plugin (figma-console MCP). Pass `fileKey` to `figma_execute` to target a file without switching the active one.

## Decisions (Karl)

- Scope is the For You tab only. The prototype bar's Zones / Rows / Cards toggle is excluded, because it's a prototype control.
- **All atoms go in WordPress Elements.** For anything that isn't an atom, ask Karl where it goes (Web DS or WordPress Elements) before building it.
- **The featured story, card and row are built as variants** of the existing WordPress Elements cards: Zone 1 Lead Article Card, 1Col Article Card and Horizontal Thumbnail Card.
- **Tab labels are "Editor's Picks" / "For You".**
- The tabs come from the production World Cup tabs, not a new design.
- The welcome modal must match the DS **ModalsCenter**, which is already specced in `components/modal.md`. If the prototype differs, fix the prototype.
- Rules: don't invent elements. Use production-accurate atoms wherever they exist. Bind every value to MNG DS variables where a token exists. Log every off-system production value for design-vs-production.

## Done

- **Clock icon added to Icons** in Web DS: the `Name=access-time` variant in the Icons set `4693:5`.
  - Node `7329:25691`, key `ddff0323eec840324a3daf837507144a9db3e2ed`, placed after `newspaper`.
  - 16×16, artwork from Icon Categories `1412:667`, fill bound to `color/gray/min`, font codepoint U+E900.
  - ⚠️ **The Web DS library needs publishing** before WordPress Elements can use this icon.
- **Gap audit complete** (see the table below).
- **Tabs scraped from production** (spec below).

## Blocker: library imports (re-tested 2026-10-23)

**Still broken on Oct 23**, after Karl relaunched the Desktop Bridge plugin in WordPress Elements. `figma.teamLibrary.getAvailableLibraryVariableCollectionsAsync()` and `getVariablesInLibraryCollectionAsync()` now answer in about 0.2s, but `importVariableByKeyAsync` (font/size/10) and `importComponentByKeyAsync` (access-time) still time out (tested at 8s and 22s). Possible cause: the bridge showed two MCP server instances (ports 9223 and 9224) from two Claude sessions.

- Every variable the atoms need is now reachable without an import, because WordPress Elements already uses it somewhere: font/size/13 `VariableID:60351d5c1d19d94946edc9a5c53565709a6a443a/6847:7`, font/size/10 `VariableID:a704424118ebeeef3c4d27cda5966f7801447ba3/6850:36`, font/style/medium `VariableID:1098f60a5a71c40d8f65024a17845de914519c30/7121:5`.
- **Still needs a manual step:** spacing/050 isn't used anywhere in WordPress Elements, and the Web DS Icons set has **unpublished changes** (access-time's publish status is `CHANGED`), so the clock icon isn't in the library yet. Karl publishes the Web DS library, then drags an Icons `access-time` instance into WordPress Elements (or binds the Timestamp gap to spacing/050 in the UI), which brings both in.

On Oct 21, **library imports in WordPress Elements hung.** `figma.variables.importVariableByKeyAsync`, `figma.importComponentByKeyAsync` and `figma.teamLibrary.*` all timed out at 25–30s. Reloading the plugin UI didn't fix it. Simple calls still worked.

- Planned fix: Karl fully closes and relaunches the Desktop Bridge plugin in WordPress Elements, and publishes the Web DS library.
- Workaround for variables the file already uses: find a node bound to the variable, read the variable ID from that node's `boundVariables`, and bind with that ID. These are already available that way:

| Variable | ID |
|---|---|
| color/theme/primary | `VariableID:d1c64621420971547fed613e54b7e0822a530f5b/7273:70` |
| color/gray/min | `VariableID:7e83e612376f9e21a46ac5776f1f05625a3336e2/7273:40` |
| color/gray/200 | `VariableID:bf7944f0fa19f9de12973ef10df59712b4a529da/7273:42` |
| font/size/12 | `VariableID:9537d462e617cebfc2bfa0d6fc40ce490d57d790/6847:3` |
| font/style/bold | `VariableID:65c3559067baa3ba9425ba629531f1c84a34da92/7121:11` |
| font/style/regular | `VariableID:33d7ff699d2ca68a39a43035968bc2240ac395bc/7121:2` |
| font/family/noto-sans | `VariableID:90d59a5504348dcedcac72cd5aa64c84e934918b/6752:40` |

- **Not yet in WordPress Elements** (they need a library import):

| Variable | Library key |
|---|---|
| font/size/10 | `a704424118ebeeef3c4d27cda5966f7801447ba3` |
| font/style/medium | `1098f60a5a71c40d8f65024a17845de914519c30` |
| spacing/050 | `a282b83e1ceef0bb087a5842c613d7a239c76524` |

Bold Coastal token values:

| Token | Value |
|---|---|
| color/theme/primary | #007580 |
| color/gray/min | #141414 |
| color/gray/100 | #393938 |
| color/gray/200 | #5E5D5C |
| color/gray/500 | #CCCAC7 |
| color/gray/max | #FFFFFF |
| spacing/050 | 4 |
| spacing/100 | 8 |

## Gap table

| # | Element | Prototype class | Closest existing | Status / next step |
|---|---|---|---|---|
| 1 | Homepage tabs (Editor's Picks / For You) | `.tabs` | Production World Cup tabs | **New.** Build from the production spec. Ask Karl where it goes. |
| 2 | Feed header "While You Were Away" | `.fyh .eb` | WP Section Title / Eyebrow, Style=Underline (`3333:42278`) | **Exists.** The "Based on what you read." subhead line is new. |
| 3 | Info tooltip | `.tip` | none (the `info` icon U+E937 exists) | **New** |
| 4 | Featured story | `.lead` | Zone 1 Lead Article Card (`3336:46156` / `3336:46155` / `3383:46111`) | **New variant.** Adds a kicker and byline/time. |
| 5 | Article card | `.card` | 1Col Article Card (Style=Media Lead, 16:9) | **New Style variant.** Adds a 1px gray/500 border, 8px radius, kicker and byline footer. |
| 6 | Article row | `.row` | Horizontal Thumbnail Card (`3362:2990` / `3362:2991` / `3383:46153`) | **New variant.** Adds a border, kicker and byline. |
| 7 | Card atoms: kicker, author, timestamp | `.kick` `.au` `.tm` | none (the WP Article Page Byline `1110:19503` is the full article byline) | **Built 2026-10-23** in Article Parts. Kicker `3609:39112` and Author `3609:39115` done; Timestamp `3621:38794` needs the clock icon and the spacing/050 binding (see Blocker). |
| 8 | Load More Articles | `.btn-link` | Button Linkstyle (`5428:3953`) | **Exists.** Check the prototype's styling against it. |
| 9 | Non-subscriber CTA panel | `.cta` | Button Primary / Secondary; WP Paywalls ▸ Engage Paywall Modal (`1495:23511`) | **New.** Compare with the Paywall modal first. |
| 10 | Welcome to For You modal | `.mc-*` | ModalsCenter (`3040:2262`) + Button Modal Close (`5335:16196`) | **Exists.** Parity check against `components/modal.md`. |
| 11 | Onboarding steps 1–3 | `.ob` `.chip` | CheckBox (`4693:690`) | Deferred (hidden in the prototype). Chips are new. |

## Specs ready to build

### Atoms (WordPress Elements)

Place them in WordPress Elements ▸ Homepage ▸ Components (`3334:42288`) ▸ Top Zone Components (`3485:67769`) ▸ Top Zone Parts ▸ **Article Parts**.

Match the existing documentation containers there, for example "Article Status Badge Container":
- White, 8px radius, 16px padding, 16px gap.
- A Header frame with a "Type" line (11 SemiBold #666) and a "Title" (22 Bold).
- A Description line (13 Regular #666).
- A "Variant Grid" frame that holds the component.

| Atom | Spec | Text property |
|---|---|---|
| **Article Section Kicker** | Noto Sans Bold 10 / 12.5 line height, 1px letter spacing, uppercase (text case), color/theme/primary. Hugs its text. | `Section` (e.g. "Crime and Public Safety") |
| **Article Author** | Noto Sans Medium 12/16, color/gray/min. Hugs its text. | `Author` (e.g. "Ruby Gonzales") |
| **Article Timestamp** | Horizontal auto layout, 4px gap (spacing/050), centered. An Icons `access-time` instance at 11×11 in color/gray/200, then the text in Noto Sans Regular **13**, line height auto, color/gray/200. | `Time` (relative: "56 mins ago", "2 hours ago", "3 days ago", "1 week ago") |

✅ **Decided (Karl, 2026-10-23): 13px**, matching the production-measured card meta in 1Col Article Card (`3352:24153`: Noto Sans Regular 13, line height auto, gray/200). The prototype's 12px `.tm` should change to 13px.

**Built (2026-10-23)**, each in its own documentation container appended to Article Parts (`3484:67765`):

| Atom | Component | Container | State |
|---|---|---|---|
| Article Section Kicker | `3609:39112` (text property `Section#3609:0`) | `3609:39117` | Done. Size, style, family and fill bound; 12.5 line height and 1px letter spacing are raw (no tokens). |
| Article Author | `3609:39115` (text property `Author#3609:1`) | `3609:39159` | Done. Size, style, family and fill bound; 16 line height raw. |
| Article Timestamp | `3621:38794` (text property `Time#3621:0`) | `3621:38786` | Text done and bound (13 / Regular / Noto Sans / gray/200). **To do:** add the access-time icon (11×11, gray/200) as the first child and bind the 4px gap to spacing/050, once the Web DS library is published. |

Cleanup: the previous session had left two stray copies of the whole Article Parts frame ("Article Section Kicker Container" `3609:39116` and "Article Author Container" `3609:39158`) under Top Zone Parts, with duplicate Related Article List Item and Article Image Placeholder components (0 instances). The Kicker and Author containers were moved into Article Parts and the stray copies deleted.

### Card variants (from the prototype CSS)

- **Card** (`.card`):
  - White, 1px #CCCAC7 border, 8px radius, clips content. The image is 16:9.
  - Body: 16px padding, 12px gap, space-between. Kicker (8px below it), then the title: Noto Serif Bold 16 / 18.88, clamped to 5 lines.
  - Footer: 1px #CCCAC7 top border, 8px top padding, author over timestamp.
  - Layout: 2-up above 639px, 1-up at ≤639px.
- **Row** (`.row`):
  - A 2-column grid: image 220px wide (min height 132), then the body (16px padding).
  - At small widths: image 120px wide (min height 110), body padding 12px.
  - Same border, radius, kicker, title and footer as the card. The title isn't clamped.
- **Featured story** (`.lead`):
  - Kicker (`.kick.blk`), then the headline: Noto Serif Bold 29/33, −0.87px letter spacing (25/29, −0.03em in the lead header).
  - Image, then the excerpt: Noto Sans 15/19, gray/100, 6px top margin.
  - Byline row: author and timestamp inline, 12px gap, 12px top margin.
- **Feed header**: Eyebrow (20/22 uppercase gray/100, 2px primary underline). Under it, the subhead in Noto Sans 13/19.5 gray/200 with the info icon and a tooltip.
- **Tooltip** (`.tip`): 240px wide, 12px padding, white, 1px #CCCAC7 border, 8px radius, shadow `0 2px 8px rgba(20,20,20,.15)`, Noto Sans Italic 13/18 gray/100. Placed 8px below its trigger, centered. Placeholder text: "Placeholder text with more information about this feature."
- **CTA panel** (`.cta`):
  - Centered, 56px top/bottom and 16px side padding.
  - 48px circle icon: `padlock` U+EA26, primary on #F1EFEB.
  - h2 in Noto Serif Bold 18/24 gray/min, then a paragraph in Noto Sans 13/19.5 gray/200, max width 330.
  - Buttons: Primary "Subscribe now" and Secondary "Sign in".
  - Small print in 11/16 gray/200: "Starting at $1.99/week. Cancel anytime."
- **Load More**: "Load More Articles", Noto Sans Bold 16/24, primary, underlined, centered, 16px top / 8px bottom padding.

### Homepage tabs (production, staging.dailylocal.com/world-cup/)

- **Markup:** `<ul class="sr-nav-tabs" role="tablist">` > `<li role="presentation">` > `<button class="tab-btn [active]" role="tab" aria-selected aria-controls>`.
- **Nav:** max width 1200, padding 0 24px (0 at ≤500px). Tab list: flex, 32px gap, scrolls sideways with the scrollbar hidden. Bar height 40.
- **Tab:** Inter 600 12px, line height normal, 0.14em (1.68px) letter spacing, uppercase, padding 12px 18px, 2px transparent bottom border, −1px bottom margin. Rendered sizes 192 / 171 / 139 × 41.
- **States:**
  - Default: #6B7280.
  - Hover: #111827.
  - Active: #000 with a 2px #C62828 bottom border.
  - Focus-visible: 2px black outline, −3px offset.
- **Wrapper:** #FAFAFA background, 1px gray (#808080) bottom border, 2rem bottom margin.
- **Off-system values to map to tokens and log for design-vs-production:**
  - Inter → Noto Sans.
  - #6B7280 / #111827 → nearest MNG grays.
  - #C62828 → color/theme/primary.
  - #FAFAFA / #808080 → MNG grays.
- The prototype's current tabs: white bar, 1px #CCCAC7 bottom border, inner width 896, 24px padding (4px on mobile).

## Next steps

1. ~~Confirm the imports work~~ Still broken (2026-10-23); see Blocker. Karl publishes the Web DS library.
2. ~~Timestamp size~~ 13px (Karl, 2026-10-23).
3. ~~Build the 3 atoms~~ Kicker and Author done. Timestamp: add the access-time icon and bind the gap to spacing/050, then screenshot.
4. Card variants: add them to 1Col Article Card, Horizontal Thumbnail Card and Zone 1 Lead Article Card, built from the atoms.
5. Tabs: ask Karl where they go, then build from the production spec mapped to tokens.
6. Tooltip and CTA panel: ask Karl where each goes, then build.
7. Parity checks for the modal (against `components/modal.md`) and for Load More (against Button Linkstyle). Fix the prototype if either differs.
8. Log the off-system values in `mng_web_ds/design-vs-production.md` and update `MNG-Web-Design-System-Status.md`. Re-export the new components with the repo's exporter (`scripts/component-export/`).
