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

## 3. Feed header info toggletip (replaces the hover tooltip)

The info icon after "Based on what you read." becomes a click/tap **toggletip**, matching the MNG Web Design System Tooltip component (Type=Toggletip, Placement=Bottom). Apply this to both copies of the feed header (`.fyh`).

Behavior:
- Remove the hover/focus-within reveal (`.tipw:hover .tip, .tipw:focus-within .tip`). The box opens when the info button is clicked or tapped, and closes on a second click, the close button, Esc, or a click outside it. When it closes from the close button or Esc, move focus back to the info button.
- Info button (`.tipb`): add `aria-expanded="false|true"` and `aria-controls` pointing at the box. Change its aria-label to "About this feed". Keep its icon, size, the 12px invisible hit-area extension and the focus-visible outline.
- Box (`.tip`): give it an id and `role="status"` (so the text is read when it opens); remove `aria-hidden`; use the `hidden` attribute when closed.

Box styles:
- Position: below the info button, centered on it, 8px gap (spacing/100), with a caret pointing up at the button.
- width 275px (max-width calc(100vw - 32px) so it never overflows on phones); background #FFFFFF (color/gray/max); 1px solid #838280 border (color/gray/300); border-radius 4px (radius/sm); box-shadow 0 8px 16px 0 rgba(0,0,0,.2) (shadow/lg).
- Layout: a row with the text area and the close button, top-aligned. Text area padding 12px (spacing/150).
- Text: `font: 400 13px/normal 'Noto Sans', sans-serif`, color #393938 (color/gray/100), not italic. Keep the placeholder copy: "Placeholder text with more information about this feature."
- Close button: 40×40px, transparent, a 12px "close" icon in #000000, `aria-label="Close"`. Focus-visible: 2px solid #000000 outline.
- Caret: 12px wide × 6px tall, pointing up, centered, with the same #838280 1px edge and #FFFFFF fill, overlapping the box's top border so it looks like one shape.

## 4. Article timestamp (already done 2026-10-23)

- `.tm` is `font: 400 13px/normal 'Noto Sans', sans-serif` (was 12px/16px), matching production's card meta. No change needed; listed so the prompt is complete.
