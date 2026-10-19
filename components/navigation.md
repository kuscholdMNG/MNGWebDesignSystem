# Navigation

> **Updated 2026-09-25 — read this first.**
> - **Where the header lives now.** The production-accurate header is the **Masthead** component set (`456:2572`, 75 variants: Device × State × Page) on the "Menus and Parts" page of **WordPress Elements** (`b1iZxkFwtAYq9rElmnCAzd`, formerly "Website Page Templates"). Its breakpoint audit is `breakpoint-audit.md` (this folder), and its production gaps are design-vs-production entries 22–25. The account dropdown's source is **AccountMenu** (`910:16425`) in the same file. The pilot Header, Account Trigger, Off-Canvas Section Panel and Account Dropdown Menu components mentioned in §3.2 and §9 were retired on 2026-09-25; the measurements in those sections are still valid.
> - **Token names.** `color/base/ink` is now `color/theme/near-black` / `color/theme/nav-text` in the main file's Colors collection (see `tokens/colors/`).
> - **Themes.** There are 3 shared themes. "Morning Call" (mcall.com) is a site on Modern Earthy, not a theme. Greeley Tribune is a Prairie Mountain Publishing site (Modern Earthy + PMP color override), so it isn't a Modern Earthy color reference; Modern Earthy's nav text color is still unconfirmed live.

**Status:** Audited (live sites). Built in Figma as the Masthead component set in WordPress Elements (see note above).
**Pilot sites:** Chicago Tribune (CT), Denver Post (DP), Orange County Register (OCR), Orlando Sentinel (OS) — structurally audited. Greeley Tribune and mcall.com joined the pilot set 2026-08-27 (added to give Modern Earthy a live representative — mcall.com also runs Modern Earthy, not a separate theme, see §5.2) but have only been checked for platform-wide typography so far — nav structure, tokens, and breakpoints haven't been looked at on either yet. See §5.2 for one concrete, ready-to-check gap this closes.
**Platform:** shared CMS (WordPress, parent theme "mason", child theme "scng"), each site runs one of 3 shared CSS themes (Measured Vibrant, Bold Coastal, Modern Earthy) plus its own color override layered on top via the WordPress Customizer — confirmed via literal theme stylesheet filenames (`measuredvibrant.css`, `boldcoastal.css`, `modernearthy.css`) and by checking the cascade directly (2026-08-27).

---

## 1. Anatomy

The header is one shared component across every page type and every pilot site. It has three structural rows:

1. **Utility bar** — weather + date + e-edition link (left), account icon + chevron + search icon (right)
2. **Masthead** — centered site wordmark/logo
3. **Primary nav row** (`.nav-primary-bottom`) — either the site's full section list (homepage only), or a section title + sub-category tabs (section fronts and articles)

A **trending ticker** sits below row 3, homepage only.

Below ~1039px, rows 1–3 collapse into a single 65px bar: hamburger icon + centered logo + account icon + search icon. The trending ticker and full nav row are removed from the layout entirely, not just hidden.

---

## 2. States

### 2.1 Breakpoint (collapsed ↔ expanded)

**Exactly `max-width: 64.9375em` = 1039px.** Confirmed by reading the literal CSS source (not inferred from screenshots) on Chicago Tribune, OC Register, and Orlando Sentinel:

```css
@media (max-width: 64.9375em) {
  .nav-wrapper-primary .nav-primary-bottom { display: none; }
  .nav-primary .icon-hamburger, .nav-primary .icon-search { display: block; }
}
```

Binary switch — there is no separate tablet layout. Verified identical behavior at 375px (mobile) and 768px (tablet); both show the collapsed 65px header. Denver Post not source-confirmed but behaves identically empirically; near-certain same shared value.

| Width | Header height | Primary nav row | Trending ticker |
|---|---|---|---|
| ≤ 1039px | 65px | removed | removed |
| > 1039px | ~226–228px | shown | shown (homepage only) |

### 2.2 Scroll (persist vs. hide)

**Header always persists — it never hides on scroll, in either direction.** This corrects an earlier misread: the CSS uses the "headroom.js" library's `headroom--pinned` / `headroom--unpinned` class names (which conventionally mean shown/hidden), but this theme has no rule that actually hides the header in the "unpinned" state — the classes are vestigial. Confirmed via computed style, not just class name, on Chicago Tribune and OC Register (both showed `transform: none`, header still rendered at `y: 0` after scrolling 500–600px).

Real visual change on scroll is background/elevation only:

| | At page top (`headroom--top`) | Scrolled (`headroom--not-top`) |
|---|---|---|
| `position` | relative | fixed, `top: 0` |
| `background` | transparent | `#FBFBFB` / `rgb(251,251,251)` |
| `box-shadow` | none | `0 3px 3px rgba(0,0,0,0.25)` |

### 2.3 Logged-out vs. logged-in

**Logged out:** clicking the account icon navigates to a full external login page (`login.npuserlogin.com`, Auth0-style), not a dropdown. Confirmed on Chicago Tribune and Orlando Sentinel.

**Logged in:** clicking the account icon opens the account dropdown menu — see §4.

⚠️ Automation note: the account-icon toggle (`div.digisubs-toggle.pushnav`) resisted both a real OS-level click and a scripted JS click/event-dispatch — likely intentional trusted-event gating on this subscription-related widget. It only opened when a human clicked it directly. Worth knowing if this component needs QA automation later.

### 2.4 Page type (homepage vs. section front vs. article)

No breadcrumb pattern exists (an earlier read of one was a width-comparison artifact, since corrected). Instead:

- **Homepage:** primary nav row shows the site's full section list.
- **Section front:** primary nav row is replaced by the section's title (styled in the site's brand/accent color — e.g. blue-purple on Chicago Tribune, teal on OC Register) plus a horizontal row of that section's sub-category tabs.
- **Article page:** identical to section front, but using the *article's own* category as the active context — not necessarily the section it happened to be linked from.

Confirmed at a consistent 1280px width on Chicago Tribune, OC Register, and Orlando Sentinel:

| Site | Section front example | Article example |
|---|---|---|
| Chicago Tribune | "Business" + Careers / Top Workplaces / Real Estate / Transportation | "Real Estate" + same 4 tabs |
| OC Register | "Sports" + Angels / Dodgers / Chargers / Rams / Ducks / Kings / Lakers / Clippers / High School / College / Soccer | "Crime and Public Safety" + Crime / Investigative Reporting / Election / Business / Housing / Politics / Environment / Weather |
| Orlando Sentinel | "News" + Latest Headlines / Politics / Education / Environment / Crime and Public Safety / Space / Transportation | "Election" + same tabs as News |

---

## 3. Sub-component: off-canvas section panel ("All Sections")

One shared component serves two triggers: the desktop "All Sections" overflow toggle *and* every mobile/tablet hamburger menu (confirmed identical panel, same content, on Chicago Tribune at both desktop and 375px). Confirmed live again this pass, at desktop width, using the screenshot-space-click technique (§9) — the trigger is trusted-event-gated like the account/search icons, but a real `computer`-tool click opens it reliably.

- Container: `.wrapper-nav.pushnav.pushnav-left.push-from-left`, `position: fixed`, `x: 0`, sits directly below the header (`y` = header height, `z-index: 1000`)
- Fixed width: **300px**, does not scale with viewport (re-confirmed)
- Background: `#FBFBFB` / `rgb(251,251,251)`
- Full-height, scrollable list (`<ul id="pushnav" class="menu">`)
- Top-level items: ~14px, weight 600, ~13px padding
- Contents (Chicago Tribune, in order): Home Page, Subscriber Services, Today's E-Editions, Advertise with Us, Business, Dining, Entertainment, En Español, News, Opinion, Politics, Sports, Chicago Magazine, Suburbs, Classifieds, Jobs, Obituaries, Special Sections, BestReviews, Branded Content, Logout — plus a "Sign up for email newsletters" CTA pinned at the bottom
- Dark backdrop dims the rest of the page while open

Per-site content varies (this is expected — it mirrors each site's own section list).

### 3.1 New finding: several top-level items expand into a nested sub-menu (accordion, not drill-down)

Not previously documented — the panel isn't a flat list. On Chicago Tribune, **13 of the 21 top-level items carry sub-menus** (Subscriber Services, Today's E-Editions, Advertise with Us, Business, Dining, Entertainment, News, Opinion, Politics, Sports, Suburbs, Obituaries, Branded Content); the rest (Home Page, En Español, Chicago Magazine, Classifieds, Jobs, Special Sections, BestReviews, Logout, Subscribe/Log In) are plain leaf links.

**Trigger & indicator:** each expandable row's `<li>` carries class `menu-item-has-children`; the chevron/arrow glyph is not an `<svg>` or `<img>` — it's an **icon-font glyph** (`font-family: icomoon`) rendered via `::before` on the row's `<a>`, absolutely positioned, right-aligned with `padding-right: 0.9375em` (~15px), vertically centered. Easy to miss in a DOM scan if you're searching for `<svg>`/`<i>` elements or a `background-image`, since it's neither.

**Expand mechanism — CSS transform + parent-height accordion:**
- Clicking a row toggles a `submenu-open` class on its `<li>`.
- The nested `<ul class="sub-menu">` lives inside the parent `<li>` at all times (not injected/removed) and uses `transform: scaleY(...)` with a `0.25s ease-in-out` transition — collapsed state scales it to nothing visible, open state to full height.
- The parent `<li>` itself has `overflow: hidden` and its `height` is animated between a collapsed value (just the row, e.g. `37.5px`) and an expanded value (row + full sub-menu height, e.g. `228.125px` for Business's 5 sub-items) — this is what actually clips/reveals the sub-menu, not `display`/`visibility`.
- **Exclusive accordion — confirmed by direct test:** opening "Sports" while "Business" was already open automatically collapsed Business. Only one section can be open at a time; this is not a multi-expand accordion.

**Sub-item styling:** same font-size/weight as the parent row (14px / 600 — no visual demotion), indented via the `sub-menu`'s own left offset (~16px), no bullet or icon. The only visual cues that an item is a child are the indent and its position directly under its (currently open) parent.

**A real, separate finding worth flagging — not a bug in what's documented above, but a DOM oddity:** for some categories (confirmed on Sports), the individual team/sub-section links (Chicago Bears, Bulls, Blackhawks, Cubs, White Sox, etc.) also exist as `class="hidden"` **top-level `<li>` siblings** directly in `#pushnav`, separate from the actual working sub-menu nested inside the Sports `<li>`. These hidden top-level duplicates appear to be unused WordPress nav-menu artifacts (leftover flat entries from how the menu was authored in the CMS) rather than part of the working accordion — the real, visible sub-items live inside the parent `<li>`'s own `<ul class="sub-menu">`. Worth flagging to engineering as menu cruft rather than modeling both structures in Figma.

**Not yet tested:** whether this same nested/accordion structure holds on Denver Post, OC Register, and Orlando Sentinel (only confirmed on Chicago Tribune this pass) — per the shared-theme pattern established throughout this doc, treated as very likely identical but not independently re-verified per-site.

### 3.2 In Figma

The live section panel is part of the Masthead set in WordPress Elements. A pilot rebuild modeled the exclusive accordion with a `State=Closed` / `State=Expanded — Business` pair (sub-items at 32px left padding vs. 16px for top-level rows, "›"/"⌄" chevrons) and used the real `icon-home3` glyph for the Home Page row. That pilot was retired on 2026-09-25; the measurements above are what matter.

---

## 4. Sub-component: account dropdown menu

Matches the **"Dropdown (Bootstrap-style)"** component flagged as documented-but-unbuilt in the previous session. Container class `.dropdown-menu.show`.

### 4.1 Sizing — confirmed NOT responsive

Fixed width regardless of viewport. Verified identical `width: 300px` at 1280px, 375px, and 340px viewports. Height grows to fit content (see §4.2). At 340px viewport the panel had only ~6px of margin to the browser edge — no built-in edge-safety margin was observed, so this is a real risk area to design for rather than copy as-is.

- Background: white
- Border radius: `0 0 5px 5px` (bottom corners only — matches the `radius/utility` token, which is for containers; kept by Karl 2026-10-01).
- Box shadow: `0 8px 16px -4px rgba(0,0,0,0.2)`
- Top padding: 8px

### 4.2 Contents — varies by site, use the fullest as reference

**Chicago Tribune (7 real items):**
1. Avatar (image only, no text)
2. Identity block — display name + email, bold 16px
3. Reader Dashboard →
4. Subscription → (secondary line: plan name, e.g. "Standard Digital Access")
5. Gifted Articles →
6. Contact Us →
7. Log Out (no chevron — direct action)

Panel height: 414px.

**Denver Post (8 real items) — use as the item-count reference:**
Same as above, with **Saved Articles** inserted between Gifted Articles and Contact Us. Panel height: 468px (confirms width is fixed but height flexes to item count).

Both sites also carry an 8th/9th hidden row: literal placeholder text **"SAMPLE MARKETING ITEM HERE"** — an unconfigured promotional slot in the shared template. Build this as an optional/empty-state slot, not a guaranteed 7th/8th row.

Reader Dashboard, Subscription, Gifted Articles, and Saved Articles all correspond to surfaces the previous session already audited in depth on the preprod Reader Dashboard — that content can be reused directly.

**OC Register and Orlando Sentinel menus:** not yet audited (deferred by request).

### 4.3 Open item

Visible hairline dividers appear between the identity block and the links, and before Log Out — but every item reports `border: none` in computed style. The actual CSS mechanism (separate element vs. box-shadow trick) is unconfirmed.

---

## 5. Design tokens

### 5.1 Reused from existing token set
- `color/base/ink` (`#1F1E1C`) — nav text color on Measured Vibrant sites
- `font/weight/semibold` (600)
- `radius/utility` (5px) — dropdown corner radius (containers only; buttons use `radius/sm`, 4px)
- Existing spacing scale (approximate matches on off-canvas panel padding)

### 5.2 New — theme-level text color (not per-masthead)
Real, sourced finding: this is **theme-level**, not brand/masthead-level, unlike the button colors. Confirmed via literal theme CSS filenames:

| Theme | File | Nav text color |
|---|---|---|
| Measured Vibrant | `measuredvibrant.css` | `#1F1E1C` (= existing `color/base/ink`, no new value needed) |
| Bold Coastal | `boldcoastal.css` | `#0A0908` (new value needed) |
| Modern Earthy | not yet observed in pilot | unconfirmed |

**Update, 2026-08-27, revised:** the "not yet observed in pilot" excuse for Modern Earthy no longer applies — Greeley Tribune joined the pilot set this date to give it a live site. It hasn't actually been checked for nav text color yet (only platform-wide typography was audited on it so far), but the row above is now directly checkable rather than blocked on site availability. **"Morning Call" is not a separate row/theme** — an earlier version of this note treated it as a 4th shared theme alongside Measured Vibrant/Bold Coastal/Modern Earthy, but a live check of mcall.com shows it loads `modernearthy.css` directly, the same theme file as Greeley Tribune, with its own Customizer color override on top (same pattern as any other one-off site). So there are 3 shared theme files confirmed to exist, not 4 — "Morning Call" is a site name, not a theme name. This also means checking Greeley Tribune for this row's Modern Earthy value effectively covers mcall.com too, modulo any site-specific override mcall.com might carry (unconfirmed either way for nav text specifically).

Recommend modeling as a token in a **theme** collection (modes: Bold Coastal / Measured Vibrant / Modern Earthy), separate from the existing per-masthead **Brand** collection — since this varies by shared theme, not by individual site. `tokens/colors/color-tokens-decision-log.md`'s built `Theme` collection already has exactly these 3 modes — no gap there once "Morning Call" is correctly understood as a site, not a 4th theme.

### 5.3 New — surface tokens needed for build
- Dropdown/off-canvas panel background (`#FBFBFB`)
- Dropdown box-shadow value
- Header scrolled-state box-shadow value
- Fixed panel width (300px) — likely a component-specific constant rather than a spacing-scale token

---

## 5.4 New — page-type variants (Obituaries, Dashboard)

Confirmed via live-site audit (Obituaries) and the Reader Dashboard v2.0 Figma file (Dashboard). Both are real, structurally distinct header variants beyond the Homepage/Section Front/Article set in §2.4.

**Obituaries** — confirmed identical on all 4 pilot sites via `getComputedStyle`/`getBoundingClientRect`, not screenshots:
- Utility bar and masthead/logo rows are unchanged from Homepage.
- The primary nav row (row 3) is entirely replaced by `.obits-search-form` + `.obit-modal-container` (a name search box + a filter modal trigger) — no section tabs, no trending ticker.
- Total header height ~208–211px (vs. Homepage's ~226–228px expanded), consistent with the missing trending ticker.
- ⚠️ **Real deviation from the Homepage breakpoint rule:** on Homepage, the hamburger icon is only visible ≤1039px (confirmed via literal CSS). On Obituaries, at a comfortably-desktop viewport, **both** the hamburger icon (`.menu-toggle .icon-hamburger`, 20×16) and the "All Sections" button (`div.menu-toggle[aria-label="Open menu of all sections"]`, ~140×64) are visible simultaneously — originally confirmed on the 4 original pilot sites, and **re-confirmed 2026-08-27 at a 1728px viewport on Greeley Tribune and mcall.com too** — same elements, same sizes, same simultaneous visibility, no difference by theme. This is a genuine, now platform-wide, content-level finding from live `getBoundingClientRect` checks, not an inference. Not yet root-caused; worth flagging to engineering as either an intentional dual-trigger pattern for this template or an unintentional leftover.
- Confirms the `endlesstributes.com` link is present in the obituaries search/filter area on all 4 pilot sites — cross-validates the "Endless Tributes" color palette built earlier in this project as this page's actual live branding target.
- Not yet tested: actual collapse behavior at ≤1039px on this specific template (window resize via automation didn't reflect in the live viewport this session — needs a manual DevTools check, same limitation as the original audit).

**Dashboard** — pulled from the existing Reader Dashboard v2.0 Figma file (`Basic Page Structure / Nav Menu / LOWA` page), not a fresh live-site audit — this file already modeled the dashboard masthead in a prior session:
- Masthead is only 2 rows (utility bar 64px + logo/masthead row 80px + a hairline divider) — **no primary nav row at all**, total ~144px vs. Homepage's ~226–228px. Makes sense: once inside the account dashboard, site-wide section nav is replaced by the dashboard's own left-hand "Section Menu," not the header.
- That file's own breakpoint convention treats 1024×768 ("Tablet - horizontal") and 1280×960 ("Desktop") as "menu always visible," with Fold/Mobile-Small/Tablet-vertical (≤768px) as togglable open/closed — a different breakpoint value (1024px) than our audited 1039px marketing-site rule. Since the Dashboard is a distinct web app from the marketing site's shared theme, this may be a legitimately different, real breakpoint rather than a conflict to resolve — not treating it as an error, just flagging that it doesn't match the 1039px rule used elsewhere.

## 5.5 New — confirmed live, logged in (Orlando Sentinel, Karl's own account)

**Logged-in header change:** confirmed real. The account icon becomes a small (~22–24px) circular avatar badge — dark navy background, white initials (server-generated, e.g. "PA"), `border-radius: 60%` — replacing whatever renders in the logged-out state. The dropdown chevron next to it is unchanged. Image source is an authenticated URL (JWT-bearing), consistent with the Auth0-style login already documented in §2.3.

**DefaultAdFree — inconclusive, this account isn't on it.** Ads rendered normally at every audited slot (`sponsorship_1`, `top_leaderboard`, `cube1/2/3_rrail`, `sponsorship_2/3/4`, `bottom_leaderboard`) while logged in as this test account (Standard Digital Access plan). So "ad-free" isn't simply "any logged-in user" — it's gated behind a specific plan/entitlement this account doesn't have. Still unaudited; need either an ad-free-eligible account or confirmation this is aspirational/not-yet-live.

**Account Dropdown Menu — content policy decided.** Orlando Sentinel's live dropdown (logged in, confirmed via direct DOM inspection) is leaner than the Denver Post reference: 300×414px, matching the Chicago Tribune reference (414px, 7 items, no Saved Articles) rather than Denver Post's 468px/8-item version. **Decision: Denver Post's item set stays canonical regardless — it's the superset.** Policy going forward: always build from whichever site has the *most* items found so far (currently Denver Post); a site with fewer items (like Orlando Sentinel) doesn't change the built component, but if a future site turns up items beyond Denver Post's 8, add those too. No Figma changes needed from this Orlando Sentinel finding.

**Still open:** OC Register's dropdown remains unaudited (needs Karl logged into that site separately).

**Cross-site SSO confirmed.** The same logged-in session carried over to Denver Post with no re-login — same account, recognized site-to-site. One inconsistency worth flagging: Denver Post rendered an actual photo avatar, while Orlando Sentinel rendered a generated initials badge ("PA") for the identical account. Not yet root-caused — could be a per-site fallback difference, not necessarily a bug.

**DefaultAdFree — found it, on OC Register.** Checked Denver Post first: `top_leaderboard` (1280×250), `cube1_rrail_atf` (305×600), `bottom_leaderboard` (1280×250), and `sponsorship_1` (537×50) all rendered with real dimensions — ads present, same as Orlando Sentinel. `sponsorship_2/3/4`, `cube2/cube3_rrail_mid/lower`, and `mobile_adhesion` were 0×0, which reads as normal unfilled-inventory noise (unrelated to account tier), not ad-free — the primary slots didn't get suppressed.

**OC Register logged in — different from Denver Post/Orlando Sentinel.** Same logged-in account (avatar confirmed via screenshot). Zero `div-gpt-ad-*` elements exist anywhere in the DOM — not zero-sized placeholders like Denver Post's unfilled slots, but no ad containers injected at all. Confirmed on two separate page loads. Visually confirmed too: no ad space between the lead headline and the next story, a genuinely clean ad-free layout.

**Resolved via logged-out re-test:** Karl logged out and had this session rescan the same URL. Logged out, OC Register renders all 11 `div-gpt-ad-*` slots (`sponsorship_1–4`, `interstitial`, `top_leaderboard`, `cube1/2/3_rrail_atf/mid/lower`, `bottom_leaderboard`, `mobile_adhesion`) — ads are back. So the zero-ad-slot state **is tied to account entitlement**, not a site-wide OC Register characteristic.

**Root cause identified — not a bug, a subscriber tier.** Per Karl: he was logged into two *different* accounts across the pilot sites, not the same account everywhere as this audit had assumed — a **Basic** tier (ads shown) on Denver Post and Orlando Sentinel, and a **Premium/ad-free** tier on OC Register. That fully explains the pattern with no inconsistency:

| State | Denver Post | Orlando Sentinel | OC Register |
|---|---|---|---|
| Logged in, Basic account | ads present | ads present | *(not tested — same account not run here)* |
| Logged in, Premium account | *(not yet tested)* | *(not yet tested)* | 0 ad slots — confirmed |
| Logged out | *(not tested)* | *(not tested)* | all 11 ad slots present |

DefaultAdFree is therefore a real, intentional **subscription-tier state** (Basic vs. Premium), independent of the Logged In/Out axis — logged-out and logged-in-Basic both show ads; only logged-in-Premium suppresses them. It should be modeled as its own variant driven by account tier, not by site. To fully confirm the mechanism is uniform across sites, the clean test would be the *same* tier tested on all 4 pilots (e.g. Premium on Denver Post and Orlando Sentinel too) — not yet done, no need to treat the current mixed-account result as a discrepancy anymore.

One unrelated oddity hit while checking this: OC Register's `body` class briefly read `mobile` even in a normal desktop-context tab load, then `desktop` on a fresh tab load of the same URL — while `window.innerWidth` stayed 360 both times, and stayed `mobile` again on this logged-out re-test. So this theme's desktop/mobile class isn't driven purely by viewport width; something else (device/UA detection?) decides it. Not blocking anything, just noted since it's a real inconsistency in the site's own responsive detection, not a fluke of this session's tooling.

**Investigated further, 2026-08-27 — mechanism narrowed down; likely not a bug at all, and not OC-Register-specific.** Set out to catch the flip in the act and instead found several concrete facts that reframe this:

- **It's not server-side at all.** Fetched OC Register's homepage HTML directly (cache-busted query string, 6 fresh fetches, no JS execution) and the literal string `desktop` never appears anywhere in the raw response — not in the `<body>` tag, not in any inline script. Whatever adds the class does it entirely client-side, after the initial HTML is already in the browser. This rules out the "server caching / edge-node UA-sniffing" theory this doc's earlier "worth engineering awareness" note implicitly assumed.
- **It's not viewport-width-driven, and that's confirmed directly, not just inferred.** At a genuinely narrow 500px window (well below both this component's 1039px nav breakpoint and Card/Teaser's 640px breakpoint), the site's own CSS correctly switches to mobile nav — the hamburger icon is `display: flex` / visible, exactly as it should be — while the `body` class at that same moment still reads `desktop`. So the class and the real responsive layout are answering two different questions.
- **Strong lead on what it actually reads:** `localStorage` on OC Register (and Denver Post — same keys, same values, so this isn't OCR-specific) carries several `aps:<id>:deviceSignal/sua` entries — `aps` = Amazon Publishing Services, one of the page's real-time-bidding/ad-tech vendors, present on every pilot site. The cached value includes `"mobile":0` and a `platform`/`browsers` block that's a direct dump of the User-Agent Client Hints structured API (`navigator.userAgentData`) — confirmed by reading `navigator.userAgentData.mobile` directly in the console, which returns `false` on this real desktop Chrome browser. **This strongly suggests the `desktop`/`mobile` body class is set from `navigator.userAgentData.mobile` (or an ad-tech SDK's cached copy of it) — i.e. it reflects the actual device/OS the browser reports itself as, not the current window/viewport size at all.** That's exactly consistent with resizing a real desktop browser window down to 500px and still getting `desktop`: Client Hints keeps reporting "not a mobile device" regardless of window size, because the browser itself hasn't changed.
- **Given that, the original flip most likely came from comparing two different testing contexts, not a live inconsistency in production.** Chrome DevTools' device-toolbar/responsive-mode emulation overrides `navigator.userAgentData.mobile` to `true` for an emulated phone profile, while a plain resized browser window (what this session's tooling does) does not — so a `mobile` reading followed by a `desktop` reading on "the same URL" is very plausibly what happens when a test pass alternates between emulated-mobile-device checks and normal-window checks, rather than the site behaving inconsistently for one real visitor.
- **Could not reproduce the flip live this pass** — 8 consecutive fresh loads of OC Register, at both ~1131px and the narrowest width this session's tooling could reach (500px; window-resize calls below that had no effect on the tab's actual viewport), all read `desktop`, matching what real Client Hints reports for this desktop browser every time.
- **The exact script that reads this signal and sets the class wasn't pinned down.** All first-party/theme JS bundles checked (the loader plugin, DFM ad-mods, the `mng-digisubs`/Sophi bundle, the `wp-mason` theme's `ads.min.js`, and the theme's `boldcoastal-async`/`common-async` chunk bundles) don't contain this logic. The remaining candidates are the third-party ad SDKs themselves (Marfeel `sdk.mrf.io`, Aditude/Raven `raven-static.aditude.io`) — their scripts are cross-origin and blocked by CORS from this tooling, so their source couldn't be read directly to confirm the exact line.

**Net:** this is very likely a real-device-type signal from an ad-tech vendor's Client Hints read, working as designed — not a caching bug, not something unique to OC Register's own code (Denver Post carries the identical signal), and not something that should block anything. Recommend closing this as "explained, not a bug" once engineering confirms which script reads `aps:*:deviceSignal/sua` (or `navigator.userAgentData.mobile` directly) and sets the class — that would fully close the loop, but the class's *purpose* is now well understood even without that last confirmation.

**Fully confirmed, 2026-08-28 — Karl set all 6 pilot tabs to a real Galaxy S8 device profile and refreshed.** This directly tested the Client Hints hypothesis above with a real mobile device signal instead of a resized desktop window, and it confirms the theory cleanly while surfacing one genuine, narrow finding:

- **The classification itself is accurate everywhere.** All 6 pilot sites reported the same emulated device correctly: `navigator.userAgentData.mobile = true`, UA = `SM-G950U`/Android, `window.innerWidth = 360`. The `aps:*:deviceSignal/sua` cache (see above) also read `"mobile":1, "model":"SM-G950U"` correctly on every site checked. No site ever misclassified this device as desktop — the underlying signal is right everywhere.
- **But the class isn't applied instantly, and how long it takes varies by site.** Checked immediately after a fresh page load, Chicago Tribune, OC Register, Orlando Sentinel, and Greeley Tribune already had `mobile` on `document.body`. Denver Post and mcall.com did not yet — their `body` class had neither `mobile` nor `desktop` at that same moment. Re-checked ~2 seconds later, both had `mobile` too, correctly, with no misclassification. Repeated the same fresh-load-then-check sequence a second time on both and got the same pattern: empty immediately after navigation, `mobile` present within about 2 seconds.
- **This fully explains the original "flip."** It was never a random inconsistency or a caching bug — it's a client-side script that applies the class with a small, variable delay after page load, and on two specific sites (Denver Post, mcall.com — one from each of two different themes, so not theme-scoped) that delay is long enough to catch mid-load if checked in the first second or two. A check made at the "wrong" moment on those two sites would read as "missing," which is easy to mistake for "flipping to something else" when compared against a site that already has it.
- **Not root-caused down to the exact script** — still blocked by CORS from reading the Marfeel/Raven SDK source directly, so it's not confirmed whether the extra delay on DP/mcall.com is ad-load weight, script ordering, or something else site-specific. But the mechanism itself is now fully explained: real device detection, working correctly everywhere, applied slightly slower on 2 of 6 sites.
- **Worth a note for engineering, not necessarily a bug ticket:** if any component's CSS depends on this class being present at first paint (rather than tolerating it arriving a beat late), Denver Post and mcall.com visitors on real mobile devices could see a very brief flash of the "no class yet" state that the other 4 sites show less of. Worth asking engineering whether anything actually depends on this class at first paint — if nothing does, this is fully closed with no action needed.

## 5.6 Major finding — Account tier is a full variant axis (sourced from the reference file)

Per Karl: logged-in users aren't just subscriber/not-subscriber — there's a third real-world tier, logged-in non-subscribers, who see ads and a different account menu with a "Subscribe" prompt. Checked the reference file Karl shared earlier ("Website Page Templates," now named "WordPress Elements," `b1iZxkFwtAYq9rElmnCAzd`) rather than guess — it has a page literally named **"Account Dropdown Menu"** with a component set called **AccountMenu** (`910:16425`) that models this in far more depth than our live-site audit captured. Treating this as the canonical structural reference for account-tier content going forward — it supersedes assumptions built only from Denver Post/Orlando Sentinel's live content.

**AccountMenu's real variant axes** (actual Figma component properties, not names we inferred):

- `Status`: loggedIn / loggedOut / alert
- `View`: open / closed
- `Device`: XS-Fold / SM-Mobile / MD-TabletV / XL-Desktop — 4 tiers, richer than the single 1039px breakpoint audited for the header nav itself. May be a legitimately different responsive model for this one component rather than a conflict with §2.1 — not resolving that assumption further without more digging.
- `UserType`: loggedIn (generic, closed-state only) / **nonSub** / **BasicSub** / **PremSub** / **groupSub** / **GroupAnon** / loggedOut

**Content by UserType** (Status=loggedIn, View=open, Device=XL-Desktop unless noted):

| UserType | Identity block | Subscription line | Gifted Articles line | Saved Articles line | Extra CTA |
|---|---|---|---|---|---|
| **nonSub** | Name + email (real account) | "Limited Access" | "Subscribe for access" | "Subscribe to Premium for access" | Prominent **"Subscribe Now"** button, right under the identity block |
| **BasicSub** | Name + email | "Basic Digital Subscriber" | "Gift articles remaining: 6" | "Subscribe for access" (still locked) | none |
| **PremSub** | Name + email | "Premium Digital Subscriber" | "Gift articles remaining: 6" | "You've saved 2 articles" (unlocked) | none |
| **groupSub** | Name + email | "Ad-Free Partner Access [...] provided by [Institution]" (placeholder text, contains a literal typo in the reference file — not a live-audited string) | "Gift articles remaining: 6" | "You've saved 2 articles" | none |
| **GroupAnon** | "Anonymous User" + an ID string, no name/email | same Subscription line as groupSub | "Gift articles remaining: 6" | "You've saved 2 articles" | none |
| **loggedOut** | — (no dropdown shown this way) | — | — | — | Header shows **"Subscribe"** + **"Log In"** buttons directly (closed, XL-Desktop); open mobile state shows "Subscribe Now" / "Log In" buttons plus the newsletter Sign Up CTA |

Every open-view variant, regardless of tier, also carries the "SAMPLE Marketing Slot content" placeholder we'd already found, **plus** a "Get Morning Report and other email newsletters" + "Sign Up" CTA footer row.

**`alert` status** (checked on PremSub): inserts a payment-issue block right after Reader Dashboard — "We're having trouble processing the payment for your subscription. To keep reading uninterrupted, please update your payment information today." plus an "Update Payment Info" button — layered on top of otherwise-unchanged PremSub content (still full access, i.e. a grace-period state, not an immediate downgrade). This is a third `Status` value alongside logged in/out, not itself a subscriber tier.

**Off-canvas Section Panel carries a matching but simpler axis**: `UserType`: all / subscriber / nonSub. Only content difference found: `nonSub` inserts one extra row, "Subscribe Now," directly under "All Sections" — the rest (11 section links, Log out, newsletter signup) is identical to `subscriber`.

**Logged-out header buttons — confirmed live on OC Register, resolves the discrepancy.** Rechecked OC Register logged out at a real 1728px desktop viewport (not the earlier mobile-emulated tab): the utility bar shows explicit **"Subscribe"** and **"Log in"** pill buttons at top-right, screenshot-confirmed — matching the reference file's `Status=loggedOut, View=closed, Device=XL-Desktop` variant exactly, real button text, real link targets (`/login?returnUrl=...`). Ads also fully present, consistent with logged-out = no entitlement.

This isn't actually a contradiction with §2.3's "account icon → external login page" finding — it's device-dependent, same as the rest of the header. §2.3's finding came from narrower/mobile-emulated tabs, where these desktop-only pill buttons have no room and the only visible control is the account icon/hamburger (`#digisubs-toggle`), which is a separate widget from the Subscribe/Log In buttons. Both are real; they just show at different Device tiers, mirroring the reference file's own per-device variants for this exact state. Not yet re-confirmed at a genuine (non-emulated) mobile width, but no reason to expect otherwise now.

**Revised account-tier list** (replaces the two-tier Basic/Premium model from §5.5):

1. **loggedOut** — no entitlement, sees ads (live-confirmed)
2. **loggedIn, nonSub** — sees ads, sees "Subscribe Now" prompts throughout the menu (the tier Karl just flagged; not yet live-audited, only confirmed in the reference file)
3. **loggedIn, BasicSub** — sees ads (live-confirmed on Denver Post/Orlando Sentinel), Saved Articles still locked per reference file
4. **loggedIn, PremSub** — ad-free (live-confirmed on OC Register), full access
5. **loggedIn, groupSub** — ad-free per reference file (institutional/partner access), full access — not yet confirmed on any live pilot site
6. **loggedIn, GroupAnon** — same access as groupSub, anonymous identity — not yet confirmed live
7. **alert** (a `Status`, layers on any tier, e.g. PremSub-with-payment-issue) — not yet confirmed live

Only tiers 1, 3, and 4 have real live-site confirmation so far; tier 2's ad behavior isn't live-confirmed yet either (only its menu content, from the reference file); tiers 5, 6, and `alert` exist only in the reference file so far.

## 6. Known open items

1. Divider mechanism inside the account dropdown — unconfirmed (§4.3)
2. OC Register and Orlando Sentinel account menu contents — not yet audited (deferred)
3. Modern Earthy's nav text color — still not confirmed live (mcall.com and canoncitydailyrecord.com are the Modern Earthy review sites; Morning Call is a site, not a theme)
4. Account dropdown's behavior below 340px viewport — untested, likely starts clipping since no responsive/edge-margin rule was found
5. Automating clicks on the account-icon toggle for future QA — real and scripted clicks both failed; only a genuine human click opened it
6. Obituaries page's simultaneous hamburger + "All Sections" visibility at desktop width (§5.4) — **confirmed 2026-08-27 on Greeley Tribune and mcall.com too, identical pattern, now confirmed platform-wide on all 6 pilot sites.** Still flagged to engineering, still not yet explained — this widens the finding's confidence but doesn't answer whether it's intentional.
7. Obituaries collapse behavior at ≤1039px — not yet tested (viewport resize via automation didn't take effect on the live page this session)
8. ~~Logged-in vs. logged-out header differences beyond account-icon destination, and the DefaultAdFree view~~ — resolved (§5.5): avatar badge confirmed; DefaultAdFree confirmed real and driven by subscriber tier (Basic vs. Premium), not by site
9. Same-tier cross-site confirmation for DefaultAdFree — current evidence used a Premium account on OC Register and Basic accounts on Denver Post/Orlando Sentinel (different accounts per site, per Karl). Testing the *same* Premium account on Denver Post and/or Orlando Sentinel would confirm the mechanism is uniform everywhere, not just inferred from OC Register.
10. Chicago Tribune not yet checked for DefaultAdFree — would complete 4-site coverage of this state.
11. **New (§5.6):** account tier is really a 7-value axis (loggedOut / nonSub / BasicSub / PremSub / groupSub / GroupAnon / alert), not the 2-value Basic/Premium model — only 3 of those 7 have live-site confirmation so far (loggedOut, BasicSub, PremSub). Need live audits for nonSub's ad behavior, and ideally groupSub/GroupAnon/alert if any pilot site actually offers institutional or grace-period states.
12. ~~Reference file shows logged-out as header-level Subscribe/Log In buttons, contradicting the account-icon-navigates-out finding~~ — resolved (§5.6): confirmed live on OC Register at real desktop width; not a contradiction, just device-dependent (same pattern as the rest of the header). Still worth a genuine (non-emulated) mobile-width re-check to fully close this out.
13. Decide whether to model the opened search form (§9) in the Masthead set, with a scrim to represent the `body::before` dimming backdrop.

---

## 9. Header findings from the pilot build

A pilot Header was built to test a decoupled structure: the Header carried only Page Type × Breakpoint × Scroll, with login state in a small nested Account Trigger (logged out = "Subscribe" + "Log in" pill buttons filled with `color/theme/primary-dark`, `#0A5962` on Bold Coastal, confirmed live on OC Register desktop; logged in = avatar + chevron). That pilot was retired on 2026-09-25 in favor of the Masthead set in WordPress Elements. The findings below came out of building and checking it and are still valid.

**Findings** (visually verified with screenshots, not just structurally checked):
- **Row heights** are 64 / 80 / 48 / 34 = 226px, **cross-site confirmed live** (not just on Chicago Tribune): Denver Post and OC Register measured byte-identical (64/80/48/34/226) at a real 1728px desktop viewport. Orlando Sentinel came in at 64/**83**/48/34 = **229px** — a small, real 3px difference in the masthead row specifically, not a measurement error. Worth a note rather than forcing it to match; likely a slightly taller logo asset on that masthead.
- **Desktop "All Sections" trigger:** real desktop headers show a hamburger + "All Sections" text label at the far left of the icon row (identically worded on all 4 pilot sites), which opens the same Off-Canvas Panel as the mobile hamburger. The weather/date group sits in the masthead row (left-aligned), with the wordmark centered.
- **New finding: the search icon toggles a hidden inline search form** (`.search-form.header-search`, `display: none` until triggered) rather than navigating to a separate search page — not previously documented. Neither a scripted click nor the first automated `computer`-tool click (aimed using raw CSS-pixel coordinates) opened it — same trusted-event-gating behavior already documented for the account icon (§2.3), compounded by a coordinate-space mismatch (the `computer` tool's click/screenshot space is scaled relative to CSS pixels — e.g. screenshot width 1465px vs. CSS `innerWidth` 1728px on this session's window, ratio ≈0.848). **Resolved:** taking a screenshot first and clicking the icon's position read directly off the screenshot (screenshot-space ≈1387,27, vs. the CSS-space guess of ≈1638,32 which missed because it exceeded the screenshot's own 1465px width) produced a real, trusted click that opened the form on Orlando Sentinel. This screenshot-space-click technique is the fix for any future automation on these trusted-event-gated toggles, not just this one.

  **Opened search form — captured live on Orlando Sentinel (desktop, 1728px viewport):**
  - Container (`.search-form.header-search`): `position: absolute`, full-width (**1728px**), **64px** tall, sits directly below the header's icon row (`y: 64`, matching the corrected Utility Bar height) — `z-index: 100`.
  - Background: `#FBFBFB` (`rgb(251, 251, 251)`) — same off-white already used elsewhere in the header.
  - Box-shadow: `0 3px 3px rgba(0,0,0,0.25)` — identical to the header's own scrolled-state shadow, already documented elsewhere in this file.
  - Input wrapper (`.input-wrapper`): transparent background, flex, 62px tall, starts at `x: 43`.
  - Text input (`input[name="s"]`): placeholder "Type your search", `15px` font, dark text (`rgb(31, 30, 28)` ≈ `color/base/ink`), left-aligned, spans most of the bar's width (**1510px**), `19.5px 4.5px` padding, starts at `x: 77, y: 66`.
  - Submit button (`.search-button`): right-aligned (`x: 1591, y: 81`), **75×32px**, background `rgb(23, 118, 196)` (`#1776C4`-ish, matches Orlando Sentinel's brand primary blue), white **600**-weight text, **5px** border-radius, `1px 6px` padding, label "Search". Note 2026-10-01: buttons are 4px (`radius/sm`); this 5px is production drift (design-vs-production entry 28).
  - **Resolved — dimming backdrop found:** it's not a DOM element at all, which is why `[class*="backdrop"]`/`[class*="overlay"]` selector searches never found it — it's a **CSS-generated pseudo-element**, `body::before`. Confirmed via `getComputedStyle(document.body, '::before')`: `content: " "`, `background: rgba(0, 0, 0, 0.5)`, `position: fixed`, covers the full viewport (`top/left/right/bottom: 0`), `z-index: 10000` (above the search form's own `z-index: 100`), `pointer-events: auto` (consistent with click-outside-to-dismiss, though dismiss-on-click wasn't separately tested). Worth remembering for any future "why can't I find this overlay in the DOM" moment on this theme — check pseudo-elements, not just elements.
  - Confirmed live on Orlando Sentinel; per Karl, the same shared-theme mechanism applies identically on Chicago Tribune, Denver Post, and OC Register (consistent with every other shared-theme structural finding in this doc) — not independently re-verified per-site, taken as confirmed rather than assumed.

  **Same pattern re-confirmed at mobile/collapsed width (360px CSS viewport, i.e. the ≤1039px Collapsed Header variant):** the search icon in the collapsed icon row (hamburger + logo + account + search) opens the identical form, same mechanism, scaled to the narrower viewport rather than restructured:
  - Container: `360px` wide (full-bleed), **64px** tall, same `#FBFBFB` background, same `0 3px 3px rgba(0,0,0,0.25)` shadow, same `z-index: 100` — but now has `10px` padding on the form itself (desktop had `0px`).
  - Text input: **288px** wide, `20.8px 4.8px` padding (desktop was `19.5px 4.5px` — near-identical, likely a sub-pixel rounding difference from the different viewport width rather than an intentional change).
  - Submit button: **62×32px** (vs. 75×32px on desktop — same height, narrower to fit), identical blue fill/white 600-weight text/5px radius/label.
  - The `body::before` dimming backdrop is present and identical in mechanism at this width too (confirmed same computed styles, scaled to the 360×740 viewport).
  - **Conclusion:** the search form is one component that scales fluidly across breakpoints (full-bleed width, fixed 64px height, same colors/shadow/radius) — it does not need a separate "Collapsed" variant with different structure, just a width-scaling instance of the same component. This simplifies the eventual Figma build.


---

## 7. Methodology notes

- All page loads given a minimum 10-second wait before scraping, per standing project rule
- Breakpoint and theme-color findings were confirmed by reading literal CSS source (stylesheet rules and filenames), not inferred from screenshots
- Mobile/tablet viewports tested via the user's own Chrome DevTools device toolbar (manual, since this session's browser automation cannot drive DevTools itself or resize the real window's viewport)
- Logged-in states required the user to log in directly; this session never enters credentials
- Obituaries findings (§5.4) used `getComputedStyle`/`getBoundingClientRect` via direct JS execution in the live page, not screenshots — consistent with the rest of this audit
- A `resize_window` browser tool exists this session, but resizing the window did not change the page's actual `window.innerWidth` on the live site (stayed fixed) — so breakpoint testing still needs the user's own DevTools device toolbar, same limitation as the original audit
- **Standing rule, added 2026-08-28 (Karl):** any time this audit needs to look at a different screen size going forward, prompt Karl to change the size manually on his end (e.g. Chrome DevTools' device toolbar with a real device profile) rather than reaching for this session's own resize tooling. This isn't just a workaround for the `resize_window` limitation above — a real device profile (like the Galaxy S8 test in §5.5) also spoofs User-Agent Client Hints (`navigator.userAgentData.mobile`, etc.), which some site behavior depends on and a plain window resize does not touch. So even if a future tooling update makes `resize_window` change the viewport, the device-profile step still needs to come from Karl's own browser, not this session's automation.

---

## 8. Should-be vs. as-built — the standing policy for reconciling reference files against production

This project already ran into this exact tension once before: `tokens/colors/color-tokens-decision-log.md` models colors as "should-be" values sourced from the Color Styles page, and for Endless Tributes specifically carries a "Production comparison" column flagging which values are a live match, which have drifted, and which are retired/not-found-live. Extending that same pattern to components, formally, going forward:

**The rule of thumb:** structure comes from the idealized reference; content and existence come from the live audit.

- **Which states/variants exist at all** (e.g., that `UserType` has 7 values, that a payment-issue `alert` status exists, that there's a `groupSub`/`GroupAnon` tier) — default to the reference file. A forward-looking design system is supposed to define target states production hasn't necessarily built yet; that's the point of having one, and it's not our job to shrink it down to only what's live today.
- **What a given state actually contains, or whether it's real today** (exact copy, real item counts, real numbers like "Gift articles remaining: 6," whether logged-out really shows two header buttons at this breakpoint) — always prefer a live audit over the reference file's placeholder content, and mark clearly when something is reference-only because it hasn't been checked, or actively couldn't be checked, live.
- Every component and every variant gets a one-line **audit status**, recorded in two places: as a short note in this doc's content tables/lists (already the pattern used in §5.5/§5.6), and as the literal Figma component **description** field on the built node, so anyone opening the file — not just this doc — sees it. Suggested vocabulary, kept short and consistent:
  - **Confirmed live** — real content from a real audited site, name the site(s)
  - **Partially confirmed** — some sub-parts audited live, others not (e.g. nonSub's menu content is reference-only, but its ad-visible status will need its own separate check)
  - **Reference-only / target** — exists in the idealized design file, no live pilot site confirmed to have it yet; still worth building as the system's intended direction, just don't hand it to engineering as "this is what site X does today"
  - **Drifted** — a live site has it, but the real content differs from the reference file's should-be version (the Endless Tributes precedent)
- This same rule already explains an earlier decision without us naming it as a policy yet: choosing the audited 1039px breakpoint over the reference file's declared tablet tier was "prefer live content over reference content" in miniature. Worth treating as the same policy, not a one-off.
