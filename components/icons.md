# Icon Font

> **Updated 2026-10-22:** production names win, always (Karl). Icons are now named by their production class everywhere (`home` → `home3`, `menu7` → `hamburger`, `enlarge7` → `enlarge`, "iTunes / Apple Music" → `music5`), with the IcoMoon name kept for finding the original artwork; the `notification` / `notification2` change is new artwork under the same names, not two new icons; 7 more IcoMoon icons joined the ADD list. See §7. This supersedes the "doc name is stale" recommendations in §3 and §5.

> **Updated 2026-10-08:** the production font is now in `tokens/icons/` (all sites use the same font) and was re-checked against the Figma Icon Categories page; current mismatches and known missing icons are in design-vs-production entry 1. Earlier history below. Current project status is in `MNG-Web-Design-System-Status.md`.

**Status:** Documentation source established; live-vs-documented name audit complete (Chicago Tribune). Figma `Icons` COMPONENT_SET (95 variants) audited and visually cross-checked against live glyphs, 2026-08-28 (see §6). Every finding from that audit walked through a live Figma + site side-by-side review with Karl, 2026-08-31 — all open items resolved (see §5). Remaining-site cross-check and full page-by-page usage audit still not done.
**Source (live):** Chicago Tribune, desktop, sitewide (icomoon icon font, embedded via `@font-face` in the shared theme's `measuredvibrant.css`)
**Source (internal, authoritative):** main MNG Web Design System file (`jFHYqhZbJjvWQmDI4myCsd`) → **"Alerts and Icons" page** → **"Proposed MNG Icon Set"** frame (`6106:4866`), the icon documentation Karl copied by hand. The 95-variant `Icons` COMPONENT_SET (`4693:5`) is on the file's Icons page (now "Icons | 2026.08.28").

---

## 1. Source of truth — what changed

An earlier pass in this project started rebuilding the icon reference sheet programmatically. **Karl deleted that build and hand-copied the documentation himself.** The hand-copied "Proposed MNG Icon Set" is now the authoritative reference for what should be in production — not anything built automatically. The 95-variant icon COMPONENT_SET was left in place and audited separately (§6).

---

## 2. What's documented ("Proposed MNG Icon Set", Alerts and Icons page)

The hand-copied documentation organizes the icon font into six categories, plus a few non-category sections:

- **User Interface** — ~41 entries (close, arrows, plus/minus, zoom, enlarge/shrink, checkmarks, menu, search, notifications, warnings, etc.)
- **Account Management** — 29 entries (cog, pen6, eye/eye-blocked, bells, users, cart, bookmarks, hearts, thumbs, stars, etc.)
- **Multimedia** — 19 entries (camera, slideshow, film4, playback controls, volume controls, etc.)
- **Engagment** [sic, as labeled on the page] — 21 entries (paperplane, share variants, print, sms, link/unlink, comments, email, gift-share, save/upload/download, phone, attachment)
- **Social Media / Brands** — 27 entries (amazon, android, appleinc, bluesky, facebook, google/google-color, instagram, linkedin, paypal, pinterest, podcast, reddit, soundcloud, spotify, stitcher, stumbleupon, stackoverflow, threads, tumblr, x/twitter, vimeo, windows8, yelp, youtube)
- **Decoration** — ~34 entries (home, office, city, store/graduation, library, flower, tree, access-time.svg, key, bin, meter, magazine, mobile, calendar, padlock, book, quill, unlocked, location, map, piggy-bank, dollar/coin-dollar, newspaper, credit-card, checkmark-circle, radio-unchecked)

Plus three non-icon-font sections, correctly kept separate from the six categories above:

- **PENDING UPDATES** — an ADD list (plus-circle, plus-circle2, minus-circle, minus-circle2, list, grid, crown, giving-hand, yield-filled, yield-outline — not yet in the font), a CHANGE list (mostly "none at this time," with a notification-icon variant noted as under consideration), and a REMOVE list ("none at this time").
- **NEED TO SOURCE/MAKE/ADD** — identified future needs not yet in the font: Obituary, Funeral Home, Find Your School.
- **"Not in Icon Font set"** — explicitly *not* icon-font glyphs: mouse-pointer cursor components, a link to the separate Newspaper Logos/Favicons Figma file, and payment-method badges (Apple Pay, Google Pay). Correctly excluded from the icon-font audit.

The page's usage-note convention: names in **blue** = modified from the source pack or built in-house; names in **struck-through red** = removed from the icon set; "DO NOT USE" = slated for removal.

---

## 3. Live-vs-documented name audit (Chicago Tribune, sitewide CSS)

**Method:** scanned every loaded stylesheet's CSS rules for custom properties matching `--icon-*` on `:root`. Found **174 unique names**, matching the count from the earlier live-site pass. Compared that list directly against the 171 unique names documented across the six categories above (the three non-font sections are excluded from this comparison on purpose).

**166 of 174 live names match a documented name exactly.** Eight names don't line up cleanly:

| Live CSS name | Documented as | What's going on |
|---|---|---|
| `hamburger` | *(not documented anywhere)* | Confirmed in active use (off-canvas panel trigger, per `navigation.md` §3). Missing from the "User Interface" category entirely. |
| `home3` | Doc has `home` (Decoration), not `home3` | Confirmed in active use (Off-Canvas Panel Home Page row, per `navigation.md` §3). The doc's `home` entry doesn't exist in the live font at all — looks like the doc name is stale and should read `home3`. |
| `home` (documented) | — | Not found live under this name. See row above — likely should be `home3`. |
| `menu7` (documented, "– Sections menu") | — | Not found live under this name. The live off-canvas trigger actually uses `hamburger` (see above), not `menu7`. This doc entry looks stale/mislabeled. |
| `enlarge` | Doc has `enlarge7`, not `enlarge` | **Resolved, 2026-08-31.** Confirmed via live-render comparison on Chicago Tribune (live `enlarge` vs. the Figma `enlarge7` entry) that both render the same "expand/fullscreen" glyph — arrows pointing outward toward the four corners. Same naming-mismatch pattern as `home`/`home3` and `menu7`/`hamburger`: the doc's `enlarge7` entry isn't missing, it's misnamed and should read `enlarge`. `shrink7` still matches live-to-doc cleanly, so this was an isolated naming mismatch on the "enlarge" side only, not a missing pair. Documentation-naming fix only, no engineering action. |
| `pinterest-p` | Documented as `pintrest-p` | **Fixed, 2026-08-31.** Simple spelling typo — corrected directly on the Figma page (`pintrest-p` → `pinterest-p`) per Karl. Not a real mismatch. |
| `google-plus` | *(not documented anywhere)* | **Confirmed dead weight, 2026-08-31.** Present in the live font, not documented. Google+ has been shut down for years; logged for engineering as a font-cleanup candidate (design-vs-production entry 1) rather than added to the documented categories. |
| `mng-podcast1` | *(not documented anywhere)* | Present live, undocumented. Per the earlier live-site pass, this shares the same codepoint (`e902`) as `android` — looks like a font-build duplicate/alias, not a distinct icon. |
| `users4` | *(not documented anywhere)* | **Ignored per Karl, 2026-08-31.** Present live (defined in the font's CSS) and also confirmed missing from the Figma component set (§6.5). Checked for actual rendered usage on Chicago Tribune's homepage, About Us page, and an article page — no live instance found anywhere; only the generic font-definition CSS rule every icon gets automatically. Karl elected to drop this from further review. |

Two more notes, not counted as mismatches:
- `Threads` (doc, capitalized) vs `threads` (live) — cosmetic case difference only, real match.
- `new-tab` — the doc shows this name in **struck-through red** ("removed from our icon set") with a quoted `"new-tab"` entry in blue next to it as the apparent replacement. Live CSS still defines `--icon-new-tab` under that exact name. **Resolved, 2026-08-31 — Karl said to ignore this one, no further action needed.**

**Everything in the PENDING UPDATES "ADD" list and the "NEED TO SOURCE/MAKE" list was confirmed still absent from the live font** — consistent with the doc marking them as not-yet-shipped.

**Not yet done:**
- This audit only checked Chicago Tribune's loaded CSS. Per your earlier instruction to skip cross-site checks once something's confirmed the same across the four pilot sites, I haven't independently re-verified this icon list against Denver Post / OC Register / Orlando Sentinel — flagging in case you want that checked before treating these findings as sitewide-confirmed across all four.
- This is a **name-level** audit only (does the CSS custom property exist). It does not check whether the actual glyph shape drawn in Figma matches the live rendered icon, and it doesn't check *where on the site* each icon is actually used (beyond the handful already confirmed via the off-canvas panel work: `hamburger`, `home3`, `search`, `arrow-down`, `plus`, `slideshow`).

---

## 4. Comparison notes

During the audit, a working copy of the documentation ("Icons comparisons") carried a red "⚠" note and live glyph captures next to each discrepancy: `home`, `menu7`, `enlarge7`, `pintrest-p` and both `new-tab` rows, plus a "Live in production, not documented" block for `hamburger`, `google-plus`, `mng-podcast1` and `users4`. That working copy was retired on 2026-09-25. Everything it showed is recorded in §3 and §5, and the name fixes Karl made were made on the authoritative documentation itself.

---

## 5. Open items

1. ~~Review the 4 "live, not documented" icons one by one with Karl (in progress — see §4) and decide whether each should be added to the documented categories or is dead weight.~~ **Done, 2026-08-31 — full review complete.** Final dispositions: `hamburger` — real icon, resolves to a doc-naming fix (see Item #2). `sphere`, `swap`, `mng-podcast` — all confirmed real, distinct icons; recommend adding to the documented categories (category TBD for `sphere`/`swap`; `mng-podcast` → Social Media/Brands). `mng-podcast1` — confirmed `android` codepoint duplicate, not added. `google-plus` — confirmed dead weight (Google+ discontinued); logged for engineering as a font-cleanup candidate (design-vs-production entry 1) rather than added to the doc. `users4` — no live rendered usage found anywhere checked (homepage, About Us, an article page); Karl elected to ignore/drop this one.
2. ~~Decide what to do about the 6 documented-but-mismatched entries — in particular whether `home`/`menu7` in the doc should be corrected to `home3`/`hamburger`.~~ **All 6 resolved, 2026-08-31.** `home`→`home3` and `menu7`→`hamburger` confirmed 2026-08-28 in a live side-by-side review (Figma component vs. the live off-canvas panel on Chicago Tribune) — same icons, Karl added a note directly on the Figma icon documentation flagging the mismatch, doc names should be corrected. `enlarge7`→`enlarge` confirmed the same way, 2026-08-31 — same "expand" glyph, doc-naming fix only. `pintrest-p`→`pinterest-p` was a plain spelling typo, corrected directly on the Figma page. Both `new-tab` rows — Karl said to ignore, no action needed.
3. ~~Fix the `pintrest-p` → `pinterest-p` spelling typo on the documented page.~~ **Done, 2026-08-31** — corrected directly on the Figma page.
4. ~~Confirm whether the `new-tab` strikethrough means a redraw-under-the-same-name or a not-yet-shipped removal.~~ **Resolved, 2026-08-31 — Karl said to ignore, no action needed.**
5. Optional: re-run this same CSS scan against the other three pilot sites to confirm the font is identical sitewide (skipped so far per your earlier "it's the same on those sites" call for the search bar — flagging in case that doesn't extend to the icon font). **Now includes two more sites to consider:** Greeley Tribune and mcall.com joined the pilot set 2026-08-27 (both run the Modern Earthy shared theme) but haven't been checked for the icon font at all — likely a platform-wide asset independent of theme, same as the type-scale finding in `design-vs-production.md`, but that's an assumption, not yet confirmed for these two.
6. ~~Audit the live 95-variant `Icons` COMPONENT_SET~~ — **done, 2026-08-28. See §6, a full new section below.**
7. A full page-by-page usage audit (article, section front, obituaries) to know exactly where each of the 174 icons is actually used on the pilot sites, vs. present in the font but unused — not done; only a handful of icons have confirmed usage sites so far.
8. ~~**New, from §6:** decide what to do about `notification-filled`/`notification-outlines` (two built Figma components with no live match and no doc mention)~~ **Resolved, 2026-08-31** — Karl confirmed this is a known missing-in-production gap (real, designed artwork that hasn't shipped to the live font yet, not stray/undecided artwork); logged for engineering as a production gap to build (design-vs-production entry 1). ~~...and the stray `google-icon-logo-svgrepo-com` component (looks like a leftover import, candidate for deletion).~~ **Corrected by Karl, 2026-08-28** — this is not a stray import; it's the required four-color Google "G" brand mark, with the monochrome `google` component serving as the fallback. Recommend renaming (not deleting) — see §6.5.
9. ~~**New, from §6:** confirm the `access-time`/`clock` and bare `mng-podcast` findings — two more name-level gaps the original §3 audit missed, caught only because this deeper Figma-driven pass cross-checked the full live list a second time.~~ **Both resolved by Karl, 2026-08-28** — see §6.5. `access-time`/`clock`: the Figma documentation entry renamed to `access-time.svg`; doc's §2 category list updated to match. `mng-podcast`: confirmed a real, distinct icon via live-render comparison; Figma container renamed from "podcast 2" to "mng-podcast"; recommend adding to Social Media/Brands category.

---

## 6. Figma `Icons` COMPONENT_SET audit (95 variants) — 2026-08-28

**Source:** main MNG Web Design System file → Icons page (then "Icons | 2026.04.17", now "Icons | 2026.08.28") → `Icons` COMPONENT_SET (node `4693:5`), the live, hand-drawn 95-variant set Karl left untouched when he hand-copied the documentation (see §1). This was the explicitly-deferred item from Open Items §6 above — now done.

### 6.1 Scope note — read this before the findings below

This component set is **not**, and was never meant to be, a 1:1 mirror of the 174-icon live font. Excluding 1 slot placeholder (`IconSLOT`) and 14 payment-method badge components (`AmEx`, `AmExSMALL`, `ApplePay`, `ApplePayMARK`, `Discover`, `DiscoverSMALL`, `GooglePay`, `googlepayIconOnly`, `MasterCard`, `MastcardSMALL`, `PayPal`, `PayPalIcon`, `Visa`, `VisaSMALL` — already correctly out of scope per §2's "Not in Icon Font set" section), there are **80 real icon candidates** in this set. The large majority of the 174 live icons simply have no component here at all — that's expected, not a punch list of "95 missing icons." Treat this section as: for the icons that *are* represented here, do they match cleanly, and are there any genuine anomalies.

### 6.2 Clean 1:1 matches

The majority of the 80 candidates match a live CSS class name exactly (`appleinc`, `bin`, `bluesky`, `book3`, `bookmark2`, `bookmark3`, `bookmarks`, `checkmark3`, `checkmark-circle`, `content_copy`, `credit-card2`, `close`, `email`, `equalizer2`, `eye`, `eye-blocked`, `facebook`, `floppy-disk`, `flower`, `flower2`, `gift2-share-01`, `google`, `info`, `info2`, `link`, `minus`, `newspaper`, `new-tab`, `notification`, `notification2`, `padlock`, `paperplane`, `pen6`, `phone`, `plus`, `question3`, `question4`, `radio-unchecked`, `reddit`, `search`, `share-more`, `slideshow`, `spam`, `stumbleupon`, `thumbs-up2`, `tree`, `tree2`, `tumblr`, `user`, `users`, `user4`, `user-plus`, `user-minus`, `warning`, `warning2` — 53 in all), plus a few more that match with only a cosmetic difference: `linkedIn`/`linkedin` (case), `share-alt (Android)`/`share-alt` and `share2 (unknown device)`/`share2` (Figma just appends a parenthetical note to its internal name), and `share-"ios_share"`/`ios_share` (Figma's name literally quotes the live class it corresponds to). No action needed on any of these.

### 6.3 Naming mismatches — visually confirmed, not missing icons

These render the **same glyph** as a live icon, just under a different name in this Figma set. Confirmed by exporting the Figma component and rendering the live CSS class side-by-side, not assumed from name similarity:

| Figma component | Renders as | Live class | Verdict |
|---|---|---|---|
| `home` | A solid house | `home3` | **Same icon — confirmed by Karl in a live side-by-side review, 2026-08-28** (Figma component vs. the live off-canvas panel's "Home Page" row on Chicago Tribune). Resolves Open Item #2 above — the doc's `home` entry isn't missing, it's misnamed; should read `home3`. Karl added a note on the Figma icon documentation flagging the name mismatch. |
| `menu7` | Three horizontal bars | `hamburger` | **Same icon — confirmed by Karl in the same live review, 2026-08-28** (Figma component vs. the live off-canvas panel's trigger icon on Chicago Tribune). Also resolves Open Item #2 — `menu7` is literally a hamburger glyph; the doc entry should be renamed, not treated as unshipped. Karl added a note on the Figma icon documentation flagging the name mismatch. |

Additionally, four **directional-arrow pairs look like the same naming-mismatch pattern**, though not rendered pixel-by-pixel against their live counterparts (the exported chevrons were visually identical to each other, which is itself worth noting):

- `arrow-left2` / `arrow-right2` / `arrow-up2` / `arrow-down2` — almost certainly live's bare `arrow-left` / `arrow-right` / `arrow-up` / `arrow-down` (Figma just carries a `2` suffix these live classes dropped).
- `arrow-rightSMALL` / `arrow-upSmall` / `arrow-downSMALL` — almost certainly live's `arrow-right11` / `arrow-up11` / `arrow-down11`. Exported and compared `arrow-right2` against `arrow-rightSMALL` directly: both are the same chevron shape, visually indistinguishable at this size — consistent with one being the "regular" and one the "small/alt" cut of the same design, matching the two-variant pattern live already has for right/up/down.
- **The odd one out: `arrow-left11` is the only direction where Figma's own name already matches live exactly.** The other three directions use a `SMALL` suffix instead of the `11` live actually uses — an internal naming inconsistency within this Figma set itself, separate from any live mismatch.

**Confirmed, 2026-08-31** — Karl reviewed this pattern and has no concern; treating both pairs as the same naming-mismatch pattern as `home`/`menu7`, no further pixel-level verification or doc action needed.

### 6.4 Important correction: `grid` (Figma) is *not* the same icon as `grid2` (live)

Worth flagging on its own because the name similarity is misleading. Figma's `grid` component renders a clean 3×3 dot/square grid — exactly what you'd expect a "grid view" icon to look like, and exactly what the PENDING UPDATES "ADD" list (§2) is asking for. But rendering live's `grid2` class produces a **wrapped gift box**, not a grid — and rendering it side-by-side with live's `gift2` shows they're pixel-identical. `grid2` appears to be a font-build codepoint duplicate of `gift2` (the same pattern already known for `mng-podcast1`/`android`), not a real grid icon that quietly shipped under a slightly different name. **Net: the PENDING "grid" request has not shipped — confirmed by Karl, 2026-08-28**, in the same live side-by-side review as the other icon findings above. Figma has artwork ready for it (the `grid` component), but production doesn't have a working grid icon yet — `grid2` is a red herring.

### 6.5 Genuinely new findings — not previously documented anywhere

- **`access-time` (live) vs. `clock` (documented) — a 9th name mismatch the original §3 CSS scan missed. Resolved, 2026-08-28.** The live font has no `clock` class; it has `access-time` instead (a Material-Icons-style name). The Decoration category (§2) documented this icon as "clock" (the hand-copied documentation actually already carried the correct filename in a parenthetical, "Time/Clock (access-time.svg)" — just easy to miss). Karl renamed the entry in the Figma documentation directly to `access-time.svg`, and this doc's §2 category list has been updated to match. Neither §3's original count ("166 of 174 match, 8 mismatches") nor this doc caught it until this deeper cross-check.
- **A bare `mng-podcast` live class exists, in addition to the already-flagged `mng-podcast1`. Resolved, 2026-08-28.** §3 only ever discussed `mng-podcast1` (the one sharing `android`'s codepoint); `mng-podcast` itself — no digit — was never mentioned. Confirmed via live-render comparison on Chicago Tribune that `mng-podcast` is a real, distinct icon (a podcast/microphone glyph), not a codepoint duplicate or alias — unlike `mng-podcast1`, which remains a pure `android` duplicate with zero Figma representation. Karl also renamed the corresponding Figma container from "podcast 2" to "mng-podcast" to match. Recommend adding `mng-podcast` to the Social Media/Brands category (§2); no engineering action needed.
- **Two more live classes with no obvious home in any documented category: `sphere` and `swap`. Resolved, 2026-08-28.** Neither maps cleanly to anything in the six documented categories (§2) the way most others do. Confirmed via live-render comparison on Chicago Tribune that both are real, distinct icons — `sphere` is a globe icon, `swap` is a crossed-arrows exchange icon — not font-build duplicates or placeholders. Recommend adding both to the documented categories (§2); exact category TBD. Joins `hamburger`, `google-plus`, `mng-podcast1`, `users4`, and now `mng-podcast` on the "live, not documented" review list (see Open Item #1).
- **Two Figma components with no live match *and* no documentation mention at all: `notification-filled` and `notification-outlines`. Resolved, 2026-08-31.** Rendered both — they're a filled and an outline exclamation-mark-in-a-circle glyph (an "alert" icon, not a bell), not in the live font under any name, and not the same thing as the PENDING UPDATES "CHANGE" list's note about "a notification-icon variant under consideration." Karl confirmed this is a known missing-in-production gap — real, designed artwork that hasn't shipped to the live font yet. Logged for engineering as a production gap to build (design-vs-production entry 1), not a doc gap.
- **An undocumented component: `google-icon-logo-svgrepo-com`,** sitting right next to the monochrome `google` component. **Corrected, 2026-08-28** — this is not a stray leftover import as first suspected. Per Karl: this is the required four-color Google "G" brand mark for standard use; the monochrome `google` component is only a fallback for cases where the four-color mark isn't technically possible. Recommend **renaming** it away from the raw svgrepo.com filename (not deleting it) and adding it to the Social Media/Brands category (§2) alongside `google`/`google-color`.
- **Live's brand icon `paypal` (documented under Social Media/Brands, §2) — confirmed intentional, no gap. Resolved, 2026-08-28.** Karl confirmed the PayPal graphics ARE present in this component set (`PayPal`, `PayPalIcon`) but are deliberately excluded from the icon font, consistent with the existing payment-badge exclusion pattern already correctly noted in §2's "Not in Icon Font set" section. No missing artwork, no action needed.
- **`users4` is now confirmed missing from this Figma set too, not just the text doc.** Corroborates the existing "live, not documented" flag from a second angle — there's no drawn artwork for it anywhere in Figma, either. **Dropped, 2026-08-31** — no live rendered usage found anywhere checked (see §3); Karl elected to ignore rather than pursue further.

### 6.6 Confirmed, no action needed — matches the existing PENDING "ADD" list

`crown`, `giving-hand`, `list`, `yield-filled`, `yield-outline` all exist as drawn Figma components but have no live match — consistent with, and now visually corroborating, the doc's own PENDING UPDATES "ADD" list (§2). (`grid` also belongs in this bucket — see §6.4 for why it needs its own callout rather than a quiet checkmark.) No `plus-circle`/`plus-circle2`/`minus-circle`/`minus-circle2` components exist in this set at all — those ADD-list items don't even have placeholder artwork yet, unlike the five above.

---

## 7. Production names, artwork sources and the next font build — 2026-10-22

Decisions (Karl, 2026-10-22):

- **Production names are kept, always,** unless an icon is brand new. Where production renamed an IcoMoon icon, the production name wins; changes to Figma labels don't need tracking. What does get tracked: the IcoMoon name, so the original artwork can be found again, and any artwork that isn't original IcoMoon artwork ("Custom").
- **`home`, `menu7`, `enlarge7`, "iTunes / Apple Music"** are `home3`, `hamburger`, `enlarge` and `music5`. In the MNG IcoMoon project (2025-03-19) U+E936 was already `home3` and U+E947 `music5`; `menu7` and `enlarge7` were IcoMoon names that production's theme CSS had renamed. Karl renamed both in the IcoMoon project on 2026-10-22.
- **`notification` and `notification2` stay.** Both are live: `notification2` shows in the Reader Dashboard's inline-message headings on Cañon City Daily Record (Saved Articles "Please upgrade your subscription to continue.", Gifted Articles "Please subscribe to continue.", Subscription "Subscribe to the news."; checked 2026-10-21, logged in, non-premium account), and the shared `mng-digisubs` plugin styles `icon-notification` in the Save Article modal's "out of space" messages. The new outline and filled artwork replaces the IcoMoon glyphs at U+E94D / U+E94E; `notification-outlines` and `notification-filled` were only working names for that artwork.
- **ADD list grows to 17:** the 10 Pending Updates icons plus headphones, sort, sort2, sort-alpha-asc, sort-alpha-desc, filter3 and filter4 from IcoMoon Ultimate (added to the Figma ADD list 2026-10-22).

Done 2026-10-22: Karl rebuilt the IcoMoon project by hand from `selection.json` (2025-03-19) and exported it (188 icons: the 171, the 17 adds, the 2 artwork swaps and the 2 renames; checked against the export). `tokens/icons/icons.json` now records `artworkSource` and `icomoonName` for every icon and lists the next font build; `icomoon.css` and `preview.html` are generated by `scripts/icon-font/build.py`.

Still open: the IcoMoon export also names `Threads-square` (production `icon-threads`) and `users4` (production `icon-user4`) differently from production, so its CSS would drop those two production classes. Rename them in the IcoMoon project before the font ships. The Figma labeling pass (production name plus "IcoMoon: name" or "Custom" on every icon) and the legend revision are next.
