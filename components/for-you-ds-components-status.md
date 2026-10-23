# For You → MNG DS components: status and handoff

> **Updated 2026-10-23** for the Tooltip (MNG Web Design System, new Tooltips page), the Homepage Tabs (Menus and Parts; design-vs-production entry 31), the three card variants (1Col Article Card, Horizontal Thumbnail Card and Zone 1 Lead Article Card, Style=For You), the prototype timestamp fix, library imports working again, the timestamp decision (13px, Karl) and the three card atoms in WordPress Elements ▸ Article Parts. Moved into the repo from the "For You Tab MVP" project the same day.

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

## Library imports (fixed 2026-10-23)

**Working again (2026-10-23).** After Karl published the Web DS library and dragged an `access-time` instance into WordPress Elements, `importVariableByKeyAsync` (spacing/050) returned at once. It's unclear which step fixed it: the publish, the manual insert, or the plugin relaunch. If imports hang again, try those three.

Earlier the same day they were **still broken**, after Karl relaunched the Desktop Bridge plugin in WordPress Elements. `figma.teamLibrary.getAvailableLibraryVariableCollectionsAsync()` and `getVariablesInLibraryCollectionAsync()` now answer in about 0.2s, but `importVariableByKeyAsync` (font/size/10) and `importComponentByKeyAsync` (access-time) still time out (tested at 8s and 22s). Possible cause: the bridge showed two MCP server instances (ports 9223 and 9224) from two Claude sessions.

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
| 1 | Homepage tabs (Editor's Picks / For You) | `.tabs` | Production World Cup tabs | **Built 2026-10-23** in WordPress Elements ▸ Menus and Parts: Homepage Tab `3629:44949`, Homepage Tabs `3629:44974`. |
| 2 | Feed header "While You Were Away" | `.fyh .eb` | WP Section Title / Eyebrow, Style=Underline (`3333:42278`) | **Exists.** The "Based on what you read." subhead line is new. |
| 3 | Info tooltip | `.tip` | none (the `info` icon U+E937 exists) | **Built 2026-10-23** in the MNG Web Design System, new page "Tooltips \| 2026.10.23": Tooltip set `7372:25744` (Type=Tooltip / Toggletip × Placement=Top / Bottom). |
| 4 | Featured story | `.lead` | Zone 1 Lead Article Card (set `3336:46157`) | **Built 2026-10-23:** `Style=For You` × Mobile / Tablet / Desktop (`3628:44769` / `3628:44822` / `3628:44874`). |
| 5 | Article card | `.card` | 1Col Article Card (set `3536:39065`) | **Built 2026-10-23:** `Style=For You` (`3628:44640`). |
| 6 | Article row | `.row` | Horizontal Thumbnail Card (set `3362:2992`) | **Built 2026-10-23:** `Style=For You` × Mobile / Tablet / Desktop (`3628:44666` / `3628:44686` / `3628:44706`). |
| 7 | Card atoms: kicker, author, timestamp | `.kick` `.au` `.tm` | none (the WP Article Page Byline `1110:19503` is the full article byline) | **Built 2026-10-23** in Article Parts: Kicker `3609:39112`, Author `3609:39115`, Timestamp `3621:38794`. |
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
| Article Section Kicker | `3609:39112` (text property `Section#3609:0`) | `3609:39117` | Done. Size, style, family and fill bound; 12.5 line height raw (no line-height primitives). Letter spacing 0 (was 1px; Karl, 2026-10-23, to match production's top nav and Subscriber Only badge). |
| Article Author | `3609:39115` (text property `Author#3609:1`) | `3609:39159` | Done. Size, style, family and fill bound; 16 line height raw. |
| Article Timestamp | `3621:38794` (text property `Time#3621:0`) | `3621:38786` | Done. Clock Icon (Icons `access-time` instance `3623:44633`, rescaled to 11×11, vector fill bound to gray/200), then the text (13 / Regular / Noto Sans / gray/200, line height auto). Gap bound to spacing/050; centered. |

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

### Card variants built (2026-10-23)

Each set got a new variant property **Style = Standard / For You**. The existing variants were renamed `Style=Standard, …` (renaming is safe; existing instances keep working and default to Standard). All new values are bound to MNG DS variables; the atoms are nested as exposed instances, so the kicker, author and time can be edited from the card. Every variant was screenshotted and checked against the prototype CSS.

| Set | New variants | Built from the prototype |
|---|---|---|
| 1Col Article Card `3536:39065` | `Style=For You` `3628:44640` (296 wide) | White (gray/max), 1px gray/500 border, radius/lg, clips. 16:9 Article Image Placeholder (`Show Image` still applies). Card Body: spacing/200 padding, spacing/150 gap: Kicker, spacing/100, headline bound to `Editorial/Titles/CardTertiaryCompact` (Noto Serif Bold 16/18.88), max 5 lines with ellipsis. Card Footer: 1px gray/500 top border, spacing/100 top padding, Author over Timestamp. |
| Horizontal Thumbnail Card `3362:2992` | `Style=For You` × `Device=Mobile` `3628:44666` (340), `Tablet` `3628:44686` (720), `Desktop` `3628:44706` (848) | Same border, radius, fill, kicker and headline (not clamped). Image left: 220 wide, min height 132 (Mobile: 120, min 110). Body padding spacing/200 (Mobile spacing/150), spacing/150 gap. Footer: Author and Timestamp in a row, spacing/150 gap, same top border. Widths are the prototype's feed column at 360 / 768 / 1280. |
| Zone 1 Lead Article Card `3336:46157` | `Style=For You` × `Device=Mobile` `3628:44769`, `Tablet` `3628:44822`, `Desktop` `3628:44874` | Cloned from Standard (same headline, excerpt and image tokens). Removed: subscriber badge, Related list. Added: a Headline Group (Kicker, spacing/050, headline) and a Byline row after the excerpt (Author + Timestamp, spacing/150 gap, 12px above it). Mobile: the excerpt's 16px bottom padding is 0 and the byline has spacing/150 bottom padding, so the bottom border sits 20px below it. |

Not built / open:
- **Hover state** (prototype `.card:hover` / `.row:hover`: primary border plus a 1px primary ring, headline in primary). Needs a State property. **Parked (Karl, 2026-10-23): come back to it later.**
- **Card body space-between:** in code the card body is space-between so footers line up when cards in a row stretch to the same height. Figma can't combine that with a fixed 12px gap, so the Figma card uses the gap (noted in the component description).
- **Featured story excerpt gap:** the prototype has 6px above the excerpt (`.lead-d`); the Figma Standard lead (production-measured) has a 4px gap. The For You variant keeps 4px. Check against production.
- **Unused properties on For You variants:** `Show Subscriber Badge`, `Show Excerpt` and `Show Meta` (1Col) and `Show Gallery Icon` (Horizontal Thumbnail) don't apply to them.
- The Figma Bridge's bound-paint colors render black in exports until the stored fallback color is set; fixed by writing the resolved value with the binding.

### Tooltip built (2026-10-23)

Karl: the prototype's tooltip was a placeholder; it goes in the MNG Web Design System, open to what tooltips in the wild do. He chose **both types in one set**, on a new page **Tooltips | 2026.10.23** (`7372:25702`, after Modal Panels), in a "Tooltip Container" doc frame (`7372:25704`).

References: production's article "type of work" popup (`#tiPopupContent` on ocregister articles: opened by clicking the "News" label, white, 1px #787878 border, 1px radius, 275px wide, 15px 10px padding, 0.9em Helvetica, 10px caret, close X); the old "Section Menu/ToolTip box" frames on "Elements to be detailed still" (dark #616262, 20px text, not a component); and the common split in other design systems between a hover **tooltip** (short label, mouse/keyboard only) and a click **toggletip** (an info button that opens an explanation; works on touch). No elevation/shadow tokens exist, so neither type has a shadow.

| Variant | Node | Spec |
|---|---|---|
| Type=Tooltip, Placement=Top / Bottom | `7372:25710` / `7372:25715` | Label property. color/gray/100 box (white text 11.6:1), Noto Sans Regular 12 color/gray/max, line height auto, spacing/050 × spacing/100 padding, radius/sm, max width 240, 12×6 caret. Hover/focus only; for icon-only buttons. |
| Type=Toggletip, Placement=Top / Bottom | `7372:25720` / `7372:25732` | Text property; Show Close (boolean). 275 wide, color/gray/max, 1px color/gray/300 border, radius/sm. Text Container (spacing/150 padding) with Noto Sans Regular 13 color/gray/100 (11.6:1), then a Button In-Line Close instance (40×40, main file `5335:16200`). 12×6 caret with a gray/300 edge. Opens on click/tap; Esc, close or outside click closes. |

Production follow-up (not logged yet): the article type-of-work popup could move to this component (Noto Sans instead of Helvetica, gray/300 border instead of #787878, radius/sm). That's open item 7 in the main status doc.

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
- The prototype's current tabs: white bar, 1px #CCCAC7 bottom border, inner width 896, 24px padding (4px on mobile). They also differ from production in the tab itself: Noto Sans 600 14/20, 0.35px letter spacing, 12px 24px padding, gray/200 text, active teal text with a 3px teal underline, and the tabs spread with space-between. **To do: update the prototype to match the built component.**

**Built (2026-10-23)** in WordPress Elements ▸ **Menus and Parts** (Karl's choice), in a new "Homepage Tabs Documentation" frame (`3629:44928`) after the Breaking News Banner:

| Component | Node | Notes |
|---|---|---|
| Homepage Tab | set `3629:44949`: `State=Default` `3629:44932`, `Hover` `3629:44936`, `Active` `3629:44940`, `Focus` `3629:44944`; text property `Label#3629:8` | Label Container (spacing/150 top/bottom, spacing/200 sides) over a 2px Underline. Noto Sans SemiBold 12 (font/size/12, font/style/semibold), line height auto, no letter spacing, uppercase. Default gray/200; Hover gray/min; Active gray/black with a theme/primary underline; Focus: absolute 2px gray/black ring inset 3px. |
| Homepage Tabs | set `3629:44974`: `Breakpoint=Desktop` `3629:44950` (1280), `Mobile` `3629:44962` (360) | gray/max bar, absolute 1px gray/300 Bottom Border behind the tabs (so the active underline covers it, like production's −1px margin). Nav 1200 wide with spacing/300 side padding (Desktop) or full width with no padding (Mobile, ≤639px). Tab List: spacing/300 gap; Editor's Picks (Active) and For You (Default). |

Color mapping (nearest MNG gray, with readable contrast): #6B7280 → gray/200 (gray/300 is closer in value but too light for 12px text on white), #111827 → gray/min, #000 → gray/black, #C62828 → theme/primary, #FAFAFA → gray/max, #808080 → gray/300. Logged as design-vs-production entry 31 and as a row in the "Other fixes" tab of the color fixes sheet.

**Rule (Karl, 2026-10-23): no off-token values.** Where production uses a value with no token, round to the nearest existing Figma token and update production later; same for breakpoints. Applied: tab side padding 18 → spacing/200 (16; a tie with 20, Karl chose 16); tab gap 32 → spacing/300 (24); tab letter spacing 1.68px → 0 and the Article Section Kicker's 1px → 0, matching production's top nav items and Subscriber Only badge (both `letter-spacing: normal`, checked live on all 6 review sites, 2026-10-23: top nav 14.06px and 15px / 600, `.subscriber-only-tag` 13px, no letter-spacing rule on any site); ≤500px → ≤639px.

**WCAG AA (text 4.5:1 on white):** gray/200 6.6:1 (default tab, timestamp), gray/min 18.4:1, gray/black 21:1, theme/primary #007580 5.5:1 (kicker; Bold Coastal). gray/300 is 3.8:1, so it fails for text; it's used only for the bar border (non-text). Production's #6B7280 on #FAFAFA is 4.6:1.

## Next steps

1. ~~Confirm the imports work~~ Working again (2026-10-23).
2. ~~Timestamp size~~ 13px (Karl, 2026-10-23).
3. ~~Build the 3 atoms~~ Done 2026-10-23, all screenshotted. ~~Prototype `.tm` 12px → 13px~~ Done 2026-10-23 in `claude-design-v3/Main.dc.html` (`font:400 13px/normal`). Not changed: the older `claude-design/Main.dc.html` and the `index.html` built from it (Oct 15), and the Claude Design canvas artifact.
4. Publish the WordPress Elements library so the atoms can be used.
5. ~~Card variants~~ Done 2026-10-23 (see "Card variants built"). Open: hover state (parked); the 6px vs 4px excerpt gap on the featured story.
6. ~~Tabs~~ Built 2026-10-23 in Menus and Parts; logged as design-vs-production entry 31; gray mapping and AA contrast confirmed. Open: update the prototype's tabs and the kicker's letter spacing (1px → 0).
10. **Prototype fixes prompt:** `components/for-you-prototype-fixes.md` collects every change the prototype needs. Add a section each time a component is built, then Karl runs it in the For You Tab MVP project once the list is complete.
7. ~~Tooltip~~ Built 2026-10-23 (see "Tooltip built"); prototype section added to the fixes prompt. **The MNG Web Design System library needs publishing.** CTA panel: ask Karl where it goes, then build.
8. Parity checks for the modal (against `components/modal.md`) and for Load More (against Button Linkstyle). Fix the prototype if either differs.
9. Log the off-system values in `mng_web_ds/design-vs-production.md` and update `MNG-Web-Design-System-Status.md`. Re-export the new components with the repo's exporter (`scripts/component-export/`).
