# Production vs. Design Differences — Engineering Handoff

> **Updated 2026-10-14:** entry 33 (breakpoints off the official sets, from the breakpoint inventory) and entry 32 (font fallbacks: Helvetica Neue, not Helvetica) added. Earlier the same day: entries 30 (Reader Dashboard breakpoints: questions for DigiScrum) and 31 (Obituaries breakpoints vs the WordPress grid, CMS team) added; entry number 30 was free (the earlier icon-font entry 30 was folded into 20).
>
> **Consolidated 2026-09-24.** Combines the Sept 22 version of this file (entries 1–17, unchanged except for the notes marked "2026-09-24") with a short duplicate created on Sept 24. That copy added one new item, now entry 18. Entry 19 and the method note at the end came from the HANDOFF and NOTE files in this folder. Entry 20 (icon font) was added 2026-09-25 from `components/icons.md`. Entry 21 (per-theme color fixes) was added 2026-09-25, when the Greeley Tribune color theme was folded into Prairie Mountain Publishing. Entries 18 and 21 were updated 2026-09-30 (Greeley exception, Hartford Courant verified) and 2026-10-01 (NEPA folded into the NEPA-PMP sub-theme; disputed sites verified live), and entry 21 now holds the full per-theme color fix list that used to be `tokens/colors/mng-colors-engineering-fixes.md` (retired). Notes for reading older entries:
> - `color-tokens.md` is now `tokens/colors/color-tokens-decision-log.md`. Current typography tokens are in `tokens/typography/typography-tokens.md`.
> - Greeley Tribune no longer has its own color theme or Figma mode (2026-09-25). Mentions of it below as a pilot site for layout, nav or typography still stand.

**Purpose:** A running list of every place live production has been found diverging from the Figma design-system spec, or where something was explicitly flagged as needing engineering (or legal) attention. Figma is the source of truth for these systems; when production disagrees, the fix belongs here as an engineering item rather than being silently absorbed into design tokens. Each entry says where the drift is, what Figma says vs. what's live, and what engineering should do about it.

**Status note:** This doc was referenced once before (in `MNG-Web-Design-System-Status.md`, Known Open Items §5 item 3) but was never actually created — it was created 2026-09-10 during the typography consolidation work, backfilling that earlier reference plus the current typography section, then backfilled again the same day with every other open "flag to engineering" item found across the project's component/audit docs (card-teaser.md, modal.md, disclosure.md, navigation.md, containers-and-ad-units.md, color-tokens.md, Reader-Dashboard-Library-Impact-Map.md).

---

## 1. Buttons — Obituaries page CTA (Chicago Tribune, Denver Post)

**Found:** 2026-09-01, during the buttons audit.

**Figma spec:** Button Primary (main file, ***Buttons page), Default size — padding 16px vertical + 20px horizontal, 14px text.

**Production:** The live `.subscribe-button` CTA (249×44, confirmed identical on Chicago Tribune and Denver Post, also appears on regular article pages — a general paywall CTA, not obituary-specific) renders with padding 14px/10px instead of 16px/20px, and font-size 15px instead of 14px. Radius and per-masthead fill color already match Figma.

**Decision (Karl, 2026-09-01):** This is not a new button size/variant — it should simply carry Button Primary's existing Default styling. Production needs to be brought in line with Figma's padding and font-size values above; no new Figma token or variant should be created for it.

**Status:** Open.

---

## 2. Reader Dashboard — Typography (2026-09-10)

**Policy:** For anything specific to the Reader Dashboard, Figma is the source of truth — even where production currently differs. MNG Web Design System's `Dashboard/*` typography tokens (in the "Dashboard Typography" collection) are kept at their Figma-specified values; any place production has been found rendering something different is recorded here instead, for engineering to either fix in production or flag back to design if the production value should actually be adopted.

### 2.1 Page title size — `Dashboard/Titles/PageDesktop`

**Figma:** Noto Serif, **26px**, Bold (700) — matches Reader Dashboard v2.0's own Figma token (`Titles/Page (desktop, tabletH)`) exactly.

**Production:** canoncitydailyrecord.com/dashboard/ (desktop width) renders this title at **36px**, via a Tailwind `lg:text-4xl` breakpoint utility class overriding the base size.

**Action needed:** Reconcile production to the Figma-specified 26px, OR — if 36px is an intentional, approved change — get that confirmed with design so Figma can be updated to match and this item retired. Until then, MNG Web Design System's token stays at 26px per the policy above.

**Status:** Open.

### 2.2 Section Title weight — `Dashboard/Titles/SectionTitle`

**Figma:** Noto Sans, 18px, Bold (700).

**Production:** One live-measured instance showed weight 600 (Semi-Bold) instead of 700.

**Caveat (lower confidence than 2.1):** The measured instance may have been an admin/debug panel ("MNG Debugger" / "Entitlements JWT") rather than genuine reader-facing UI.

**Action needed:** Confirm on a real reader-facing Section Title instance whether it's 700 (matches Figma) or genuinely 600.

**Status:** Open.

### 2.3 `font/size/10` — unconfirmed in production

**Figma:** Defined at 10px in Reader Dashboard v2.0's Type Primitives, carried into MNG Web Design System.

**Production:** No confirmed live sighting during this audit (only canoncitydailyrecord.com/dashboard/ was checked).

**Action needed:** Low priority — confirm where (if anywhere) this size is actually used live.

**Status:** Open.

---

## 3. Color Tokens — mcall.com primary/primary-dark shift

**Found:** 2026-08-27, color token audit.

**Figma spec:** Brand collection, Morning Call mode — `primary` = `#166291`, `primary-dark` = `#014B78`.

**Production:** mcall.com's live-rendered `--primary` (read correctly, on the WordPress Customizer's actual scope) is `#014B78` — an exact match for the Figma table's `primary-dark`, not `primary`.

**Action needed:** Determine whether the site is live-rendering the wrong step of its own color ramp, or whether the Figma table's column values are shifted for this row specifically. Not root-caused.

**Note (2026-09-25):** Morning Call's full list of color fixes (6, including this one) is in entry 21.

**Status:** Open.

---

## 4. Article Card / Teaser

### 4.1 Denver Post — Section Highlight shows 4 headline items instead of 3

**Found:** Article Card / Teaser audit.

**Figma / platform norm:** Every pilot site (Chicago Tribune, OC Register, Orlando Sentinel, Greeley Tribune, mcall.com) shows exactly 3 headline items in the Section Highlight module.

**Production:** Denver Post shows 4 — and this isn't theme-scoped, since OC Register shares Denver Post's Bold Coastal theme but still shows 3.

**Action needed:** Confirm whether this is a deliberate per-site editorial choice or a real inconsistency worth fixing.

**Status:** Open — not yet root-caused.

### 4.2 Section title style (color, underline, sizing) doesn't match Figma on any of the 6 pilot sites

**Found:** Article Card / Teaser audit, §4.4 / Open Item 3.

**Figma spec (Karl's 2026-09-01 decision):** Section Highlight / "Latest Headlines" title — text color `color/gray/100`, a 2px underline in the site's own `--primary`, unified size/weight/letter-spacing per the eyebrow decision.

**Production:** None of the 6 pilot sites match the full spec. Text color is wrong on all 6. The underline itself doesn't exist at all on 4 of 6 sites (Chicago Tribune, Orlando Sentinel, OC Register, Denver Post) — only the 2 Modern Earthy sites have the underline mechanism, and only the 2 Bold Coastal sites match the size/weight.

**Action needed:** Ready to hand to engineering as a fully-specified spec to implement across all 6 sites.

> **Note (2026-09-24):** The "unified size/weight" part of this spec is out of date. On 2026-09-09 the single 20px eyebrow was replaced with per-theme eyebrow tokens: Bold Coastal 20/400/Sans, Measured Vibrant 17/700/Sans, Modern Earthy 21/400/Serif (see `tokens/typography/typography-decision-log.md`, decision 6). The color and underline parts of the spec still stand. Confirm the size/weight part with Karl before handing this to engineering.

**Status:** Open.

### 4.3 Responsive layout rules vary by container context (not fully mapped)

**Found:** Article Card / Teaser audit, §5 Open Item 8.

**Detail:** `feature-medium` and `headline-only` responsive (`flex-direction`) rules change depending on the parent container class (e.g. `.landing-four-up-hybrid`, `.landing-three-one`, `.slow .feature-top` each carry their own breakpoint overrides for the same classes). This overlaps with the upcoming Containers component and hasn't been fully mapped — flagging so it isn't mistaken for one universal rule.

**Status:** Open / informational — needs a dedicated mapping pass.

### 4.4 Excerpt/dek color needs re-verification (minor)

**Detail:** The dek/excerpt color (~`#484642`, sampled from Chicago Tribune) was derived via an rgb→hex rounding pass that wasn't double-checked the way other colors in the doc were.

**Status:** Open — low priority, worth a re-check before treating as final.

---

## 5. Reader Dashboard — Modal

**Figma source:** "ModalsCenter" library component, Reader Dashboard v2.0. **Live source:** East Bay Times preprod, account-verification flow.

### 5.1 Card border mismatch

Figma's ModalsCenter has a 1px `color/gray/300` border on the card; the live card was recorded relying on shadow only, with no border distinguished. Both may be true (a subtle border could be present but visually indistinguishable from the shadow) — not resolved either way.

**Status:** Open.

### 5.2 Backdrop opacity mismatch

Live backdrop is 45% black; the Figma-modeled value is 50% black — close, and not even built into the component as a literal property either way.

**Status:** Open — low priority.

### 5.3 Fixed 444px width, narrow-viewport behavior untested

The modal card is a fixed 444px, not fluid/responsive. Behavior at narrow viewports has not been tested.

**Status:** Open.

### 5.4 Password "Update" flow is unstyled design debt

Clicking "Update" for password doesn't open a modal — it navigates to a separate, essentially unstyled page (`/reset-password/`: Arial font, square corners, plain black button border, default gray input border) that matches none of the design system.

**Action needed:** This is design debt to flag, not a pattern worth capturing faithfully — needs a real design pass, not a Figma-matching exercise.

**Status:** Open.

### 5.5 Destructive-action modals unexplored

Only the account-verification modal was captured live. Other triggers (e.g. canceling a subscription) were deliberately not explored to avoid triggering irreversible account actions, so their modal spec is unconfirmed.

**Status:** Open — needs a human to click through and report back rather than automated exploration.

---

## 6. Reader Dashboard — Disclosure

### 6.1 Two competing disclosure/accordion patterns need reconciliation

Production's live Reader Dashboard (e.g. chicagotribune.com/user-tools/dashboard) uses a chevron/icon-based accordion pattern, different from the simpler text-link toggle documented from preprod (the pattern actually built in Figma). The chevron pattern is currently out of scope because that surface is being replaced — but if it survives the replacement, the two patterns will need to be reconciled into one.

**Status:** Open — contingent on what survives the Reader Dashboard replacement.

### 6.2 Coverage and behavior gaps

Only one instance of the disclosure pattern (Login Methods on Profile) was found and tested; other tabs (Subscription, Benefits, etc.) weren't checked for additional instances. Whether expand/collapse is animated or instant was never confirmed.

**Status:** Open.

---

## 7. Reader Dashboard — Design System Architecture

**Found:** Reader-Dashboard-Library-Impact-Map.md.

**Detail:** Modal, Disclosure, and Empty State/Status Badge had been rebuilt by hand as pilot copies instead of using Reader Dashboard v2.0's components, so they could drift out of sync.

**Resolved 2026-09-25:** the hand-built copies were retired. The sources are now the real components in the main file: ModalsCenter, Button Linkstyle and InLineMessage.

**Status:** Resolved.

---

## 8. Containers, Images & Ad Units

### 8.1 `object-fit: fill` on card images — distortion risk

Both hero and feature-medium images use `object-fit: fill` with no `aspect-ratio` set, meaning images are stretched to exactly fill their container rather than cropped-to-fill (`cover`). Distortion is currently minimal because sampled images happen to be close to the container's aspect ratio, but an editor uploading an off-ratio image would visibly stretch/squash it.

**Action needed:** Confirm with engineering whether `fill` is intentional or should be `cover`, since this is a live distortion risk on any off-ratio upload.

**Status:** Open.

### 8.2 Main content container width — Chicago Tribune vs. Denver Post

Chicago Tribune's `main` container measures 1260px at a 1280px viewport; Denver Post measures 1245px at the same viewport — a real 15px difference, not explained by Denver Post running a different theme (it doesn't — confirmed both load real shared theme stylesheets with their own Customizer overrides, same pattern as every other site).

**Status:** Open — not root-caused; could be a scrollbar-width artifact of that specific page load rather than a genuine CSS difference.

### 8.3 Orlando Sentinel — ad slots register lazily on mobile homepage

On Orlando Sentinel's mobile homepage, only the `mobile_adhesion` slot registered with Google Publisher Tag at initial load; the other 10 ad containers exist in the DOM but didn't register in `getSlots()` even after scrolling most of the page and waiting. This looks like Freestar (Orlando Sentinel's header-bidding wrapper, different from the other 5 pilot sites) registering slots lazily/progressively rather than upfront.

**Action needed:** Confirm with engineering whether this is expected Freestar behavior or worth a longer dwell-time re-check.

**Status:** Open.

### 8.4 No visible ad-disclosure label

No "Advertisement"/"Sponsored" text label or `aria-label` was found near any ad container on any of the 6 pilot sites — only Google's own AdChoices icon (rendered inside the ad iframe itself, not site-authored markup).

**Action needed:** Confirm with engineering/legal whether the absence of an explicit disclosure label at the container level is intentional, since AdChoices alone is a weaker disclosure than what many other publishers use.

**Status:** Open — legal/compliance relevance.

---

## 9. Navigation

### 9.1 Obituaries page — hamburger + "All Sections" both visible at desktop width

**Figma / platform rule:** On the homepage, the hamburger icon is only visible at ≤1039px.

**Production:** On the Obituaries page, at a comfortably-desktop viewport, both the hamburger icon and the "All Sections" button are visible simultaneously — confirmed on all 6 pilot sites (Chicago Tribune, Denver Post, OC Register, Orlando Sentinel, Greeley Tribune, mcall.com), including at a 1728px viewport.

**Action needed:** Still not explained — genuinely flagged to engineering to confirm whether this is intentional for the Obituaries template or a bug.

**Status:** Open.

### 9.2 Cross-site avatar inconsistency for the same logged-in account

Cross-site SSO is confirmed working (same session carries from one site to another with no re-login). But for the identical account, Denver Post rendered an actual photo avatar while Orlando Sentinel rendered a generated initials badge ("PA").

**Action needed:** Confirm whether this is a per-site fallback difference (e.g. photo failed to load/sync on one site) or a real bug.

**Status:** Open — not root-caused.

### 9.3 Reader Dashboard's own breakpoint convention differs from the marketing site's

The Reader Dashboard treats 1024×768 and 1280×960 as "menu always visible," a 1024px breakpoint — different from the audited 1039px rule on the main marketing-site nav. Since the Dashboard is a distinct web app from the shared marketing-site theme, this may be a legitimately different, real breakpoint rather than a conflict.

**Status:** Informational / low priority — flagged for awareness, not treated as an error.

### 9.4 Hidden duplicate nav `<li>` artifacts

On some categories (confirmed on Sports), the individual sub-section links (e.g. Chicago Bears, Bulls, Blackhawks, Cubs, White Sox) exist twice: once in the real working sub-menu, and again as `class="hidden"` top-level `<li>` siblings directly in the nav — apparent unused WordPress nav-menu artifacts.

**Status:** Open — worth a cleanup pass, low risk/low priority.

### 9.5 Device-class first-paint timing (Denver Post, mcall.com)

A device-signal CSS class is added client-side (confirmed not server-side) slightly later on Denver Post and mcall.com than the other 4 sites — likely real device detection working correctly, just applied a beat slower on those two.

**Action needed:** Worth asking engineering whether any component's CSS actually depends on this class being present at first paint. If nothing does, this needs no action.

**Status:** Open — low priority, likely closable with a single confirmation.

---

## 10. Color Tokens — Neutral gray scale (`color/gray/*`) mismatch

**Found:** 2026-09-10, CRUX Style Library color-token audit / production repertoire check (requested by Karl).

**Figma spec (source of truth):** the main file's `color/gray/100–600` (Colors collection):

| Token | Value |
|---|---|
| `color/gray/100` | `#393938` |
| `color/gray/200` | `#5E5D5C` |
| `color/gray/300` | `#838280` |
| `color/gray/400` | `#A7A6A3` |
| `color/gray/500` | `#CCCAC7` |
| `color/gray/600` | `#F1EFEB` |

**Production:** every site in the repertoire ships its own `--site-branding-gray-100` through `--site-branding-gray-600` CSS custom properties, and all 6 sites use the identical (wrong) values:

| CSS custom property | Live value |
|---|---|
| `--site-branding-gray-100` | `#38322A` |
| `--site-branding-gray-200` | `#5D5B5A` |
| `--site-branding-gray-300` | `#9D9A98` |
| `--site-branding-gray-400` | `#AAA7A4` |
| `--site-branding-gray-500` | `#D7D6D2` |
| `--site-branding-gray-600` | `#F1EFEB` (matches the design system at this step only) |

**Sites verified (6/6 match, all identical):** ocregister.com, denverpost.com, chicagotribune.com, orlandosentinel.com, canoncitydailyrecord.com, mcall.com. Verified via a direct CSS custom-property scan of each site's live stylesheets (Claude in Chrome), not a screenshot/visual check.

**Note:** the live production values exactly match CRUX Style Library's `grayRoot/100–600` token set — a separate, seemingly superseded scale that isn't CRUX's own primary `color/gray/*` ramp either (CRUX's own `color/gray/*` matches the design system's values above exactly). It looks like production was built against an older/alternate gray ramp and was never updated when the design system's `color/gray/*` scale (consistent with CRUX's own `color/gray/*`) became canonical.

**Decision (Karl, 2026-09-10):** Use the design system's existing grays as the source of truth. CRUX's `grayRoot` scale was NOT added as a new token set — production should be corrected to match the existing `color/gray/*` values instead.

**Action needed:** Update each site's `--site-branding-gray-100` through `--site-branding-gray-600` custom properties to the design-system values in the table above.

**Status:** Open.

---

## 11. Color Tokens — Endless Tributes / Obituaries palette live-production audit

**Found:** 2026-09-10, live-production verification of the 9 documented Endless Tributes colors (Shared Platform Reference — Style Guide section, Endless Tributes — Style Guide sub-section, now migrated into MNG Web Design System's Color Pallets page) against denverpost.com's obituaries listing page and an obituary article subpage. Verified via Claude in Chrome: a `getComputedStyle()` scan of `backgroundColor`/`color`/`borderColor`/`boxShadow`/`fill` across all rendered DOM elements, plus a separate `document.styleSheets` rule-text scan (for rules not currently applied to any rendered element, and for actual `:hover`/`:active` pseudo-class declarations, since a synthetic `:hover` match after a simulated hover did not reliably surface them).

**Figma spec (Endless Tributes — Style Guide, 9 documented colors):**

| Token | Hex |
|---|---|
| Primary (Scarlet) | `#8d092d` |
| Primary-light | `#c00c3d` |
| Primary-lighter | `#f15f87` |
| Primary-dark | `#770000` |
| Primary-darker | `#4d0000` |
| Tan | `#a39c8a` |
| Tan-light | `#e8e6e2` |
| Secondary (Sage) | `#b3bc9c` |
| Tertiary (Brown) | `#3a252b` |

**Production findings (Denver Post obituaries listing + article page):**

- **Confirmed live matches (2):** Primary `#8d092d` — found. Tan `#a39c8a` — found, on the "Remove Filters" button.
- **Confirmed hover state (1):** Primary-light `#c00c3d` is not a static element color anywhere on the page, but is defined and applied as the `:hover` state of the Primary `#8d092d` button — a genuine match, just only visible on interaction rather than as a resting-state color.
- **Drifted (1):** Tan-light — Figma spec is `#e8e6e2`; the live production value is `#ecede7`. Close but not identical.
- **Fully absent from all loaded CSS (3):** Primary-lighter `#f15f87`, Primary-dark `#770000`, Primary-darker `#4d0000` — not found anywhere in computed styles or stylesheet rule text on the pages checked.
- **Defined in CSS but not rendered on the pages checked (2):** Secondary/Sage `#b3bc9c` (referenced as `--quaternary-obit`) and Tertiary/Brown `#3a252b` are both present as CSS variable declarations, but neither is applied to any visible element on Denver Post's `/obituaries` listing or the article subpage checked. Tertiary/Brown's rule is scoped to a `.obits-homepage-content` selector that isn't present on the pages checked — it may render on a different obituaries page (e.g. a dedicated homepage view) not covered by this pass.

**Obituaries Widget CSS variables (`--*-obit`) — live status:** all 5 (`--primary-obit`, `--primary-obit-light`, `--secondary-obit`, `--tertiary-obit`, `--quaternary-obit`) are still declared live at `:root` on Denver Post, despite being flagged "NEED TO REMOVE THESE FROM CODE" in the design documentation. Of the 5, only `--primary-obit` and `--primary-obit-light` are actually applied to visible elements; `--secondary-obit`, `--tertiary-obit`, and `--quaternary-obit` are declared but unused on the pages checked.

**Newly discovered, undocumented color:** `#ccc7bc` (a beige) — found live on two elements not accounted for in any of the existing Endless Tributes / Obituaries Widget documentation: the "Send Flowers" banner (`.obit-tribute-wrapper`) and the Guestbook "Post Your Message" submit button (`guestbook-form-submit`). Does not match any documented token.

**Note on scope:** only Denver Post was checked in this pass (Karl scoped the request to "any one" production site). The other 5 sites in the repertoire (ocregister.com, chicagotribune.com, orlandosentinel.com, canoncitydailyrecord.com, mcall.com) have not yet been checked for these colors.

**Figma action taken:** ~~none of these findings...~~ **Superseded 2026-09-10.** The original plan was to record these findings without adding them to Figma's Brand/Colors Variables groups, since MNG Web Design System's `Colors` collection only had a fixed 7-color-slot-per-theme model (`theme/primary`, `theme/secondary`, `theme/tertiary`, `theme/primary-light`, `theme/primary-dark`, `theme/primary-lighter`, `theme/primary-darker`) with no room for the Endless Tributes palette's 9 colors without restructuring all 20 modes. **Karl's resolution:** rather than trying to shoehorn the tributes palette into the existing per-theme slot model (or into its own one-off "Endless Tributes" mode), all 9 colors were added as a new, separate `color/tributes/*` variable group — `primary-lighter`, `primary-light`, `primary`, `primary-dark`, `primary-darker`, `secondary`, `tertiary`, `tan`, `tan-light` — each carrying the same universal value across all 20 modes (BoldCoastal, ModernEarthy, MeasuredVibrant, DenverPost, Endless Tributes, and all 15 masthead-specific modes). This matches how obituary pages actually render in production: identically regardless of which site's masthead brand is active, so a single shared value per token across every mode is correct, not a compromise. The `--*-obit` CSS widget variables (`--primary-obit`, `--primary-obit-light`, `--secondary-obit`, `--tertiary-obit`, `--quaternary-obit`) and the undocumented `#ccc7bc` beige are unaffected by this — the widget vars are a live-code cleanup item for engineering, and `#ccc7bc` remains genuinely undocumented (doesn't match any of the 9 tributes tokens), so both stay open below.

**Status:** Open for the `--*-obit` widget CSS variables (still live despite the "remove" flag) and the undocumented `#ccc7bc` beige. **Resolved 2026-09-10** for the tributes palette itself — all 9 colors are now proper Figma variables (`color/tributes/*`) applied across all 20 brand groups; the tan-light production drift (`#e8e6e2` spec vs. `#ecede7` live) is still an open engineering item to reconcile.

---

## 12. Ad Units — Homepage "Ad Blocks" slot after Blueconic/Most Popular is undersized (300×250 instead of 300×600)

**Found:** 2026-09-14, during the five-width (340/360/768/1024/1280) homepage production-parity audit.

**Figma action taken:** Per Karl's instruction, this ad instance was updated in Figma to the production-accurate `Cube 1 RRail ATF 300x600` block at every width where it appears (Mobile 340/360, and the new 768/Tablet build), replacing the previous `Cube Article 300x250` placeholder — specifically so the Figma mockups now make this gap visible rather than quietly matching the undersized code.

**Figma spec (now, post-fix):** `Cube 1 RRail ATF 300x600` — matches the size production is actually observed serving.

**Production:** Live GPT ad-slot scanning (`iframe[id^="google_ads_iframe"]` DOM query, cross-referenced against scroll position) on ocregister.com found this slot — `cube2_rrail_mid` — rendering at 300×600 at both mobile (340/360) and tablet (768) widths, at every width checked.

**Action needed:** Confirm whether the live implementation for this ad slot is intentionally 300×250 somewhere in code (unlikely, given production itself serves 300×600 into it) or whether this was simply never corrected after being built against an earlier/incorrect spec. Since Figma now shows the corrected 300×600 size, any remaining 300×250 assumption in the live templates should be treated as the bug to fix, not Figma.

**Status:** Open.

---

## 13. Masthead — Top-leaderboard ad slot renders at inconsistent sizes across page types

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

## 14. Masthead — Top nav bar overflows its container at the 1040–1279px (Tier 4) breakpoint

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

## 15. Masthead — Article scrolled-state headline overflows behind the bookmark/share icons

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

**Figma spec:** Not reproduced. Figma's Article `Scrolled` variant uses a fixed placeholder headline ("Roughly forty characters of the article t...") short enough that it doesn't hit this edge case, so the component itself doesn't currently demonstrate the bug. Unlike the Tier 4 top-nav overflow (entry #14, a systemic issue reproducible with any content at that width), this one only shows up in the narrower part of the desktop range, so it wasn't rebuilt into the static mock — it's flagged here for engineering instead.

**Action needed:** Give the headline element a max-width (or text-overflow: ellipsis truncation) tied to the actual available space before the bookmark/share-icon cluster at all desktop widths, not just the wider end of the range — the current layout only holds up above ~1700px.

**Status:** Open.

---

## 16. Masthead — Reader Dashboard shows the top nav-links row and "TRENDING:" bar, which the design explicitly excludes

**Found:** 2026-09-15, during the Reader Dashboard masthead audit (`breakpoint-audit.md`), on canoncitydailyrecord.com/dashboard/, logged in as a subscriber, at 1100px and 1040px (both above the masthead's 1039px desktop-nav threshold).

**Production:** At desktop widths, the Reader Dashboard's masthead renders the full top nav-links row (News / Local News / Sports / Things to Do / Opinion / Obituaries / Marketplace / On the Record / BestReviews) and a "TRENDING:" bar (e.g. "Fremont County Nonprofit Guide 2026," "Royal Gorge Living") above the breadcrumb and page content — the same two rows Home's masthead shows at this tier.

**Figma spec:** The `Masthead` component's `Device=XL-Desktop, Page=Dashboard` variant (`456:2715`, and the equivalent `Scrolled` variant `456:2840`) does **not** include a nav-links row or trending bar — it's just the top utility row (hamburger/All Sections, avatar, search) plus the weather/date/logo row, at 144px total versus Home's 497px 4-row structure.

**Decision (Karl, 2026-09-15):** Figma is correct — the Reader Dashboard should **not** display the trending bar or top navigation. What production shows at canoncitydailyrecord.com/dashboard/ is the bug, not a Figma gap. No Figma changes made.

**Action needed:** Engineering to suppress the nav-links row and "TRENDING:" bar on the Reader Dashboard page template at desktop widths, so it matches the intentionally-minimal masthead Figma already models.

**Note:** confirmed only on canoncitydailyrecord.com (the one site used for this phase, per Karl's direction) — not cross-checked against the other 5 repertoire sites.

**Status:** Open.

---

## 17. Video carousel ("Videos from @OCRegister") — fixed-height iframe leaves ~200px of unused blank space at narrow (340–360px) widths

**Found:** 2026-09-16, during a systematic 340px/360px breakpoint sweep across all homepage components (per Karl — checking widths narrower than any explicit CSS breakpoint, since 640px is the first real tier boundary). Verified twice: once via a narrowed real desktop Chrome window, and again via true mobile device emulation (Pixel 9 UA, touch-enabled, no desktop scrollbar) at both 340px and 360px, on ocregister.com.

**Production:** The `.dfm-page-middle-flex-container` block (a single Flourish-hosted `<iframe src="https://flo.uri.sh/visualisation/21363813/embed" title="Video from @OCRegister">`) renders at a fixed height of 490px at both 340px and 360px viewport widths. At these widths the visible content inside the iframe — header ("Videos from @OCRegister"), subtitle, the row of video tiles, and the horizontal scroll-indicator bar — only fills roughly the top 260–265px of that height, leaving about 200px of blank white space below the scroll indicator before the next section (Photos) begins. Confirmed identically at both 340px and 360px, and identically whether tested via a narrowed desktop window or true mobile emulation, so this isn't a testing-methodology artifact — it's a real rendering behavior at these widths.

**Figma spec:** The `Videos from OCRegister Carousel` component (built 2026-09-16, see the homepage template audit section 3.35, since retired) sizes its outer frame to HUG its actual content height at every placed width — header + subtitle + tile row + scroll indicator, with no trailing blank space. It does not reproduce this gap, since the gap appears to be a property of the live Flourish embed's own fixed iframe height, not something the surrounding page template's CSS controls (no dedicated `@media` rules were found for `.dfm-page-middle-flex-container` itself in this or the earlier 3.2x-era investigation).

**Action needed:** Since the iframe height is most likely set via the Flourish visualisation's own embed configuration rather than page-template CSS, this is probably a Flourish-settings fix rather than a template fix — either make the embed size its iframe responsively to actual content height at narrow widths, or set a shorter fixed height specifically for the sub-640px range. Flagging for whoever owns the Flourish embed configuration to confirm whether that's adjustable there.

**Status:** Open.

---

## 18. Color Tokens — Greeley Tribune inherits three colors from the PMP override

**Found:** 2026-09-24, Prairie Mountain Publishing color audit (live check of all 19 PMP sites).

**Figma spec:** Colors collection, Greeley Tribune mode — `primary-lighter` `#708F9F`, `primary-darker` `#395B71`, `tertiary` `#FF5722`.

**Production:** greeleytribune.com's customizer (`div#page`) sets only `primary` `#536E7F`, `primary-light` `#5B7B8B` and `primary-dark` `#44687F`, and those match Figma. The other three steps are inherited from the PMP color override that every PMP site loads: `primary-lighter` `#47B6FF`, `primary-darker` `#171E44`, `tertiary` `#303F9F`.

**Action needed:** Decide whether Greeley should carry the Figma values for those three steps (engineering adds them to its customizer) or inherit the PMP values (design updates the Greeley mode to match).

**Decided 2026-09-25 (Karl):** neither. Greeley Tribune is a PMP site and has no color theme of its own. The Greeley Tribune Figma mode became Prairie Mountain Publishing, and the Greeley Tribune style guide was removed. PMP's should-be values are the Measured Vibrant values. That turns this entry around: greeleytribune.com's three `div#page` overrides are now the mismatch.

~~**Action needed now (engineering):** on greeleytribune.com, remove the `div#page` Customizer overrides…~~

**Updated 2026-09-30 (Karl):** Greeley's three `div#page` overrides (`--primary` `#536E7F`, `--primary-light` `#5B7B8B`, `--primary-dark` `#44687F`) are a **documented exception**, not a mismatch. They stay as they are. They're noted under the PMP style guide in Figma (no red outline) and carried as Greeley's site tokens in the export. Greeley only needs the two PMP-wide fixes in entry 21 (`primary-lighter`, `tertiary`).

**Status:** Resolved (exception documented). No engineering action for these three tokens.

---

## 19. Typography — headline tiers measured live with no matching Figma style

**Found:** 2026-08-27, live typography audit (recorded in a handoff note since retired). **Re-measured 2026-09-24** on ocregister, denverpost, chicagotribune, orlandosentinel, canoncitydailyrecord, mcall and greeleytribune. The values were identical on all 7.

**Production:**

| Role | Size | Weight | Line height | Letter spacing |
|---|---|---|---|---|
| Second-tier homepage card headline | 26px | 700 | 30.3px | -0.91 |
| Third-tier card headline | 20px | 700 | 23.6px | -0.4 |
| Fourth-tier card headline | 19px | 600 | 24px | -0.665 |
| Section Highlight headline list | 15px | 600 | 19px | -0.15 |
| Related ("More News") headline | 18px | 600 | 21px | normal |
| Body copy | 16.5px | 400 | 27px | -0.165 |
| Lead story, top of page | 29px | 700 | 32.8px | -0.87 |
| Lead story, media block | 29px | 700 | 33px | -1.16 |

**Also found:** on Bold Coastal the 19px and 15px headlines are Noto Sans, even though the theme's heading font is Noto Serif. The old Figma Title style used an averaged -1.0 letter spacing that matched neither lead-story variant.

**Resolved 2026-09-24 (design side):** added as Figma Editorial styles:
- `CardSecondary`, `CardTertiary`, `CardQuaternary`, `HeadlineList`, `RelatedHeadline`, `TitleMedia` and `Editorial/Body/Default`.
- A new theme token, `font/theme/small-headline-family`.
- Title's letter spacing corrected to -0.87.

See `tokens/typography/typography-tokens.md`. Production matches the new styles, so no engineering action is needed.

**Status:** Resolved.

---

## 20. Icon font — mismatches with the Figma icon page, dead and duplicate glyphs, and known missing icons

**Found:** 2026-08-28 to 2026-08-31, icon font audit (`components/icons.md` §3, §5, §6). Added here 2026-09-25: `icons.md` said these were in this handoff, but they had never been logged.

**Figma spec (source of truth):** the `Icons` component set in the main MNG Web Design System file (node `4693:5`, 95 variants) and the documented icon list on its Icons page.

**Production (live icon font, checked on chicagotribune.com):**

| Item | What's wrong | Action |
|---|---|---|
| `google-plus` | Still in the live font. Google+ was shut down years ago, and the icon isn't documented. | Remove from the font. |
| `mng-podcast1` | Same codepoint (`e902`) as `android` — a font-build duplicate, not a separate icon. | Remove the alias. |
| `grid2` | Renders the same gift-box glyph as `gift2`, not a grid. The requested "grid" icon has not shipped. | Remove the alias; ship the real `grid` icon (artwork exists in Figma). |
| `notification-filled`, `notification-outlines` | Designed in Figma (filled and outline exclamation-in-a-circle alert icons) but missing from the live font under any name. Karl confirmed these are real, finished icons waiting to ship. | Add to the font. |


**Updated 2026-10-08:** re-checked glyph by glyph against the Figma **Icon Categories** frame (main file, Icons | 2026.08.28, node `1412:13`) using the font extracted from ocregister.com (`tokens/icons/`). **All MNG sites use the same icon font** (Karl, 2026-10-08), so these findings apply everywhere. Of the 171 documented icons, 162 match production by name and glyph. Third-party vendor icons and the "Need to source/make/add" list are out of scope.

### 20.1 Mismatches between the Figma page and the production font

| Figma name | Production | Action |
|---|---|---|
| `grid2` | `icon-grid2` shows the gift glyph (U+E930, same as `gift2`). The Figma grid2 artwork (9 dots) **is in the font** at U+E932, with no class. | Point `icon-grid2` at U+E932. (Supersedes the 2026-08 note above that the grid hasn't shipped: the 9-dot glyph is there, just not wired up. The square-tile `grid` in Pending Updates is a different icon; see 20.2.) |
| `windows8` | `icon-windows8` shows warning2 (U+E986). The Windows logo is in the font at U+E987, with no class. | Point `icon-windows8` at U+E987. |
| `book3` | `icon-book3` points at U+0065 (the letter "e"). The closed book is in the font at U+E993, with no class. | Point `icon-book3` at U+E993. |
| `content_copy` | No class. The glyph is in the font at U+E921. | Add `icon-content_copy` (or the agreed name) → U+E921. |
| `ios_share` | No class. The glyph is in the font at U+E93A. | Add `icon-ios_share` → U+E93A. |
| `home`, `menu7`, `enlarge7` | Same glyphs, but production names them `icon-home3`, `icon-hamburger` and `icon-enlarge`. Already listed in the Figma page's CHANGE section and in `components/icons.md` §3 as naming fixes. | Decide which name wins (design and dev); rename the Figma entry or add the Figma name as a production alias. |
| "iTunes / Apple Music" | Same glyph as `icon-music5`; no class with this name. | Naming only; no font change. |
| *(none)* | `icon-google-plus` (no glyph), `icon-mng-podcast1` (= android) and `icon-users4` (= user4) have no Figma entry. `google-plus` and `mng-podcast1` are in the table above; `users4` was set aside by Karl 2026-08-31. U+E941 (a second padlock) is in the font with no class and no Figma entry. | Remove the dead classes; U+E941 can go in a font rebuild. |

### 20.2 Known missing icons (to be added; not mismatches)

Listed in the Figma page's **Pending Updates**. None is in the production font under any name. Figma artwork for all 12 is in `tokens/icons/svg-missing/`.

- **ADD:** `plus-circle`, `plus-circle2`, `minus-circle`, `minus-circle2`, `list`, `grid` (square tiles), `crown`, `giving-hand`, `yield-filled`, `yield-outline`.
- **CHANGE:** `notification-outlines` (replaces `notification`) and `notification-filled` (replaces `notification2`). Same items as the `notification-filled` / `notification-outlines` row above.

**Status:** Open.

---

## 21. Color Tokens — theme and sub-theme color fixes (every publication)

**Found:** 2026-08-03 production columns of the Color Pallets | 2026.09.10 style guides (PMP re-audited 2026-09-24, Hartford Courant verified 2026-09-25, NEPA and the disputed Tribune sites verified 2026-10-01). Logged here 2026-09-25, when every style guide's red-dashed production callouts were carried into the portable color files. The full per-theme list moved here from `tokens/colors/mng-colors-engineering-fixes.md` on 2026-09-30 (that file is retired).

**Figma spec (source of truth):** each theme's or sub-theme's should-be column on the Color Pallets page, and the matching Colors collection mode. Every row in the tables below is a red-dashed callout in that theme's "in Production" column. Fix production; don't change the tokens.

**How to read this:** find the publication in the index at the end of this entry, then go to its theme or sub-theme. Every site on that theme or sub-theme needs those fixes. Documented site exceptions are listed separately and need no fix. The same data is per publication in `tokens/colors/mng-colors-sites.csv` (`engineering_fixes` column) and `tokens/colors/mng-colors.tokens.json` (`$extensions.com.mng.mismatches`).

**Where to read colors live:** themed variables on `document.querySelector('#page')`, not `:root` (the Customizer override is scoped to `#page`; see the method note at the end of this doc).

**Most common gaps:** `--primary-lighter` isn't set on most themes (the page falls back to a shared default), and Measured Vibrant, its sub-themes and NEPA-PMP all render `--tertiary` as `#303F9F` instead of their design values.

**Status:** Open.

### Summary

| Theme / sub-theme | Level | Parent | Fixes | Publications |
|---|---|---|---|---|
| Bold Coastal | theme | — | 2 | 2 |
| Modern Earthy | theme | — | 4 | 25 |
| Measured Vibrant | theme | — | 2 | 23 |
| Denver Post | sub-theme | Bold Coastal | 3 | 1 |
| East Bay Times | sub-theme | Bold Coastal | 2 | 1 |
| The Mercury News | sub-theme | Bold Coastal | 1 | 1 |
| St. Paul Pioneer Press | sub-theme | Bold Coastal | 5 | 1 |
| Petaluma Argus-Courier | sub-theme | Bold Coastal | 1 | 1 |
| The Press Democrat | sub-theme | Bold Coastal | 3 | 2 |
| The Sonoma Index-Tribune | sub-theme | Bold Coastal | 1 | 1 |
| The Baltimore Sun | sub-theme | Bold Coastal | — | 1 |
| Capital Gazette | sub-theme | Bold Coastal | 3 | 1 |
| Morning Call | sub-theme | Modern Earthy | 6 | 1 |
| 21C Michigan Sites (Combined) | sub-theme | Modern Earthy | 3 | 4 |
| Boston Herald | sub-theme | Modern Earthy | 4 | 1 |
| Daily Herald | sub-theme | Modern Earthy | — (not live on MNG themes yet) | 1 |
| NEPA-PMP | sub-theme | Modern Earthy | 2 | 24 |
| Chicago Tribune | sub-theme | Measured Vibrant | 2 | 1 |
| South Florida Sun Sentinel | sub-theme | Measured Vibrant | 2 | 1 |
| Orlando Sentinel | sub-theme | Measured Vibrant | 2 | 1 |
| GrowthSpotter | sub-theme | Measured Vibrant | 2 | 1 |
| Hartford Courant | sub-theme | Measured Vibrant | 6 | 1 |
| Endless Tributes | product | — | — | 0 |

### Bold Coastal

Loads: `boldcoastal.css`. Figma mode: BoldCoastal. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#1799a5` | `MISSING` | Define --primary-lighter: #1799a5 (boldcoastal.css, body). It isn't set today. |
| `--tertiary` | `#f4a700` | `#00838f` (Theme default (body)) | Change --tertiary from #00838f to #f4a700 (boldcoastal.css, body). |

**Publications:** Orange County Register (ocregister.com), Torrance Daily Breeze (dailybreeze.com)

### Modern Earthy

Loads: `modernearthy.css`. Figma mode: ModernEarthy. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#fe521e` | `MISSING` | Define --primary-lighter: #fe521e (modernearthy.css, body). It isn't set today. |
| `--primary` | `#cc3300` | `#bc3b10` (Theme default (body)) | Change --primary from #bc3b10 to #cc3300 (modernearthy.css, body). |
| `--primary-darker` | `#a52804` | `MISSING` | Define --primary-darker: #a52804 (modernearthy.css, body). It isn't set today. |
| `--tertiary` | `#00828f` | `#ff5722` (Theme default (body)) | Change --tertiary from #ff5722 to #00828f (modernearthy.css, body). |

**Publications:** Kingston Daily Freeman (dailyfreeman.com), Oneida Daily Dispatch (oneidadispatch.com), Saratogian (saratogian.com), The Troy Record (troyrecord.com), Lake County News-Herald (news-herald.com), Lorain Morning Journal (morningjournal.com), Delaware County Times (delcotimes.com), Norristown Times Herald (timesherald.com), Reading Eagle (readingeagle.com), The Lansdale Reporter (thereporteronline.com), The Pottstown Mercury (pottsmerc.com), Trentonian (trentonian.com), West Chester Daily Local (dailylocal.com), Main Line Media News (mainlinemedianews.com), Silicon Valley (siliconvalley.com), Nashoba Valley Voice (nashobavalleyvoice.com), Lowell Sun (lowellsun.com), Sentinel & Enterprise (Fitchburg) (sentinelandenterprise.com), LA Daily News (dailynews.com), Pasadena Star-News (pasadenastarnews.com), Press Enterprise (Riverside) (pressenterprise.com), San Bernardino Sun (sbsun.com), San Gabriel Valley Tribune (sgvtribune.com), Whittier Daily News (whittierdailynews.com), Excelsior California (excelsiorcalifornia.com)

### Measured Vibrant

Loads: `measuredvibrant.css`. Figma mode: MeasuredVibrant. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Publications:** Marin Independent Journal (marinij.com), Chico Enterprise-Record (chicoer.com), Lake County Record-Bee (record-bee.com), Monterey Herald (montereyherald.com), Santa Cruz Sentinel (santacruzsentinel.com), Ukiah Daily Journal (ukiahdailyjournal.com), Vacaville Reporter (thereporter.com), Vallejo Times-Herald (timesheraldonline.com), Woodland Daily Democrat (dailydemocrat.com), Oroville Mercury-Register (orovillemr.com), Red Bluff Daily News (redbluffdailynews.com), Eureka Times-Standard (times-standard.com), Fort Bragg Advocate-News (advocate-news.com), The Mendocino Beacon (mendocinobeacon.com), Paradise Post (paradisepost.com), The Willits News (willitsnews.com), Inland Valley Daily Bulletin (dailybulletin.com), Long Beach Press-Telegram (presstelegram.com), Redlands Daily Facts (redlandsdailyfacts.com), San Diego Union-Tribune (sandiegouniontribune.com), Daily Press (dailypress.com), New York Daily News (nydailynews.com), The Virginian-Pilot (pilotonline.com)

### Denver Post (sub-theme of Bold Coastal)

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: DenverPost. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#c81632` | `#af1628` | Change --primary-lighter from #af1628 to #c81632 (Customizer, div#page). |
| `--primary-light` | `#af1628` | `#c81632` | Change --primary-light from #c81632 to #af1628 (Customizer, div#page). |
| `--tertiary` | `#ffc518` | `#a13b1e` | Change --tertiary from #a13b1e to #ffc518 (Customizer, div#page). |

**Publications:** The Denver Post (denverpost.com)

### East Bay Times (sub-theme of Bold Coastal)

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: East Bay Times. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--secondary` | `#ffc518` | `#eeff41` | Change --secondary from #eeff41 to #ffc518 (Customizer, div#page). |
| `--subsite-custom` | `undocumented` | `#0097a7` | Production sets --subsite-custom: #0097a7, but design has no value. Design to confirm: document it, or engineering removes it. |

**Publications:** East Bay Times (eastbaytimes.com)

### The Mercury News (sub-theme of Bold Coastal)

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: The Mercury News. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--subsite-custom` | `undocumented` | `#0097a7` | Production sets --subsite-custom: #0097a7, but design has no value. Design to confirm: document it, or engineering removes it. |

**Publications:** The Mercury News (mercurynews.com)

### St. Paul Pioneer Press (sub-theme of Bold Coastal)

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: St. Paul Pioneer Press. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#0187e0` | `MISSING` | Define --primary-lighter: #0187e0 (Customizer, div#page). It isn't set today. |
| `--primary-darker` | `#005892` | `MISSING` | Define --primary-darker: #005892 (Customizer, div#page). It isn't set today. |
| `--secondary` | `#ffea00` | `MISSING` | Define --secondary: #ffea00 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#f4a700` | `MISSING` | Define --tertiary: #f4a700 (Customizer, div#page). It isn't set today. |
| `--subsite-custom` | `#0097a7` | `#ffffff` (div#page override) | Change --subsite-custom from #ffffff to #0097a7 (Customizer, div#page). |

**Publications:** St. Paul Pioneer Press (twincities.com)

### Petaluma Argus-Courier (sub-theme of Bold Coastal)

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: Petaluma Argus-Courier. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--secondary` | `#ffea00` | `MISSING` | Define --secondary: #ffea00 (Customizer, div#page). It isn't set today. |

**Publications:** Petaluma Argus-Courier (petalumanews.com)

### The Press Democrat (sub-theme of Bold Coastal)

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: The Press Democrat. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--secondary` | `#ffea00` | `MISSING` | Define --secondary: #ffea00 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#006fb7` | `#d10f14` (div#page override) | Change --tertiary from #d10f14 to #006fb7 (Customizer, div#page). |
| `--subsite-custom` | `undocumented` | `#eeeeee` (div#page override) | Production sets --subsite-custom: #eeeeee, but design has no value. Design to confirm: document it, or engineering removes it. |

**Publications:** The Press Democrat (pressdemocrat.com), Sonoma County Gazette (sonomacountygazette.com)

### The Sonoma Index-Tribune (sub-theme of Bold Coastal)

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: The Sonoma Index-Tribune. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--secondary` | `#ffea00` | `MISSING` | Define --secondary: #ffea00 (Customizer, div#page). It isn't set today. |

**Publications:** The Sonoma Index-Tribune (sonomanews.com)

### The Baltimore Sun (sub-theme of Bold Coastal)

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: none (not a Figma mode).

> Uses its documented Figma styles as is. No production comparison is tracked.

**Publications:** The Baltimore Sun (baltimoresun.com)

### Capital Gazette (sub-theme of Bold Coastal)

Loads: `boldcoastal.css + Customizer override (div#page)`. Figma mode: none (not a Figma mode). Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#3c6f95` | `#285f87` (div#page override) | Change --primary-lighter from #285f87 to #3c6f95 (Customizer, div#page). |
| `--primary-dark` | `#004171` | `#004e87` (div#page override) | Change --primary-dark from #004e87 to #004171 (Customizer, div#page). |
| `--primary-darker` | `#04365a` | `#014a52` (Theme default (inherited)) | Change --primary-darker from #014a52 to #04365a (Customizer, div#page). |

**Publications:** Capital Gazette (capitalgazette.com)

### Morning Call (sub-theme of Modern Earthy)

Loads: `modernearthy.css + Customizer override (div#page)`. Figma mode: Morning Call. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#5399c4` | `MISSING` | Define --primary-lighter: #5399c4 (Customizer, div#page). It isn't set today. |
| `--primary-light` | `#27719f` | `#337ca9` (div#page override) | Change --primary-light from #337ca9 to #27719f (Customizer, div#page). |
| `--primary` | `#166291` | `#014b78` (div#page override) | Change --primary from #014b78 to #166291 (Customizer, div#page). |
| `--primary-darker` | `#00385a` | `MISSING` | Define --primary-darker: #00385a (Customizer, div#page). It isn't set today. |
| `--secondary` | `#eeff41` | `MISSING` | Define --secondary: #eeff41 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#ff5722` | `MISSING` | Define --tertiary: #ff5722 (Customizer, div#page). It isn't set today. |

**Publications:** The Morning Call (mcall.com)

### 21C Michigan Sites (Combined) (sub-theme of Modern Earthy)

Loads: `modernearthy.css + Customizer override (div#page), identical on all 4 sites`. Figma mode: 21C Michigan Sites (Combined). Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#3e7cb2` | `MISSING` | Define --primary-lighter: #3e7cb2 (Customizer, div#page). It isn't set today. |
| `--primary-dark` | `#32476c` | `#3a527a` (div#page override) | Change --primary-dark from #3a527a to #32476c (Customizer, div#page). |
| `--primary-darker` | `#2c3b55` | `#003d66` (Theme default (inherited)) | Change --primary-darker from #003d66 to #2c3b55 (Customizer, div#page). |

**Publications:** Daily Oakland Press (theoaklandpress.com), Macomb Daily (macombdaily.com), Mount Pleasant Morning Sun (themorningsun.com), The News-Herald (Southgate) (thenewsherald.com)

### Boston Herald (sub-theme of Modern Earthy)

Loads: `modernearthy.css + Customizer override (div#page)`. Figma mode: Boston Herald. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#3c81c7` | `MISSING` | Define --primary-lighter: #3c81c7 (Customizer, div#page). It isn't set today. |
| `--primary-darker` | `#0f496f` | `MISSING` | Define --primary-darker: #0f496f (Customizer, div#page). It isn't set today. |
| `--secondary` | `#eeff41` | `MISSING` | Define --secondary: #eeff41 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#ff5722` | `MISSING` | Define --tertiary: #ff5722 (Customizer, div#page). It isn't set today. |

**Publications:** Boston Herald (bostonherald.com)

### Daily Herald (sub-theme of Modern Earthy)

New palette, added 2026-10-15 (Karl). Planned delivery: `modernearthy.css + Customizer override (div#page)`. Not a Figma mode (the Colors collection is at its 20-mode limit); the spec is the "Daily Herald — Style Guide" section on the Color Pallets page and `tokens/themes/daily-herald.tokens.json`.

No fixes yet: dailyherald.com still runs on Everyware (verified 2026-09-24), so there is no production column to compare. When it moves to Modern Earthy, set all ten values in the Customizer (`div#page`): `--primary-lighter` `#3b97dc`, `--primary-light` `#087abe`, `--primary` `#0072b4`, `--primary-dark` `#0066a2`, `--primary-darker` `#0e598b`, `--secondary` `#eeff41`, `--tertiary` `#ff5722` (`--near-black`, `--white` and `--nav-text` use the Modern Earthy defaults `#1a1a1a` / `#fafafa` / `#1a1a1a`). Then audit it like the other sub-themes.

**Publications:** Daily Herald (dailyherald.com)

### NEPA-PMP (sub-theme of Modern Earthy)

Loads: `modernearthy.css + color override on body: site-pmp style.min.css (PMP sites) or each NEPA site's own site plugin (site-citizensvoice, site-thetimes-tribune, site-wcexaminer, site-republicanherald, site-standardspeaker), identical values`. Figma mode: NEPA-PMP. Production audited 2026-10-01.

> One color sub-theme for two groups: the 19 PMP sites (shared site-pmp stylesheet) and the 5 NEPA sites (each site's own plugin stylesheet). Verified live 2026-10-01: NEPA sets the same six variables on body with identical values, and renders the same type as PMP.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits modernearthy.css :root default #47b6ff) | Define --primary-lighter: #717fd1 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (site-pmp / NEPA site override (body)) | Change --tertiary from #303f9f to #eb5300 (site-pmp style.min.css on PMP sites, each NEPA site plugin on NEPA sites; body). |

**Publications:** Colorado Daily (coloradodaily.com), Julesburg Advocate (julesburgadvocate.com), Lamar Ledger (lamarledger.com), The Citizens' Voice (Wilkes-Barre) (citizensvoice.com), Scranton Times-Tribune (thetimes-tribune.com), Wyoming County Examiner (wcexaminer.com), Republican Herald (Pottsville) (republicanherald.com), Standard-Speaker (Hazleton) (standardspeaker.com), Boulder Daily Camera (dailycamera.com), Greeley Tribune (greeleytribune.com), Longmont Times-Call (timescall.com), Loveland Reporter-Herald (reporterherald.com), Akron News-Reporter (akronnewsreporter.com), BoCoPreps (bocopreps.com), Broomfield Enterprise (broomfieldenterprise.com), Brush News-Tribune (brushnewstribune.com), Buffzone (buffzone.com), Cañon City Daily Record (canoncitydailyrecord.com), Colorado Hometown Weekly (coloradohometownweekly.com), Estes Park Trail-Gazette (eptrail.com), Fort Morgan Times (fortmorgantimes.com), South Platte Sentinel (southplattesentinel.com), Sterling Journal-Advocate (journal-advocate.com), The Burlington Record (burlington-record.com)

### Chicago Tribune (sub-theme of Measured Vibrant)

Loads: `measuredvibrant.css (Measured Vibrant values; own Figma mode)`. Figma mode: Chicago Tribune.

> No style guide of its own; audited under Measured Vibrant, whose production callouts apply.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#717fd1` | `MISSING` (inherits shared default #47b6ff) | Define --primary-lighter: #717fd1 (measuredvibrant.css, body). It isn't set today; the page falls back to #47b6ff. |
| `--tertiary` | `#eb5300` | `#303f9f` (Theme default (body)) | Change --tertiary from #303f9f to #eb5300 (measuredvibrant.css, body). |

**Publications:** Chicago Tribune (chicagotribune.com)

### South Florida Sun Sentinel (sub-theme of Measured Vibrant)

Loads: `measuredvibrant.css + Customizer override (div#page)`. Figma mode: South Florida Sun Sentinel. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#4a92af` | `MISSING` | Define --primary-lighter: #4a92af (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#ab9500` | `#303f9f` (Theme default (inherited)) | Change --tertiary from #303f9f to #ab9500 (Customizer, div#page). |

**Publications:** South Florida Sun Sentinel (sun-sentinel.com)

### Orlando Sentinel (sub-theme of Measured Vibrant)

Loads: `measuredvibrant.css + Customizer override (div#page)`. Figma mode: Orlando Sentinel. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#5c95dd` | `MISSING` | Define --primary-lighter: #5c95dd (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#48a395` | `#303f9f` (Theme default (inherited)) | Change --tertiary from #303f9f to #48a395 (Customizer, div#page). |

**Publications:** Orlando Sentinel (orlandosentinel.com)

### GrowthSpotter (sub-theme of Measured Vibrant)

Loads: `measuredvibrant.css + Customizer override (div#page)`. Figma mode: GrowthSpotter. Production audited 2026-08-03.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#529950` | `MISSING` | Define --primary-lighter: #529950 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#e7632a` | `#303f9f` (Theme default (inherited)) | Change --tertiary from #303f9f to #e7632a (Customizer, div#page). |

**Publications:** GrowthSpotter (growthspotter.com)

### Hartford Courant (sub-theme of Measured Vibrant)

Loads: `measuredvibrant.css + site-tribune style.min.css + Customizer override (div#page)`. Figma mode: Hartford Courant. Production audited 2026-09-25.

> Verified live 2026-09-25: loads measuredvibrant.css + site-tribune style.min.css, with a div#page Customizer override (primary, light and dark all #2b7ea5). Production matches the Figma production column.

| Token | Design | Production | Fix |
|---|---|---|---|
| `--primary-lighter` | `#5796bd` | `MISSING` | Define --primary-lighter: #5796bd (Customizer, div#page). It isn't set today. |
| `--primary` | `#166d95` | `#2b7ea5` (div#page override) | Change --primary from #2b7ea5 to #166d95 (Customizer, div#page). |
| `--primary-dark` | `#084e6f` | `#2b7ea5` (same as --primary (div#page)) | Change --primary-dark from #2b7ea5 to #084e6f (Customizer, div#page). |
| `--primary-darker` | `#171e44` | `MISSING` | Define --primary-darker: #171e44 (Customizer, div#page). It isn't set today. |
| `--secondary` | `#eeff41` | `MISSING` | Define --secondary: #eeff41 (Customizer, div#page). It isn't set today. |
| `--tertiary` | `#6a54ca` | `MISSING` | Define --tertiary: #6a54ca (Customizer, div#page). It isn't set today. |

**Publications:** Hartford Courant (courant.com)

### Endless Tributes

Loads: `obituaries pages, identical on every site`. Figma mode: Endless Tributes.

> Shared obituaries palette. Production gaps are logged in entry 11.

### Documented exceptions (no fix needed)

These sites intentionally differ from their sub-theme. They are noted in Figma under the sub-theme's style guide without red outlines. Leave them as they are (see also entry 18).

#### Greeley Tribune (greeleytribune.com), under NEPA-PMP

| Token | NEPA-PMP value | Site value (keep) | Set in |
|---|---|---|---|
| `--primary` | `#3f51b5` | `#536e7f` | div#page Customizer override |
| `--primary-light` | `#5869ca` | `#5b7b8b` | div#page Customizer override |
| `--primary-dark` | `#32408f` | `#44687f` | div#page Customizer override |

It still needs the sub-theme fixes above for the tokens it doesn't override.

### Platform-wide (all publications)

- Universal grays: every site ships `--site-branding-gray-100…600` with the old CRUX `grayRoot` values. Change them to `color/gray/100…600`. See entry 10.
- Obituaries: `--*-obit` widget variables still live, tan-light drift (`#ecede7` vs `#e8e6e2`) and the undocumented `#ccc7bc`. See entry 11.

### Needs a live check before fixing

None. The sites whose theme was disputed (the 5 NEPA sites, Daily Press, The Morning Call, New York Daily News, GrowthSpotter) were verified live on 2026-10-01; see their notes in `tokens/colors/mng-colors-sites.csv`.

### Index: every publication

| Publication | Domain | Cluster | Theme | Sub-theme | Fixes |
|---|---|---|---|---|---|
| Daily Oakland Press | theoaklandpress.com | 21C Michigan | Modern Earthy | 21C Michigan Sites (Combined) | 3 |
| Macomb Daily | macombdaily.com | 21C Michigan | Modern Earthy | 21C Michigan Sites (Combined) | 3 |
| Mount Pleasant Morning Sun | themorningsun.com | 21C Michigan | Modern Earthy | 21C Michigan Sites (Combined) | 3 |
| The News-Herald (Southgate) | thenewsherald.com | 21C Michigan | Modern Earthy | 21C Michigan Sites (Combined) | 3 |
| Kingston Daily Freeman | dailyfreeman.com | 21C New York | Modern Earthy | — | 4 |
| Oneida Daily Dispatch | oneidadispatch.com | 21C New York | Modern Earthy | — | 4 |
| Saratogian | saratogian.com | 21C New York | Modern Earthy | — | 4 |
| The Troy Record | troyrecord.com | 21C New York | Modern Earthy | — | 4 |
| Lake County News-Herald | news-herald.com | 21C Ohio | Modern Earthy | — | 4 |
| Lorain Morning Journal | morningjournal.com | 21C Ohio | Modern Earthy | — | 4 |
| Delaware County Times | delcotimes.com | 21C Pennsylvania | Modern Earthy | — | 4 |
| Main Line Media News | mainlinemedianews.com | 21C Pennsylvania | Modern Earthy | — | 4 |
| Norristown Times Herald | timesherald.com | 21C Pennsylvania | Modern Earthy | — | 4 |
| Reading Eagle | readingeagle.com | 21C Pennsylvania | Modern Earthy | — | 4 |
| The Lansdale Reporter | thereporteronline.com | 21C Pennsylvania | Modern Earthy | — | 4 |
| The Pottstown Mercury | pottsmerc.com | 21C Pennsylvania | Modern Earthy | — | 4 |
| Trentonian | trentonian.com | 21C Pennsylvania | Modern Earthy | — | 4 |
| West Chester Daily Local | dailylocal.com | 21C Pennsylvania | Modern Earthy | — | 4 |
| East Bay Times | eastbaytimes.com | BANG | Bold Coastal | East Bay Times | 2 |
| Marin Independent Journal | marinij.com | BANG | Measured Vibrant | — | 2 |
| Silicon Valley | siliconvalley.com | BANG | Modern Earthy | — | 4 |
| The Mercury News | mercurynews.com | BANG | Bold Coastal | The Mercury News | 1 |
| Boston Herald | bostonherald.com | Boston | Modern Earthy | Boston Herald | 4 |
| Nashoba Valley Voice | nashobavalleyvoice.com | Boston | Modern Earthy | — | 4 |
| Colorado Daily | coloradodaily.com | Colorado Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Julesburg Advocate | julesburgadvocate.com | Colorado Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Lamar Ledger | lamarledger.com | Colorado Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Daily Herald | dailyherald.com | Daily Herald | Modern Earthy (planned) | Daily Herald | — (not live on MNG themes yet) |
| The Denver Post | denverpost.com | Denver | Bold Coastal | Denver Post | 3 |
| Lowell Sun | lowellsun.com | Fitch | Modern Earthy | — | 4 |
| Sentinel & Enterprise (Fitchburg) | sentinelandenterprise.com | Fitch | Modern Earthy | — | 4 |
| Republican Herald (Pottsville) | republicanherald.com | NEPA | Modern Earthy | NEPA-PMP | 2 |
| Scranton Times-Tribune | thetimes-tribune.com | NEPA | Modern Earthy | NEPA-PMP | 2 |
| Standard-Speaker (Hazleton) | standardspeaker.com | NEPA | Modern Earthy | NEPA-PMP | 2 |
| The Citizens' Voice (Wilkes-Barre) | citizensvoice.com | NEPA | Modern Earthy | NEPA-PMP | 2 |
| Wyoming County Examiner | wcexaminer.com | NEPA | Modern Earthy | NEPA-PMP | 2 |
| Chico Enterprise-Record | chicoer.com | Norcal | Measured Vibrant | — | 2 |
| Eureka Times-Standard | times-standard.com | Norcal | Measured Vibrant | — | 2 |
| Lake County Record-Bee | record-bee.com | Norcal | Measured Vibrant | — | 2 |
| Monterey Herald | montereyherald.com | Norcal | Measured Vibrant | — | 2 |
| Oroville Mercury-Register | orovillemr.com | Norcal | Measured Vibrant | — | 2 |
| Red Bluff Daily News | redbluffdailynews.com | Norcal | Measured Vibrant | — | 2 |
| Santa Cruz Sentinel | santacruzsentinel.com | Norcal | Measured Vibrant | — | 2 |
| Ukiah Daily Journal | ukiahdailyjournal.com | Norcal | Measured Vibrant | — | 2 |
| Vacaville Reporter | thereporter.com | Norcal | Measured Vibrant | — | 2 |
| Vallejo Times-Herald | timesheraldonline.com | Norcal | Measured Vibrant | — | 2 |
| Woodland Daily Democrat | dailydemocrat.com | Norcal | Measured Vibrant | — | 2 |
| Fort Bragg Advocate-News | advocate-news.com | Norcal Weeklies | Measured Vibrant | — | 2 |
| Paradise Post | paradisepost.com | Norcal Weeklies | Measured Vibrant | — | 2 |
| The Mendocino Beacon | mendocinobeacon.com | Norcal Weeklies | Measured Vibrant | — | 2 |
| The Willits News | willitsnews.com | Norcal Weeklies | Measured Vibrant | — | 2 |
| Boulder Daily Camera | dailycamera.com | PMP | Modern Earthy | NEPA-PMP | 2 |
| Greeley Tribune | greeleytribune.com | PMP | Modern Earthy | NEPA-PMP | 2 |
| Longmont Times-Call | timescall.com | PMP | Modern Earthy | NEPA-PMP | 2 |
| Loveland Reporter-Herald | reporterherald.com | PMP | Modern Earthy | NEPA-PMP | 2 |
| Akron News-Reporter | akronnewsreporter.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| BoCoPreps | bocopreps.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Broomfield Enterprise | broomfieldenterprise.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Brush News-Tribune | brushnewstribune.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Buffzone | buffzone.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Cañon City Daily Record | canoncitydailyrecord.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Colorado Hometown Weekly | coloradohometownweekly.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Estes Park Trail-Gazette | eptrail.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Fort Morgan Times | fortmorgantimes.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| South Platte Sentinel | southplattesentinel.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Sterling Journal-Advocate | journal-advocate.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| The Burlington Record | burlington-record.com | PMP Weeklies | Modern Earthy | NEPA-PMP | 2 |
| Excelsior California | excelsiorcalifornia.com | SCNG | Modern Earthy | — | 4 |
| Inland Valley Daily Bulletin | dailybulletin.com | SCNG | Measured Vibrant | — | 2 |
| LA Daily News | dailynews.com | SCNG | Modern Earthy | — | 4 |
| Long Beach Press-Telegram | presstelegram.com | SCNG | Measured Vibrant | — | 2 |
| Orange County Register | ocregister.com | SCNG | Bold Coastal | — | 2 |
| Pasadena Star-News | pasadenastarnews.com | SCNG | Modern Earthy | — | 4 |
| Press Enterprise (Riverside) | pressenterprise.com | SCNG | Modern Earthy | — | 4 |
| Redlands Daily Facts | redlandsdailyfacts.com | SCNG | Measured Vibrant | — | 2 |
| San Bernardino Sun | sbsun.com | SCNG | Modern Earthy | — | 4 |
| San Diego Union-Tribune | sandiegouniontribune.com | SCNG | Measured Vibrant | — | 2 |
| San Gabriel Valley Tribune | sgvtribune.com | SCNG | Modern Earthy | — | 4 |
| Torrance Daily Breeze | dailybreeze.com | SCNG | Bold Coastal | — | 2 |
| Whittier Daily News | whittierdailynews.com | SCNG | Modern Earthy | — | 4 |
| Petaluma Argus-Courier | petalumanews.com | Sonoma | Bold Coastal | Petaluma Argus-Courier | 1 |
| Sonoma County Gazette | sonomacountygazette.com | Sonoma | Bold Coastal | The Press Democrat | 3 |
| Sonoma Magazine | sonomamag.com | Sonoma | — | — | n/a (not on MNG themes) |
| The Press Democrat | pressdemocrat.com | Sonoma | Bold Coastal | The Press Democrat | 3 |
| The Sonoma Index-Tribune | sonomanews.com | Sonoma | Bold Coastal | The Sonoma Index-Tribune | 1 |
| Capital Gazette | capitalgazette.com | Tribune | Bold Coastal | Capital Gazette | 3 |
| Chicago Tribune | chicagotribune.com | Tribune | Measured Vibrant | Chicago Tribune | 2 |
| Daily Press | dailypress.com | Tribune | Measured Vibrant | — | 2 |
| GrowthSpotter | growthspotter.com | Tribune | Measured Vibrant | GrowthSpotter | 2 |
| Hartford Courant | courant.com | Tribune | Measured Vibrant | Hartford Courant | 6 |
| New York Daily News | nydailynews.com | Tribune | Measured Vibrant | — | 2 |
| Orlando Sentinel | orlandosentinel.com | Tribune | Measured Vibrant | Orlando Sentinel | 2 |
| South Florida Sun Sentinel | sun-sentinel.com | Tribune | Measured Vibrant | South Florida Sun Sentinel | 2 |
| The Baltimore Sun | baltimoresun.com | Tribune | Bold Coastal | The Baltimore Sun | — |
| The Morning Call | mcall.com | Tribune | Modern Earthy | Morning Call | 6 |
| The Virginian-Pilot | pilotonline.com | Tribune | Measured Vibrant | — | 2 |
| St. Paul Pioneer Press | twincities.com | Twin Cities | Bold Coastal | St. Paul Pioneer Press | 5 |

---

## 22. Spacing — 10px and 14px values off the 4/8 grid

**Found:** 2026-10-01, while creating the spacing tokens. Measured live on chicagotribune.com (homepage, 1728px viewport, every visible element's padding, margin and gap).

**Figma spec (source of truth):** spacing follows the 4/8 grid. The main file's "Spacing & Radius" collection has `spacing/050` 4, `spacing/100` 8, `spacing/150` 12, `spacing/200` 16, `spacing/250` 20, `spacing/300` 24.

**Decision (Karl, 2026-10-01):** 10px and 14px are production drift, not design values. They are not tokens; production should move to the nearest grid value.

**Production:**

| Where | Live value | Fix |
|---|---|---|
| `.subscribe-button` (header, footer and article paywall CTA) | padding 14px / 10px | Use Button Primary Default: 16px / 20px (`spacing/200` / `spacing/250`). Same fix as entry 1. |
| Main content wrapper (left/right page gutter) | padding 0 10px | Use `spacing/100` (8px) or `spacing/150` (12px); confirm with design which one. |
| `ul.footer-menus`, `div.colophon` | padding 0 10px | Same as the page gutter. |

**Context:** on that page 10px appears 17 times. The grid values are far more common (16px 79, 12px 46, 32px 36, 8px 34, 4px 28). Other off-grid values also appear (15px 38, 17px 20, 19px 17, 3px 28) and should be reviewed in a later pass.

**Engineering patch (ready to apply):**

```css
/* 22a. Subscribe CTA = Button Primary Default (also closes entry 1) */
.subscribe-button {
  padding: 16px 20px;   /* was 14px 10px; spacing/200 vertical, spacing/250 horizontal */
  font-size: 14px;      /* was 15px */
}

/* 22b. Page gutter. GUTTER = 8px (spacing/100) or 12px (spacing/150), pending Karl */
.main-content-wrapper,   /* placeholder: the wrapper with padding: 0 10px today */
ul.footer-menus,
div.colophon {
  padding-left: GUTTER;  /* was 10px */
  padding-right: GUTTER; /* was 10px */
}
```

Check after the change: the subscribe CTA keeps its 44px min height and its fill color per masthead, and the header, body and footer edges still line up with each other.

**Status:** Open. 22a is ready for Engineering. 22b needs one design decision first (8px or 12px).

---

## 23. Radius — buttons are 4px; 5px on a button is drift

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
/* 23a. Masthead search submit = button radius */
.search-button {
  border-radius: 4px;   /* was 5px; radius/sm */
}
/* Leave the account dropdown at 0 0 5px 5px (radius/utility, container). */
```

**Status:** Open. Ready for Engineering.

---

## 24. Breaking News bar — Denver Post uses primary-lighter instead of secondary

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

**Also noted:** Denver Post's live `--tertiary` is `#A13B1E`, but its token is `#FFC518`; and its live `--primary-light` / `--primary-lighter` (`#C81632` / `#AF1628`) are the reverse of the tokens (`#AF1628` / `#C81632`). Check these against entry 21's Denver Post section.

## 25. Sponsored content badge — needs to be fixed in production

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

## 26. Mobile adhesion — empty sticky bar shows at 1024px and up

**Found:** 2026-10-02, ocregister.com at a 1024px window (homepage and article page).

**Figma spec (source of truth):** `mobile_adhesion` exists only below 1024px — Ad Blocks `Mobile Adhesion 320x50` / `300x50` on mobile and `Mobile Adhesion 728x90` at tablet (768). The 1024, 1100 and 1280 templates have no adhesion unit (the 1024 floating anchor was removed 2026-10-02).

**Production:** at 1024px the `#mobile-adhesion` container is still fixed to the bottom of the viewport (1024×90, with its Close button), but the GPT slot has no valid size at that width (`getSizes(1024)` returns an empty list), so no ad can ever load. Readers see an empty bar.

**Fix:** hide the `#mobile-adhesion` container (and its Close button) at the same breakpoint where the slot's size mapping goes empty (≥1024px), or remove the container from the DOM at desktop widths. Check the other five review sites.

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

## 28. Upcoming Events (CitySpark widget) — font family

**Found:** 2026-10-07, ocregister.com (homepage `.csLayHolder` → `.cswidholder` iframe, CitySpark template).

**Figma spec (source of truth):** WordPress Elements `Upcoming Events Widget` matches production's layout, sizes, spacing and colors exactly (Karl, 2026-10-07), but sets all text in **Noto Sans**, like the rest of the design system.

**Production:** every text element in the widget is **Roboto Condensed**: the title "Upcoming Events" 400 20/22, the "See All Events" and "Add your event" buttons 400 12/15, the card dates 400 11, event names 700 13/14, venues 400 12/14, date-strip days 400 15/20 uppercase and dates 400 20/19.

**Fix:** change the CitySpark widget template's font to Noto Sans (same sizes and weights) on every site, with whoever manages the CitySpark account.

## 29. Article breadcrumbs — label font family and text color

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

## 30. Reader Dashboard — breakpoints close to, but not on, the Figma screen widths (questions for DigiScrum)

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

## 31. Obituaries — breakpoints that don't match the WordPress grid (for the CMS team)

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

## 32. Font fallbacks — Helvetica instead of the design stacks (all sites)

**Found:** 2026-10-14, computed `font-family` on all 6 review sites (ocregister, denverpost, chicagotribune, orlandosentinel, canoncitydailyrecord, mcall): nav labels, section headers, card headlines, excerpts, footer and obituaries. **Team:** CMS (WordPress themes).

**Design** (main file, Fonts page, Font Styles and Fallbacks `2768:1051`; tokens `font.family.noto-sans` / `font.family.noto-serif`, CSS `--mng-font-family-noto-sans` / `-serif`):

| Stack | Design (should be) | Production |
|---|---|---|
| Sans (`$body`) | `"Noto Sans", "Helvetica Neue", Arial, sans-serif` | `"Noto Sans", Helvetica, sans-serif` |
| Serif (`$heading`) | `"Noto Serif", Georgia, "Times New Roman", serif` | `"Noto Serif", Helvetica, serif` |

The same two stacks apply on every theme; each theme only chooses which one its headings and body use. Obituaries follow the site's theme.

**Fix:** in the theme font-family definitions, replace `Helvetica` with **Helvetica Neue** (then Arial) in the sans stack (Karl, 2026-10-14), and use Georgia, then Times New Roman, in the serif stack instead of Helvetica. The fallbacks only show when Noto doesn't load, so nothing changes visually when the web fonts work.

**Status:** Open.

## 33. Breakpoints off the official sets — WordPress themes, trust indicators, digisubs (all 6 sites)

**Found:** 2026-10-14, live CSS scan of the homepage, an article and the obituaries page on all 6 review sites (`tokens/breakpoint-inventory.json`, built by `scripts/breakpoint-inventory/`). Every value below was found on all 6 sites (the three theme stylesheets share their media queries). **Teams:** CMS, DigiScrum. **Updated 2026-10-14** with Karl's decisions.

**Design:** two official sets (EXPORT-STANDARD.md section 6). WordPress code follows the **WordPress grid** (min-widths 320 / 640 / 800 / 1040 / 1280; max-widths 639 / 799 / 1039 / 1279). Everything else, including the digisubs plugin and app (Karl, 2026-10-14), follows the **MNG Device breakpoints** (min-widths 340 / 360 / 768 / 1024 / 1280; max-widths 339 / 359 / 767 / 1023 / 1279). Of the 56 values kept in the inventory, 13 are official, 34 are drift (below) and 9 are component breakpoints. Left out: third-party code (paywall, cookie consent, ad vendors), the WordPress admin bar, and the digisubs modal, spoof banner, push prompt, share box and employee debugger (not documented, Karl), and the special investigative header template (see below).

**Production (drift) and fix:** move each rule to the official breakpoint in the right-hand column. The Sports Radar template and the promotion widget follow the WordPress grid (Karl, 2026-10-14). "Off by one" rules (`max-width: 340 / 360 / 800 / 1024 / 1040 / 1280`) overlap the official boundary by 1px and should be one less. The Obituaries values (624 / 625, 1299 / 1300) and the photo gallery (734 / 735) are also in entry 31.

**WordPress themes** (team: CMS; snap to the WordPress grid):

| Production | Where | Snap to |
|---|---|---|
| `(max-width: 405px)` | Sports Radar page template (#content.sports-radar-content; local template styling embedded Sportradar data widgets). | `(max-width: 639px)` (WordPress grid s) |
| `(max-width: 500px)` | Sports Radar page template. | `(max-width: 639px)` (WordPress grid s) |
| `(max-width: 535px)` | Sports Radar page template. | `(max-width: 639px)` (WordPress grid s) |
| `(max-width: 624px)` | Obituaries 1-column layout (entry 31). | `(max-width: 639px)` (WordPress grid s) |
| `(min-width: 625px)` | Obituaries 2-column start (entry 31). | `(min-width: 640px)` (WordPress grid s) |
| `(max-width: 700px)` | Promotion widget (.promotion-widget, homepage promo tiles, e.g. Chicago Tribune Fun and Games / Tribune Store). | `(max-width: 639px)` (WordPress grid s) |
| `(max-width: 734px)` | Photo gallery widget (.gallery-container; also entry 31). Fix (Karl). | `(max-width: 799px)` (WordPress grid m) |
| `(min-width: 735px)` | Photo gallery widget (also entry 31). Fix (Karl). | `(min-width: 800px)` (WordPress grid m) |
| `(max-width: 800px)` | Off by one: (max-width: 800px) overlaps m; should be 799 (#featured-flex-landing-three). | `(max-width: 799px)` (WordPress grid m) |
| `(max-width: 900px)` | Promotion widget title. | `(max-width: 799px)` (WordPress grid m) |
| `(max-width: 930px)` | Footer cookie notice button (Karl: fix to 1039). | `(max-width: 1039px)` (WordPress grid l) |
| `(max-width: 960px)` | Sports Radar page template. | `(max-width: 1039px)` (WordPress grid l) |
| `(max-width: 1280px)` | Off by one: (max-width: 1280px) overlaps xl; should be 1279 (.custom-dfm-section.dark-layout). | `(max-width: 1279px)` (WordPress grid xl) |
| `(max-width: 1299px)` | Obituaries listing (entry 31). | `(max-width: 1279px)` (WordPress grid xl) |
| `(min-width: 1300px)` | Obituaries "stop scaling" (entry 31). | `(min-width: 1280px)` (WordPress grid xl) |

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

## How to use this doc

Add a new dated, numbered entry whenever a Figma-vs-production gap or an explicit engineering/legal flag is found during an audit, rather than quietly "fixing" the design tokens to match whatever production happens to do. Mark each item's status (Open / Fixed / Confirmed-intentional) as it gets resolved, and keep the original finding text rather than deleting it once resolved — see how `tokens/colors/color-tokens-decision-log.md` and the component audit docs annotate resolved items in place, for the pattern to follow here too.

**Method note for live color checks** (from a 2026-08-27 note, since retired): read themed CSS variables such as `--primary` on `document.querySelector('#page')`, not on `document.documentElement`. The WordPress Customizer's per-site override is scoped to `#page`, so reading at `:root` only shows the theme default. That mistake once produced a false drift finding on Modal and Disclosure.
