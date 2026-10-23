# MNG Web Design System — instructions for Claude

> **Updated 2026-10-23:** moved here from the Claude project instructions and merged with section 7 ("Standing rules") of `MNG-Web-Design-System-Status.md`, so the rules live in one place, in the repo. This file is the source of truth for how to work in this project. Change a rule here; the project instructions only point to this file.

We are building a full design system based on in-production websites in our footprint.

## Start of every session

- The project lives in GitHub: https://github.com/kuscholdMNG/mng_web_ds. The local copy is `~/Github/mng_web_ds` on Karl's Mac. If that folder isn't connected to the session, ask Karl to connect it. The Google Drive project folder is retired; never save to it.
- Read `MNG-Web-Design-System-Status.md`. It's the source of truth for current status and open items.
- Read `README.md` before saving anything, and follow its names, folder map, filing rules and "Working in GitHub" section. Update existing files in place. Never create copies like "file (1).md", zips, or catch-all folders like "Claude outputs".
- When you finish work that changes status, update the status doc in place, with the date at the top ("Updated YYYY-MM-DD for …").

## GitHub

- Commit every change with a clear message and push. Value changes that need Karl's review go on a branch with a pull request; everything else goes straight to `main`.
- Never commit credentials, `.DS_Store` files, `__pycache__` / `.pyc` files or zips.

## Names

- Prose and Figma: "MNG Web Design System". GitHub repo and local folder: `mng_web_ds`. Claude project: "MNGWebDesignSystem". Code identifiers and the dist package: `mng_web_design_system`.

## Figma files

- MNG Web Design System (main library): `jFHYqhZbJjvWQmDI4myCsd`
- WordPress Elements (page templates, Masthead): `b1iZxkFwtAYq9rElmnCAzd`
- Reader Dashboard v2.0: `PhXogWaQcnNSnQqxyRu4b2`. Part of the MNG Web Design System; not added to the token files yet.
- CRUX Style Library: `uwKNDnGRH0otKDrgYiWmUw`. Read-only. Never edit.
- Never move components between files, because live instances depend on them. Renaming is safe. Value changes need Karl's review.
- Never use `figma_arrange_component_set` or `autoArrange: true`. It once deleted the Button / Primary set. Position components by hand.
- Never edit or audit the main file's "*** Style Guide | Reader Dashboard things" page (Karl, 2026-10-02). It's covered by Reader Dashboard v2.0.
- On the Buttons page, keep the older `Button` sets in `Frame 13001` as they are (Karl, 2026-10-02).
- The Fonts page documents fallbacks and font changes, so it keeps its non-Noto specimens. Everywhere else, text is Noto Sans or Noto Serif.
- The Figma design-system audit tool reports 0/100 for "Token Architecture" on this plan. That's a tool limitation, not a real defect.

## Exports

- Every token and component export follows `EXPORT-STANDARD.md`: DTCG 2025.10 `.tokens.json` only; hex is the color source of truth (RGBA and color objects are generated); Figma → code only; never add to the legacy `figma-exports/`; never hand-edit `dist/`. Preview PNGs are committed to GitHub; no Git LFS.
- Breakpoints: two official sets for now. MNG Device breakpoints (core; Figma screen widths 340/360/768/1024/1280; Reader Dashboard) and WordPress grid breakpoints (320/640/800/1040/1280; WordPress themes incl. Obituaries; legacy). The goal is the Device set only.

## Design vs. production

- Design (Figma) is the source of truth. Tokens always carry design spec values. Never change a token to match production. Mark the gap in Figma with the red-dashed outline and log it in `design-vs-production.md`.
- Engineering handoff: `design-vs-production.md`, read on GitHub (https://github.com/kuscholdMNG/mng_web_ds/blob/main/design-vs-production.md). Fixes checklist: the "MNG color fixes checklist" Google Sheet (https://docs.google.com/spreadsheets/d/17oRvVmGWZgnfvKzupvgX7SEtA9b-uK6guqyufM4bxBk/edit), tabs "Color fixes" and "Other fixes". When a fix changes, update the sheet and the repo together.
- Documented exceptions (currently only Greeley Tribune's primary, light and dark) are part of the design, not mismatches.
- Use DTCG token naming (e.g. `color/theme/primary`, `font/size/16`).
- Sub-site colors (`subsite-custom`) cascade from the parent theme: a theme's value is shown on every related sub-theme style guide unless the sub-theme has its own override (Denver Post, The Press Democrat, St. Paul Pioneer Press, The Baltimore Sun, South Florida Sun Sentinel). If the parent theme has no value, it's documented as missing on every related sub-theme.
- On the Color Pallets page, a style guide shows a production column only when production differs from the design spec. With no mismatch, it shows the design spec column alone.

## Icons

- Icons keep their production (icon font) names, always, unless an icon is brand new (Karl, 2026-10-22).
- In Figma, each icon shows its production name plus a gray "IcoMoon: name" (original IcoMoon artwork, the name to search for in IcoMoon) or a blue "Custom" (MNG artwork). The same facts are in `tokens/icons/icons.json` (`icomoonName`, `artworkSource`).
- Engineering gets the icon font package directly from the MNG IcoMoon project.

## Checking live sites

- Check all the standard review sites, not just one: ocregister, denverpost, chicagotribune, orlandosentinel, canoncitydailyrecord, mcall.
- Never resize browser windows. When a check needs a different viewport width, stop and ask Karl to resize the window himself. Say which width is needed, and continue only after he confirms.
- Wait at least 10 seconds for a page to load before measuring. Read colors on `#page`, not the page root.
- Never enter passwords or credentials on any site, even if provided. Karl logs in himself.
- On Reader Dashboard Gifted Articles, never click "Remove".
