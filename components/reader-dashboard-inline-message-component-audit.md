# InLineMessage Component — Variant Audit & Reorg Proposal
**Date:** September 8, 2026 (file references updated 2026-09-25)
**Scope:** The `InLineMessage` component set — the shared alert/panel/message pattern used across the Reader Dashboard (gift articles, subscriptions, newsletters, profile, etc.) and referenced piecemeal elsewhere in the design system.

**Related doc:** `Reader-Dashboard-Library-Impact-Map.md`, in the MNGWebDesignSystem folder root. Its scope is different from this doc — it maps which files/pages across the whole footprint would be affected by a Reader Dashboard v2.0 → v2.1 library publish (component usage/exposure, not variant-axis design), compiled 2026-09-02 across three rounds of scanning. See §6 below for how the two connect.

---

## 1. Files involved

| File | Role |
|---|---|
| **MNG Web Design System** (main file, formerly "UI Style Guide", `jFHYqhZbJjvWQmDI4myCsd`), page "In-Line Content Containers \| 2026.01.02" | Home of the master `InLineMessage` **COMPONENT_SET** (node `2776:2`) — 114 built variants. This is the source-of-truth component. |
| **Reader Dashboard v2.0** (`PhXogWaQcnNSnQqxyRu4b2`), page "Components \| 2026.02.25" | Consumes `InLineMessage` as **instances** (e.g. `Alert Container` → `InLineMessage` instance, `2ndSection Content` → nested `InLineMessage` instance) across Profile Panel, Subscription Panel, Upgrade/Cancel Subscription, Gifted Articles, Newsletters, Support, Benefits, and Notification Preferences pages. This is the live product file the pattern actually ships from. |

**Key finding:** there is exactly one component that needs reorganizing — `InLineMessage` in the main file — and its problems propagate: because it's hard to consume correctly, pieces of it have been re-drawn by hand elsewhere rather than instanced (the pilot Empty State Card, Status Badge and Modal error alert, since retired). Every hand-drawn copy is one more thing to keep in sync with the source.

---

## 2. Current variant structure

`InLineMessage` has **four variant properties**:

- **Device** — `Desktop, TabletH, TabletV, Mobile, FOLD, Menus` (6 values)
- **Priority** — `none, Confirmation, Medium, High, low` (5 values)
- **Location** — `Header, AcctMenu, DashProfileDisplayName, DashSubsUpgradeError, DashSubsCCError, DashSubscriptionCCinfo, DashSubsNonSub, DashSubsCCexp, DashGiftNoneLeft, DashGiftCTAnonSub, DashGiftEmpty, DashSavedEmpty, DashSavedFull, DashSavednonSub, DashSMSEdit, DashSMSSetUpMVP, DashSMSSetUpv2, DashSubsCancelError, DashSubsCCupdate, DashSubsAcctShareALL, StandAlone, NewspapersLINA, NewspapersStndSub, ModalError, CustomCheckout, OptOutReSub, OptOutUnsub, PrintSubError1, PrintSubError2, Registration, Login` (31 values)
- **PanelType** — `Panel, Alert, HeaderAlert` (3 values)

That's a theoretical matrix of 6 × 5 × 31 × 3 = **2,790 possible combinations** — of which **114 are actually built** (≈4% coverage). That sparseness is the tell: these four properties aren't really cross-cutting design states. They're one axis doing its job (Priority) plus three things bolted on that don't belong as variants.

### What the data actually shows
- **`Location` almost fully determines `PanelType`.** Of the 31 Location values, 29 pair with exactly one PanelType every time (e.g. `DashGiftEmpty`, `DashSavedEmpty`, `NewspapersLINA`, `ModalError`, `Login`, `Registration` → always `Alert`; `DashProfileDisplayName`, `DashSMSEdit`, `CustomCheckout`, `StandAlone` → always `Panel`; `Header`, `AcctMenu` → always `HeaderAlert`). Only `DashSubsAcctShareALL` spans two PanelTypes, and even there `Priority` is what actually switches it. PanelType is, in practice, a **derived** property — not an independent design decision someone makes per instance.
- **`Location` almost fully determines `Priority` too.** Most Location values are built at exactly one Priority (`DashSubsCCexp` is always `High`, `OptOutUnsub`/`OptOutReSub` are always `Confirmation`, `DashSubsNonSub` is always `Medium`, etc.). The only places Priority genuinely varies independently are the generic `Header` and `AcctMenu` alert bar and `DashSubsAcctShareALL`.
- **In other words: `Location` isn't a design variant — it's a content label.** Each of the 29 "Dash\*/Newspapers\*/OptOut\*/PrintSubError\*" values is really "this specific real-world screen," fully baked as its own component rather than being the same container with different text/CTA content dropped in. That's why the matrix is 96% empty: nobody was ever going to combine `Location=DashGiftEmpty` with `Priority=High` — that combination doesn't mean anything. It was never a matrix to begin with.
- **`Device` conflates two different things.** Five of its six values (`Desktop, TabletH, TabletV, Mobile, FOLD`) are genuine responsive breakpoints. The sixth, `Menus`, isn't a screen size at all — it's a placement context (inside an account dropdown menu). Mixing "how big is the viewport" with "where does this render" in one property is why `Device=Menus` reads oddly next to `Device=Mobile`.
- **Internal structure isn't consistent across variants**, which matters because component properties (and any future prop wiring) only propagate cleanly when the internal layer tree matches. Spot-checking a handful of variants found: the close/dismiss control is a real reusable `Button In-Line Close` instance (named `Button PanelClose` until 2026-10-02) in some variants and a plain, non-instanced `Close Button` frame in others; the content wrapper is named `Content`, `Contents`, or `Alert Content` depending on which variant you're in; and at least one variant (`Device=Desktop, Priority=High, Location=Header, PanelType=HeaderAlert`) has an internal layer still named `In-lin Alert - Mobile - Low` — a leftover from being duplicated off a different variant and never renamed. None of this is visible from the Assets panel; it only shows up once you're inside the layers.

---

## 3. Recommended axis reorganization

Collapse four variant properties down to **two real variant axes**, and move everything else to component properties that don't multiply the matrix:

**Keep as variants (true, independent visual states):**
- **Priority** — `None, Low, Medium, High, Confirmation` — this is a legitimate design-state axis (it changes color token, icon, and emphasis) and should stay a variant.
- **Placement** (rename from PanelType, and absorb what Location was actually doing structurally) — collapse to the real container archetypes that exist: `HeaderAlert` (top-of-page banner), `MenuAlert` (inside the account dropdown), `Panel` (embedded in a dashboard panel), `Modal` (blocking alert/confirmation), `Standalone` (full-width page-level message). That's ~5 values instead of Location's 31, and it's the thing a designer is actually choosing when they place the component.

**Move out of variants entirely, as component properties:**
- **Device → drop as a variant**, handle with responsive auto-layout + constraints on a single component instead (Figma's own guidance treats variants as for meaningfully different states, not pure resizing — see §4). Keep a real `Device` variant only where the *layout structure* genuinely differs between breakpoints, not just size — audit each Placement value to check whether that's actually true before defaulting to "yes."
- **Title / Body / CTA label → Text properties.** This is what 29 of the 31 Location values were actually doing — swapping copy. A `Title` and `Body` text property (and `CTA Label` if the button text varies) turns "one baked component per screen" into "one component, per-instance text override," which is exactly the pattern Figma's docs recommend text properties for.
- **Icon / CTA button → Instance-swap properties**, with a curated set of preferred instances (warning icon, success icon, info icon; primary button, hyperlink, no CTA) instead of each combination being its own frozen component.
- **Show Subtitle / Show CTA / Show Close Button → Boolean properties** toggling layer visibility, instead of separate components for "with" and "without."

**Net effect:** the realistic variant count drops from 114 (sparse, 4% of a 2,790-cell matrix) to something like **Priority (5) × Placement (5) = 25 cells**, most of which will actually get used, with every real-world screen (gift articles empty state, subscription errors, opt-out confirmations, etc.) becoming an *instance* of one of those 25 with text/icon/CTA overridden — not a 26th, 27th, 28th... baked component.

This would also let the Empty State, Status Badge and Modal error alert be built as real instances of the reorganized component instead of hand-drawn copies — closing the loop Karl flagged in the homepage audit.

---

## 4. Best practices (Figma's own guidance)

Pulled from Figma's Help Center, since these directly explain why the current structure grew the way it did:

- **Variant properties should represent genuinely variable design states** — Figma's own example is "size, state, or color" for a button. `Location` fails this test: it's not a design state, it's which page the message happens to live on.
- **Boolean properties are for toggling layer visibility**, e.g. "buttons with and without an icon" — "instead of creating variants for each state, apply a boolean property to the icon's layer visibility." That's a direct match for `InLineMessage`'s subtitle/CTA/close-button presence, which is currently baked into which of 114 components you pick rather than a toggle on one.
- **Text properties let you mark which text is editable** from the properties panel or canvas — the mechanism that should be carrying `InLineMessage`'s per-screen copy instead of a `Location` variant.
- **Instance-swap properties let you curate preferred nested instances** (a default plus a shortlist), which is the right tool for the icon and CTA variation currently baked per-Location.
- **Every variant in a set must share the same properties and internal layer structure** — Figma flags this as a hard requirement for variants to combine cleanly, and it's exactly where `InLineMessage` is inconsistent today (`Content` vs `Contents` vs `Alert Content`, instanced vs. non-instanced close button). This should be fixed as part of the reorg regardless of which axes survive, or new component properties won't propagate reliably across all 114 (soon-to-be ~25) variants.
- **For large variant sets, organize visually in rows/columns/grids** before combining, so the multi-dimensional structure is legible to anyone browsing the library — worth doing regardless, but especially once this drops from 114 to ~25 cells that should read as a clean grid rather than a wall.

Sources:
- [Create and use variants – Figma Learn](https://help.figma.com/hc/en-us/articles/360056440594-Create-and-use-variants)
- [Explore component properties – Figma Learn](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties)

---

## 5. Open questions for Karl
1. Confirm the proposed **Placement** values (`HeaderAlert / MenuAlert / Panel / Modal / Standalone`) actually cover every real screen currently modeled by the 31 Location values — I derived these from the PanelType groupings, not a screen-by-screen design review.
2. Is `Device` ever a genuine structural difference for this component (not just resizing), or can all breakpoints collapse into one responsive component? I'd want a couple of real Desktop-vs-Mobile pairs pulled up side by side in Figma to check before committing either way.
3. Once the axes are agreed, do you want me to actually rebuild `InLineMessage` in the main file (new properties, consolidated variants, internal layer renames), or just hand off this plan for your team to execute?
4. Should the Empty State, Status Badge and Modal error alert be built as instances of the reorganized component as a follow-up pass, or is that out of scope for now?
5. ~~Where does the Library Impact Map live?~~ Resolved — `Reader-Dashboard-Library-Impact-Map.md` in the MNGWebDesignSystem folder root. Its own next-step items (Account Selector Feat., Single Use Landing Pages, Email Options for Non-Registered Users) are about the v2.1 publish, separate from the InLineMessage rework above — flagging in case you want both workstreams sequenced together.

---

## 6. Cross-reference with the Library Impact Map

The Impact Map (compiled 2026-09-02, three rounds of scanning with 100% coverage by the final round) was built for a different purpose — mapping which of ~21 files across the footprint instantiate Reader Dashboard v2.0 components, ahead of a planned v2.0 → v2.1 library publish — but it overlaps with this audit in two useful ways:

- **It independently flagged the same hand-rebuilt-copy drift problem** found in §1 (Modal, Disclosure, Empty State Card and Status Badge built as freehand copies rather than real instances). Those pilot copies have since been retired (design-vs-production entry 15).
- **It confirms where `InLineMessage` sits in the wider component landscape.** The Impact Map counted Reader Dashboard v2.0's own "Components" page at 21 component sets / 467 variants, and separately confirmed `InLineMessage` doesn't live there — Reader Dashboard v2.0 only *instances* it (e.g. its "Alert Container" and "2ndSection Content" patterns). That matches what I found directly in Figma: the real master is in the main file, and Reader Dashboard v2.0 is a consumer, not the source. The Impact Map's "In-Line Content Containers" line item (6× `Title-SubLevel`) is a different, smaller component on that same page — not `InLineMessage` itself.
- **It's a reminder this isn't the only overgrown component.** By final (Round 3, complete-coverage) count, the Impact Map's biggest exposure isn't a single "heaviest" file so much as two different measures pointing at two different files: **Email Options for Non-Registered Users** has the largest raw footprint (2,709 matched instances across 6 of 7 pages, concentrated in the newsletter-sublist and markets/regions atoms), while **Account Selector Feat.** is the most *architecturally* dependent — "effectively built entirely out of Reader Dashboard v2.0 atoms." Underlying both, the **Nav family** (NavMenu, NavItem, IndicatorLeft/IndicatorRight, NavItemLabel) is the component family with the single widest blast radius of anything measured, touching nearly every consumer file including WordPress Elements and the main file. If a variant-axis cleanup like this one is worth doing for `InLineMessage`, the Nav family is the next place I'd look — happy to run the same kind of audit on it if useful.
