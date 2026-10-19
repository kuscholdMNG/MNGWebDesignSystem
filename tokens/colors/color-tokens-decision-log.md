# Color Tokens — Decision Log (through 2026-10-15)

> **Superseded for values (2026-09-24).** The current color values for every theme and site live in `mng-colors.tokens.json` in this folder (with `mng-colors.css` and `mng-colors-sites.csv`; engineering fixes are in `production-vs-design-differences.md` entry 21). Keep this file for the history: why tokens were added, renamed, removed or excluded. The newest decisions are in §8–§11.
>
> **Changed since this was written:**
> - The export now includes The Baltimore Sun, Capital Gazette and `subsite-custom`, reversing the exclusions noted below. Those values come from the Figma style guides, not from Figma variables (Figma's Colors collection is capped at 20 modes).
> - Prairie Mountain Publishing (19 sites, including Greeley Tribune) is its own sub-theme: `modernearthy.css` + `site-pmp` color override. Since 2026-09-25 it is a Figma mode (it replaced the Greeley Tribune mode) and uses the Measured Vibrant should-be values. See §8.
> - The four collections described below (Theme, Brand, Primitives, Endless Tributes) were a first build. Their values now live in the MNG Web Design System file's single `Colors` collection (`3749:16`) and in the portable export.

**Status:** First built as four Figma variable collections (Theme, Brand, Primitives, Endless Tributes), now consolidated into the `Colors` collection — this doc is the durable reference for where each value came from.
**Source:** The pre-existing "Color Styles" Figma page (since retired). Every value below is sourced from the **left-hand list** in each site/theme Style Guide section (the "should-be"/target column), confirmed by reading each row's actual on-canvas x-position rather than relying on frame names or labels, since naming was inconsistent across sections.
**Excluded from source, per explicit decision:** The Baltimore Sun and Capital Gazette (no Style Guide data requested); `subsite-custom` (too sparse — only defined for a handful of sites, not being modeled as a formal variable).

---

## 1. Theme collection

Modes: Measured Vibrant, Bold Coastal, Modern Earthy.

**2026-08-27, corrected — no gap here after all.** An earlier note on this line claimed there are 4 shared default themes and that this collection was missing a mode for a "Morning Call" theme. That was wrong: a live check of mcall.com (the site people call "Morning Call") shows it loads `modernearthy.css` with its own color override on top via the WordPress Customizer, same as every other one-off site. There is no separate "Morning Call" theme file; it's a site name, not a 4th shared theme. This collection's 3 modes (Measured Vibrant, Bold Coastal, Modern Earthy) already cover every shared theme that actually exists — nothing to add here.

**Now checked, 2026-08-27:** mcall.com's own Brand-collection row (§2) was live-confirmed via the Customizer-scope check used platform-wide this date. Its live Customizer `primary` value came back as `#014B78`, which matches this doc's `primary-dark` for Morning Call (not `primary`, `#166291`) — see §2 and the note there for detail. (Greeley Tribune was checked the same day; see §8 for why it no longer has its own row.)

| Variable | Measured Vibrant | Bold Coastal | Modern Earthy |
|---|---|---|---|
| `color/theme/primary-lighter` | `#717FD1` | `#1799A5` | `#FE521E` |
| `color/theme/primary-light` | `#5869CA` | `#00838F` | `#E03400` |
| `color/theme/primary` | `#3F51B5` | `#007580` | `#CC3300` |
| `color/theme/primary-dark` | `#32408F` | `#0A5962` | `#B93611` |
| `color/theme/primary-darker` | `#171E44` | `#014A52` | `#A52804` |
| `color/theme/secondary` | `#EEFF41` | `#FFEA00` | `#EEFF41` |
| `color/theme/tertiary` | `#EB5300` | `#F4A700` | `#00828F` |
| `color/theme/near-black` | `#1F1E1C` | `#0A0908` | `#1A1A1A` |
| `color/theme/white` | `#FBFBFB` | `#FFFFFF` | `#FAFAFA` |

**Modern Earthy `tertiary`:** set to `#00828F` per your instruction, using the hex text as ground truth. Its rgb text on the source page was previously wrong (a typo, corrected — see §6) and unrelated to the sibling production row's `#FF5722`, which I'd mistakenly conflated with this row in an earlier pass.

**`color/theme/divider` removed.** It came from `card-teaser.md`'s live-site divider audit (Chicago Tribune/Orlando Sentinel = `#C8C4C0`, Denver Post/OC Register = `#D7D6D2`), mapped onto Measured Vibrant / Bold Coastal — but that doc itself flags this exact site pairing as inconsistent with other theme-based groupings found in the same audit, so modeling it as a clean theme-level token wasn't well-supported. Not bound to any component, so removing it was a clean delete. **Re-checked 2026-08-27 against the verified site/theme mapping** (Orlando Sentinel is Measured Vibrant with its own override; Denver Post is Bold Coastal with its own override, not the "bespoke" theme an earlier note claimed — see `card-teaser.md` §4.3) — the divider pairing still doesn't line up with real theme membership either way, so the removal decision stands, just for a corrected reason.

**~~Modern Earthy now has a live pilot site (Greeley Tribune, joined 2026-08-27)~~ Corrected 2026-09-24:** Greeley Tribune loads `modernearthy.css`, but its colors come from the PMP override plus its own div#page customizer values. It's a PMP site, not a Modern Earthy color reference. `color/theme/nav-text` is still unconfirmed on Modern Earthy sites (only typography has been audited so far). Worth confirming directly next time nav is in scope, per `navigation.md` §5.2.

---

## 2. Brand collection

17 modes (Chicago Tribune and Orange County Register use their theme's should-be values directly since they have no separate one-off Style Guide section; the other 15 have their own).

| Site | primary-lighter | primary-light | primary | primary-dark* | primary-darker | secondary | tertiary |
|---|---|---|---|---|---|---|---|
| Chicago Tribune | `#717FD1` | `#5869CA` | `#3F51B5` | `#32408F` | `#171E44` | `#EEFF41` | `#EB5300` |
| Denver Post | `#C81632` | `#AF1628` | `#8E1024` | `#7D161E` | `#641614` | `#003459` | `#FFC518` |
| Orange County Register | `#1799A5` | `#00838F` | `#007580` | `#0A5962` | `#014A52` | `#FFEA00` | `#F4A700` |
| Orlando Sentinel | `#5C95DD` | `#1879C9` | `#1776C4` | `#156CB4` | `#1360A0` | `#EEFF41` | `#48A395` |
| East Bay Times | `#A0D0ED` | `#007AB8` | `#006DA3` | `#006394` | `#00527A` | `#FFC518` | `#CD2709` |
| The Mercury News | `#A0D0ED` | `#007AB8` | `#006DA3` | `#006394` | `#00527A` | `#FFC518` | `#CD2709` |
| St. Paul Pioneer Press | `#0187E0` | `#007ACC` | `#006FB7` | `#0065A8` | `#005892` | `#FFEA00` | `#F4A700` |
| Petaluma Argus-Courier | `#A8681A` | `#905A17` | `#7E4E14` | `#643D0D` | `#492C09` | `#FFEA00` | `#006FB7` |
| The Press Democrat | `#D10F14` | `#BA0D12` | `#9E0B0F` | `#8F0A0E` | `#6E0B0C` | `#FFEA00` | `#006FB7` |
| The Sonoma Index-Tribune | `#149DE6` | `#107DB7` | `#0E70A4` | `#0D6391` | `#0C5983` | `#FFEA00` | `#F4A700` |
| Morning Call | `#5399C4` | `#27719F` | `#166291` | `#014B78` | `#00385A` | `#EEFF41` | `#FF5722` |
| 21C Michigan Sites (Combined) | `#3E7CB2` | `#2A6496` | `#3A537A` | `#32476C` | `#2C3B55` | `#9DAABD` | `#FF5722` |
| ~~Greeley Tribune~~ **Prairie Mountain Publishing** (2026-09-25, §8) | `#717FD1` | `#5869CA` | `#3F51B5` | `#32408F` | `#171E44` | `#EEFF41` | `#EB5300` |
| Boston Herald | `#3C81C7` | `#2C6FB2` | `#005D9C` | `#00538A` | `#0F496F` | `#EEFF41` | `#FF5722` |
| Hartford Courant | `#5796BD` | `#2B7EA5` | `#166D95` | `#084E6F` | `#171E44` | `#EEFF41` | `#6A54CA` |
| GrowthSpotter | `#529950` | `#1D8734` | `#1A7C2E` | `#176E29` | `#146024` | `#EEFF41` | `#E7632A` |
| South Florida Sun Sentinel | `#4A92AF` | `#2A728F` | `#136383` | `#115975` | `#0F4F68` | `#EEFF41` | `#AB9500` |

\* Renamed from `color/brand/primary-border` to `color/brand/primary-dark` (same values). It's the button hover fill and focus stroke color.

**Verification note:** every value above was re-checked directly against the left-hand-column position of its source row in Figma (not just against frame names/labels).

**Live-confirmed 2026-08-27 (Denver Post, Orlando Sentinel):** both sites' live-rendered `--primary` (read on the WordPress Customizer's actual scope rather than at `:root` — see `modal.md` for why that distinction matters) matches this table exactly: Denver Post `#8E1024`, Orlando Sentinel `#1776C4`.

**⚠️ Discrepancy found, mcall.com (2026-08-27):** live-rendered `--primary` on mcall.com is `#014B78` — that's an exact match for this table's **`primary-dark`** column for Morning Call, not `primary` (`#166291`). Either the site is live-rendering the wrong step of its own color ramp, or this table's column values are shifted for this row specifically. Not yet root-caused (production-vs-design entry 3).

---

## 3. Primitives collection — Universal Grays & Universal Alert Colors

Single "Value" mode. Source: "Shared Platform Reference — Style Guide" → "Universal Grays (Proposed — All Themes Should Use)" / "Universal Alert Colors".

| Variable | Value | Note |
|---|---|---|
| `color/gray/black` | `#000000` | Source row is explicitly labeled "color-black (DO NOT USE)" — excluded last round, added back per your request. Use `gray/min` for new work. |
| `color/gray/min` | `#141414` | |
| `color/gray/100` | `#393938` | |
| `color/gray/200` | `#5E5D5C` | |
| `color/gray/300` | `#838280` | |
| `color/gray/400` | `#A7A6A3` | |
| `color/gray/500` | `#CCCAC7` | |
| `color/gray/600` | `#F1EFEB` | |
| `color/gray/max` | `#FFFFFF` | |
| `color/feedback/low-success` | `#2E8000` | Renamed from `color/feedback/low` (Karl, 2026-09-10). |
| `color/feedback/medium` | `#856A00` | |
| `color/feedback/high-error` | `#CC2B27` | Renamed from `color/feedback/high` (Karl, 2026-09-10). |

---

## 4. Endless Tributes collection

Single "Value" mode. Source: "Shared Platform Reference — Style Guide" → "Should-Be vs Production (per original MNG Web Design System)" → "Endless Tributes — Updates."

**Mirrored into MNG Web Design System, 2026-09-10:** all 9 of these colors now also exist in MNG Web Design System's `Colors` collection (`VariableCollectionId:3749:16`) as a new `color/tributes/*` variable group, with the same value across all 20 modes rather than being squeezed into the existing 7-color-slot-per-theme pattern or modeled as a one-off theme mode. This reflects how obituary pages actually render in production — identically regardless of which site's masthead brand is active — so a single universal value per token is correct.

| Variable | Value | Production comparison |
|---|---|---|
| `color/tributes/primary-lighter` | `#F15F87` | Retired — not found live anywhere |
| `color/tributes/primary-light` | `#C00C3D` | Live match (`--primary-obit-light`) |
| `color/tributes/primary` ("Scarlet") | `#8D092D` | Live match (`--primary-obit`) |
| `color/tributes/primary-dark` | `#770000` | Retired — not found live anywhere |
| `color/tributes/primary-darker` | `#4D0000` | Retired — not found live anywhere |
| `color/tributes/secondary` ("Sage") | `#B3BC9C` | Live match, renamed to `--quaternary-obit` in production CSS |
| `color/tributes/tertiary` ("Brown") | `#3A252B` | Live match, hardcoded (no longer a variable) |
| `color/tributes/tan` | `#A39C8A` | Live match, hardcoded |
| `color/tributes/tan-light` | `#E8E6E2` | Drifted in production (`#ECEDE7`) |

---

## 5. Resolved this round

1. **`color/brand/primary-border` → `color/brand/primary-dark`.** It wasn't just a naming leftover — it's the button hover fill and focus stroke color. Renamed rather than deleted.
2. **`color/gray/black` (`#000000`) added** to Primitives, with a description noting the source flags it "DO NOT USE" and that `gray/min` is preferred for new work.
3. **Modern Earthy `tertiary` set to `#00828F`** (the literal left-hand hex text), per your explicit instruction — overriding my earlier recommendation of `#FF5722`.

## 6. Hex vs. RGB audit (source page data quality)

Scanned all 333 color rows across every section of the Color Styles page for hex/rgb text mismatches. Found 3, all in Modern Earthy's should-be block (`Frame 1 > Modern Earthy — Theme Default — Brand / Primary (should-be)`) — no other theme, one-off site, or shared-reference section had any. In every case the hex text was treated as correct, and the rgb text on the Color Styles page itself was corrected to match:

| Variable | Hex (correct, unchanged) | RGB text — before | RGB text — after |
|---|---|---|---|
| `--primary-lighter` | `#FE521E` | `rgb(254, 82, 29)` | `rgb(254, 82, 30)` |
| `--primary-darker` | `#A52804` | `rgb(65, 40, 4)` | `rgb(165, 40, 4)` |
| `--tertiary` | `#00828F` | `rgb(130, 143, 100)` | `rgb(0, 130, 143)` |

No Figma Variable values changed as a result of this fix — the variables were already built from the hex text. This was purely a correction to the reference page's rgb labels.

## 7. CRUX Style Library color comparison: decisions (2026-09-10)

Carried over from `CRUX-Gap-Analysis.md`, which was retired on 2026-09-24. All of its color values are already in `mng-colors.tokens.json` or `production-vs-design-differences.md`. Only these decisions were found nowhere else:

1. **CRUX's semantic role tokens are not adopted.** That covers `color/text/*`, `color/background/*`, `color/border/*`, `color/action/subscribe/*`, `color/breadcrumb/active` and `color/gray/footer`.
2. **CRUX's component-level color tokens are not adopted.** That covers `component/button/*`, `component/focusRing/color`, `component/modal/backdrop` and `component/breakingBar/*`. MNG components bind directly to primitive and brand variables instead.
3. **CRUX's `grayRoot/100–600` scale is not adopted.** Production still uses it, which is logged as a production fix (production-vs-design entry 10).
4. **CRUX's `brown/100–400`, `brand/bgCommon` and obituary `secondaryObit` (`#946C82`) were skipped.**
5. **Color stays out of typography tokens.** CRUX bakes color into about 15 type styles; MNG keeps color and type separate.
6. **Publication coverage:**
   - "21C Michigan Sites (Combined)" covers The Oakland Press, Macomb Daily, The Morning Sun and The News-Herald.
   - Lowell Sun uses Modern Earthy as is.
   - NY Daily News uses Measured Vibrant plus a subsite override.
   - None of these three groups gets its own mode.
7. **Orange County Register was swapped out for South Florida Sun Sentinel** in the Figma Colors collection to stay within the 20-mode limit. OC Register uses the Bold Coastal values.
8. **Denver Post `primary-darker` typo fixed** to `#641614`.
9. **The Baltimore Sun and Capital Gazette are not Figma modes.** Their values live in the export. ~~Capital Gazette's design-vs-production mismatches were deliberately not logged.~~ Reversed 2026-09-25: every theme's mismatches are now logged (§8).

## 8. Greeley Tribune → Prairie Mountain Publishing; engineering callouts (2026-09-25)

1. **PMP uses the Measured Vibrant should-be values** (Karl). The PMP style guide's spec column (node `7027:37883`) was updated to them: `primary-lighter` `#717FD1`, `primary-light` `#5869CA`, `primary` `#3F51B5`, `primary-dark` `#32408F`, `primary-darker` `#171E44`, `secondary` `#EEFF41`, `tertiary` `#EB5300`. Neutrals stay `#1A1A1A` / `#FAFAFA` (nav-text `#1A1A1A`). PMP is still its own sub-theme, not Measured Vibrant: it loads `modernearthy.css` + `site-pmp`.
2. **The Greeley Tribune Figma mode became "Prairie Mountain Publishing"** (same mode ID `6857:12`, so any component bound to it now shows PMP). The mode count stays at 20. Its values were set to item 1.
3. **The Greeley Tribune — Style Guide section was deleted** from the Color Pallets page. Greeley stays listed under PMP's "Sites Using This Theme", with its `div#page` override (`primary` `#536E7F`, `primary-light` `#5B7B8B`, `primary-dark` `#44687F`) noted there. ~~Outlined in red as a site-level mismatch.~~ Changed 2026-09-30: it's a documented exception, not a mismatch (§9).
4. **Red-dashed outlines mark every production mismatch.** In PMP's production column, `primary-lighter` (not set, falls back to `#47B6FF`) and `tertiary` (`#303F9F`) were outlined, using the same stroke as Measured Vibrant.
5. **Every publication in the export lists its theme, sub-theme and fixes.** The Figma callouts are carried into `mng-colors.tokens.json` (`$extensions.com.mng.mismatches`), `mng-colors-sites.csv` (`engineering_fixes`) and the new `mng-colors-engineering-fixes.md` (merged into `production-vs-design-differences.md` entry 21 on 2026-09-30). This covers all 22 themes and sub-themes, Capital Gazette included.
6. ~~**The Baltimore Sun has no should-be spec**, so its tokens use its production values and no mismatches are listed. **Hartford Courant**'s parent theme file isn't recorded; both are flagged for follow-up.~~ Resolved in §9.

## 9. Greeley exception, Hartford Courant, The Baltimore Sun (2026-09-30)

1. **Greeley Tribune's overrides are a documented exception, not a mismatch** (Karl). Its `div#page` Customizer values (`primary` `#536E7F`, `primary-light` `#5B7B8B`, `primary-dark` `#44687F`) are intentional. In Figma the red outlines were removed and the values are noted under the PMP style guide's "Sites Using This Theme". In the export they're Greeley's site tokens (`$extensions.com.mng.exceptions` in the JSON, `site_overrides` in the CSV, a site block in the CSS). Engineering doesn't change them. Greeley still needs the two PMP-wide fixes (`primary-lighter`, `tertiary`).
2. **Hartford Courant runs Measured Vibrant** (verified live 2026-09-25). courant.com loads `measuredvibrant.css` + `plugins/site-plugins/site-tribune/dist/css/style.min.css`, with a `div#page` override setting `primary-light`, `primary` and `primary-dark` all to `#2B7EA5`. Everything else is inherited: `primary-lighter` `#47B6FF`, `primary-darker` `#171E44`, `secondary` `#EEFF41`, `tertiary` `#303F9F`. That matches the Figma style guide's production column, so its 6 callouts stand. It's now recorded as a sub-theme of Measured Vibrant (Figma style guide note, export and docs).
3. **The Baltimore Sun uses its documented Figma styles as is** (Karl). No should-be spec is needed and no production comparison is tracked, so it has no fixes and no follow-up.
4. **One Engineering handoff doc** (Karl). The per-theme fix list from `mng-colors-engineering-fixes.md` moved into `production-vs-design-differences.md` entry 21, and the separate file was retired. The rebuild script now writes entry 21 directly.

## 10. NEPA-PMP and the disputed-site live checks (2026-10-01)

1. **NEPA and PMP share one color sub-theme, NEPA-PMP** (Karl: "if it matches exactly, update the PMP Style Guide to NEPA-PMP"). Checked live on all 5 NEPA sites and canoncitydailyrecord.com: each NEPA site loads `modernearthy.css` plus its own plugin (`site-citizensvoice`, `site-thetimes-tribune`, `site-wcexaminer`, `site-republicanherald`, `site-standardspeaker`), which sets the same six variables on `body` as `site-pmp` (`primary` #3F51B5, `primary-light` #5869CA, `primary-dark` #32408F, `primary-darker` #171E44, `secondary` #EEFF41, `tertiary` #303F9F; `primary-lighter` unset, falls back to #47B6FF). Type matched too (lead headline, dek, section title, nav, body).
2. **In Figma:** the PMP style guide was renamed "NEPA-PMP — Theme Style Guide", its notes now cover both delivery routes, and the NEPA site list moved there from the Modern Earthy style guide. The Colors collection mode "Prairie Mountain Publishing" was renamed "NEPA-PMP" (same mode ID, so bound components are unaffected). Should-be values are unchanged (Measured Vibrant values).
3. **In the export:** the sub-theme key is now `nepa-pmp` (was `prairie-mountain-publishing`). The NEPA sites now carry NEPA-PMP's 2 fixes instead of Modern Earthy's 4. Engineering note: on NEPA the fix goes in 5 separate site plugins, not one shared stylesheet.
4. **Disputed themes resolved, matching Figma:** Daily Press (Measured Vibrant), New York Daily News (Measured Vibrant + `site-tribune`), GrowthSpotter (Measured Vibrant + `site-tribune`, own ramp), The Morning Call (Modern Earthy + its own override). On Morning Call, `secondary` and `tertiary` aren't in the override but inherit the design values, so 2 of its 6 Figma callouts don't change what renders; Karl decided 2026-10-01 to keep them as missing/wrong: the values should be set explicitly, so all 6 callouts stand.

## 11. Daily Herald sub-theme (2026-10-15)

1. **Daily Herald gets its own Modern Earthy sub-theme** (Karl; palette approved by the other team and merged 2026-10-19), placed in the Modern Earthy row of the Color Pallets page next to NEPA-PMP. Key `daily-herald`; dailyherald.com now resolves Modern Earthy → Daily Herald instead of "not on MNG themes".
2. **Primary `#0072B4` is given; the rest was extrapolated and approved by Karl.** The light/dark steps reuse the OKLCH lightness and chroma steps of the other blue sub-themes (Boston Herald, Morning Call, St. Paul Pioneer Press), with the hue held at the primary's:

   | Token | Hex | Step from primary (OKLCH) | Text on it |
   |---|---|---|---|
   | `primary-lighter` | `#3b97dc` | L +0.12 | `#141414` (5.8:1) |
   | `primary-light` | `#087abe` | L +0.025, C +0.004 (kept at 4.6:1 with white) | `#ffffff` (4.6:1) |
   | `primary` | `#0072b4` | given | `#ffffff` (5.2:1) |
   | `primary-dark` | `#0066a2` | L −0.04, C −0.01 | `#ffffff` (6.1:1) |
   | `primary-darker` | `#0e598b` | L −0.085, C −0.028 | `#ffffff` (7.5:1) |

   `primary-light` takes a smaller step than Boston Herald's (+0.066) so white text still passes AA; with the usual step it would drop to 4.4:1.
3. **Secondary `#eeff41` and tertiary `#ff5722`** match the other blue Modern Earthy sub-themes (Boston Herald, Morning Call). Near-black, white and nav-text are the Modern Earthy defaults (`#1a1a1a`, `#fafafa`, `#1a1a1a`).
4. **Not a Figma mode.** The Colors collection is at Figma's 20-mode limit, so, like The Baltimore Sun and Capital Gazette, the values live in the token files and in the Figma style guide (swatches unbound).
5. **No production audit.** dailyherald.com still runs on Everyware (verified 2026-09-24). Its production column in Figma says so; production-vs-design entry 21 lists the ten Customizer values to set when it moves.
