# Article Page — To-Do

> **Updated 2026-10-14:** added item 2 (special investigative header template). 2026-10-02: current Figma file names.

Running list of Article-page-specific gaps found during component audits, kept separate from the general Masthead/breakpoint audit so Article-page work doesn't get buried in it.

---

## 1. Trust/Source tooltip component — needs to be built in Figma

**Found:** 2026-09-15, during the masthead breakpoint audit (`breakpoint-audit.md`), 375px pass, Article page, default load.

**What production shows:** A small tooltip/popover appears over the headline area on article pages, anchored to a trust/sourcing-standard indicator near the "NEWS · [Section]" label. It's a white box with a speech-bubble pointer and its own close (X) button, containing this copy:

> "Based on facts, either witnessed and verified directly by the reporter, or reported and confirmed from knowledgeable sources."

Screenshot reference: captured live on ocregister.com at 375px width (see masthead audit for the full screenshot).

**Gap:** No equivalent component exists yet in Figma (checked WordPress Elements → Menus and Parts, and the Masthead component set — not present there or elsewhere as far as this audit covered).

**Action needed:** Build this as a proper Figma component — tooltip/popover with pointer, close (X) affordance, and the trust-standard copy above as editable text. Confirm with Karl whether this should live near the Masthead/article-header components or as its own standalone "Trust Indicator" component, and whether the copy is static or varies by content type.

**Status:** Open.

---

## 2. Special investigative header template — find it in production

**Found:** 2026-10-14, during the breakpoint inventory (`tokens/breakpoint-inventory.json`). The theme CSS has a special investigative report template (`#content.special-investigative-header .special-investigative`: section header, cover, feature-top, about and callout sections) with its own breakpoints (`max-width: 730 / 1150px`, plus 500 / 600 / 750 / 900 / 1024).

**Gap:** No live page using it was found on the 6 review sites (Chicago Tribune's Investigations section uses the normal section layout), and there's nothing for it in WordPress Elements.

**Action needed:** when more article pages are added to WordPress Elements, find a live special investigative report page, build the template in Figma and classify its breakpoints (Karl, 2026-10-14). Until then they're left out of the breakpoint inventory and design-vs-production entry 33.

**Status:** Open (future).
