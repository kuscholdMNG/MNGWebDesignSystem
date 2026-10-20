# Typography Tokens

> **Updated 2026-09-24.**
> - Every token and value in this doc was re-checked against the live Figma variables on 2026-09-24 and matches.
> - Modern Earthy eyebrow is now **confirmed**, not a placeholder. See §3.
> - **Added 2026-09-24:** 7 new Editorial styles (card tiers, headline list, related headline, lead-story media variant, body copy) and a new theme token, `font/theme/small-headline-family`. Measured live the same day on 7 sites.
> - History and reasoning live in `typography-decision-log.md` (this folder). Known Figma-vs-production gaps live in `design-vs-production.md` (repo top level).

**Status:** Built in Figma Variables in the MNG Web Design System file: collections Type Primitives, Typeography Tokens (collection name is misspelled in Figma), Typography Theme and Dashboard Typography. This doc is the reference for the current token catalog: names, values and where each came from.

**Structure:** Type Primitives (raw values) → Editorial + Shared composites in "Typeography Tokens" (theme-aware through the Family property) → Dashboard composites in "Dashboard Typography" (fixed, not theme-aware; Reader Dashboard only).

---

## 1. Type Primitives collection

Single "Mode 1": one flat value per token, used by everything below.

### Font family

| Variable | Value |
|---|---|
| `font/family/noto-sans` | `"Noto Sans"` |
| `font/family/noto-serif` | `"Noto Serif"` |

In Figma the variables hold bare family names. In code (`tokens/core/typography.tokens.json`, `dist/`) each family carries the CSS stack from the Fonts page (Font Styles and Fallbacks, `2768:1051`, condensed 2026-10-14): `"Noto Sans", "Helvetica Neue", Arial, sans-serif` and `"Noto Serif", Georgia, "Times New Roman", serif`. Every theme uses these two stacks; obituaries follow the site's theme. Production currently falls back to Helvetica on both (`"Noto Sans", Helvetica, sans-serif` / `"Noto Serif", Helvetica, serif`).

### Font size

| Variable | Value | Note |
|---|---|---|
| `font/size/10` | 10px | Ported from Reader Dashboard v2.0. Not yet seen live. Reader Dashboard only. |
| `font/size/11` | 11px | Related-article timestamp under the Top Zone lead (`.primary-related li time`, 400, line height 20.625). Confirmed live 2026-10-08. |
| `font/size/12` | 12px | Utility/chip label size, measured live. Also the footer copyright size. |
| `font/size/13` | 13px | Small button / caption size, measured live. Matches CRUX `xs`. |
| `font/size/14` | 14px | Medium/primary button label (~14.06px measured live). |
| `font/size/15` | 15px | Primary nav-bar label (600, Noto Sans, not theme-varying) and the Section Highlight headline list (`HeadlineList`). Confirmed live. |
| `font/size/15-2` | 15.2px | Article breadcrumb type-of-work label and its " • " bullet (400, line height 15.2). Confirmed live 2026-10-08; production renders it in Helvetica (design-vs-production entry 6). |
| `font/size/16` | 16px | Reader Dashboard body, nav items, card subtitles/links. **Not** the editorial body size (see `16-5`). |
| `font/size/16-5` | 16.5px | Universal editorial body copy. Confirmed live on all 6 audited sites/themes. |
| `font/size/18` | 18px | Reader Dashboard Section Title and the article-page "More News" headlines (`RelatedHeadline`). Confirmed live. |
| `font/size/19` | 19px | Large/full-width CTA button label (~19.2px measured live) and the fourth-tier card headline (`CardQuaternary`). |
| `font/size/20` | 20px | Homepage module header (600) and the third-tier card headline (`CardTertiary`, 700). Both follow `font/theme/heading-family`. Not the eyebrow; the eyebrow uses `font/theme/eyebrow-*` (§3). |
| `font/size/21` | 21px | Most Popular / Recommended rank number (600, line height 32). Confirmed live 2026-10-08. |
| `font/size/23` | 23px | Article deck/subhead. Confirmed live across all sites/themes. |
| `font/size/24` | 24px | Reader Dashboard profile display name (confirmed live). No confirmed editorial use. |
| `font/size/25` | 25px | Top Zone lead headline below 640px (700, line height 29, −0.03em). Confirmed in production CSS 2026-10-08. |
| `font/size/26` | 26px | Second-tier homepage headline card. Confirmed live across all sites/themes. |
| `font/size/29` | 29px | Lead-story homepage card headline. |
| `font/size/31` | 31px | Article headline below 640px (700, line height 34.1, −0.03em; 32 / 36.8 at 640–1039px, 36 / 41.4 at 1040px+). Confirmed in production CSS 2026-10-08. |
| `font/size/36` | 36px | Article H1 / main headline. Confirmed live across all sites/themes. |
| `font/size/40` | 40px | Section-front page H1 (e.g. a category page's "Sports" heading). Confirmed live on ocregister.com/sports/ and chicagotribune.com/sports/ (`class="section-header"`). Not a kicker/category label, which is 16px/700/uppercase. |

### Font weight

| Variable | Value | Note |
|---|---|---|
| `font/weight/regular` | 400 | |
| `font/weight/medium` | 500 | Confirmed live on article deck/subhead text. |
| `font/weight/semibold` | 600 | Confirmed live on headline tiers and module headers. |
| `font/weight/bold` | 700 | |

---

## 2. Editorial & Shared composites ("Typeography Tokens" collection)

Single "Mode 1". Theming happens through the `Family` property, which aliases the theme-aware "Typography Theme" collection (§3). Size, weight, line height and letter spacing are the same across all shared themes; only Family varies.

### Editorial/Titles/Display: Article H1

| Property | Value |
|---|---|
| Family | → `font/theme/heading-family` |
| Size | 36px |
| Weight | → `font/weight/bold` (700) |
| Line height | 41.4px |
| Letter spacing | -1.08 |

### Editorial/Titles/Title and TitleMedia: lead-story homepage headline

Production uses two versions of the 29px lead-story headline, so there are two styles. Both use the heading family, 29px (`font/size/29`) and weight 700. Before 2026-09-24, Title used an averaged -1.0 letter spacing, which matched neither.

| Style | Where | Line height | Letter spacing |
|---|---|---|---|
| `Editorial/Titles/Title` | Top of the homepage (feature-large in feature-primary) | 32.8px | -0.87 |
| `Editorial/Titles/TitleMedia` | Homepage media block (feature-large in feature-media) | 33px | -1.16 |

### Homepage card tiers, headline list and related headlines (added 2026-09-24)

All use the size and weight primitives. Line height and letter spacing are stored as numbers. Measured live 2026-09-24, identical on ocregister, denverpost, chicagotribune, orlandosentinel, canoncitydailyrecord, mcall and greeleytribune.

| Style | Where | Family | Size | Weight | Line height | Letter spacing |
|---|---|---|---|---|---|---|
| `Editorial/Titles/CardSecondary` | Section Highlight, feature-medium | heading-family | 26 | 700 | 30.3 | -0.91 |
| `Editorial/Titles/CardTertiary` | Top-of-page block, feature-small | heading-family | 20 | 700 | 23.6 | -0.4 |
| `Editorial/Titles/CardQuaternary` | Section Highlight, feature-medium + feature-large | small-headline-family | 19 | 600 | 24 | -0.665 |
| `Editorial/Titles/HeadlineList` | Section Highlight headline-only list (most common headline on the page) | small-headline-family | 15 | 600 | 19 | -0.15 |
| `Editorial/Titles/RelatedHeadline` | "More News" list on article pages | heading-family | 18 | 600 | 21 | 0 |

CardTertiary (20/700) is not the module header (`Editorial/ModuleHeader`, 20/600). They're different elements that share a size.

### Editorial/Body/Default: article body copy (added 2026-09-24)

| Property | Value |
|---|---|
| Family | → `font/theme/body-family` |
| Size | → `font/size/16-5` |
| Weight | → `font/weight/regular` (400) |
| Line height | 27px |
| Letter spacing | -0.165 |

### Editorial/Titles/Subtitle: article deck/subhead

| Property | Value |
|---|---|
| Family | → `font/theme/heading-family` |
| Size | 23px |
| Weight | 500 (Medium) |
| Line height | 29.9px |
| Letter spacing | -0.529 |

Note: Figma's font list has no Noto Serif Medium, so Figma mockups of this token on serif themes render at Regular. Production uses a variable font that supports true 500.

### Editorial/Titles/SectionHeader: section-front page H1

Replaces CRUX's `sectionH1` and `mastheadSectionH1` (identical duplicates at 40/700).

| Property | Value |
|---|---|
| Family | → `font/theme/heading-family` |
| Size | 40px |
| Weight | → `font/weight/bold` (700) |

### Editorial/Navigation/PrimaryLabel: primary site nav-bar label

Confirmed live 2026-09-10 on all 6 repertoire sites; not theme-varying.

| Property | Value |
|---|---|
| Family | Noto Sans (flat) |
| Size | → `font/size/15` |
| Weight | → `font/weight/semibold` (600) |

### Editorial/ModuleHeader: homepage module header

The visible bold header on a homepage widget. Different from the theme eyebrow. Confirmed live 2026-09-10 on all 6 repertoire sites.

| Property | Value |
|---|---|
| Family | → `font/theme/heading-family` |
| Size | → `font/size/20` |
| Weight | → `font/weight/semibold` (600) |

Each site also has a 30px/600 `h2` in the same spot, but it's a screen-reader-only (visually hidden) label, so it is deliberately not a token.

### Editorial/Footer/Copyright: footer copyright/legal line

Confirmed live 2026-09-10 on all 6 repertoire sites (~12.48px measured); not theme-varying.

| Property | Value |
|---|---|
| Family | Noto Sans (flat) |
| Size | → `font/size/12` |
| Weight | → `font/weight/regular` (400) |

### Shared/Buttons: button label sizes (not theme-aware)

Measured live from production buttons.

| Variable | Value | Use |
|---|---|---|
| `Shared/Buttons/Utility/Size` | → 12px | Utility/chip label |
| `Shared/Buttons/Small/Size` | → 13px | Small button label |
| `Shared/Buttons/Medium/Size` | → 14px | Medium/primary button label |
| `Shared/Buttons/Large/Size` | → 19px | Large/full-width CTA button label |

---

## 3. Typography Theme collection

Modes: Bold Coastal, Modern Earthy, Measured Vibrant. Feeds the `Family` properties in §2 and holds the eyebrow tokens.

`font/theme/small-headline-family` (added 2026-09-24) is for the 19px and 15px homepage headlines. On Bold Coastal these are sans even though its heading family is serif, so they can't use `heading-family`. Confirmed live 2026-09-24 on all 7 sites checked.

| Variable | Bold Coastal | Modern Earthy | Measured Vibrant |
|---|---|---|---|
| `font/theme/heading-family` | Noto Serif | Noto Sans | Noto Serif |
| `font/theme/body-family` | Noto Sans | Noto Serif | Noto Sans |
| `font/theme/small-headline-family` | Noto Sans | Noto Sans | Noto Serif |
| `font/theme/eyebrow-size` | 20px | 21px | 17px |
| `font/theme/eyebrow-weight` | 400 | 400 | 700 |
| `font/theme/eyebrow-family` | Noto Sans | Noto Serif | Noto Sans |

**Confidence:**
- Bold Coastal eyebrow: confirmed live on ocregister.com and denverpost.com.
- Measured Vibrant eyebrow: confirmed live on chicagotribune.com and orlandosentinel.com.
- Modern Earthy eyebrow: **confirmed** (updated 2026-09-24). 21px/400/Noto Serif was measured live on mcall.com and canoncitydailyrecord.com. Both load `modernearthy.css`, and Cañon City Daily Record is a Prairie Mountain Publishing site.
- PMP sites (all 19) load `modernearthy.css`, so they use the **Modern Earthy** typography column. The PMP color override changes colors only.
- Morning Call is not a theme. It's a site (mcall.com) that runs Modern Earthy with its own color override.
- `heading-family` / `body-family`: confirmed live across all 6 sites, 2026-08-27. The pairing is reversed on Modern Earthy, the only theme where the heading is sans.
- The eyebrow family doesn't always follow `heading-family`. On Modern Earthy the heading is Noto Sans but the eyebrow is Noto Serif.

---

## 4. Dashboard Typography collection

Single mode, **not theme-aware**. Mirrors Reader Dashboard v2.0's own Figma tokens exactly and renders the same on every site. Family properties alias the flat `font/family/*` primitives (§1), never the theme tokens in §3. For anything Reader Dashboard-specific, **Figma is the source of truth, even where production differs.**

| Token | Family | Size | Weight | Notes |
|---|---|---|---|---|
| `Dashboard/Titles/PageDesktop` | Noto Serif | 26px | 700 | Matches Reader Dashboard v2.0's Figma token. Production shows 36px at desktop; see `design-vs-production.md`. |
| `Dashboard/Titles/PageMobile` | Noto Serif | 26px | 700 | Matches production at mobile/tabletV/Fold breakpoints. |
| `Dashboard/Titles/SectionTitle` | Noto Sans | 18px | 700 | One live instance measured 600, probably an admin panel; see `design-vs-production.md`. |
| `Dashboard/Titles/SubtitleLabel` | Noto Sans | 14px | 700 | |
| `Dashboard/Titles/SubtitleValue` | Noto Sans | 14px | 400 | |
| `Dashboard/NavMenuItems/Default` | Noto Sans | 16px | 400 | |
| `Dashboard/NavMenuItems/InFocus` | Noto Sans | 16px | 700 | |
| `Dashboard/Card/Title` | Noto Sans | 18px | 700 | |
| `Dashboard/Card/Subtitle` | Noto Sans | 16px | 400 | |
| `Dashboard/Card/HelperText` | Noto Sans | 14px | 400 | |
| `Dashboard/Card/Footnote` | Noto Sans | 12px | 400 | |
| `Dashboard/Card/Links` | Noto Sans | 16px | 400 | |
| `Dashboard/Card/SubscriberBadge` | Noto Sans | 12px | 600 | Also raw LetterSpacing 10% and LineHeight 22.7px (no shared primitive). |
| `Dashboard/Body/Default` | Noto Sans | 16px | 400 | |

`font/size/10` (§1) is also Reader Dashboard-only. No composite uses it yet and it hasn't been seen live.

---

## 5. Open items / known gaps

1. **Most tokens are a reference catalog, not yet applied to layers.** As of the 2026-09-09 audit, no font-size primitive (and most composites) were bound to any real text layer in the file.
2. **CRUX Style Library is never edited.** Standing rule from Karl (2026-09-10): no edits, aliases or deletions in CRUX. Its font tokens stay as reference only, and its fallback-stack mismatch (§1) stays a permanent difference.
3. ~~Line height and letter spacing were confirmed only on serif themes.~~ **Resolved 2026-09-24:** Modern Earthy (mcall.com, canoncitydailyrecord.com, greeleytribune.com) uses exactly the same line height and letter spacing as the serif themes on every headline tier checked.
4. **`font/size/24` has weak editorial use** (one uncertain sighting). It's kept for its confirmed Reader Dashboard use.
5. See `design-vs-production.md` for every known place production differs from these values.
