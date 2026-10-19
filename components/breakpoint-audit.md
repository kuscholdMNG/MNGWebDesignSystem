# Breakpoint Audit

> **Updated 2026-10-02** for current Figma file names and retired handoff notes. Audit content dates from 2026-09-14 to 2026-09-15.
*(Renamed 2026-09-15 from "Masthead Breakpoint Audit" — broadened in scope to catalog every element breakpoint found during the audit, not just the masthead nav.)*

**Date started:** September 14, 2026
**Production reference:** ocregister.com (OC Register)
**Figma source:** "WordPress Elements" file → **Menus and Parts** page → `Masthead` component set (node `456:2572`)
**Also covers:** non-masthead element breakpoints found incidentally while scanning full pages (ad units, content templates, widgets) — see "Site-wide element breakpoint catalog" below.

---

## Scope

Reviewing masthead accuracy (Figma vs. production) for: **Home Page, Section Front, Article Page**.

Excluded from this pass, flagged for a separate follow-up once the above three are done: **Obituaries**, **Reader Dashboard**. (Both already exist as `Page` variants on the same Masthead component set, so the follow-up is scoped to the same component.)

At every breakpoint/page combination, two states are captured (per Karl's addition to scope):
- **Default** — as loaded, no scroll
- **Scrolled** — after scrolling down a short distance (masthead behavior changes on scroll — matches the component set's own `State=Scrolled` variant, and the `.headroom--top` scroll-behavior CSS class confirmed live on OCR)

Ads on screen are logged at each pass (name/size/position), excluding any popups/interstitials. Popups encountered are flagged to Karl to close manually — not dismissed automatically. Viewport resizing between breakpoints is done manually by Karl; Claude does not resize the window itself.

**Scope broadened 2026-09-15:** while investigating whether Obituaries has masthead-specific breakpoints, a full unfiltered `CSSMediaRule` scan surfaced several other elements' breakpoints on the same page (ad units, homepage/article content templates, a photo-gallery widget, search-results listing). Rather than discard that, every element breakpoint found from here forward — masthead or not — gets logged in the new "Site-wide element breakpoint catalog" section below, so this document works as one reference instead of splitting nav-specific and everything-else findings across files.

---

## Real production breakpoints (from literal CSS, not assumed)

Pulled directly from ocregister.com's loaded stylesheets — every `@media` rule whose inner selectors touch `.site-header`, `.nav-primary`, `.nav-wrapper-primary`, `.logo`, `.search-form`, `.header-placeholder`, etc. Converted from `em` (16px base) to px:

| Real tier | CSS range | What changes |
|---|---|---|
| 1 | ≤639px | Mobile masthead: stacked logo, hidden search, hamburger nav |
| 2 | 640–799px | `.header-placeholder`/`.logo`/digisubs & search behavior shift |
| 3 | 800–1039px | Search bar / subscribe-menu layout shifts again |
| 4 | 1040–1279px | Header flips to desktop nav (the documented 1039↔1040 hamburger breakpoint) |
| 5 | ≥1280px | Widest nav spacing; no further header-specific rule found above this |

**Test widths used for this audit** (one per real tier, per Karl): **375 / 700 / 1024 / 1100 / 1280**, plus **1728** as a sanity check that nothing changes further above 1280.

## Figma `Masthead` component coverage vs. real tiers

The component set's `Device` variant has 5 tiers with these built widths:

| Figma `Device` | Built width | Real CSS tier it lands in |
|---|---|---|
| XS-Fold | 340px | Tier 1 (≤639) |
| SM-Mobile | 360px | Tier 1 (≤639) |
| MD-TabletV | 768px | Tier 2 (640–799) |
| LG-TabletH | 1024px | Tier 3 (800–1039) |
| XL-Desktop | ~~1280px~~ → **1040px** (resized 2026-09-15) | Tier 4 (1040–1279) **and** Tier 5 (≥1280) |

**Gap found → closed, 2026-09-15:** nothing in Figma originally represented **Tier 4 (1040–1279px)** — the exact width where production's header switches from hamburger to full desktop nav. The 1100px pass (below) confirmed production renders identically at 1100 and 1280 (same structure, same ad size), so rather than build a separate Tier 4 `Device` variant, Karl opted to resize `XL-Desktop`'s built width down from 1280 to **1040px** — the real breakpoint — so the existing variant now honestly represents both Tier 4 and Tier 5 (this fix originally covered Home/SectionFront/Article only — see the "Obituaries Figma breakpoint-width audit" section below for where the same gap was later found and closed for Obituaries too, and flagged but not yet fixed for Dashboard).

Also note: XS-Fold (340) and SM-Mobile (360) are two separate Figma variants that both fall inside the same real CSS tier (≤639) — kept as separate device mockups (different literal test widths within Tier 1) rather than merged, per the labeling work below.

**✅ Labeled with literal pixel ranges, 2026-09-15 (per Karl's request — whole component set, all 5 Page types):** the `Device` variant's five values were renamed in place, across all 75 variants in the component set, to embed each one's real breakpoint range directly in the name, so the range is visible anywhere the variant name shows up (variant picker, dev mode, layer names) without needing to cross-reference this doc:

| Old `Device` value | New `Device` value |
|---|---|
| `XS-Fold` | `XS-Fold (≤639px · built 340px)` |
| `SM-Mobile` | `SM-Mobile (≤639px · built 360px)` |
| `MD-TabletV` | `MD-TabletV (640–799px)` |
| `LG-TabletH` | `LG-TabletH (800–1039px)` |
| `XL-Desktop` | `XL-Desktop (≥1040px)` |

Ranges use our own measured real CSS tiers (the table above), not generic/assumed breakpoint conventions — confirmed with Karl before executing. XS-Fold and SM-Mobile share the same real-tier range (both ≤639px), so each also carries its own literal built width to stay distinguishable. Middle-dot (`·`) used instead of a comma inside the XS-Fold/SM-Mobile values, since Figma parses variant names as comma-separated `Prop=Value` pairs — tested first on a disposable clone (confirmed a comma inside a value breaks `componentPropertyDefinitions` parsing with a "Component set has existing errors" state) before touching any real variant. All 75 renames verified afterward: `componentPropertyDefinitions['Device'].variantOptions` parses cleanly to the 5 new values, no duplicate names, 75 children still present. `State` values (`Default`/`AdFree`/`Scrolled`/`AdFree-Scrolled`) were left as-is — they're user/scroll states, not breakpoints, so out of scope for this labeling pass.

Also updated the two on-canvas column-header label frames above/below the whole Masthead grid on the "Menus and Parts" page (`Frame 12728` id `456:2550`, `Frame 12729` id `1071:17529`) — each of the 5 column headers had its matching range appended (e.g. `XL-Desktop - 1040x960` → `XL-Desktop - 1040x960 — ≥1040px`). Text boxes are fixed-width per column and confirmed single-line (no wrap/overflow) after the edit.

`Page` variants available: `Home`, `SectionFront`, `Article`, `Obituaries`, `Dashboard`.

---

## Site-wide element breakpoint catalog

*Every distinct element breakpoint found during this project, regardless of whether it's part of the masthead. The masthead nav tiers above remain the primary reference for header work; this table is the catch-all for everything else so nothing gets lost. Add a row here any time a scan (like the Obituaries CSSMediaRule sweep) turns up a new element boundary, even off-topic ones.*

| Element / selector | Breakpoint | Page(s) confirmed | What changes | Masthead-relevant? |
|---|---|---|---|---|
| `.obits-search-form` / `.obits-search-bar` | **624px** (flat px) | Obituaries | `flex-direction: row → column` — search form stacks; Endless Tributes logo shrinks to `max-width: 35%` | **Yes** — inside the masthead's obits search widget; does not match the site-wide 639px Tier 1 boundary |
| `#content .obit-search-content.filter-open` / `.obit-search-content-et.filter-open` | **800px** (`50em`) | Obituaries | `padding-left` changes when the filter panel is expanded | **Yes** — masthead search widget, filter-open state only |
| `#obit-filter-popup` (+ date-filter sub-rules) | 320–639px (`20em`–`39.9375em`) | Obituaries | Date-filter popup sizing | Yes — inside Tier 1, doesn't add a new boundary |
| `.obits-content-header .nav-primary-middle` (accuweather-wrap, hidden-logo, sponsorship) | 320–1039px (`20em`–`64.9375em`), one combined range | Obituaries | Nav-primary-middle search-widget area | Yes — collapses at the existing 1039px Tier 3/4 boundary, not a new one |
| `.nav-wrapper-primary .nav-primary-middle` | 1039px (`64.9375em`) | Obituaries (and all pages) | `display: none` | Yes — matches the existing site-wide tier boundary |
| `.category aside`, `.feature-section .feature-wrapper`, `.feature-section .feature-top .feature-large` | 800px (`50em`) | Obituaries (homepage/article template — likely site-wide) | Homepage/article content grid layout | No — general content template, unrelated to the masthead |
| `.dfp-ad.dfp-top_leaderboard` | 1000px (`min-width: 1000px`) | Obituaries | Top leaderboard ad placement | No — ad unit |
| `.obit-leaderboard.bottom` | 1000px (`62.5rem`) | Obituaries | Bottom leaderboard ad placement | No — ad unit |
| `#content.obits-content .obit-bottom .landing-item .mng-obit-listing .obit-article-search-result` | 1300px (`81.25em`/`81.25rem`) | Obituaries | Obituary search-results listing layout | No — page content, not masthead |
| `.gallery-container`, `.gallery-title`, `.gallery-content`, `.gallery-element` | ~625–734px (`39.0625rem`–`45.875rem`) and ~735–1299px (`45.9375rem`–`81.1875rem`) | Obituaries (likely site-wide — appears to be a shared photo-gallery widget) | Gallery widget responsive steps | No — unrelated widget, happened to be on the same page |

**Not yet catalogued:** Home / Section Front / Article were only scanned for masthead-specific selectors (`.site-header`, `.nav-primary`, `.nav-wrapper-primary`, `.logo`, `.search-form`, `.header-placeholder`) during the original pass — a full unfiltered scan like the one run on Obituaries hasn't been done on those pages yet, so their non-masthead element breakpoints aren't in this table. Worth doing if/when this catalog needs to be comprehensive across all page types, not just Obituaries.

---

## Findings by breakpoint

### 375px (Tier 1 — mobile) — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=SM-Mobile` (360, closest built width).*

**Structure match:** Production masthead at 375px = single 65px row: hamburger, centered logo, account icon (chevron), search icon. No weather/date/trending strip (correctly collapsed). This matches Figma's `SM-Mobile` row structure exactly. Logged-out account icon in production is a plain person glyph vs. Figma's avatar-photo mock — expected difference (Figma mocks a logged-in state), not a bug.

**Scroll behavior:** Confirmed via live CSS class (`headroom--top` → `headroom--not-top headroom--unpinned` after ~450px scroll). The masthead row stays pinned/sticky at the same 65px height; only the ad below it scrolls out of view. Figma's `State=Scrolled` variant correctly shows the same bare row with no ad — **matches**.

**⚠️ Discrepancy found — top ad slot inconsistent across Page variants:**
| Page | Figma `Default` variant shows | Production actually shows |
|---|---|---|
| Home | Ad box labeled **"Top Leaderboard 320x100"** attached below masthead (component total height 180px) | Real ad slot (`div-gpt-ad-top_leaderboard`) renders at **320x50** |
| Section Front | **No ad** below masthead at all (component is just the bare 64px row) | Real ad slot renders at **320x100**, directly below masthead |
| Article | **No ad** below masthead at all (bare 64px row) | Real ad slot renders at **320x50**, directly below masthead |

So Figma only modeled the top ad for the Home variant, and even there the labeled size (320x100) didn't match what Home actually serves (320x50) — it's Section Front that actually gets the 320x100 size.

**Resolved in Figma, 2026-09-15:** per Karl, added/corrected the ad placeholder on all three `Default`-state Page variants (SM-Mobile tier) to match live production — Home → `Top Leaderboard 320x50` (corrected), Section Front → `Top Leaderboard 320x100` (added), Article → `Top Leaderboard 320x50` (added). All three screenshot-verified clean, no overlap.

**Logged for engineering, 2026-09-15:** the underlying production inconsistency (same ad position serving different sizes per page type) is now entry #19 in `design-vs-production.md` (Engineering Handoff), flagged for production to be made consistent.

**Also logged:** the Trust/Source tooltip popup found on the Article page (see Popups below) doesn't have a Figma component yet — added as a new to-do in `Article-Page-To-Do.md`.

**Home Page**
- Default: masthead row + Top Leaderboard ad directly below.
- Scrolled: bare masthead row, ad scrolled out of view.
- Ads on screen (default): `top_leaderboard` 320x50 @ (10,81); sticky `mobile-adhesion` 320x50 fixed at bottom.
- Ads on screen (scrolled ~450px): sticky `mobile-adhesion` 320x50 only.

**Section Front** (ocregister.com/news/)
- Default: masthead row + Top Leaderboard ad directly below.
- Scrolled: bare masthead row, same sticky behavior as Home.
- Ads on screen (default): `top_leaderboard` **320x100** @ (10,81); sticky `mobile-adhesion` 320x50.
- Ads on screen (scrolled): sticky `mobile-adhesion` 320x50 only.

**Article Page**
- Default: masthead row + Top Leaderboard ad directly below.
- Scrolled: bare masthead row, same sticky behavior.
- Ads on screen (default): `top_leaderboard` 320x50 @ (10,81); sticky `mobile-adhesion` 320x50.
- Ads on screen (scrolled): sticky `mobile-adhesion` 320x50 only.
- **Popup encountered (flagged live):** a trust/sourcing-standard tooltip ("Based on facts, either witnessed and verified directly by the reporter, or reported and confirmed from knowledgeable sources.") appeared overlaying the headline area on load, with its own close (X) button. Did not obstruct the masthead itself. Not dismissed automatically — see Popups section below.

---

### 700px (Tier 2) — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=MD-TabletV` (768).*

**Structure match:** Masthead is still the mobile-collapsed row at 700px — hamburger, centered logo, account icon, search icon, 65px tall. No weather/date/trending strip yet (expected — that shift happens at Tier 4/1040px+ per the real CSS breakpoints, not here). Matches Figma's `MD-TabletV` row structure.

**Scroll behavior:** Same sticky-pinned pattern as 375px (`headroom--top` → `headroom--not-top headroom--unpinned`, row stays visible, ad scrolls away). Matches Figma's `Scrolled` variant.

**Ad-size nuance — spot-checked at literal 768px, 2026-09-15, resolved:** Figma's `MD-TabletV` tier shows the top ad consistently on all three Page variants, labeled **"Top Leaderboard 728x90."** At 700px, production never renders that (container capped at 645px — a 728-wide ad can't fit). Re-checked at exactly **768px** (Figma's own built width) on all three page types: **confirmed — the ad slot does switch to 728x90 there** (Home: Capital One 728x90; Section Front: Capital One 728x90; Article: Horan & McConaty 728x90). So Figma's 728x90 label is accurate, just not reachable at 700px.

**Real takeaway:** the ad slot's own responsive breakpoint sits somewhere in **701–768px** — narrower than that, and somewhere at/before 768px, wider. That's a separate breakpoint from the header/nav CSS tier boundaries (which don't move until 1040px), so our "one width per real CSS tier" approach can under-count ad-specific breakpoints. Worth keeping in mind for any future breakpoint work: header structure and ad-slot sizing don't necessarily share the same responsive boundaries.

**Also observed at 768px, Article page:** the sticky bottom `mobile-adhesion` slot rendered a 300×250 creative inside a container only 90px tall (visual overflow — the ad extends past its own container's declared height). Peripheral to the masthead itself, but flagging since it's a layout quirk worth knowing about.

**Popup, recurring:** the same trust/source tooltip from the 375px Article pass reappeared here at 768px on Article page load (same content, same X-close). Did not appear at 700px on the same Article page — seems intermittent rather than 100% reliable, but confirms it's a real, recurring element (already logged in `Article-Page-To-Do.md`).

**Home Page**
- Default: masthead row + top ad directly below.
- Scrolled: bare masthead row, ad scrolled out of view.
- Ads on screen (default): `top_leaderboard` container 645 wide, creative 300x50 @ left:183; sticky `mobile-adhesion` (container 685x90, creative 320x50).
- Ads on screen (scrolled ~450px): sticky `mobile-adhesion` only.

**Section Front**
- Default: masthead row + top ad directly below.
- Scrolled: bare masthead row, same sticky behavior.
- Ads on screen (default): `top_leaderboard` container 645 wide, creative **320x100** @ left:173; sticky `mobile-adhesion`.
- Ads on screen (scrolled): sticky `mobile-adhesion` only.

**Article Page**
- Default: masthead row + top ad directly below.
- Scrolled: bare masthead row, same sticky behavior.
- Ads on screen (default): `top_leaderboard` container 645 wide, creative 300x50 @ left:183; sticky `mobile-adhesion`.
- Ads on screen (scrolled): sticky `mobile-adhesion` only.
- No popup encountered this pass (the trust/source tooltip from the 375px Article pass did not reappear).

---

### 1024px (Tier 3) — ✅ reviewed 2026-09-15

**🔴 Major structural mismatch found — bigger than the mobile ad-sizing issue.**

**Production (all three page types, confirmed live):** the masthead at 1024px is still the same collapsed mobile-style row seen at 375/700/768px — hamburger, centered logo, account icon, search icon, 65px tall. No weather/date, no visible nav links, no "Trending" strip. This is correct/expected per the real CSS: the header doesn't flip to the desktop nav layout until 1040px (Tier 4), and 1024 < 1040.

**Figma `Device=LG-TabletH` (1024), by contrast, is inconsistent across Page variants and doesn't match production on any of them:**
- **Home:** shows the *full desktop-style* masthead — hamburger **plus "All Sections" label**, weather/date block, centered logo, section nav links row (News/Fakeville Local/Sportsball/etc.), "Trending:" strip, **and** a `Top Leaderboard 728x90` ad. This is essentially the same treatment as the XL-Desktop variant, not what 1024px actually looks like live.
- **Section Front:** shows only the bare logo row (hamburger, logo, account, search) with **no ad** — no weather/nav/trending, unlike Home's variant.
- **Article:** same as Section Front — bare logo row, **no ad**.

So at this tier, Home, Section Front, and Article don't even agree with *each other* in Figma, and none of them matches what's actually live. This looks like the same kind of per-page-variant drift found at the mobile tier, but larger in scope (whole nav structure and weather module, not just an ad box).

**Correction:** on closer inspection, Section Front and Article *did* already have an ad at this tier (728x90) — just undersized for 1024's real 970x250. Only Home had the full-desktop-treatment structural problem.

**Fixed in Figma, 2026-09-15, per Karl ("fix the Figma components to match what you're finding in production"):**
- **Home** (`Default` and `Scrolled`): removed the full-desktop-style content (weather/date block, nav link row, Trending strip) and replaced it with the same collapsed masthead row structure already correctly used by Section Front/Article at this tier — hamburger, centered logo, account icon, search icon. Cloned directly from the (now-corrected) Section Front component to guarantee identical structure.
- **All three (`Default` state):** ad swapped from `Top Leaderboard 728x90` to `Top Leaderboard 970x250` (Desktop device variant), container/component heights resized to fit (346px total, up from 186/337).
- All six affected variants (Home/SectionFront/Article × Default/Scrolled) screenshot-verified clean afterward — all three Page variants are now structurally identical at this tier and match live production exactly: same collapsed row, same 970x250 ad, same sticky-scroll behavior.

**Home Page**
- Default: collapsed masthead row + `top_leaderboard` ad directly below, rendering full-size 970x250 at this width (bigger than the 320/728 sizes seen at narrower widths).
- Scrolled: bare masthead row, ad scrolled out of view (`headroom--not-top headroom--unpinned`).
- Ads on screen (default): `top_leaderboard` 970x250 @ (20,81); `cube1_rrail_atf` 300x1050 right-rail ad also on screen (enters view at this width since the 2-column body layout starts here); sticky `mobile-adhesion` (728x90 creative).
- Ads on screen (scrolled): right-rail `cube1_rrail_atf` remains on screen (tall unit); sticky `mobile-adhesion`.
- **Popup:** the trust/source tooltip reappeared again here (Article page, see below) — reappeared on Home? No — confirmed only on Article this pass, see Article notes.

**Section Front**
- Default: collapsed masthead row + `top_leaderboard` ad, also 970x250 at this width — matches Home's size (the per-page-type ad-size split seen at mobile/tablet tiers has converged to a single uniform size by 1024).
- Scrolled: bare masthead row, same sticky behavior.
- Ads on screen (default): `top_leaderboard` 970x250 @ (20,81); `cube1_rrail_atf` 300x600 right-rail (different height than Home's — 600 vs 1050, page-specific); sticky `mobile-adhesion`.
- Ads on screen (scrolled): right-rail ad still visible; sticky `mobile-adhesion`.

**Article Page**
- Default: collapsed masthead row + `top_leaderboard` ad, 970x250 (same size as Home/Section Front at this width).
- Scrolled: bare masthead row, same sticky behavior.
- Ads on screen (default): `top_leaderboard` 970x250 @ (20,81); sticky `mobile-adhesion`.
- **Popup, recurring:** the same trust/source tooltip appeared again here on default load (identical copy/behavior to the 375px and 768px sightings). Third confirmed sighting on Article page — appears frequently but not on literally every load (didn't show at 700px).

---

### 1100px (Tier 4 — no dedicated Figma variant) — ✅ reviewed 2026-09-15

**Confirmed: production switches to the full desktop masthead exactly where the CSS said it would.** At 1100px, all three page types show the complete desktop treatment — hamburger + "All Sections" label, weather/date, centered logo, Subscribe/Log in buttons + search, full section nav row, "Trending" strip — header height **226px**, matching the previously-documented 64/80/48/34=226 desktop masthead measurement. This is a real, structurally different masthead from what Tiers 1–3 show, confirming the 1040px breakpoint is correct and meaningful.

**Compared against the nearest Figma variant, `XL-Desktop` (built at 1280, no 1040–1279 variant exists):** structurally a strong match — same weather/date block, nav row, Trending strip, and the `Top Leaderboard 970x250` ad matches production exactly. Two differences worth noting, neither a surprise:
1. **Account state:** Figma shows a logged-in avatar; production (logged out) shows "Subscribe"/"Log in" pill buttons instead. Already a known, previously-documented distinction (see `navigation.md` §2.3) — not a new finding.
2. **⚠️ New — Scrolled-state mismatch:** Figma's `XL-Desktop` `Scrolled` variant shrinks all the way down to a bare row (hamburger only, no "All Sections" text, no Subscribe/Login). **Production's actual scrolled state at 1100px keeps "All Sections" next to the hamburger, and keeps the Subscribe/Log in buttons and search visible** — it only drops the weather/date, nav links, and Trending strip, shrinking from 226px to 65px rather than fully collapsing to the mobile-style bare row. Will confirm this holds at literal 1280px during that pass, then fix Figma's `XL-Desktop` `Scrolled` variants (all three page types) to match if confirmed.

**Open question for Karl (unchanged from the original gap flag):** should a dedicated `Device` variant be built for the 1040–1279px range, given production already treats it identically to what 1280px shows (same structure, same ad size)? If 1100 and 1280 behave identically in production, it's possible XL-Desktop's existing build could simply be treated as covering both, rather than needing a new tier — your call.

**Home Page**
- Default: full desktop masthead, 226px. Ads on screen: `sponsorship_1` ~320x50 (top-right, next to logo); `top_leaderboard` 970x250; `cube1_rrail_atf` 300x1050 right-rail (on screen at this width).
- Scrolled: shrinks to 65px, keeps "All Sections" + hamburger, logo, Subscribe/Log in, search. Ads on screen: right-rail `cube1_rrail_atf` remains visible (tall unit).

**Section Front**
- Default: full desktop masthead, 226px, includes "News" section title next to logo. Ads on screen: `sponsorship_1` ~320x50; `top_leaderboard` 970x250; `cube1_rrail_atf` 300x486 right-rail.
- Scrolled: same shrink-to-65px behavior as Home.

**Article Page**
- Default: full desktop masthead, 226px. Ads on screen: `sponsorship_1` ~320x50; `top_leaderboard` 970x250; `cube1_rrail_atf` 300x1050 right-rail.
- Scrolled: same shrink-to-65px behavior.
- **Popup, 4th sighting:** same trust/source tooltip on Article default load, consistent with every prior width tested on this page (375/768/1024/1100). Confirms it's genuinely tied to the Article page template, not a specific breakpoint.

---

### 1280px (Tier 5) — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=XL-Desktop`.*

**Structure match confirmed — closes the 1100px open question:** production at 1280px is structurally identical to 1100px on all three page types: same full desktop masthead (hamburger + "All Sections", weather/date, centered logo, Subscribe/Log in + search, full nav row, "Trending" strip), same 226px header height, same `Top Leaderboard 970x250` ad. No new structural behavior appears between 1100 and 1280 — confirms Tiers 4 and 5 are visually one and the same masthead treatment in production, just wider spacing.

**⚠️ New finding — Article's Scrolled state is structurally different from Home/Section Front:** confirmed by screenshot (not just class/height matching, which is what led to an unverified assumption at the 1100px pass):
- **Home & Section Front, Scrolled:** shrink from 226px → 65px, keep "All Sections" next to the hamburger, keep logo, Subscribe/Log in buttons, and search visible.
- **Article, Scrolled:** also shrinks to 65px, but shows a completely different content set — a breadcrumb ("Section Name | Roughly forty characters of the article t...") in place of "All Sections," plus a row of share icons (bookmark, Facebook, email, X, Reddit, gift/share, link) in place of Subscribe/Log in + search. This is unique to the Article template.

**Fixed in Figma, 2026-09-15, per Karl ("build our Figma component breakpoints to match what is in production... resize XL to a narrower width"):**
1. **Scrolled-state content fix:** Home-Scrolled and Section Front-Scrolled were both showing the wrong bare-hamburger-only content (same gap flagged at the 1100px pass). Fixed by cloning the correct "All Sections" + logo + Subscribe/Login + search row (from Section Front's own `Default` top row) into both Scrolled variants. Checked Article-Scrolled against production first — it already correctly showed the breadcrumb + share-icon pattern, so it needed no content fix.
2. **Width resize, 1280 → 1040px:** since production treats Tier 4 (1040–1279) and Tier 5 (≥1280) identically, rather than build a separate Tier 4 variant, resized `XL-Desktop`'s built width down to **1040px** — the real breakpoint — across all 9 Home/Section Front/Article variants (`Default`, `AdFree`, `Scrolled`). Verified first on two `Default` variants that nothing overflows or clips at the narrower width (checked both Home's and Section Front's longer nav-link rows), then applied the same resize to the remaining 7. All 9 screenshot-verified clean afterward:

   | Variant | Final size |
   |---|---|
   | Home Default | 1040×497 |
   | Section Front Default | 1040×497 |
   | Article Default | 1040×497 |
   | Home AdFree | 1040×215 |
   | Section Front AdFree | 1040×215 |
   | Article AdFree | 1040×215 |
   | Home Scrolled | 1040×64 (content fixed) |
   | Section Front Scrolled | 1040×64 (content fixed) |
   | Article Scrolled | 1040×64 (already correct) |

3. **On-canvas labels:** searched the Menus and Parts page for any text layer referencing the Masthead's breakpoint widths (proximity search around the component, text search for "1280"/"XL-Desktop"/etc., nearby section/frame names) — found none tied to Masthead. The only "1280"-adjacent text found on the page belongs to an unrelated component far outside the Masthead's canvas area (looks like Reader Dashboard labeling) and was left untouched. **Conclusion: there are no separate on-canvas labels to update for this component** — the component's own built width (now 1040px) and this audit doc are the only places the breakpoint number is recorded, and both are now updated. Karl separately pointed out the real container: a column-header label row (`Frame 12728`/`Frame 12729`, above and below the whole Masthead grid on the Menus and Parts page) that applies to every Page/State variant at once — that label was updated from "XL-Desktop - 1280x960" to "XL-Desktop - 1040x960" on both the top and bottom copies.

**Post-fix follow-up, 2026-09-15 — Top Nav and Trending overflow at the 1040px width:**

Once the component was rebuilt at 1040px, two rows within it turned out to have their own overflow problems, found and fixed in two rounds:

4. **First pass (superseded in part by #5 below):** the top nav links row still carried a stale fixed-width box (1202px) left over from the 1280px layout, extending 81px past each edge of the new 1040px container even though the visible text itself stayed centered and technically not clipped. Resized the row to fill its parent (1040px) on all three page types, which snapped it flush — no visible change to content, just removed the oversized invisible bounding box. Separately, the Trending strip's real content (4 headlines) no longer fit in 1040px and was overflowing the right edge by ~47–87px; first attempt tightened item spacing from 32px to 8px so all 4 items fit without truncating any text.

5. **Revised per Karl:** the Trending-strip spacing tighten was reverted back to the original 32px, and the strip's container was set to clip its content instead — the last headline now crops hard at the 1040px edge rather than the row being cramped. Separately, Karl asked to look again at how a real production site handles a top nav that doesn't fit, using Chicago Tribune (one of the project's standing 6-site review list) at 1040px width as the reference: its `.nav-primary` row (11 items) is 1100.8px wide inside a 973.75px wrapper, and because the page sets `overflow-x: hidden`, the row just centers and gets clipped on both edges — no wrap, no shrink, first/last items cut off mid-word. A quick cross-site check (same 6 sites) found Chicago Tribune and Orlando Sentinel both carry the most top-nav items (11) and trending items (6) of the six — see the table in the chat record of this pass; OC Register 8/5, Denver Post 9/3, The Morning Call 10/4, Greeley Tribune 7/2.

   Per Karl's direction ("we need to build it this way regardless"), rebuilt the Figma nav row to intentionally match this broken production treatment rather than hide it: brought Home, Section Front, and Article's top nav rows up to 11 items each (added placeholder items — Home/Article gained Business/Politics/Entertainment/Suburbs; Section Front, which already used a themed 10-item "Things To Do" style list, gained one more: Shopping), let the row size to its natural (now wider) content width instead of force-fitting it to the container, and set the row's parent to clip at the component's 1040px bounds. Result: the row is centered and overflows both edges, first/last items cut off mid-word — visually matching Chicago Tribune's live bug. Logged as entry #20 in `design-vs-production.md` (Engineering Handoff) for production to actually fix (smaller font/spacing at this tier, wrap, or an overflow menu — whatever the real fix, it needs to be platform-wide since at least two sites already hit 11 items).

**Home Page**
- Default: full desktop masthead, 226px — matches 1100px exactly. Ads on screen: `sponsorship_1` ~320x50 (top-right next to logo); `top_leaderboard` 970x250; `cube1_rrail_atf` 300x1050 right-rail.
- Scrolled: shrinks to 65px, keeps "All Sections" + hamburger, logo, Subscribe/Log in, search — now matches Figma after the content fix. Ads on screen: right-rail `cube1_rrail_atf` remains visible.

**Section Front**
- Default: full desktop masthead, 226px, "News" section title next to logo — matches 1100px. Ads on screen: `sponsorship_1` ~320x50; `top_leaderboard` 970x250; `cube1_rrail_atf` right-rail.
- Scrolled: same shrink-to-65px, "All Sections" pattern as Home — now matches Figma after the content fix.

**Article Page**
- Default: full desktop masthead, 226px. Ads on screen: `sponsorship_1` ~320x50; `top_leaderboard` 970x250; `cube1_rrail_atf` 300x1050 right-rail.
- Scrolled: breadcrumb ("Section Name | Roughly forty characters of the article t...") + share-icon row (bookmark/Facebook/email/X/Reddit/gift/link) in place of "All Sections"/Subscribe/Login — structurally distinct from Home/Section Front, and Figma's existing Article-Scrolled variant already matched this correctly, no fix needed.
- **Popup, 5th sighting:** same trust/source tooltip on Article default load. Consistent across every width tested (375/768/1024/1100/1280) — confirms it's tied to the Article page template itself, not any particular breakpoint.

---

### 1728px (sanity check — still Tier 5) — ✅ reviewed 2026-09-15
*Confirms nothing changes beyond 1280px; compared against the same `Device=XL-Desktop` variant. 1728px is Karl's full screen width on this machine (confirmed via `window.screen.width`), so this pass closes out the gap left when the session moved into the Ad-Free audit before this width was captured logged-out.*

**Confirmed: structurally identical to 1100px and 1280px.** Same full desktop masthead (hamburger + "All Sections", weather/date, centered logo, Subscribe/Log in + search, full nav row, "Trending" strip), same shrink-to-65px scrolled behavior on Home/Section Front (keeping "All Sections", logo, Subscribe/Log in, search), same Article-specific scrolled breadcrumb + share-icon treatment. No new structural behavior at this width — Tiers 4/5 remain one masthead treatment all the way from 1040px up through the widest screen tested.

**Home Page**
- Default: full desktop masthead. Ads on screen: `sponsorship_1` banner (Regal Rewards+) next to logo; `top_leaderboard` (Regal Rewards+, full-width); `cube1_rrail_atf` right-rail (tall unit).
- Scrolled: shrinks to 65px, keeps "All Sections" + hamburger, logo, Subscribe/Log in, search. Right-rail ad remains visible on scroll.

**Section Front**
- Default: full desktop masthead, "Sports" section title next to logo. Ads on screen: `sponsorship_1` (Implements/farm equipment ad); `top_leaderboard` (Southwest Airlines, loaded after a brief delay); `cube1_rrail_atf` right-rail (Ebglyss).
- Scrolled: same shrink-to-65px behavior as Home.

**Article Page**
- Default: full desktop masthead. Ads on screen: `sponsorship_1` (Great Smoky Mountains); `top_leaderboard` (Tremfya); `cube1_rrail_atf` right-rail (Clay Travis & Buck Sexton / IFCJ). **Popup, 9th sighting overall:** trust/sourcing tooltip reappeared again, consistent with every width tested on this page except 700px.
- Scrolled: breadcrumb + headline + share-icon row, same pattern as 1100/1280px. **Entry #21 cross-validated logged-out:** DOM inspection shows the identical measurement as the Ad-Free pass at this width — headline's right edge (x 1185px) sits 241px clear of the share widget's left edge (x 1426px), no overlap. Confirms entry #21 is genuinely independent of login state, as already concluded from the Ad-Free measurements.

**Figma comparison:** spot-checked `456:2573` (XL-Desktop Default Home) — structurally matches production exactly (Subscribe/Log In buttons, sponsorship + top-leaderboard ad placeholders sized correctly). No drift since the 1280→1040 rebuild earlier in this project; no further Figma changes needed at this width.

---

## Ad-Free Masthead Audit

**Started:** 2026-09-15, per Karl. Same scope and method as the main audit above (Home/Section Front/Article, Default + Scrolled, all established breakpoints), but logged into an ad-free OC Register account instead of logged out. Each breakpoint below is paired against the matching logged-out breakpoint section above (Karl confirmed reusing the earlier logged-out audit as the baseline rather than re-browsing logged out each time).

**User Status fix, done before the breakpoint passes below:** Karl pointed to the `User Status` source container (Figma node `456:5671`, WordPress Elements → Menus and Parts), which holds the shared `AccountMenu`/`UserStatus` component sets that feed the account icon into every Masthead variant. Checked every variant in the `Masthead` component set (all Device tiers × Default/AdFree/Scrolled × Home/Section Front/Article) and found all 39 were wired to `UserType=loggedIn`/`status=subscriber` — meaning Default and Scrolled states (which represent the logged-out baseline) were incorrectly showing the logged-in avatar. Fixed by swapping all 30 Default/Scrolled variants to their matching `loggedOut` `AccountMenu` variant per Device tier; left the 9 AdFree variants untouched since ad-free is itself a logged-in-subscriber state and was already wired correctly. Verified: XL-Desktop Default now shows "Subscribe"/"Log In" buttons instead of an avatar; SM-Mobile Default now shows the plain person-icon glyph instead of a photo avatar — both now match the original logged-out audit's findings.

### 375px — ✅ reviewed 2026-09-15

Ad-free masthead is a bare row (hamburger, logo, avatar, search) with no ad, on all three page types. Default and Scrolled render identically since there's nothing to lose on scroll. Figma's `AdFree` SM-Mobile variants (Home/Section Front/Article, all 360×64) already matched exactly, avatar included — no fixes needed. Popup (trust/source tooltip) reappeared on the Article page.

### 700px — ✅ reviewed 2026-09-15

Same pattern as 375px: bare row, no ad, all three page types, Default = Scrolled. Figma's `AdFree` MD-TabletV variants (768×64) already matched — no fixes needed. Popup reappeared on Article.

### 1024px — ✅ reviewed 2026-09-15

Same pattern again: bare row, no ad, Default = Scrolled, avatar correct. Figma's `AdFree` LG-TabletH variants (1024×64) already matched — no fixes needed. Popup reappeared on Article.

### 1100px — ✅ reviewed 2026-09-15

Same bare-row/no-ad pattern for Default state confirmed across all three page types. Scrolled state also checked directly (not just inferred) on Home, Section Front, and Article:

- **Home** — Default: bare row, no leaderboard ad, avatar confirms logged-in status. Scrolled: compact sticky masthead, same pattern as prior breakpoints. (Note: a right-rail house promo for the print replica/e-Edition appeared on this load — not a third-party ad slot and not part of the Masthead component itself, so out of scope for this audit, but noted for completeness.)
- **Section Front (Sports)** — Default: bare row, no ad, avatar visible. Scrolled: compact sticky masthead, consistent.
- **Article** — Default: bare row, no ad, avatar visible. Scrolled: see finding below. **Popup, 5th sighting:** the trust/sourcing tooltip reappeared again on Article default load, same as every prior width tested (375/700/1024/1100).

**⚠️ New finding — Article Scrolled masthead: title text overflows behind the sharing widget.** At 1100px, the scrolled Article masthead shows a breadcrumb + headline ("National Politics | Judge blocks Kennedy Center board from putting…") followed by a bookmark icon and the share-icon row (Facebook/X/Reddit/Print/Gift). The headline text box (`.article-title`) renders at its full natural width based on the actual headline length, but the bookmark icon (`.saveArticleButton`) sits at a fixed position in the row that doesn't account for how long the headline actually is — so for a headline this long, the last few characters render directly underneath the bookmark icon, visually cut off/obscured rather than cleanly truncated. Confirmed via DOM inspection: the headline's own box (x 462–847px) overlaps the bookmark icon's position (x 778–809px) by about 69px. This isn't ad-free-specific — it would happen for any long headline regardless of login state — but it was caught during this pass. Logged as a new entry (#15) in `design-vs-production.md` for engineering to fix (the headline needs a max-width/truncation tied to the actual space available before the bookmark/share icons, not a fixed generous budget). Not replicated in Figma — Figma's Article Scrolled variant uses a fixed placeholder headline length that doesn't hit this edge case, and unlike the Top Nav overflow (a systemic, always-reproducible layout bug), this one is data-dependent on headline length, so it's flagged for engineering rather than rebuilt into the static mock.

**Figma `AdFree` variants re-verified post User Status fix:** `822:3434` (SectionFront) and `824:4625` (Article) both still correctly show the logged-in avatar treatment, confirming they were untouched by the earlier Default/Scrolled loggedOut fix (as expected — AdFree was already correct going in).

---

### 1040px (XL-Desktop tier) — ✅ reviewed 2026-09-15

Same bare-row/no-ad pattern for Default state confirmed across all three page types, now at the exact width Figma's `XL-Desktop` variants are built to:

- **Home** — Default: bare row, no ad, avatar visible. Scrolled: compact sticky masthead, consistent.
- **Section Front (Sports)** — Default: bare row, no ad, avatar visible, full nav row fits (Sports has fewer items than News, doesn't hit the Tier-4 overflow). Scrolled: compact sticky masthead, consistent.
- **Article** — Default: bare row, no ad, avatar visible. **Popup, 7th sighting overall:** trust/sourcing tooltip reappeared again on default load. Scrolled: overflow bug (entry #21) reconfirmed and worse at this width — see below.

**Entry #21 reconfirmed at this width, with a larger overlap.** DOM inspection: headline box x 430–815px, bookmark icon x 720–751px — a 95px overlap (vs. 69px at 1100px), with the bookmark icon now sitting directly on top of a headline word rather than just clipping the tail. Since this is exactly the width Figma's XL-Desktop tier now targets, this is a closer, more directly relevant match to what the component's live-content equivalent would show — but per the reasoning above, it remains a data-dependent (headline-length) issue rather than a systemic one, so it's still not being force-built into the static Figma mock. Updated `design-vs-production.md` entry #21 with this additional measurement.

**Figma `AdFree` variants:** `819:1845` (Home), `822:3434` (SectionFront), `824:4625` (Article) — all previously confirmed correct at the 1040px rebuild; no changes needed this pass.

---

### 1728px (sanity check, Karl's max screen width) — ✅ reviewed 2026-09-15

Confirmed via `window.screen.width` that 1728px is the full display width on Karl's machine — this doubles as the project's widest sanity-check tier. Same bare-row/no-ad pattern for Default state confirmed across all three page types:

- **Home** — Default: bare row, no ad, avatar visible. Scrolled: compact sticky masthead, consistent.
- **Section Front (Sports)** — Default: bare row, no ad, avatar visible. Scrolled: compact sticky masthead, consistent.
- **Article** — Default: bare row, no ad, avatar visible. **Popup, 8th sighting overall:** trust/sourcing tooltip reappeared again on default load.

**Entry #21 resolves cleanly at this width — closes out the investigation.** At 1728px the scrolled Article masthead shows the headline cleanly truncated with a proper ellipsis, no overlap with the bookmark/share icons. DOM inspection confirms: the headline's container (`.entry-title`) sizes down correctly, its rendered text box (`.article-title`, right edge x 1185px) sits 241px clear of the share widget's left edge (x 1426px) — a comfortable margin, not a near-miss. This completes the picture across all three widths tested:

| Width | Overlap |
|---|---|
| 1040px | 95px (worst) |
| 1100px | 69px |
| 1728px | none — 241px clearance |

This confirms entry #21 is purely a narrow-viewport problem (not fixed-headline-length-dependent as the initial 1100px write-up guessed) — the underlying CSS issue is that the headline's flex/width allocation doesn't shrink correctly relative to the fixed-width share widget below some threshold between 1100px and 1728px. Updated `design-vs-production.md` entry #21 with this full width-comparison table so engineering has the complete picture rather than a single data point.

---

## Project-wide fix: new `AccountMenu` `Device=LG-TabletH` variant (2026-09-15)

**Found while auditing Obituaries at 1024px, but affects Home/SectionFront/Article too.**

Root cause, traced via `figma_execute`: the account-icon-vs-buttons rendering doesn't come from `AccountMenu`'s own `Device` property (which only has `SM-Mobile`/`MD-TabletV`/`XL-Desktop`) — it comes from a **nested** sub-component, `UserStatus` (node `456:5728`, its own component set with a *separate* `Device` axis of just `Desktop`/`mobile`). Every masthead variant built at the `LG-TabletH` (1024px) tier was using `AccountMenu`'s `XL-Desktop` variant as a stand-in (no dedicated `LG-TabletH` option existed), and `XL-Desktop`'s `UserStatus` is wired to `Device=Desktop` — the full "Subscribe"/"Log In" pill-button treatment. That's a real structural mismatch: production stays in the collapsed mobile-style row (plain person icon + chevron, no buttons) all the way through 1024px, only switching to the desktop treatment at 1040px. This exact issue was flagged and believed fixed for Home/SectionFront/Article during the original 1024px pass (cloning Section Front's collapsed-row structure) — but the later project-wide "logged-in avatar" bug fix (all 30 Default/Scrolled variants) re-wired `AccountMenu` back to `Device=XL-Desktop` at this tier, silently reintroducing the button-treatment mismatch. It was caught this time because the Obituaries fix surfaced it directly.

**Fix (per Karl):** rather than reuse `MD-TabletV`'s variant as a stand-in, added a proper new `AccountMenu` variant — `Status=loggedOut, View=Closed, Device=LG-TabletH, UserType=loggedOut` (node `3407:50999`) — cloned from `MD-TabletV`'s (visually correct) icon treatment and screenshot-verified. Re-wired all 8 affected `Default`/`Scrolled` `AccountMenu` instances at the `LG-TabletH` tier to this new variant: **Home, Section Front, Article, and Obituaries**, both states. `Dashboard`'s `LG-TabletH` variants were left untouched (still `loggedIn`) — that phase hasn't started yet, out of scope here.

**Design-system hygiene issue — found and fixed, 2026-09-15 (per Karl):** `AccountMenu`'s `MD-TabletV` and `SM-Mobile` variants (plus the new `LG-TabletH` clone, which inherited it) each wrapped their real, live `UserStatus` instance inside an extra, empty `FRAME` also named "UserStatus" — leftover cruft from an earlier detach, not a broken link itself (the nested instance underneath was always live and correctly resolving to `Device=mobile, status=none`), but redundant structure that didn't match `XL-Desktop`'s clean single-instance pattern. **Fixed** by removing the empty wrapper frame in all three variants (`MD-TabletV`, `SM-Mobile`, `LG-TabletH`) and reparenting the live instance directly into the row frame, matching `XL-Desktop`'s structure exactly. Screenshot-verified pixel-identical before/after in all three cases — purely a structural cleanup, no visual change.

## Obituaries masthead audit

*Continuation of the project — the HANDOFF note it pointed to was retired; current status is in `MNG-Web-Design-System-Status.md`. **Logged-out pass complete** (all 7 widths: 375/700/1024/1100/1040/1280/1728, default + scrolled). **Ad-Free (logged-in) pass complete** (same 7 widths — see `## Obituaries Ad-Free Masthead Audit` below). Reader Dashboard not started.*

### Breakpoint investigation: does Obituaries differ from Home/SectionFront/Article? — ✅ resolved 2026-09-15

**Karl's question:** *"Can we see if Obituaries has different breakpoints than the pages we already reviewed?"*

**Answer: Yes — two genuinely new, Obituaries-specific breakpoints exist, both inside the Endless Tributes search widget embedded in the masthead nav. Everything else initially flagged as a stray value turned out to belong to unrelated page content, not the masthead.**

Resolved via a full `document.styleSheets` → `CSSMediaRule` scan on ocregister.com/obituaries/ (375px, logged out), tracing every remaining media-query value back to its actual selector:

| Value | Belongs to | New masthead breakpoint? |
|---|---|---|
| **624px** (`.obits-search-bar`, flat px, not em) | `.obits-search-form` switches `flex-direction: row → column` (real structural stack, not just cosmetic margin); Endless Tributes logo shrinks to `max-width: 35%`. Confirmed via the actual CSS declarations (`flex-direction: column` is unambiguous — not dead/unused CSS). | **Yes.** Does not match the site-wide 639px Tier 1 boundary (15px off) — this is a real, independent boundary specific to the obituaries search widget. |
| **800px** (`50em`) | `#content .obit-search-content.filter-open` / `.obit-search-content-et.filter-open` — `padding-left` changes when the filter panel is expanded. | **Yes**, but only for the filter-open expanded state — a secondary boundary between Tier 1 (639) and Tier 3 (1039), not present on Home/SectionFront/Article. |
| 800px (`50em`), also | `.category aside`, `.feature-section`, `.feature-large` — general homepage/article template CSS, unrelated to the masthead. | No — out of scope, same value coincidentally reused elsewhere on the page. |
| 1000px (`62.5rem`) | `.dfp-ad.dfp-top_leaderboard`, `.obit-leaderboard.bottom` — ad placement/sizing only. | No — ad content, not masthead nav. (Per this project's own standing note, live ad measurements aren't a reliable breakpoint signal anyway.) |
| 1300px (`81.25em`/`81.25rem`) | `.obit-article-search-result` — obituary search-results listing layout. | No — page content, not masthead. |
| 320px (`20em`) | Lower bound of the existing filter-popup date range (320–639px, inside Tier 1) and of `.obits-content-header .nav-primary-middle` (accuweather/hidden-logo/sponsorship), which spans 320–1039px as one combined range. | No — just the existing Tier 1 lower bound and the existing 1039px upper bound; confirms known tiers, not a new one. |
| ~734–735px (`45.875rem`/`45.9375rem`) | `.gallery-container`, `.gallery-title`, `.gallery-content`, `.gallery-element` — unrelated photo-gallery widget. | No — not obituaries- or masthead-specific at all. |

Also confirmed: `.nav-wrapper-primary .nav-primary-middle` (the search-widget area) collapses via `display: none` at the standard `64.9375em` (1039px) boundary, same as every other page type — consistent with existing findings.

**✅ Confirmed 2026-09-15 (live visual + DOM check):** Karl resized to 626px — `.obits-search-form` computed `flex-direction: row` (side-by-side), matching the above-624px expectation. Karl then resized to 618px — `.obits-search-form` computed `flex-direction: column`, and the screenshot confirms the search input and filter-icon button stack vertically. The 624px breakpoint behaves exactly as the CSS predicted; no discrepancy with Figma.

**Figma implication:** the `Masthead` component's `Page=Obituaries` variants don't currently model either the 624px or 800px (filter-open) states — worth a call on whether these are in scope for this component or belong to a separate Endless Tributes widget spec.

### 700px (Tier 2) — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=MD-TabletV` (768), `Page=Obituaries`.*

**Structure match — default:** nav row (hamburger / centered wordmark / account icon+chevron) → "Obituaries" title + sponsorship ad → search bar (`.obits-search-form`) → "Powered by Endless Tributes" → "Submit an Obituary" button. Matches Figma's `Device=MD-TabletV, State=Default, Page=Obituaries` (`456:3726`) structure exactly.

**Structure match — scrolled:** confirmed via DOM measurement (not just visual) that the "Obituaries" title and sponsorship ad collapse to `0×0` on scroll (`headroom--not-top headroom--unpinned`, though — consistent with the project's earlier "unpinned is vestigial" finding — the header container itself stays pinned/visible). What remains sticky at top: nav row → search bar → submit button. This **exactly matches** Figma's `Device=MD-TabletV, State=Scrolled, Page=Obituaries` (`456:3915`), which already shows the same collapsed structure — good fidelity, no fix needed here.

**⚠️ Bug found and fixed, 2026-09-15 (per Karl) — Obituaries `AccountMenu` instances were wired to the wrong variant entirely:** both `456:3726` (Default) and `456:3915` (Scrolled) had their `AccountMenu` instance (nodes `456:3750` / `456:3938`) pointed at `Status=loggedIn, View=Closed, Device=XL-Desktop, UserType=loggedIn` — wrong on three separate axes (login state, device tier, *and* user type), not just showing the avatar-vs-icon symptom noticed visually. This is the same class of bug already fixed project-wide for Home/SectionFront/Article's Default/Scrolled variants. **Fixed** by setting both instances' properties to `Status=loggedOut, View=Closed, Device=MD-TabletV, UserType=loggedOut`, matching the corrected Home/SectionFront/Article pattern exactly. Screenshot-verified: both variants now show the plain person-silhouette icon + chevron, matching production.

**Ad placeholder — correction to the previous write-up, no fix needed:** on closer inspection the label reads **"Sponsorship 1, 300x50 ADVERTISEMENT"** — "Sponsorship 1" is the ad slot's own name (matching production's `div-gpt-ad-sponsorship_1`), not "1300x50" as originally misread from the screenshot's tight kerning. The instance is already `Ad Blocks` component `Device=All, Name=Sponsorship 1 300x50` (`526:8809`) — confirmed correct against production's own GPT slot definition, which declares exactly two valid sizes for this slot: **300x50** and **320x50** (verified via `googletag.pubads().getSlots()` — not just an observed rendered size, which fluctuates). So this placeholder was already accurate; retracting the earlier flag.

**No popup encountered** at 700px, default or scrolled.

---

### 1024px (Tier 3) — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=LG-TabletH` (1024), `Page=Obituaries`.*

**Structure match — default and scrolled:** same pattern as 700px — nav row → "Obituaries" title + sponsorship ad → search bar → "Powered by Endless Tributes" → "Submit an Obituary" (default), collapsing to nav row + search bar + submit on scroll. Matches Figma's `456:3653` (Default) and `456:3977` (Scrolled) exactly.

**Account icon:** correctly shows the plain person icon + chevron on both states — this is the variant that surfaced the project-wide `AccountMenu` `Device=LG-TabletH` gap and the `UserStatus` wrapper-frame cleanup (see above). Now fixed and verified.

**Ad — exact match:** `div-gpt-ad-sponsorship_1` rendered its iframe at **300×50**, an exact match for both the GPT-declared size and the Figma `Sponsorship 1 300x50` placeholder. No fix needed — confirms the earlier "1300x50 misread" correction was right.

**No popup encountered** at 1024px, default or scrolled.

### 1100px (Tier 4) — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=XL-Desktop` (1280, nearest built variant — same convention as Home/SectionFront/Article), `Page=Obituaries`.*

**Structure match — default:** production switches to the full desktop masthead here, same as Home/SectionFront/Article at this tier — hamburger + "All Sections," centered logo, "Subscribe"/"Log In" buttons, search icon, then "Obituaries" title + sponsorship ad + search bar + "Powered by Endless Tributes" + "Submit an Obituary." Matches Figma's `456:3394` structure exactly.

**Structure match — scrolled:** shrinks to nav row (keeps "All Sections," Subscribe/Log In, search) + search bar + submit button, same shrink-not-collapse pattern already documented for Home/SectionFront/Article at this tier. Matches Figma's `456:3468` exactly.

**Ad — exact match:** Figma's placeholder here is `Sponsorship 1, 320x50` (the wider sibling of the `300x50` used at narrower tiers) — production's `div-gpt-ad-sponsorship_1` iframe measured exactly **320×50**. Another confirmed match, no fix needed.

**No popup encountered** at 1100px, default or scrolled.

### 1040px (XL-Desktop tier, literal built width) — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=XL-Desktop` (`456:3394` Default, `456:3468` Scrolled), `Page=Obituaries` — this is the variant's actual built width, not just the nearest one.*

**⚠️ Correction, 2026-09-15:** this claim was wrong when originally written — at the time of this pass, `Device=XL-Desktop, Page=Obituaries` was actually still built at **1280px**, not 1040px; the note above incorrectly assumed the same project-wide XL-Desktop resize applied to Home/SectionFront/Article had also been applied to Obituaries, without directly verifying the Obituaries component's own `width` property. It hadn't been. See the breakpoint-width audit below (after the `456:3977` overflow note) for the actual finding and fix. The structural/content observations above remain accurate — only the built-width claim was wrong.

**Structure match — default and scrolled:** identical pattern to 1100px — full desktop masthead (All Sections, Subscribe/Log In, search) → title + ad → search bar → submit (default); shrinks to nav row + search bar + submit on scroll, no full collapse. Matches Figma exactly at both states.

**Ad — exact match:** `div-gpt-ad-sponsorship_1` iframe measured **320×50** again, consistent with 1100px and matching Figma's `Sponsorship 1, 320x50` placeholder.

**No popup encountered** at 1040px, default or scrolled.

### 1280px (Tier 5) — ✅ reviewed 2026-09-15

Identical pattern to 1040px/1100px — structure, ad size (**320×50**, exact Figma match), and scrolled behavior all consistent, no new behavior at this width. Confirms 1040–1280 behave as one tier for Obituaries, same as already established for Home/SectionFront/Article. No popup encountered.

### 1728px (sanity check — still Tier 5) — ✅ reviewed 2026-09-15

**Structure match — default and scrolled:** identical to 1040/1100/1280px — no new behavior at the widest width tested, consistent with the same finding already established for Home/SectionFront/Article.

**Ad oddity, flagged but out of scope:** `div-gpt-ad-sponsorship_1` rendered a **300×250** creative at 1728px (vs. the 320×50 banner seen at 1040–1280px) — a size outside the two the slot declared via `googletag` earlier in this project (300x50/320x50). Visually, no ad box was visible in the title row at all (the space was blank) despite the element reporting `display: block; visibility: visible` at that size/position. Per this project's own standing note, live ad measurements/creative fluctuate and aren't a reliable signal for Figma sizing on their own — not treating this as a masthead-fidelity issue, just flagging the oddity in case it recurs.

**✅ Re-checked and closed out, 2026-09-15:** re-loaded ocregister.com/obituaries/ fresh at 1728px. The `.sponsorship-ad-wrapper` element is present in the DOM at the same position/width as before, but rendered with `height: 0` and empty innerHTML — no creative of any size loaded into it this time, and `googletag.pubads().getSlots()` returned 0 slots (GPT hadn't defined/rendered anything into that wrapper on this load). Note: this re-check ran in a still-logged-in session (`pafdainew@mailinator.com`), not a fresh logged-out one, so it isn't a perfect repeat of the original logged-out observation — but the underlying behavior (an ad wrapper that renders inconsistently: sometimes a 320x50 banner, sometimes an oversized 300x250 creative, sometimes nothing at all) is the same pattern already seen across both the logged-out and Ad-Free passes at this width. Formally closing this out as **ad-inventory noise, not a masthead/Figma-fidelity issue** — no engineering or Figma action needed. `design-vs-production.md` is not updated for this; it was never treated as an engineering-actionable mismatch.

**This completes the full logged-out pass for Obituaries: 375/700/1024/1100/1040/1280/1728px, default + scrolled, all reviewed.**

### Figma node `456:3977` overflow flag — ✅ resolved, false positive 2026-09-15

An earlier broad diagnostic scan flagged `Device=LG-TabletH, State=Scrolled, Page=Obituaries` (node `456:3977`) for several named elements ("Proposed," "Group 76," "Frame 11974," "Search Field," "About") extending far outside the component's own bounds, and this one specifically looked different from the scan's other (confirmed false-positive) hits.

Direct inspection via `figma_execute` resolves it as **the same kind of false positive as the others**: the component has two direct children — `Masthead Container` (the real render) and `Obits Nav - What it is.` (a documentation/reference frame that fits flush within the component's own bounds). Inside that reference frame sits a `Proposed` frame with `visible: false`, and *that* hidden frame is the direct parent of `Group 76` → `Frame 11974` → `Search Field`/`About` — the exact chain the earlier scan flagged. Because Figma never renders a subtree under a hidden ancestor, none of those nested layers actually show up in the component's output, regardless of their own individual `visible: true` flags. No fix needed; this is an inert "before/after" comparison frame, not a live overflow bug.

### Obituaries Figma breakpoint-width audit — ✅ corrected 2026-09-15

*Per Karl's follow-up request to confirm or correct the built widths of every `Page=Obituaries` `Device` variant against the project's established real breakpoint tiers, rather than assume the earlier Home/SectionFront/Article fix carried over.*

Checked every `Page=Obituaries` component's own `width` property directly in Figma (not assumed from naming) against the canonical table in "Figma `Masthead` component coverage vs. real tiers" above:

| Figma `Device` | Expected built width | Obituaries actual (before this pass) | Match? |
|---|---|---|---|
| XS-Fold | 340px | 340px (`Default` 456:3592, `AdFree` 827:5968, `Scrolled` 456:3857) | ✅ Yes |
| SM-Mobile | 360px | 360px (`Default` 456:3531, `AdFree` 827:5440, `Scrolled` 456:3799) | ✅ Yes |
| MD-TabletV | 768px | 768px (`Default` 456:3726, `AdFree` 827:5573, `Scrolled` 456:3915) | ✅ Yes |
| LG-TabletH | 1024px | 1024px (`Default` 456:3653, `AdFree` 827:5676, `Scrolled` 456:3977) | ✅ Yes |
| XL-Desktop | 1040px | **1280px** (`Default` 456:3394, `AdFree` 827:6067, `Scrolled` 456:3468) | ❌ **No — mismatch found** |

**Finding:** Obituaries' `XL-Desktop` variants were never actually resized to 1040px during the earlier project-wide fix (that fix's own write-up, above, only lists 9 Home/SectionFront/Article variants — Obituaries wasn't in scope at the time, since it hadn't been audited yet). The two "literal built width" notes elsewhere in this Obituaries section (in the logged-out and Ad-Free 1040px write-ups) incorrectly assumed otherwise without checking — corrected in place above.

**Fixed:** resized all `Page=Obituaries, Device=XL-Desktop` variants from 1280px → **1040px** — `Default` (456:3394), `AdFree` (827:6067), `Scrolled` (456:3468), and the new `AdFree-Scrolled` (3415:52128, built earlier in this same pass). All four use vertical auto-layout with `FILL`-sized children, so the resize was a clean reflow with no manual repositioning needed. Screenshot-verified all four afterward: no clipping or overflow anywhere (Obituaries' XL-Desktop layout has no long nav-link row or Trending strip like Home/SectionFront/Article did, so this resize carried none of that fix's follow-on overflow work). Heights unchanged (261px Default/AdFree, 145px Scrolled/AdFree-Scrolled).

**Also noted, not fixed (out of scope for this pass):** `Page=Dashboard, Device=XL-Desktop` (`Default` 456:2996/456:3175 lineage, `Scrolled` 456:3047 lineage) is **also** still built at 1280px, not 1040px — the same gap, just on the Reader Dashboard masthead rather than Obituaries. Karl's request this round was scoped to Obituaries; flagging Dashboard here so it isn't lost, in case it's worth a follow-up pass.

## Obituaries Ad-Free Masthead Audit (logged-in pass)

*Live session confirmed logged in as a subscriber throughout (avatar visible top-right, 0 GPT ad slots on page, no "Subscribe"/"Log In" text) — same Chrome session carried over from the Home/SectionFront/Article Ad-Free pass, no re-login needed.*

**Figma coverage note, flagged up front:** the `Masthead` component set's `State` property is a single-select (`Default` / `AdFree` / `Scrolled` — mutually exclusive, confirmed via `componentPropertyDefinitions`), so there is no "AdFree + Scrolled" combination variant for any page. For Home/SectionFront/Article this was harmless because their AdFree masthead is already just the bare collapsed row at every width tested, so Default and Scrolled render identically and the single `AdFree` variant matched both live states. **Obituaries is different:** its "Obituaries" title heading is part of the Default content and demonstrably collapses away on scroll (confirmed on live production below), so the single Figma `State=AdFree` variant can only match production's logged-in **default** state, not its logged-in **scrolled** state, at any width where the title is present. This is a genuine Figma coverage gap, not a production bug — worth a call from Karl on whether a dedicated `AdFree`+`Scrolled` combination (for Obituaries, and potentially Dashboard) is in scope.

### 375px — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=SM-Mobile, State=AdFree, Page=Obituaries` (`827:5440`).*

**Structure match — default:** hamburger / centered logo / avatar+chevron row → "Obituaries" title → search bar (`.obits-search-form`) → "Powered by Endless Tributes" → "Submit an Obituary" button. Matches Figma `827:5440` exactly, including no ad row. `AccountMenu` instance (`827:5462`) correctly wired `Status=loggedIn, View=Closed, Device=SM-Mobile, UserType=loggedIn` — no fix needed here (this device tier wasn't part of the earlier AccountMenu bug sweep, and it's already correct).

**Scrolled — matches live behavior, but no Figma variant exists to compare against (see coverage note above):** live scroll collapses the "Obituaries" title away; nav row → search bar → "Powered by Endless Tributes" → submit button stay sticky. Structurally consistent with the logged-out Scrolled pattern already documented at other widths — just no AdFree-specific Figma build to confirm pixel-for-pixel.

**Ad slots:** 0, confirmed via `googletag.pubads().getSlots()` — correctly ad-free.

**No popup encountered** at 375px (the Osano cookie-consent banner was present in the DOM but already dismissed/hidden — not a new popup).

### 700px (Tier 2) — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=MD-TabletV, State=AdFree, Page=Obituaries` (`827:5573`).*

**Structure match — default:** identical pattern to 375px — nav row → "Obituaries" title → search bar → "Powered by Endless Tributes" → "Submit an Obituary." Matches Figma `827:5573` exactly.

**⚠️ Bug found and fixed, 2026-09-15 — AccountMenu wired to wrong device tier:** the `AccountMenu` instance inside `827:5573` (`827:5597`) was wired to `Status=loggedIn, View=Closed, Device=XL-Desktop, UserType=loggedIn` — correct login state (this is genuinely a logged-in AdFree context) but wrong device tier. A proper `Status=loggedIn, View=Closed, Device=MD-TabletV, UserType=loggedIn` variant already exists (`910:16514`), so this was a simple remap, not a new-variant build. **Fixed** by setting the instance's `Device` property to `MD-TabletV`. Screenshot-verified byte-identical before/after (same export byte length) — confirms this was a pure correctness fix with zero visual regression, consistent with the earlier project-wide AccountMenu device-mapping issue (same root cause, different branch of the Status/UserType axis).

**Scrolled — matches live behavior, no Figma variant to compare against** (see AdFree/Scrolled coverage note above): title collapses, nav row + search bar + submit stay sticky, consistent with the logged-out Scrolled pattern at this width.

**Ad slots:** 0, confirmed via `googletag.pubads().getSlots()`.

**No popup encountered** at 700px.

### 1024px (Tier 3) — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=LG-TabletH, State=AdFree, Page=Obituaries` (`827:5676`).*

**Structure match — default and scrolled:** same pattern as 375/700px — nav row → "Obituaries" title → search bar → "Powered by Endless Tributes" → "Submit an Obituary," collapsing to nav row + search bar + submit on scroll. Matches Figma exactly.

**⚠️ Gap found and fixed, 2026-09-15 — no `AccountMenu` variant existed for `Device=LG-TabletH` on the loggedIn branch:** the `AccountMenu` instance inside `827:5676` (`827:5700`) was wired to `Status=loggedIn, View=Closed, Device=XL-Desktop, UserType=loggedIn` — same root cause as the 700px MD-TabletV finding above, but this time there was no existing `LG-TabletH` variant on the loggedIn branch to remap to (the `AccountMenu` component set only had `SM-Mobile`, `MD-TabletV`, and `XL-Desktop` built for `Status=loggedIn, View=Closed`). **Fixed** by cloning the `MD-TabletV` loggedIn variant and renaming it to `Status=loggedIn, View=Closed, Device=LG-TabletH, UserType=loggedIn` (new node `3414:51875`), the same method used earlier in this project for the `loggedOut` branch's `LG-TabletH` gap. Then rewired `827:5700` to the new variant. One cleanup note: an intermediate script error during creation left an orphaned duplicate-named clone in the component set, which briefly broke `variantProperties` resolution (`"Component set for node has existing errors"`); found and removed it immediately, then re-verified the set was clean (0 duplicate names) before finishing. **Screenshot-verified byte-identical before/after** — confirms the loggedIn `AccountMenu` doesn't actually vary visually by device tier (avatar + chevron + search icon look the same across `SM-Mobile`/`MD-TabletV`/`XL-Desktop`, and now `LG-TabletH`), so this was purely a correctness/consistency fix, not a visible bug.

**Ad slots:** 0, confirmed via `googletag.pubads().getSlots()`.

**No popup encountered** at 1024px.

### 1100px (Tier 4) — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=XL-Desktop, State=AdFree, Page=Obituaries` (`827:6067`, nearest built variant — same convention as the logged-out pass).*

**Structure match — default:** full desktop masthead — "All Sections" + logo + avatar/chevron + search icon → "Obituaries" title → search bar → "Powered by Endless Tributes" → "Submit an Obituary." Matches Figma `827:6067` exactly. `AccountMenu` instance (`827:6092`) is correctly wired `Status=loggedIn, View=Closed, Device=XL-Desktop, UserType=loggedIn` — no fix needed here, since the parent component itself is genuinely the `XL-Desktop` tier (unlike the 700px/1024px findings above, where a narrower parent's internal `AccountMenu` was incorrectly defaulting to `XL-Desktop`).

**Structure match — scrolled:** shrinks to nav row (All Sections, logo, avatar) + search bar + submit button, title collapses — same shrink-not-collapse pattern as the logged-out pass at this tier.

**Ad slots:** 0, confirmed via `googletag.pubads().getSlots()`.

**No popup encountered** at 1100px.

### 1040px (XL-Desktop tier, literal built width) — ✅ reviewed 2026-09-15

Identical pattern to 1100px — structure, `AccountMenu` wiring (already correct at this tier), and scrolled behavior all consistent. `Device=XL-Desktop, State=AdFree, Page=Obituaries` (`827:6067`) is this variant's actual built width, not just the nearest one. 0 ad slots, no popup. **Correction, 2026-09-15:** same correction as noted in the logged-out pass above — this variant was actually still built at 1280px at the time of this pass, not 1040px. Corrected in the breakpoint-width audit (see the Obituaries logged-out section).

### 1280px (Tier 5) — ✅ reviewed 2026-09-15

Identical pattern to 1040px/1100px — structure, `AccountMenu` wiring, and scrolled behavior all consistent, no new behavior at this width. Confirms 1040–1280 behave as one tier for the Obituaries AdFree masthead too, matching the logged-out pass's own finding. 0 ad slots, no popup.

### 1728px (sanity check — still Tier 5) — ✅ reviewed 2026-09-15

Identical to 1040/1100/1280px — no new behavior at the widest width tested, consistent with the same finding already established for the logged-out pass. 0 ad slots, no popup. **The 1728px ad-serving oddity flagged in the logged-out pass (300x250 creative instead of the expected 320x50 banner) did not reproduce here** — consistent with it being ad-inventory noise rather than a masthead-fidelity issue, since there's no ad slot at all in the AdFree state to exhibit it.

**This completes the full Ad-Free (logged-in) pass for Obituaries: 375/700/1024/1100/1040/1280/1728px, default + scrolled, all reviewed.**

## Reader Dashboard masthead audit

*Final phase of this project — the HANDOFF note it pointed to was retired; current status is in `MNG-Web-Design-System-Status.md`. Tested on **canoncitydailyrecord.com/dashboard/** (per Karl's direction) rather than ocregister.com, using a logged-in test subscriber account (`pafdainew@mailinator.com`) — the Reader Dashboard is a logged-in-only page, so there is no separate logged-out pass for this page type, matching Figma's own `Page=Dashboard` variant set (`Default`/`Scrolled` only, no `AdFree` state).*

**Figma coverage note:** unlike Obituaries, the `Page=Dashboard` branch of the `Masthead` component set is fully built out — all 5 device tiers × both `Default` and `Scrolled` states (10 variants total, confirmed via the component set's children). No variant-coverage gaps going into this pass.

### Breakpoint investigation: does the Dashboard body use different breakpoints than the masthead? — ✅ confirmed, per the handoff's own flag

**The handoff document flagged this exact question up front:** *"the Dashboard is documented elsewhere (`Reader-Dashboard-Library-Impact-Map.md`) as its own web app with a different breakpoint convention (1024px 'menu always visible' vs. the 1039px marketing-site rule)."*

Confirmed via literal CSS on the live page: the Dashboard's own React-rendered content root, `#reader-dashboard-island-root`, has its own `screen and (width >= 1024px)` and `screen and (width >= 1280px)` media rules (currently just padding adjustments — `padding-top`/`padding-bottom` — not yet observed to change the sidebar/content structure itself, though this needs the visual passes below to confirm fully). This is a **genuinely different breakpoint system from the masthead**, which still uses the standard `64.9375em` (1039px) boundary for its own nav collapse (`.pushnav`, `.nav-wrapper-primary` — confirmed unchanged from the marketing-site convention).

**Practical implication to watch for during this pass:** between 1024px and 1038px, the masthead above the Dashboard content will still render in its collapsed/mobile style (hamburger nav, no full desktop nav — per the standard 1039px cutoff), while the Dashboard body/sidebar area may already have switched to its wider "desktop" treatment (per its own 1024px cutoff). If so, this is a real, page-specific layout seam that doesn't exist on the marketing pages (Home/SectionFront/Article/Obituaries), where a single 1039px boundary governs the whole masthead. Confirming this visually at the 1024px pass below.

**Confirmed directly at 1024px, per Karl's own question — the "Reader Dashboard ▾" dropdown menu is the concrete example of this:** this new page-section nav element (the "Reader Dashboard" heading with a chevron, which expands into an accordion listing Profile / Subscription / Benefits / Saved Articles / Gifted Articles / Newsletters / Mobile Apps / Get Support) uses Tailwind's `lg:` responsive prefix directly in its class list (`cursor-pointer lg:cursor-default`, and its wrapper uses `lg:static lg:w-auto lg:border-b-0 lg:h-[49px]`). Tailwind's default `lg` breakpoint is `min-width: 1024px`, confirmed live via `window.matchMedia('(min-width: 1024px)')` returning `false` at 375px (dropdown is interactive/`cursor: pointer`) — matching the same 1024px threshold already found on `#reader-dashboard-island-root`. **This is the "menu always visible" behavior from the handoff:** below 1024px the menu is a collapsible accordion (must tap to expand); at 1024px and above it becomes non-interactive (`cursor-default`), i.e. permanently expanded/visible rather than needing a toggle. Confirming the visual form of "permanently expanded" at the 1024px+ passes below.

**Scope note per Karl (2026-09-15):** the breadcrumb row ("HOME > READER DASHBOARD") sits between the masthead and this dropdown on production, but is explicitly **out of scope** for the masthead audit — page content, not masthead. The "Reader Dashboard ▾" dropdown itself **is in scope** going forward. Good news: it's already present in Figma's `Page=Dashboard` components (confirmed on `Device=SM-Mobile, State=Default` — node `456:3300` — which already shows the masthead nav row followed directly by the "Reader Dashboard ▾" row, correctly omitting the breadcrumb). No Figma gap here, just confirming fidelity as we go.

### Reader Dashboard Menu — documented breakpoints (per Karl, 2026-09-15)

**Karl clarified: this dropdown/menu is already fully documented in a separate Figma library file, `Reader Dashboard v2.0` (fileKey `PhXogWaQcnNSnQqxyRu4b2`) — we don't build it, we just need to know where it lives.** Found on page **"Basic Page Structure / Nav Menu / LOWA | 2025.06.13"**, frame **"Reader Dashboard Menu"** ([link](https://www.figma.com/design/PhXogWaQcnNSnQqxyRu4b2/Reader-Dashboard-v2.0?node-id=410-32420)). This frame documents the menu at 5 explicit breakpoints, each labeled with a literal viewport size and directly mapped to our `Masthead` component's own `Device` naming:

| Documented viewport | Label | Menu behavior | Maps to `Masthead` `Device` | Component reference |
|---|---|---|---|---|
| 340×882 | Fold | Closed (collapsible) | `XS-Fold` | instance `1184:30364` → main component `Device=XS-Fold` |
| 340×882 | Fold | Open | `XS-Fold` | component `567:54709`, "Reader Dashboard \| Mobile \| LOWA" |
| 360×800 | Mobile - Small | Closed (collapsible) | `SM-Mobile` | instance `1184:30086` → main component `Device=SM-Mobile` |
| 360×800 | Mobile - Small | Open | `SM-Mobile` | component `567:51793`, "Reader Dashboard \| Mobile \| LOWA" |
| 768×1024 | Tablet - vertical | Closed (collapsible) | `MD-TabletV` | instance `1181:30233` → main component `Device=MD-TabletV` |
| 768×1024 | Tablet - vertical | Open | `MD-TabletV` | component `567:50322`, "Reader Dashboard \| TabletV \| LOWA" |
| 1024×768 | Tablet - horizontal | **"Menu always visible"** | `LG-TabletH` | instance `1172:30784` → main component `Device=LG-TabletH` |
| 1280×960 | Desktop | **"Menu always visible"** | `XL-Desktop` | instance `1172:30238` → main component `Device=XL-Desktop` |

**This is the authoritative, literal answer to "are there documented breakpoints here?"** and it independently corroborates the live-CSS finding above: the collapsible/interactive dropdown behavior holds through `MD-TabletV` (768px), and **"menu always visible" begins exactly at the `LG-TabletH` tier (1024px)** — matching the Tailwind `lg:` (`min-width: 1024px`) class-driven behavior confirmed live. The documented set uses slightly different literal pixel widths (340/360/768/1024/1280) than this project's own standard test widths (375/700/1024/1100/1040/1280/1728), but they land in the same `Device` tiers, so no conflict — our existing test widths remain valid for the masthead-level pass; this table is the reference to point to if anyone asks specifically about the dropdown menu's own documented sizes.

**Note:** attempted to screenshot the Mobile-Small Closed/Open component instances directly from this library file for a visual double-check; both came back as blank/empty exports (likely an off-canvas or render-state quirk in this file, not investigated further since Karl's ask here was scope/location, not a pixel audit of this library).



### 375px — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=SM-Mobile, State=Default, Page=Dashboard` (`456:3300`) in `WordPress Elements`.*

**Structure match — default:** hamburger / centered logo / avatar+chevron / search icon row → "Reader Dashboard ▾" dropdown row. Matches Figma `456:3300` exactly (confirms Figma correctly omits the breadcrumb, which is out of scope per Karl). Clicked the dropdown live: expands into an accordion listing Profile / Subscription / Benefits / Saved Articles / Gifted Articles / Newsletters / Mobile Apps / Get Support — matches the left-sidebar nav items seen at wider Default widths, just collapsed into a mobile accordion (see the documented-breakpoints table above for the authoritative Open/Closed spec).

**Scrolled — matches Figma, confirmed via both headroom states:** while actively scrolling down, the header briefly shows `headroom--not-top headroom--unpinned` and the nav row (hamburger/logo/avatar/search) appears to scroll away — but per this project's own established finding (documented earlier for Home/SectionFront/Article/Obituaries), this transient "unpinned" state is vestigial, not the design-relevant sticky state. Scrolling back up even slightly flips the header to `headroom--not-top headroom--pinned`, and the **full nav row + breadcrumb + "Reader Dashboard ▾" row all reappear together, pinned at the top** (confirmed via `getBoundingClientRect()`: `.site-header` sits at `top: 0`, full 104px height, and a zoomed screenshot confirms the hamburger/logo/avatar row is genuinely present, not just occupying empty space). This matches Figma's `Device=SM-Mobile, State=Scrolled, Page=Dashboard` (`456:3348`) exactly, which depicts the same two-row pinned structure. No fix needed — initial read of a compressed screenshot at the "unpinned" transient state briefly looked like a mismatch; re-confirmed clean after checking the pinned state directly.

**Ad slots:** 0 (Reader Dashboard is a logged-in-only, ad-free page by nature — no ad units present at any width, confirmed via `googletag.pubads().getSlots()`).

**No popup encountered** at 375px.

### 700px (Tier 2) — ✅ reviewed 2026-09-15
*Compared against Figma: `Device=MD-TabletV, State=Default/Scrolled, Page=Dashboard` (`456:3152` / `456:3177`).*

**Structure match — default:** nav row → "Reader Dashboard ▾" dropdown (still collapsed/interactive at this width — confirmed `window.matchMedia('(min-width: 1024px)')` returns `false` at 700px, consistent with the documented breakpoint table above). Matches Figma `456:3152`.

**⚠️ Bug found and fixed, 2026-09-15 — AccountMenu wired to wrong device tier (same class as the Obituaries findings):** both `456:3152` (Default, instance `456:3175`) and `456:3177` (Scrolled, instance `456:3200`) had their `AccountMenu` wired to `Status=loggedIn, View=Closed, Device=XL-Desktop, UserType=loggedIn` instead of `MD-TabletV`. **Fixed** both by remapping `Device` to `MD-TabletV` (existing variant `910:16514`, no new variant needed). Screenshot-verified byte-identical before/after on the Default variant — confirms this is the same purely cosmetic-metadata issue as the Obituaries Ad-Free findings, not a visible bug.

**Scrolled — matches Figma:** full nav row + "Reader Dashboard ▾" row pinned together on scroll-up, same pattern as 375px. Matches Figma `456:3177`.

**Ad slots:** 0.

**No popup encountered** at 700px.

### 1024px (Tier 3) — ✅ reviewed 2026-09-15 — the seam flagged above, confirmed live

**This is exactly the "menu always visible" transition documented above, confirmed empirically:** `window.matchMedia('(min-width: 1024px)')` is `true` at this width, so the "Reader Dashboard ▾" dropdown is gone — replaced by the full static sidebar list (Profile / Subscription / Benefits / Saved Articles / Gifted Articles / Newsletters / Mobile Apps / Get Support), all shown at once, no toggle needed. **But** `window.matchMedia('(min-width: 64.9375em)')` (the masthead's own 1039px threshold) is still `false` — confirming the masthead nav bar itself is still supposed to be in its collapsed/mobile style (hamburger only, no "All Sections"), exactly the seam predicted in the breakpoint investigation: **the masthead and the Dashboard body are on two different breakpoint systems, and 1024–1038px is where that becomes visible.**

**⚠️ Bug found and fixed, 2026-09-15 — Figma's `Device=LG-TabletH` Dashboard masthead was showing the wrong (desktop) nav style:** compared against `Device=LG-TabletH, State=Default, Page=Dashboard` (`456:2996`) and `State=Scrolled` (`456:3047`), Figma was incorrectly showing "☰ All Sections" (the expanded desktop nav treatment) instead of the collapsed hamburger-only style that production actually uses at 1024px (confirmed live: no "All Sections" text visible in the masthead at this width) and that every other page type in this same component set already uses correctly at this same `LG-TabletH` tier (verified directly against `Device=LG-TabletH, Page=Obituaries`, which renders correctly). **Root cause:** the nested `SectionMenu` → `SectionMenuHeader` → "All Sections" title text had an instance-level `opacity: 1` override on the Dashboard variants specifically, while the equivalent text on every correctly-rendering page type (e.g. Obituaries) has `opacity: 0` — all other component properties (`Device=XL-Desktop` on both the `SectionMenu` and `SectionMenuHeader` sub-instances, identical on both Obituaries and Dashboard) were actually the same on both, so this was a one-off visual override, not a variant-wiring issue. **Fixed** by setting the "All Sections" title's `opacity` to `0` on both `456:2996` (Default) and `456:3047` (Scrolled). Screenshot-verified: masthead now correctly shows hamburger-only, matching production and every other page type.

**Also fixed while here, same class as the recurring `AccountMenu` bug:** both variants' `AccountMenu` instances were wired to `Device=XL-Desktop` instead of `LG-TabletH` (using the same `LG-TabletH` loggedIn variant created earlier in the Obituaries Ad-Free pass, `3414:51875` — no new variant needed here). Screenshot-verified byte-identical, confirming pure hygiene fix.

**Scope confirmation — the sidebar/menu is correctly *not* part of the masthead at this tier:** scrolled the live page and confirmed the Profile/Subscription/etc. sidebar list scrolls away with the page body content (it is not sticky/pinned), while only the masthead nav row + breadcrumb stay pinned on scroll-up. This confirms Figma is right to omit the sidebar/menu entirely from the `LG-TabletH`/`XL-Desktop` masthead components (`456:2996` is 64px tall, masthead-only) — unlike the `SM-Mobile`/`MD-TabletV` tiers, where the "Reader Dashboard ▾" dropdown trigger row genuinely is part of the sticky masthead (104px tall components) and correctly in scope per Karl's instruction above.

**Ad slots:** 0.

**No popup encountered** at 1024px.

### 1100px (Tier 4) — ✅ reviewed 2026-09-15 — production bug found, logged as #16

**Masthead now crosses its own 1039px threshold too** (`window.matchMedia('(min-width: 64.9375em)')` → `true`): production shows the full desktop masthead — "All Sections" + avatar + search → weather/date + logo → **nav-links row** (News / Local News / Sports / Things to Do / Opinion / Obituaries / Marketplace / On the Record / BestReviews) → **"TRENDING:" bar** (Fremont County Nonprofit Guide 2026, Royal Gorge Living) → breadcrumb → static sidebar (Profile/Subscription/etc., "always visible" per the 1024px Dashboard-body breakpoint).

**✅ Resolved — this is a production bug, not a Figma gap (per Karl, 2026-09-15):** compared against `Device=XL-Desktop, State=Default, Page=Dashboard` (`456:2715`) — Figma's component is only 144px tall (just the "All Sections/avatar" row + weather/logo row), versus Home's 497px 4-row structure (`456:2573`, which includes a nav-links row and an ad/trending row). Karl confirmed **the Reader Dashboard should not display the trending bar or top navigation — Figma's minimal treatment is intentional and correct.** What production shows at canoncitydailyrecord.com/dashboard/ (the full nav-links row + "TRENDING:" bar at this width) is the actual bug. **No Figma changes made.** Logged as a new engineering-track entry: **`design-vs-production.md` #16.**

**AccountMenu:** correctly wired `Status=loggedIn, View=Closed, Device=XL-Desktop, UserType=loggedIn` (`653:9230`) — no fix needed, this is the genuinely-XL-Desktop tier.

**Ad slots:** 0.

**No popup encountered** at 1100px.

### 1040px (XL-Desktop tier, literal built width) — ✅ reviewed 2026-09-15

Identical pattern to 1100px — full desktop masthead, nav-links row, trending bar, static "always visible" sidebar. Same production bug noted above applies (nav-links/trending shouldn't render here at all, per Karl — see #16 in `design-vs-production.md`), not re-logging separately. `Device=XL-Desktop, State=Default, Page=Dashboard` (`456:2715`) is this variant's actual built width. 0 ad slots, no popup.

### 1280px (Tier 5) — ✅ reviewed 2026-09-15

Identical pattern to 1040px/1100px — nav-links row + "TRENDING:" bar still incorrectly present (same production bug, #16 in `design-vs-production.md`), static sidebar, no new behavior at this width. 0 ad slots, no popup.

### 1728px (sanity check — still Tier 5) — ✅ reviewed 2026-09-15

Identical to 1040/1100/1280px — no new behavior at the widest width tested, including the #16 production bug (nav-links row + trending bar still present). 0 ad slots, no popup.

**This completes the full Reader Dashboard masthead audit: all 7 widths (375/700/1024/1100/1040/1280/1728px), default + scrolled, reviewed.**

## Follow-up (out of scope for this pass)

**Reader Dashboard masthead audit is now complete** (see `## Reader Dashboard masthead audit` above) — this was the last remaining phase of the original project scope (Home → SectionFront → Article → Obituaries → Reader Dashboard, per the handoff doc). No further follow-up phases remain from that original scope. Two open items carried over from earlier passes, both low-priority/optional:
- A 620–630px visual confirmation of the Obituaries 624px search-bar stacking behavior (CSS evidence is unambiguous, so this is confirmatory only).
- The Figma AdFree/Scrolled coverage gap for Obituaries (no combined `State` value exists for that combination) — needs a call on whether it's worth building.

## Popups encountered

- **375px, Article page, default load:** a "trust/sourcing standard" tooltip popover appeared over the headline area (small speech-bubble box with an X close button), reading: "Based on facts, either witnessed and verified directly by the reporter, or reported and confirmed from knowledgeable sources." Flagged live to Karl; did not block the masthead area. Logged as a to-do in `Article-Page-To-Do.md` (Figma component doesn't exist yet).
- **768px spot-check, Article page, default load:** same tooltip reappeared (identical copy/behavior). Did not appear at 700px on the same page — seems intermittent, not guaranteed on every load.
- **1024px, Article page, default load:** same tooltip, third sighting. Still Article-page-specific in every sighting so far.
- **1100px, Article page, default load:** same tooltip, fourth sighting.
- **1280px, Article page, default load:** same tooltip, fifth sighting — appeared at every width tested on the Article page except 700px.
- **1100px, Article page, default load, Ad-Free/logged-in pass:** same tooltip, sixth sighting overall. Confirms the popup is tied to the Article template regardless of login/ad state.
- **1040px, Article page, default load, Ad-Free/logged-in pass:** same tooltip, seventh sighting overall.
- **1728px, Article page, default load, Ad-Free/logged-in pass:** same tooltip, eighth sighting overall — appeared at every width tested on the Article page except 700px, across both the logged-out and ad-free passes.
- **1728px, Article page, default load, logged-out pass:** same tooltip, ninth sighting overall.

## Summary

**Logged-out audit (Home / Section Front / Article, all 6 widths: 375/700/1024/1100/1280/1728):** ✅ complete at all six widths, including the 1728px pass added as a follow-up after the Ad-Free audit was finished. 1728px is structurally identical to 1100px and 1280px on all three page types — no new behavior at the widest width tested.

**Ad-Free audit (Home / Section Front / Article, all 6 widths):** complete at all six widths (375/700/1024/1100/1040/1728). Every width shows the same pattern: bare masthead row, no ad units, logged-in avatar. A systemic bug was found and fixed in Figma before this pass began — all 30 Default/Scrolled Masthead variants were incorrectly wired to show a logged-in subscriber avatar instead of the correct logged-out treatment (Subscribe/Log In buttons on desktop, plain person icon on mobile); the 9 AdFree variants were already correct and untouched.

**New engineering findings from this project, logged in `design-vs-production.md`:**
- **#14 — Top nav bar overflows its container at 1040–1279px (Tier 4).** Systemic, reproducible with any content at that width; Figma was rebuilt to match production's real overflow behavior (11-item nav, natural width, parent-clipped) rather than hide it.
- **#15 — Article scrolled-state headline overflows behind the bookmark/share icons.** Root-caused across three widths, cross-validated in both the logged-out and Ad-Free passes: worst at 1040px (95px overlap), still present at 1100px (69px overlap), fully resolved by 1728px (241px clearance, identical measurement in both passes) — a narrow-viewport layout bug, not a headline-length or login-state coincidence. Not replicated in Figma since it only shows up in the narrower part of the desktop range and Figma's placeholder headline doesn't trigger it.

**Popups:** the same trust/sourcing tooltip on the Article page reappeared 9 times across every width tested except 700px, across both the logged-out and ad-free passes — confirmed template-level, not breakpoint- or login-state-specific. Logged as a to-do in `Article-Page-To-Do.md`.

**Obituaries masthead audit (logged-out pass) — complete, 2026-09-15:** all 7 widths (375/700/1024/1100/1040/1280/1728), default + scrolled, structurally matches Figma at every width after fixes. Along the way this pass surfaced and fixed two project-wide issues that also affected Home/Section Front/Article: the `AccountMenu`/`LG-TabletH` device-mapping gap (was showing desktop Subscribe/Log In buttons instead of the mobile-style icon at 1024px) and a `UserStatus` detached-wrapper-frame cleanup (`MD-TabletV`/`SM-Mobile`/new `LG-TabletH` variants). Also confirmed two genuine Obituaries-specific breakpoints (624px, 800px) inside the Endless Tributes search widget, not present on the other page types — see the Site-wide element breakpoint catalog and the breakpoint-investigation write-up above. The 620–630px visual confirmation of the 624px stacking behavior is now done (confirmed, no discrepancy). The 1728px ad-serving oddity (300x250 creative rendered instead of the expected 320x50 banner, ad box not visually appearing) has been re-checked and formally closed out as ad-inventory noise, not a masthead-fidelity issue — no engineering or Figma action needed.

**Obituaries masthead audit (Ad-Free / logged-in pass) — complete, 2026-09-15:** all 7 widths (375/700/1024/1100/1040/1280/1728), default + scrolled, structurally matches Figma at every width after fixes. Confirmed logged in as a subscriber throughout (avatar visible, 0 GPT ad slots), carrying over the same Chrome session from the earlier Home/SectionFront/Article Ad-Free pass — no re-login needed. Two more AccountMenu device-mapping gaps were found and fixed, same root cause as the earlier LG-TabletH finding but on the **loggedIn** branch this time: at 700px (MD-TabletV), the AccountMenu was wired to `Device=XL-Desktop` when a correct `MD-TabletV` loggedIn variant already existed — simple remap; at 1024px (LG-TabletH), no loggedIn variant existed for that device tier at all, so a new `Status=loggedIn, View=Closed, Device=LG-TabletH, UserType=loggedIn` variant was created (cloned from MD-TabletV) and wired in. Both fixes were screenshot-verified byte-identical to the pre-fix render — the loggedIn AccountMenu doesn't actually vary visually across device tiers, so these were pure correctness/consistency fixes, not visible bugs. At 1100/1040/1280px the AccountMenu was already correctly wired (those widths map to the genuinely-XL-Desktop Figma variant). **✅ Resolved 2026-09-15:** the Figma coverage gap flagged above (no combined "AdFree + Scrolled" state) has been built out, per Karl's approval. The single-select `State` property on the `Masthead` component set now has a 4th value, `AdFree-Scrolled`, alongside `Default`/`AdFree`/`Scrolled`. Five new variants were added (`Page=Obituaries` × each of the 5 Device tiers: XS-Fold, SM-Mobile, MD-TabletV, LG-TabletH, XL-Desktop), each built by cloning the corresponding `Scrolled` variant (which already has the collapsed/compact "Obituaries" title-hidden structure and no ad-block instances) and re-wiring its nested `AccountMenu` instance from `Status=loggedOut, UserType=loggedOut` to `Status=loggedIn, UserType=loggedIn` — matching the same pattern the existing `AdFree` variants use. Screenshot-verified on XL-Desktop and MD-TabletV: the new variant correctly shows the logged-in avatar+chevron (not Subscribe/Log In buttons) with the title collapsed, everything else identical to the `Scrolled` variant. Component set integrity confirmed after the change (75 total children, no duplicate names, `componentPropertyDefinitions.State.variantOptions` now `["Default","AdFree","Scrolled","AdFree-Scrolled"]`). Scope was Obituaries only, per Karl's answer to the specific question asked — Dashboard was not touched since no equivalent gap was flagged for it during that pass (Dashboard's AdFree/Scrolled treatment wasn't found to diverge the way Obituaries' did); worth a follow-up look if Dashboard's masthead ever grows the same title-collapse-on-scroll behavior. No new production-side engineering mismatches were found — everything here was Figma-side and fixed directly, so `design-vs-production.md` stays at #15.

**Reader Dashboard masthead audit — complete, 2026-09-15:** all 7 widths (375/700/1024/1100/1040/1280/1728), default + scrolled, tested on **canoncitydailyrecord.com/dashboard/** (per Karl's direction — a different site than the rest of this project) using a logged-in test subscriber account. This is a logged-in-only page, so there's a single pass (no separate logged-out/Ad-Free split), matching Figma's own `Page=Dashboard` variant set (`Default`/`Scrolled` only, no `AdFree`).

Key findings: (1) Documented the Reader Dashboard's own page-body breakpoints, which genuinely differ from the masthead's 1039px rule — the dropdown/sidebar menu switches from a collapsible accordion to "always visible" at exactly 1024px (`LG-TabletH`), confirmed both via live CSS (`lg:` Tailwind classes) and an authoritative source: the separate `Reader Dashboard v2.0` Figma library documents this same menu at 5 explicit breakpoints (340/360/768/1024/1280px), all mapping cleanly onto the Masthead's own `Device` names — logged as a reference table rather than rebuilt, per Karl. (2) Fixed the same recurring `AccountMenu` device-mapping bug at 700px and 1024px (`MD-TabletV`/`LG-TabletH`), same pattern as the Obituaries Ad-Free pass, zero visual change. (3) Fixed a real Figma bug at the `LG-TabletH` tier (1024px): the masthead was incorrectly showing the expanded "All Sections" desktop nav treatment instead of the collapsed hamburger-only style that production (and every other page type in this component set) uses at that width — root cause was a stray instance-level opacity override on the "All Sections" title text, now corrected to match. (4) Confirmed the sidebar/menu is correctly excluded from the masthead component at the `LG-TabletH`/`XL-Desktop` tiers (it scrolls with page content there, unlike the sticky dropdown-trigger row at narrower tiers). (5) **New engineering-track finding, logged as #16:** production shows a full nav-links row and "TRENDING:" bar on the Dashboard page at desktop widths (1040/1100/1280/1728px) that Figma's intentionally-minimal Dashboard masthead correctly omits — confirmed with Karl that Figma is right and production needs to suppress those rows.

**All five of Karl's 2026-09-15 follow-up items are now complete, on top of the original fully-audited project scope (Home → SectionFront → Article → Obituaries → Reader Dashboard):** (1) the 620–630px Obituaries search-bar stacking behavior is confirmed, no discrepancy; (2) the Obituaries AdFree/Scrolled Figma coverage gap is closed (new `State=AdFree-Scrolled` variant, 5 devices); (3) the 1728px Obituaries ad-serving oddity is re-checked and closed out as ad-inventory noise; (4) the Obituaries `XL-Desktop` breakpoint-width mismatch is found and corrected (was 1280px, now 1040px); (5) every `Device` variant across the whole Masthead component set (all 5 Page types, 75 variants) is now labeled with its literal real-CSS pixel range, and the on-canvas column-header labels were updated to match. Only open item: Dashboard's `XL-Desktop` variants (`Page=Dashboard`) have the same 1280px-vs-1040px width mismatch found for Obituaries, flagged but not fixed — out of scope for this round since Karl's request was specifically about Obituaries' widths, but worth a quick follow-up pass.
