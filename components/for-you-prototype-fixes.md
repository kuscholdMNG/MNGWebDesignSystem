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

## 4. Feed header subhead

The line under "While You Were Away" ("Based on what you read." + the info button), in both copies of `.fyh`:

- `.fyh p`: `font: 400 13px/normal 'Noto Sans', sans-serif`; color #5E5D5C (color/gray/200); keep the 6px top margin; gap between the text and the info button 4px (spacing/050; was 6px).
- Info icon (`.tipb .ic`): 12px, color #5E5D5C (was 13px). Keep the button's invisible 12px hit-area extension and focus outline.
- Leave the eyebrow (`.eb`) as it is.

## 5. Load More (replaces the "Load More Articles" link)

Use the production Load More (the same rule as production's `.load-more` / `.show-more-videos`, Figma: WordPress Elements ▸ Show More Affordance). Apply to both copies of the `.lm` block. Keep the click behavior (`loadMore`, `canMore`).

- Change the label to "Load More" (shown uppercase by CSS). Make the button a full-width block; remove `.btn-link` from it.
- Copy production's CSS exactly, including its colors (this one deliberately uses production values, not tokens):

```css
.load-more { position: relative; display: inline-block; width: 100%; padding: 40px 0; border: 0; border-top: 1px solid #D7D6D2; background: none; font: 700 16px/1 'Noto Sans', sans-serif; color: #007580; text-align: center; text-transform: uppercase; cursor: pointer; }
.load-more::before { content: ""; position: absolute; left: 50%; top: -5px; width: 35px; height: 35px; background-color: #FBFBFB; border-bottom: 1px solid #D7D6D2; border-left: 1px solid #D7D6D2; transform: rotate(-45deg) translateY(-50%); }
.load-more:hover { color: #0A0908; }
.load-more:focus-visible { outline: 2px solid #000000; outline-offset: 5px; }
```

- Remove the old `.lm` padding (16px 0 8px) so the 40px above and below comes from the button. It's the same at every width; don't add breakpoints.

## 6. Non-subscriber CTA panel (reuse the Reader Dashboard "subscribe" panel)

Replace the `.cta` block with the MNG Web Design System InLineMessage panel used by Reader Dashboard for locked features (Figma: In-Line Content Containers ▸ InLineMessage, Priority=Medium, Location=DashSubsNonSub, PanelType=Alert).

Content:
- Title: "Your personalized feed is waiting"
- Description: "Subscribe to unlock a feed tailored to what you actually read — local news, sports, tech, and more."
- One button: "Subscribe Now" (the existing primary button, `.btn .btn-p`).
- Remove the padlock circle (`.cta-ic`), the "Sign in" button and the price line ("Starting at $1.99/week…").

Styles:
- Panel: background #F1EFEB (color/gray/600), border-radius 5px (radius/utility), no border, no shadow. Full width of the feed column.
- Padding 24px (spacing/300) and 16px between rows (spacing/200); at ≤639px, padding 16px (spacing/200) and 8px between rows (spacing/100).
- Header row: the `notification2` icon (16px, icomoon U+E94E) then the title, 8px apart (spacing/100), left-aligned. Icon and title color #856A00 (color/feedback/medium).
- Title: `font: 700 16px/normal 'Noto Sans', sans-serif`.
- Description: `font: 400 16px/normal 'Noto Sans', sans-serif`, color #141414 (color/gray/min), left-aligned.
- Button: centered under the description, at its natural width.
- Keep the panel's spacing from the content above and below as it is now.

## 7. Welcome to For You modal (one small fix)

The modal (`.mc`) already matches the MNG Web Design System ModalsCenter: 444px card (24px narrower than the viewport on phones), 8px radius, 1px gray/300 border, shadow 0 8px 16px rgba(0,0,0,.2) (shadow/lg), 40/40/24 padding (24 at ≤639px), 16px gaps, 20px Bold title and 16px subtitle, the bordered body box (gray/500, 4px radius, 24px padding, 16px at ≤639px), the centered primary button, the round close button (32px, gray/600 with a gray/400 edge; white with a gray/500 edge on hover), and the 50% black backdrop.

- Change the card border color from #83827F to #838280 (the exact color/gray/300 value).
- Keep the `info` icon in the header (ModalsCenter's sample uses `notification`; the icon is content and can change).

## 8. Article timestamp (already done 2026-10-23)

- `.tm` is `font: 400 13px/normal 'Noto Sans', sans-serif` (was 12px/16px), matching production's card meta. No change needed; listed so the prompt is complete.
