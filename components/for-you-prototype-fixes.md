# For You prototype fixes: prompt for the prototype project

> **Updated 2026-10-23.** Started with the homepage tabs and the kicker letter spacing. More sections get added here as each For You component is built in Figma (tooltip, CTA panel, modal and Load More parity checks, card hover). When the list is complete, paste everything below the line into the For You Tab MVP project in one go. Status and node IDs: `components/for-you-ds-components-status.md`.

Every value below is an existing MNG Web Design System token (hex shown for Bold Coastal). Where production used a value with no token, it has been rounded to the nearest token (Karl, 2026-10-23), so don't reintroduce the old production values.

---

In `claude-design-v3/Main.dc.html`, update the For You prototype to match the MNG Web Design System components built from it. Use only the values given below. Don't add new colors, sizes or spacing, and don't change anything else on the page. When you're done, check at 340, 360, 768, 1024 and 1280 that nothing overflows the page.

## 1. Homepage tab bar (Editor's Picks / For You)

Rebuild the tab bar to match the production World Cup tabs (staging.dailylocal.com/world-cup/), with token values. Keep the tab labels, the order and the existing tab-switching behavior (`st.tab`).

Markup (production pattern):
- `<ul class="tabs-list" role="tablist">` > `<li role="presentation">` > `<button class="tab" role="tab" aria-selected="true|false" aria-controls="[panel id]">`
- Give each panel a matching id and `role="tabpanel"`. Update `aria-selected` when the tab changes.

Bar (`.tabs`):
- Full width, background #FFFFFF (color/gray/max), 1px solid #838280 bottom border (color/gray/300).

Nav (`.tabs-in`):
- max-width 1200px, centered, padding 0 24px (spacing/300).
- At ≤639px (the existing `@container page (max-width:639px)` query): padding 0.
- Tabs are left-aligned, not spread out: remove `justify-content:space-between`.
- Tab list: display flex, gap 24px (spacing/300), `overflow-x:auto` with the scrollbar hidden (`scrollbar-width:none` and `::-webkit-scrollbar{display:none}`), so extra tabs scroll sideways.

Tab (`.tab`):
- `font: 600 12px/normal 'Noto Sans', sans-serif`; letter-spacing 0; text-transform uppercase.
- padding 12px 16px (spacing/150, spacing/200) at every width (remove the 12px 14px mobile override).
- background none, border 0, plus a 2px solid transparent bottom border and margin-bottom -1px, so the active underline sits over the bar's 1px border.
- Default color #5E5D5C (color/gray/200).
- Hover color #141414 (color/gray/min).
- Active (`.tab.on` / `aria-selected="true"`): color #000000 (color/gray/black), border-bottom-color #007580 (color/theme/primary). Remove the old `::after` 3px teal bar and the teal active text.
- Focus-visible: outline 2px solid #000000, outline-offset -3px.
- Check that the tabs line up and the active underline covers the bar border.

## 2. Article kicker letter spacing

- `.kick`: letter-spacing 0 (was 1px), to match production's top nav items and Subscriber Only badge. Leave its other values as they are.

## 3. Article timestamp (already done 2026-10-23)

- `.tm` is `font: 400 13px/normal 'Noto Sans', sans-serif` (was 12px/16px), matching production's card meta. No change needed; listed so the prompt is complete.
