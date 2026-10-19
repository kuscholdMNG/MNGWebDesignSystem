# Modal

> **Updated 2026-09-25** (last change recorded in this doc). Current project status is in `MNG-Web-Design-System-Status.md`.

**Status:** ✅ **Specced from Figma 2026-09-01.** The Figma source is the **ModalsCenter** component set in the main MNG Web Design System file (`jFHYqhZbJjvWQmDI4myCsd`, Modal Panels page, node `3040:2262`), which Reader Dashboard v2.0 uses as a library component across its Profile Panel, Upgrade Subscription, Cancel Subscription, Update Payment Information, and Notification Preferences pages. Per Karl's direction 2026-09-01 ("Reader Dashboard designs are here..."), this Figma source superseded the live-site scrape below as the accurate source of truth — and the two agree almost exactly (see §6), which is a good cross-check. The spec models the Profile Panel's account-verification instance specifically (the same "email you a verification code" flow captured live below), `Device=TabletH` variant, instance id `6628:26265` in Reader Dashboard v2.0. A pilot rebuild of this modal was retired on 2026-09-25; use ModalsCenter.
**Live-site source (original audit, 2026-08-xx):** `preprod.eastbaytimes.com/dashboard` (Reader Dashboard), triggered from Profile → Display Name "Update"
**Implementation:** `react-modal` library (`ReactModal__Content` class), styled with Tailwind utility classes

⏸️ **Live-site follow-up paused:** the Reader Dashboard is its own separate React/Tailwind application, distinct from the main WordPress-based site (confirmed via Tailwind class names throughout, e.g. `md:pr-2`, `p-4 md:p-6`). It also appears to be mid-transition — see §5. Capturing this app's own responsive breakpoints (likely Tailwind's defaults, not the main site's 1039px nav breakpoint) is still an open task, but deeper audit of this live surface is on hold now that the Figma spec covers the actual design-system deliverable.

---

## 1. Example captured

Triggered by clicking "Update" next to Display Name: **"Please Verify Your Account Before Continuing"** — an account-verification prompt requiring an emailed code before the display-name edit can proceed. (Did not click through — stopped at "Maybe Later" to avoid actually triggering a verification email on a live account.)

## 2. Structure & measurements

**Backdrop:**
- Full-viewport, `position: fixed`
- `background: rgba(0, 0, 0, 0.45)`

**Card (`.ReactModal__Content`):**
- Fixed width: **444px** (Tailwind `w-[444px]` — not responsive/fluid; worth checking behavior on narrow viewports separately, not yet tested)
- Background: white
- Border radius: **8px**
- Box shadow: `0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)` — this is Tailwind's default `shadow-xl`
- Padding: `40px 40px 24px` (more breathing room on top/sides than bottom, presumably to sit closer to the action buttons)
- Close (✕) icon, top-right corner

**Heading:**
- `font-size: 20px`, `line-height: 24px`, `font-weight: 700`
- Color keyed to a Tailwind custom color named `text-gray-min` in source — worth finding out what hex this actually resolves to and whether "gray-min" is a naming convention already in use elsewhere in the codebase (possible existing token naming worth aligning with)
- Small info icon (ⓘ) sits inline before the heading text

**Body copy box:**
- A bordered inset box around the explanatory text (not just plain paragraph text)
- `border: 1px solid rgb(204, 202, 199)` (~`#CCCAC7`, Tailwind `border-gray-500`)
- `border-radius: 4px`
- `padding: 24px` (`p-4 md:p-6` — so this is itself responsive, unlike the fixed-width card)

**Actions:**
- Primary button ("Send Verification Code"): `background: rgb(0, 109, 163)` (`#006DA3`), white text, `font-weight: 700`, `border-radius: 4px`, `padding: 8px 16px` — same blue as the Disclosure link color (see `disclosure.md`).
- **Resolved 2026-08-27 — this was never actually a drift.** An earlier pass compared this button's color against a live read of the shared theme's `--primary` CSS variable and got a mismatch (`#006DA3` vs. `#006FB7`), written up as a possible drift. A follow-up pass changed the suspect but kept the same underlying mistake. The real explanation is a measurement error: `--primary` was read on `document.documentElement` (the `<html>` element). The WordPress Customizer's real per-site override is scoped to `div#page` (the main content wrapper), a descendant of `<html>`, not an ancestor — so it never flows back up to affect what `<html>` reports. Reading `--primary` correctly, on `#page` itself (which is what any real button on the page actually inherits from), returns `#006DA3` on both `preprod.eastbaytimes.com` and production `eastbaytimes.com` — an exact match for the button. Karl confirmed the site's real CSS architecture is a three-layer cascade (theme defaults → SCSS/CSS overrides, which include a generic `#006FB7` placeholder at `:root` → WordPress Customizer overrides scoped to `#page`, which is what actually renders) — this is that cascade working exactly as intended. No drift, no bug, no engineering question. Confirmed the same pattern (theme/SCSS placeholder overridden correctly by a `#page`-scoped Customizer value) on every other pilot site too.
- Secondary action ("Maybe Later"): plain text link, same blue, no button chrome, `padding: 4px 8px`

## 3. Tokens

The primary button/link color (`#006DA3`) maps cleanly to East Bay Times' own Brand `primary` token (since 2026-10-19 the shared The Mercury News + East Bay Times mode, `color/theme/primary`) — confirmed correct as of the 2026-08-27 resolution above. No open question remains here; this was a measurement-methodology issue on our side, not a production or documentation problem.

New tokens still needed:
- Modal backdrop: `rgba(0,0,0,0.45)`
- Modal card radius: `8px`
- Modal card shadow (Tailwind `shadow-xl` equivalent)
- Modal card fixed width: `444px`
- Inset body-box border color (`#CCCAC7`) and radius (`4px`)

## 4. Other findings from this pass

**Password "Update" is not a modal** — it navigates to a separate full page, `/reset-password/`. That page is essentially unstyled: Arial font, square corners, plain black 3px button border, default gray input border (`rgb(157,154,152)`) — none of it matches the design system. This is a design-debt gap to flag, not a pattern worth capturing faithfully.

**Subscription tab redirects elsewhere:** navigating to the Subscription tab on this preprod dashboard shows only a message: "To view and manage your Subscription Details, please visit the Reader Dashboard on dailynews.com." So subscription management has already moved off this surface entirely — another sign this whole area is mid-transition, reinforcing the pause noted at the top of this file.

## 5. Open items (live-site audit)

1. Only one true modal instance was captured. Other triggers (e.g. any destructive actions like canceling a subscription) were **not** explored — those are exactly the kind of irreversible/account-changing actions this session avoids triggering, so they'd need the user to click through themselves and report back.
2. Responsive behavior of the 444px fixed width at narrow viewports not tested.
3. Whether other modals in the system share this exact same shell (444px, 8px radius, same shadow) or vary by purpose is unconfirmed — this is one data point, not yet a proven pattern. **Partially resolved by the Figma spec below:** the ModalsCenter component IS reused across Upgrade Subscription, Cancel Subscription, Update Payment Information, and Notification Preferences — confirming this is one shared shell, not a one-off.
4. "text-gray-min" — **resolved.** This is exactly our `color/gray/min` token (#141414) — the live site's own naming convention already matches ours.
5. This app's own responsive breakpoints (likely Tailwind defaults — `sm`/`md`/`lg`/`xl`) not yet captured.

## 6. Figma spec — ModalsCenter measurements (2026-09-01)

Sourced directly from the ModalsCenter component's real geometry (not the generic/default variant):

| Property | Live-site value (§2 above) | Figma-measured value | Match? |
|---|---|---|---|
| Card width | 444px (fixed) | 444px | ✅ exact |
| Card radius | 8px | 8px (`radius/lg`) | ✅ exact |
| Card padding | 40/40/24 (implied left=40) | 40 top / 40 right / 24 bottom / 40 left | ✅ exact |
| Card border | none noted live (shadow instead) | 1px `color/gray/300` (#83827F) | Figma adds a border; live relies on shadow only — both may be true (shadow-xl could be layered on top of a subtle border we didn't visually distinguish live) |
| Heading | 20px/700, "text-gray-min" | Noto Sans Bold 20px, `color/gray/min` | ✅ exact |
| Body box border | `#CCCAC7`, radius 4px, padding 24 | `color/gray/500` (#CCCACA — effectively the same value, rounding only), radius 4px (`radius/sm`), padding 24 | ✅ exact |
| Primary button color | site's own `--primary` (e.g. #006DA3 on East Bay Times) | `color/brand/primary` — mode-bound per site | ✅ same mechanism, confirms it's brand-primary-bound rather than a hardcoded color |
| Backdrop opacity | 45% black | modeled at 50% black (not built into the component — see below) | close, not built as a literal component property either way |

**Not modeled as a component property:** the full-viewport backdrop dimming is a page-level behavior (how/where the modal is invoked), not part of the Modal component itself — same treatment either source would call for.

**Tokens used:** `radius/lg` = 8 and `radius/sm` = 4 (radius tokens aren't Figma variables yet — see the Status doc's open items), and `color/feedback/error` = #CC2B27 for the nested InLineMessage error variant's icon/title (exact match against the Figma source).

**Parts:** the primary CTA is a Button Primary (Default size) labeled "Send Verification Code"; the two text-link CTAs are Button Linkstyle (see `disclosure.md` §6); the inline error box is the InLineMessage error variant (see `empty-state-status-badge.md`).

**Not specced here:** the "Form Field" sub-component nested in the Body Container slot for flows that collect a code, and the rest of the ModalsCenter family (6 Device variants × many content combinations) — this doc covers the account-verification use case only.
