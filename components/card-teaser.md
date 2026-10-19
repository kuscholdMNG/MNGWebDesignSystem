# Article Card / Teaser

> **Updated 2026-09-25 — read this first.** Three things below have been superseded by later decisions:
> 1. **Eyebrow / section-title size and weight.** The 2026-09-01 "20px/400/0.7px on every theme" decision never shipped. Eyebrows are now per theme: Bold Coastal 20/400 Sans, Measured Vibrant 17/700 Sans, Modern Earthy 21/400 Serif (`tokens/typography/typography-decision-log.md`, decision 6). The text color (`color/gray/100`) and 2px `--primary` underline decisions still stand (design-vs-production entry 15.2). The Section Title / Eyebrow component lives in WordPress Elements (`3333:42278`).
> 2. **Bold Coastal's Sans 19px headline is not a bug.** On 2026-09-24 Karl made it a design token: `font/theme/small-headline-family` = Bold Coastal Sans, Modern Earthy Sans, Measured Vibrant Serif, used by the 19px (`CardQuaternary`) and 15px (`HeadlineList`) styles. Production matches, so no engineering action (design-vs-production entry 9).
> 3. **Headline type values.** The current values are the Editorial styles in `tokens/typography/typography-tokens.md` (re-measured on 7 sites 2026-09-24). In particular the 15px headline-list links are Sans on Bold Coastal, not Serif on every site.
>
> The rest of this doc (card anatomy, the 640px breakpoint, divider colors, Section Highlight structure) is still accurate.

**Status:** Audited (live sites, homepage only) — component overall not yet built in Figma. **Eyebrow/module-header title style (size/weight superseded — see note above)** — originally decided 2026-09-01 (Karl): canonical size/weight/letter-spacing = Denver Post's Bold Coastal values (20px/400/0.7px) on every theme, text = `color/gray/100`, underline = 2px site's own `--primary` — see §2.4, §4.4. Ready for engineering; not yet live anywhere. **The title/eyebrow style is built as the Section Title / Eyebrow component** in WordPress Elements (`3333:42278`). The rest of Card/Teaser (the article cards themselves) is still not built.
**Pilot sites:** Chicago Tribune (CT), Denver Post (DP), Orange County Register (OCR), Orlando Sentinel (OS) — structurally audited. Greeley Tribune and mcall.com joined the pilot set 2026-08-27 (both run the Modern Earthy shared theme — "Morning Call" is mcall.com's own name, not a separate theme); as of 2026-08-27 all 6 pilot sites are fully audited for this component — `feature-medium` headline font-family (§2.2), divider color/title style (§2.3–§2.4), and Section Highlight structural composition (§3) — with no open items remaining on Greeley Tribune/mcall.com specifically (see Open Items §9).
**Platform:** same shared CMS as Navigation (WordPress, "mason"/"scng" themes)

---

## 1. Core finding: one `<article>` component, several modifier-class variants

There is no separate "card" and "teaser" component — every homepage content block, from the lead story to a single text-only headline link, is the **same `<article>` element** with a different modifier class controlling which sub-parts render and how they're sized. Confirmed present on all 4 pilot sites:

| Modifier class | Role | Has image? | Has dek/excerpt? | Has timestamp? |
|---|---|---|---|---|
| `feature-large` | Hero / lead story | Yes (large) | Yes | No |
| `feature-medium` | Secondary story row | Yes (medium) | Yes | No |
| `headline-only` | Text-only list link | No (image suppressed even if the post has one) | No | Yes (`<time>`) |

This is a good sign for the design system: it means Figma should model **one Article component with variant properties** (size: large/medium/headline-only, plus image/no-image, dek/no-dek, timestamp/no-timestamp) rather than three unrelated components.

---

## 2. Anatomy

### 2.1 `feature-large` (hero)

Structure (`section.feature-primary > article.feature-large`):
- Flex row (at ≥40em/640px — see §2.1.1 for the responsive behavior), two children:
  - `div.article-info` — `header > h3.entry-title > a.article-title` (headline), then `div.excerpt` (dek), then (on this instance) a `Related` mini-list — see §2.4
  - `figure > a > img` — image, sits to the right of the text at desktop width

No eyebrow/kicker or byline was found in the hero header on any of the 4 sites (just headline text).

**Headline typography — fluid, not a single fixed value:**
At ≥40em (640px): `font-size: 1.8125em` (=29px), `line-height: 1.13` (=32.77px), `font-weight: 700`, `font-family: "Noto Serif", Helvetica, serif`, `color: #000` — confirmed via literal CSS source on Chicago Tribune and Denver Post (`.feature-primary .feature-large header .entry-title { font-size: 1.8125em; line-height: 1.13; }`, `min-width: 40em`). Below 640px, the live-measured size drops to **25px / line-height 29px** (same weight/family/color) — this is the mobile-first base size that the 40em rule overrides upward, not a separate breakpoint-specific override we found written out explicitly. **Correction from the previous version of this doc:** earlier this was reported as "identical 29px across all 4 sites" — that was true at desktop width only; it's a responsive/fluid value, not a single fixed token. Treat it as one typography token with (at least) two size steps, not a flat value.

#### 2.1.1 Responsive behavior (resolves earlier open item)

Tested live at 375px on Chicago Tribune (device toolbar) and cross-checked via literal CSS source on Chicago Tribune + Denver Post:

- `article.feature-large` switches `flex-direction` from `column` (stacked: headline block, then image, then excerpt) to `row` (image beside text) at **`min-width: 40em` (640px)** — confirmed via source, not inferred.
- **This solves the earlier mystery of "a second, empty `<figure>`" flagged as an open item:** the component actually ships *two* `<figure>` instances — one nested inside `header` (used only below 640px) and one as a direct sibling of `.article-info` (used only at ≥640px) — toggled with plain `display: none` / `display: block`, not a single image being repositioned. Source, both confirmed on Chicago Tribune and Denver Post:
  ```css
  /* ≥40em */
  .feature-primary .feature-large > figure { display: block; }
  .feature-primary .feature-large > .article-info figure { display: none; }
  /* <40em (implicit default, not written explicitly — this is the mobile-first base) */
  ```
- **This is a different breakpoint from Navigation's 1039px.** Do not reuse `nav`'s breakpoint token for cards — this needs its own (`40em` / `640px`).
- `article.feature-medium` was also confirmed live to switch to `flex-direction: column` below this same range, consistent with the hero. `article.headline-only` stays a flex row throughout (it has no image to reflow, so row vs. column is largely moot for it).
- **Now confirmed live at 375px on all 4 pilot sites** (Chicago Tribune, Denver Post, OC Register, Orlando Sentinel): identical behavior across every site — hero `flex-direction: column`, mobile-only `<figure>` visible / desktop `<figure>` hidden, hero headline `25px/700/29px line-height`, `feature-medium` also column, `headline-only` stays row. No per-site variation found at this breakpoint, unlike the typography/color splits in §4. This is a genuinely uniform, shared-theme behavior.

**Dek (`div.excerpt`):** `15px / 400`, `line-height: 19px` (CT sample), `"Noto Sans", Helvetica, sans-serif`, `color: rgb(72,70,66)` (~`#48463F`... actually rounds to `#48463C`, ~`#484642`).

### 2.2 `feature-medium` (secondary row)

Structure (`article.feature-medium`): flex row, `figure` (image, left) + `div.article-info` (header + excerpt, right). No timestamp.

**Superseded 2026-09-24 — not a bug.** The Sans-on-Bold-Coastal result below is now the design rule (`font/theme/small-headline-family`; see the note at the top). The original 2026-08-27 write-up is kept for history:

**(Historical) Confirmed engineering bug, fully scoped 2026-08-27 — isolated to the Bold Coastal theme file:**

Per Karl, the actual design rule for this headline is: **Serif on Bold Coastal and Measured Vibrant, Sans on Modern Earthy — no per-site exceptions.** The original version of this section compared one sampled instance per site and concluded (wrongly) that this was a clean per-site split. Checking multiple `feature-medium` instances on every one of the 6 pilot sites' homepages shows it isn't per-site at all — it's per-*instance*, and tracks whether the `<article>` element has picked up a **duplicate `feature-large` class alongside `feature-medium`** on the same element. That duplicate class consistently drops the size/weight from 26px/700 to 19px/600 on **every** pilot site — that part is universal and not theme-dependent, so it's probably not a bug (more likely deliberate: this smaller size shows up specifically on the non-lead stories inside a Section Highlight module). Font *family*, however, only breaks on one theme:

| Site (theme) | `feature-medium` only | `feature-medium feature-large` (duplicate class) |
|---|---|---|
| Chicago Tribune (Measured Vibrant) | 26px/700/Serif — matches rule | 19px/600/**Serif** — matches rule |
| Orlando Sentinel (Measured Vibrant) | 26px/700/Serif — matches rule | 19px/600/**Serif** — matches rule |
| Greeley Tribune (Modern Earthy) | 26px/700/Sans — matches rule | 19px/600/**Sans** — matches rule |
| mcall.com (Modern Earthy) | 26px/700/Sans — matches rule | 19px/600/**Sans** — matches rule |
| OC Register (Bold Coastal) | 26px/700/Serif — matches rule | 19px/600/**Sans** — **violates rule**, should be Serif |
| Denver Post (Bold Coastal) | 26px/700/Serif — matches rule | 19px/600/**Sans** — **violates rule**, should be Serif |

So: **the bug is isolated to Bold Coastal.** Both of its live representatives (OC Register, Denver Post) render the duplicate-class variant in Sans when the rule requires Serif. Measured Vibrant and Modern Earthy each got checked across both of their live representatives and comply with the rule at every instance, on both the single- and duplicate-class variants. This reads like a font-family declaration in `boldcoastal.css`'s rule for the duplicate-class combination that was set to Sans instead of Serif — likely copied from (or defaulting to) Modern Earthy's value rather than Bold Coastal's own. Flagged in `design-vs-production.md`'s "At a glance" table and Open Question #4 (2026-08-27) as a confirmed engineering bug, not a design decision or a Blueconic issue.

### 2.3 `headline-only` (text-only list item)

Used inside the "Latest Headlines" module (§2.4) and inside Section Highlight modules (§3).

**Size identical across all sites:** link text `15px / 600`, `line-height: 19px`, `color: #000`. Family follows `font/theme/small-headline-family` (Sans on Bold Coastal and Modern Earthy, Serif on Measured Vibrant — corrected 2026-09-24; this line previously said Noto Serif everywhere). Token: `Editorial/Titles/HeadlineList`.

Timestamp: separate `<time>` element, `13px / 400`, `color: rgb(93,91,90)` (~`#5D5B5A`), relative format ("1 hour ago").

**Divider between items:** real `border-bottom: 1px solid` on every `<li>` except the last one in the list (not a box-shadow trick, and not a border-*top*-on-every-item-except-the-first as this doc previously said — **mechanism corrected 2026-08-27**: verified by walking the DOM directly, it's `border-bottom` on the `<li>` wrapper, and the *last* item is the one with no border, not the first). Visually this produces the same result either way (a line between adjacent items, none after the last one), so nothing about the rendered page was wrong — just the CSS mechanism described here.

**Resolved 2026-08-27 — this is a clean, theme-scoped token, not a cross-site inconsistency.** Checked all 6 pilot sites: the divider color groups perfectly by *real* theme membership (not the originally-assumed, incorrect mapping — see Methodology in `design-vs-production.md`), with a third, distinct value for Modern Earthy now that Greeley Tribune and mcall.com have been checked:

| Theme | Sites | Divider color |
|---|---|---|
| Measured Vibrant | Chicago Tribune, Orlando Sentinel | `#C8C4C0` |
| Bold Coastal | Denver Post, OC Register | `#D7D6D2` |
| Modern Earthy | Greeley Tribune, mcall.com | `#DDD8D5` |

Each theme's two live representatives match exactly. No engineering action needed — this was only ever confusing because of the wrong site/theme mapping used earlier in this project; with the corrected mapping it's a straightforward per-theme token.

### 2.4 "Latest Headlines" module

A titled `ul` of `headline-only` items (`div.headline-list > h2.headline-list-title + ul`). The module title styling (same element as the Section Highlight title, §3) — size, weight, uppercase transform — is **theme-scoped, confirmed resolved 2026-08-27**, with a third, distinct Modern Earthy value now that Greeley Tribune and mcall.com have been checked:

| Theme | Sites | Size / weight / transform | Title text color (live) | Underline below title (live) |
|---|---|---|---|---|
| Measured Vibrant | Chicago Tribune, Orlando Sentinel | 17px / 700 / uppercase | Per-site brand `primary` (CT `#3F51B5`, OS `#1776C4` — turns out to literally be each site's own `--primary`, not just a similar-looking accent) | **None** — `border-bottom-width: 0px`, confirmed via computed style and a zoomed screenshot crop on Chicago Tribune |
| Bold Coastal | Denver Post, OC Register | 20px / 400 / uppercase | `#38322A` (flat, identical on both — not either site's own `primary`) | **None** — same `0px` |
| Modern Earthy | Greeley Tribune, mcall.com | 21px / 400 / uppercase | `#5D5B5A` (flat, identical on both — not either site's own `primary`) | **2px solid, each site's live `--primary`** — Greeley Tribune `#536E7F` (matches its documented `primary` exactly), mcall.com `#014B78` (matches mcall.com's live-rendered `--primary`, which is itself the already-flagged `primary`/`primary-dark` mismatch from `tokens/colors/color-tokens-decision-log.md` — this underline is just inheriting that existing bug, not a new one) |

So the size/weight/transform is a clean per-theme token — no engineering action needed, see §4.3. The *title text color and underline* used to be an open design question (§4.4) — **Karl decided it 2026-08-27:** every site's title text should be `color/gray/100` (`#393938`), and every site should have an underline below the title in that site's (or theme's) `--primary` color. Right now, no live site matches this spec on the text color, and only the two Modern Earthy sites have any underline at all (see §4.4 for the full gap list).

**Extended verification, 2026-09-01 (Karl's request) — theme-correlation confirmed beyond the 2-site pilot sample.** Even though the size/weight/transform split above was already resolved 2026-08-27, it rested on only 2 live sites per theme. Karl asked to check additional sites running Measured Vibrant specifically, sourced from the full "Sites Using This Theme" list on the Figma Colors page, to rule out coincidence. Checked 4 more Measured Vibrant sites beyond Chicago Tribune/Orlando Sentinel, using the `textTransform:uppercase` computed-style detection method: **all 4 match exactly** — `17px / 700 / uppercase`, `letter-spacing: 0.595px`.

| Site | Size / weight / transform | Letter-spacing | Title color observed |
|---|---|---|---|
| Santa Cruz Sentinel | 17px / 700 / uppercase | 0.595px | `rgb(63, 81, 181)` |
| Monterey Herald | 17px / 700 / uppercase | 0.595px | `rgb(63, 81, 181)` |
| San Diego Union-Tribune | 17px / 700 / uppercase | 0.595px | `rgb(63, 81, 181)` |
| Chico Enterprise-Record | 17px / 700 / uppercase | 0.595px | `rgb(63, 81, 181)` |

That brings Measured Vibrant's confirmed-matching sample to 6 sites (Chicago Tribune, Orlando Sentinel, plus these 4), all identical on size/weight/transform/letter-spacing — strong confirmation the split is a real per-theme token, not a per-site coincidence. One side-note worth flagging separately: all 4 newly-checked sites render the title in `rgb(63,81,181)` (`#3F51B5`) — Chicago Tribune's own `--primary` — rather than each site's own brand primary (§2.4's table shows Orlando Sentinel using its own `#1776C4`, for example). That suggests these 4 smaller sites may not carry their own Customizer color override and are falling back to a shared default, rather than each having distinct branding here. Not investigated further since it's moot either way once Karl's `color/gray/100` decision (§4.4) ships — flagging only as a residual curiosity, not a new open item.

Bold Coastal and Modern Earthy were not re-checked with additional sites this round — Karl's request was scoped to Measured Vibrant only. If the same extended-sample confirmation is wanted for the other two themes later, the same method applies.

**Superseded 2026-09-09 — eyebrows are per theme again (see note at top).** Historical: **Canonical decision, 2026-09-01 (Karl) — supersedes the "keep it themed" resolution above.** Given the strengthened evidence above, Karl decided the eyebrow/module-header title style should be standardized platform-wide on **Denver Post's (Bold Coastal's) numeric style**, not left as a 3-way per-theme token:

| Property | Canonical value | Source |
|---|---|---|
| Font size | `20px` | Denver Post / OC Register (Bold Coastal) |
| Font weight | `400` (Regular) | Denver Post / OC Register |
| Text transform | `uppercase` | unchanged, already universal |
| Letter-spacing | `0.7px` | Denver Post / OC Register |
| Line-height | `22px` | Denver Post / OC Register |
| Text color | `color/gray/100` (`#393938`) | already decided 2026-08-27, §4.4 — unchanged |
| Underline | `2px solid`, that site's own live `--primary` | already decided 2026-08-27, §4.4 — unchanged |
| Font-family | **unchanged** — stays each theme's own body font (Noto Sans on Measured Vibrant/Bold Coastal, Noto Serif on Modern Earthy) | this axis was never in dispute; only size/weight/letter-spacing/line-height are being unified |

This means Measured Vibrant (currently `17px/700/ls 0.595px`) and Modern Earthy (currently `21px/400/ls ~0.735px`) both need to change their numeric scale to match Bold Coastal's exactly — Bold Coastal itself is already at the target value and needs no size/weight change, only the text-color and underline fixes from §4.4. See §4.3/§4.4 for the consolidated live-gap table and the full per-site before/after values.

---

## 3. Sub-component: Section Highlight ("landing-item" / "section-highlight")

A composite curated-section widget, not a single card — e.g. "Politics" (CT), "Colorado News" (DP), "Crime and Public Safety" (OCR), "Local News" (OS), "Business" (GT), "Local News" (MC). Structure — **corrected 2026-08-27** to add one wrapper level this doc previously skipped:

- `section.section-highlight > h2.entry-title` (section name, styled identically to the "Latest Headlines" title — see §4) followed by `div.section-highlight-content`, which contains:
  - `div.section-feature` — a wrapper around **one `article.feature-medium`** (the section's top story; this wrapper `div` was missed in the previous version of this doc, which described `feature-medium` as a direct child of `.section-highlight-content` — it isn't, on any of the 6 sites checked)
  - A `ul.headline-list` of `article.headline-only` items (the section's next few stories — see item count note below)

So this widget is literally "reuse the feature-medium + headline-only variants inside a titled wrapper" — no new card design, just composition.

**Structural composition — fully resolved 2026-08-27, all 6 pilot sites now walked node-by-node** (this closes the last open piece of Open Item §9): Chicago Tribune, Denver Post, OC Register, Orlando Sentinel, Greeley Tribune, and mcall.com all build this widget with the exact same DOM shape — `section.section-highlight` → `h2.entry-title` + `div.section-highlight-content` → `div.section-feature` (wrapping one `article.feature-medium`, itself often also carrying the duplicate `feature-large` class per §2.2) + `ul.headline-list` of `article.headline-only` items. No structural divergence anywhere — Greeley Tribune and mcall.com (Modern Earthy) compose the widget identically to the other 4 sites.

**New finding while confirming this, 2026-08-27 — headline-list item count isn't uniform:** Denver Post's Section Highlight modules list **4** `headline-only` items ("Colorado News," "Politics," both checked) where every other pilot site lists **3** (Chicago Tribune, OC Register, Orlando Sentinel, Greeley Tribune, mcall.com — all checked, all exactly 3). This isn't theme-scoped — OC Register shares Denver Post's Bold Coastal theme file but still shows 3, matching everyone else — so it reads as a Denver Post–specific content/template setting, not a design or engineering split. Flagged for awareness; not yet root-caused, and not necessarily a bug (could be a deliberate per-site editorial choice, similar to the account-dropdown item-count difference already noted in `navigation.md`).

On the homepage these widgets appear inside a `div.landing-row.landing-four-up` grid (4 fixed-width ~296px columns), interleaved with standalone `feature-large` cards at the same width — this grid/interleaving pattern itself is a layout concern for the "Containers" component (next in the priority list), not the card itself.

---

## 4. Design tokens

### 4.1 Reused / confirmed global
- Hero headline: `29px / 700 / #000`, family follows the theme heading font — now tokenized as `Editorial/Titles/Title` (top of page) and `Editorial/Titles/TitleMedia` (media block). See `typography-tokens.md`.
- `headline-only` link: `15px / 600 / #000` — now tokenized as `Editorial/Titles/HeadlineList` (small-headline family, Sans on Bold Coastal).
- Timestamp: `13px / 400 / #5D5B5A` — identical on all 4 sites (not yet cross-checked on OCR/OS at the byte level, but visually and structurally identical).

### 4.2 ~~Resolved as design intent; confirmed as an engineering bug, isolated to Bold Coastal~~ — superseded 2026-09-24, not a bug (see note at top)
**`feature-medium` headline font-family is not an open design question anymore** — per Karl, Serif on Bold Coastal and Measured Vibrant, Sans on Modern Earthy, full stop (see §2.2). The token should be themed exactly like `color/theme/*` already is: one mode per theme, no per-site exceptions. What still needs engineering, not a design decision: **checked across all 6 pilot sites (2026-08-27), only Bold Coastal breaks this rule.** OC Register and Denver Post render the headline in Sans whenever the article also carries a duplicate `feature-large` class, when it should be Serif per the rule above. Chicago Tribune, Orlando Sentinel (Measured Vibrant), Greeley Tribune, and mcall.com (Modern Earthy) all comply on every instance checked, including their own duplicate-class instances — so this isn't a platform-wide issue, it's narrowly a Bold Coastal CSS bug.

**Added to `design-vs-production.md`'s "At a glance" table and Open Question #4 (2026-08-27, then updated twice same day).** Initially flagged for the Blueconic team; corrected to engineering; then, once Karl confirmed the actual per-theme rule and all 6 sites were checked, upgraded to a fully scoped, confirmed engineering bug on Bold Coastal only (OC Register, Denver Post).

### 4.3 ~~Open finding: the two "groups" don't line up with each other~~ — fully resolved 2026-08-27

For `headline-only` divider color and "Latest Headlines"/Section Highlight title style, the site groups are **{Chicago Tribune, Orlando Sentinel} vs {Denver Post, OC Register}**:

| | CT | OS | DP | OCR |
|---|---|---|---|---|
| Headline-list title | 17px/700, uppercase, accent color | 17px/700, uppercase, accent color | 20px/400, uppercase, `#38322A` | 20px/400, uppercase, `#38322A` |
| Divider color | `#C8C4C0` | `#C8C4C0` | `#D7D6D2` | `#D7D6D2` |

But for `feature-medium` headline typography (§2.2), the groups are **{Chicago Tribune, OC Register} vs {Denver Post, Orlando Sentinel}** — the opposite pairing from the table above.

This means these can't both be explained by a single "2 themes, 4 sites split cleanly" story (which would otherwise have been a tidy parallel to the Measured Vibrant / Bold Coastal nav-text-color split in `navigation.md` §5.2). Something is inconsistent at the per-component level rather than a clean theme switch. Recording this precisely rather than guessing which grouping is "correct" — this needs either an engineering answer or a deliberate design-system decision to normalize.

**Correction, 2026-08-27 (revised):** the theme mapping this section leaned on was wrong, and went through two versions before landing on the verified one. Originally assumed: Denver Post = Measured Vibrant, Orlando Sentinel = Bold Coastal. A note from a sibling conversation working on this same project then corrected Orlando Sentinel to Measured Vibrant (with its own color override) — that part holds up. It also described Denver Post as "bespoke, not a shared theme" — that part does **not** hold up: a live check of Denver Post's actual loaded stylesheet shows it uses `boldcoastal.css`, the same shared theme file as OC Register, with its own color override on top via the WordPress Customizer (same mechanism as every other one-off site, including Orlando Sentinel and Greeley Tribune) — not something categorically bespoke. Verified live, cross-checked against multiple sites, and confirmed via direct explanation from Karl of how the platform's CSS cascade actually works (theme file → SCSS override layer → Customizer override, in that order).

So, with the *actually correct* mapping — CT/OCR/DP all sharing an architecture (a shared theme file + Customizer override, DP and OCR each keeping their own), OS on Measured Vibrant with its own override — there still isn't a clean 2-theme split available to explain either grouping above. Real theme-file membership is CT=Measured Vibrant, OCR=Bold Coastal, DP=Bold Coastal, OS=Measured Vibrant — so DP and OCR actually *share* a theme file, which doesn't match either grouping's pairing (DP pairs with OCR in one table above, with OS in the other, with neither matching real theme membership). Both groupings above stand as genuinely unexplained per-component customization, not a theme artifact. See `design-vs-production.md` for the platform-wide typography finding this correction came out of — it also found something *not* broken here: type scale (size/weight/line-height) is a universal platform constant, and font family (separately from the two groupings above) really is theme-scoped, just not in a way that explains `feature-medium` or the divider/title split.

**Full resolution, 2026-08-27:** this mystery was actually two separate things wearing one write-up.

The *original* `feature-medium` grouping in this row (a single sample per site) is superseded by §2.2's instance-level finding — it isn't a per-site split, it's a per-instance one, tied to the duplicate `feature-large` class, and it's a confirmed engineering bug on OC Register and Denver Post specifically (see §2.2, §4.2).

The **divider-color / headline-list-title grouping** ({CT, OS} vs {DP, OCR}) is a genuinely different element (§2.3-§2.4, the module title and list divider, not the headline) — and once Greeley Tribune and mcall.com were checked too (2026-08-27), it turned out to be **exactly explained by real theme membership**: {CT, OS} = Measured Vibrant, {DP, OCR} = Bold Coastal, and Greeley Tribune/mcall.com (Modern Earthy) supply a clean third value that matches neither. The paragraph above claiming this "doesn't match either grouping's pairing" was simply wrong — it is a perfect match once you use the *corrected* mapping (DP and OCR really do share Bold Coastal; CT and OS really do share Measured Vibrant). **Divider color stays a themed token as-is (§2.3) — that part of this resolution still stands, no engineering action needed there.** But the *headline-list-title size/weight* half of this resolution was superseded 2026-09-01 — see §2.4's "Canonical decision" callout and §4.4's updated gap table below: rather than keeping 3 per-theme size/weight values, Karl decided to standardize every theme on Bold Coastal's numeric style. The only piece that's still a genuine open question is nothing — text color and underline were decided 2026-08-27 (§4.4), and size/weight was decided 2026-09-01 (§2.4) — this whole title-style question is now fully closed as a design decision; what remains is purely an engineering build-out (see §4.4's gap table).

### 4.4 ~~Section-title style (accent color, size/weight, underline)~~ — fully decided by Karl, 2026-08-27 + 2026-09-01

`navigation.md` §2.4 documented OC Register's section-front title color as **teal**. The Section Highlight / Latest Headlines title on OC Register's homepage, however, computes to `rgb(56,50,42)` / `#38322A` — a neutral brown, not teal. So the "brand accent color" is not a single reusable value even within one site; it depends on which module you're looking at. Chicago Tribune, by contrast, does reuse the same blue-purple (`#3F51B5`) for both its nav section-front title (per `navigation.md`) and its homepage headline-list title. Not yet resolved which sites/components share a token and which don't — flagging rather than assuming.

**Widened, 2026-08-27:** now that all 6 sites have been checked (§2.4), this isn't just an OC Register quirk. Denver Post shares OC Register's exact `#38322A` (not a per-site brand color at all), and Greeley Tribune/mcall.com share their own exact `#5D5B5A` between each other too. Measured Vibrant's two sites (Chicago Tribune, Orlando Sentinel) turned out to be using their own `--primary` directly as the title text color.

**Decision, 2026-08-27 (Karl):** every site's title text should be `color/gray/100` (`#393938`), and every site should have an underline below the title in that site's/theme's `--primary` color. Per Karl: "the design on Bold Coastal is better" — i.e. the calmer, more restrained typographic treatment (larger, regular-weight, neutral-colored) — but the actual color values on *every* site still need to change to match this spec.

**Decision, 2026-09-01 (Karl) — extended to size/weight too.** Following the extended Measured Vibrant verification (§2.4), Karl decided to go all the way and make the *entire* title style match Denver Post/Bold Coastal, not just color: size `20px`, weight `400` (Regular), letter-spacing `0.7px`, line-height `22px`, on every theme — see §2.4's "Canonical decision" callout for the full value table. This supersedes §4.3's earlier "keep size/weight themed, no engineering action needed" call. Font-family is unaffected — it stays each theme's own body font.

**Current live gap, re-verified 2026-09-01 against the full canonical spec (size/weight + color + underline):**

| Site | Theme | Size/weight/letter-spacing now | Target | Text color now | Target | Underline now | Target |
|---|---|---|---|---|---|---|---|
| Chicago Tribune | Measured Vibrant | 17px/700/0.595px | 20px/400/0.7px | `#3F51B5` (its own `primary`) | `#393938` | None | 2px, `#3F51B5` |
| Orlando Sentinel | Measured Vibrant | 17px/700/0.595px | 20px/400/0.7px | `#1776C4` (its own `primary`) | `#393938` | None | 2px, `#1776C4` |
| OC Register | Bold Coastal | 20px/400/0.7px — **already matches** | 20px/400/0.7px | `#38322A` (shared, not its own `primary`) | `#393938` | None | 2px, `#007580` (its documented `primary`) |
| Denver Post | Bold Coastal | 20px/400/0.7px — **already matches; this is the reference site** | 20px/400/0.7px | `#38322A` (shared, not its own `primary`) | `#393938` | None | 2px, `#8E1024` |
| Greeley Tribune | Modern Earthy | 21px/400/~0.735px | 20px/400/0.7px | `#5D5B5A` (shared, not its own `primary`) | `#393938` | 2px, `#536E7F` — already correct mechanism | Keep mechanism; size/color still need the fix above |
| mcall.com | Modern Earthy | 21px/400/~0.735px | 20px/400/0.7px | `#5D5B5A` (shared, not its own `primary`) | `#393938` | 2px, `#014B78` | Keep the mechanism, but this inherits the still-open `primary`/`primary-dark` mismatch from `tokens/colors/color-tokens-decision-log.md` — once that's fixed, this underline will pick up the corrected value automatically since it's already reading live `--primary` |

Re-verified live 2026-09-01 with a precise `h2.headline-list-title` selector (a looser selector used briefly earlier in this same session picked up decoy sibling elements on a couple of sites and produced false readings — caught and corrected before writing this table). All 6 rows above match the 2026-08-27 findings exactly; nothing has shipped to production yet.

So: text color needs to change on all 6 sites, no exceptions. Size/weight/letter-spacing needs to change on the 4 non-Bold-Coastal sites (Chicago Tribune, Orlando Sentinel, Greeley Tribune, mcall.com) — OC Register and Denver Post are already at the target numeric style. The underline needs to be *added* on 4 sites (Chicago Tribune, Orlando Sentinel, OC Register, Denver Post) — it doesn't exist there at all today. Greeley Tribune and mcall.com already have the right underline *mechanism* (a real border reading live `--primary`) and don't need engineering changes for the underline itself, only size and text color.

### 4.5 New tokens needed for build (not yet modeled)
- Excerpt/dek color `#484642` (approx, from CT sample) — needs re-verification, rounding was imprecise on this read
- Three divider colors, one per theme, confirmed 2026-08-27 (§2.3, §4.3): Measured Vibrant `#C8C4C0`, Bold Coastal `#D7D6D2`, Modern Earthy `#DDD8D5`. No longer pending — ready to model as a themed token.
- Section Highlight / headline-list title — *size/weight superseded 2026-09-09 by per-theme eyebrow tokens; color and underline still stand.* Historical: **fully decided 2026-09-01**, superseding the earlier "3-way themed token" note: one canonical size/weight/letter-spacing/line-height (20px/400/0.7px/22px, matching Denver Post/Bold Coastal) on every theme, not a per-theme value (§2.4). Title *text color* (`color/gray/100`/`#393938`) and *underline* (2px, site/theme `--primary`) were decided 2026-08-27 and stand unchanged (§4.4). None of this is live-correct on any of the 6 pilot sites yet except the underline *mechanism* on the 2 Modern Earthy sites, and the size/weight on the 2 Bold Coastal sites (which are the reference values).

---

## 5. Open items

1. ~~feature-medium headline typography split (serif/26px vs sans/19px) — needs a canonical decision~~ — **Superseded 2026-09-24: Sans on Bold Coastal at 19px is the design rule, not a bug.** Historical: **resolved as a design question, confirmed and fully scoped as an engineering bug, 2026-08-27.** Per Karl: Serif on Bold Coastal & Measured Vibrant, Sans on Modern Earthy, no exceptions. Checked across all 6 pilot sites: only Bold Coastal (OC Register, Denver Post) violates this — see §2.2, §4.2. Flagged in `design-vs-production.md` (initially mis-flagged as a Blueconic issue, corrected to engineering same day). The universal size/weight change tied to the duplicate `feature-large` class (26/700 → 19/600, on all 6 sites) is a separate, likely-intentional behavior, not part of this bug.
2. ~~Cross-cutting inconsistency between the two "site groupings" found in this component vs. each other~~ — **fully resolved 2026-08-27**, see §4.3. Both halves are now explained: the `feature-medium` half is the Bold Coastal engineering bug (item 1); the divider-color/headline-list-title half is a clean, correctly-functioning per-theme token once checked against the corrected theme mapping and a third (Modern Earthy) data point.
3. ~~Section-title accent color doesn't consistently match the nav's documented section-front accent color~~ — **Size/weight part superseded 2026-09-09 (per-theme eyebrows); color and underline still stand, tracked in design-vs-production 4.2.** Historical: **fully decided, 2026-08-27 + 2026-09-01** (see §4.4). Karl's call: title text = `color/gray/100` (`#393938`) on every site; underline below the title = that site's/theme's `--primary`, also on every site; and (added 2026-09-01) size/weight/letter-spacing = Denver Post's Bold Coastal values (20px/400/0.7px) on every theme too, not a per-theme value. Live gap: text color and size/weight are wrong on all 4 non-Bold-Coastal sites (Chicago Tribune, Orlando Sentinel, Greeley Tribune, mcall.com) and text color alone is wrong on OC Register/Denver Post (their size/weight already matches); the underline itself doesn't exist yet on 4 of 6 (Chicago Tribune, Orlando Sentinel, OC Register, Denver Post) — Greeley Tribune and mcall.com already have the right underline mechanism. Ready to hand to engineering as a concrete, fully-specified spec — no design decisions remain open on this component's title style.
4. ~~Hero's second, empty `<figure>` in the header~~ — **resolved**, see §2.1.1: it's the mobile-width image duplicate, not a paywall/lock icon slot.
5. ~~Mobile/narrow-viewport stacking behavior~~ — **fully resolved**, see §2.1.1. Breakpoint = 40em/640px, confirmed by source on CT+DP and live-tested at 375px on all 4 pilot sites — identical behavior everywhere, no per-site variation.
6. Excerpt/dek color needs a precise re-check (see §4.5) — the rgb→hex rounding done in this pass wasn't double-verified the way other colors in this doc were.
7. ~~OC Register and Orlando Sentinel's Section Highlight modules were confirmed to exist (same classes present) but not walked node-by-node~~ — **resolved 2026-08-27**, see §3: walked node-by-node on all 6 pilot sites now, identical structure everywhere (including the `div.section-feature` wrapper this doc had previously omitted). Surfaced one new, unrelated finding in the process — Denver Post's headline-list item count (4) doesn't match the other 5 sites (3) — see §3.
8. `feature-medium`'s and `headline-only`'s responsive rules turned out to vary by parent container context (e.g. `.landing-four-up-hybrid`, `.landing-three-one`, `.slow .feature-top` all have their own breakpoint-specific `flex-direction` overrides for the same classes) — this is genuinely complex and overlaps with the upcoming Containers component. Not fully mapped here; flagging so it isn't mistaken for a single universal rule.
9. ~~Greeley Tribune and mcall.com (Modern Earthy) haven't been audited for this component at all~~ — **fully resolved 2026-08-27.** Both sites' `feature-medium` headlines (§2.2), their divider-color/headline-list-title values (§2.3–§2.4), and Section Highlight's structural composition (§3) have now all been checked and are accounted for — both comply with the confirmed rules, both supplied Modern Earthy's third, distinct theme value everywhere a 3-way split applies, and both build the Section Highlight widget with the identical DOM structure used on the other 4 sites. Nothing left open on Greeley Tribune/mcall.com for this component.

---

## 6. Methodology notes

- All page loads given a minimum 10-second wait before scraping, per standing project rule.
- Findings based on `getComputedStyle` and DOM-structure walks (parent/child relationships, class names), not screenshot inference — consistent with the Navigation audit's approach.
- Color values reported as both the browser's computed `rgb()` and a converted hex; where a conversion might be imprecise, flagged explicitly rather than presented as exact (see §4.5, §5.6).
- This pass covered homepage instances only. Section-front and article-page teaser instances (e.g. "More from this section" modules) were not audited — likely reuse the same `feature-medium`/`headline-only` variants, but not confirmed.
- **Standing rule, added 2026-08-28 (Karl):** any mobile/screen-size testing this component needs going forward gets prompted to Karl to set up manually (real device profile in his own Chrome DevTools), not done via this session's own browser-resize tooling — see `design-vs-production.md`'s Methodology section and `navigation.md` §7 for why (a plain resize doesn't spoof the device signals some site behavior actually reads).
