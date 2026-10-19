---
name: Action Button
slug: action-button
layer: core
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set: "Button Action"
figma_node: "7075:6357"
component_key: f2d61dd8cfa1619da4987e7b90ac60f2fbb6c102
variants: 4
tokens: action-button.tokens.json
skeleton: action-button.html
exported: 2026-10-14
---

# Action Button

> Small icon + label utility action (documented example: "Copy Link"). No box at rest; a 1px black border appears on Hover/Pressed. Figma set name: `Button Action`.

## Figma

- File: **MNG Web Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Button Action` · 7075:6357](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6357) · key `f2d61dd8cfa1619da4987e7b90ac60f2fbb6c102`
- Documentation frame: [Action Button — Documentation](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6715) · overview: [previews/action-button--documentation.png](previews/action-button--documentation.png)

## Properties

| Property | Default | Options |
|---|---|---|
| State | Default | Default, Hover, Pressed, InFocus |

## Variants

| Variant | Size | Node | Instances | Preview |
|---|---|---|---|---|
| `Default` | 95×32 | [7075:6358](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6358) | 1 | ![](previews/action-button--default.png) |
| `Hover` | 95×32 | [7075:6415](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6415) | 1 | ![](previews/action-button--hover.png) |
| `Pressed` | 95×32 | [7075:6513](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6513) | 1 | ![](previews/action-button--pressed.png) |
| `InFocus` | 95×32 | [7075:6464](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6464) | 1 | ![](previews/action-button--infocus.png) |

## Anatomy

Default variant `Default` (hidden layers marked):

- **State=Default** `COMPONENT`: 95×32, horizontal, gap 1, padding 0/0/0/0, hug×hug
  - **Button** `FRAME`: 95×32, horizontal, gap 8, padding 8/8/8/8, hug×hug
    - **Content** `FRAME`: 79×16, horizontal, gap 4, padding 0/0/0/0, hug×hug
      - **Icon Left** `INSTANCE`: 16×16, horizontal, gap 8, padding 0/0/0/0, fixed×fixed, instance of Icons (Name=content_copy)
      - **Label** `TEXT`: 59×9, hug×hug, "Copy Link", Noto Sans Bold 12px
      - **Icon Right** `INSTANCE`: 16×16, horizontal, gap 8, padding 0/0/0/0, fixed×fixed, instance of Icons (Name=content_copy), **hidden**

InFocus variant `InFocus`:

- **State=InFocus** `COMPONENT`: 95×32, horizontal, gap 1, padding 0/0/0/0, hug×hug
  - **Button** `FRAME`: 95×32, horizontal, gap 8, padding 8/8/8/8, hug×hug
    - **Content** `FRAME`: 79×16, horizontal, gap 4, padding 0/0/0/0, hug×hug
      - **Icon Left** `INSTANCE`: 16×16, horizontal, gap 8, padding 0/0/0/0, fixed×fixed, instance of Icons (Name=content_copy)
      - **Label** `TEXT`: 59×9, hug×hug, "Copy Link", Noto Sans Bold 12px
      - **Icon Right** `INSTANCE`: 16×16, horizontal, gap 8, padding 0/0/0/0, fixed×fixed, instance of Icons (Name=content_copy), **hidden**
  - **Focus Ring** `FRAME`: 97×34, fixed×fixed, absolute

## Component tokens

From `action-button.tokens.json`. References point at system tokens (`tokens/core/`, `tokens/themes/`); the CSS variable is `--mng-` + the token path. A literal value means the Figma layer isn't bound to a token.

| Token | Value |
|---|---|
| `action-button.base.button.border-color` | `{color.gray.min}` |
| `action-button.base.button.border-radius` | `{radius.sm}` |
| `action-button.base.button.border-style` | solid |
| `action-button.base.button.border-width` | 1px |
| `action-button.base.button.padding-bottom` | `{spacing.100}` |
| `action-button.base.button.padding-left` | `{spacing.100}` |
| `action-button.base.button.padding-right` | `{spacing.100}` |
| `action-button.base.button.padding-top` | `{spacing.100}` |
| `action-button.base.button.content.gap` | `{spacing.050}` |
| `action-button.base.button.content.icon-left.height` | 16px |
| `action-button.base.button.content.icon-left.icon-color` | `{color.gray.min}` |
| `action-button.base.button.content.icon-left.width` | 16px |
| `action-button.base.button.content.label.color` | `{color.gray.min}` |
| `action-button.base.button.content.label.font-family` | `{font.family.noto-sans}` |
| `action-button.base.button.content.label.font-size` | `{font.size.12}` |
| `action-button.base.button.content.label.font-weight` | `{font.weight.bold}` |
| `action-button.base.root.border-radius` | `{radius.sm}` |
| `action-button.state-infocus.focus-ring.border-color` | `{color.gray.black}` |
| `action-button.state-infocus.focus-ring.border-radius` | `{radius.sm}` |
| `action-button.state-infocus.focus-ring.border-style` | solid |
| `action-button.state-infocus.focus-ring.border-width` | 2px |

## Behavior and breakpoints

No Breakpoint property: one size at every width.

- Single size at every breakpoint (95×32, HUG). No Breakpoint property. It stays compact (32px), not 40px (Karl, 2026-10-02).
- Width hugs icon + label; swapping the label changes the width.
- **Focus ring:** InFocus adds one `Focus Ring` frame, absolutely positioned 1px outside the element, with a 2px OUTSIDE stroke bound to `color/gray/black`. It draws outside the component and never changes its size or moves anything inside or around it (a 40px button reads as 46px with the ring). In CSS: `outline: 2px solid var(--mng-color-gray-black); outline-offset: 1px;` or an absolutely positioned pseudo-element; never a border or padding change.

## Accessibility

- Keyboard focus: the `InFocus` variant shows the focus ring (see Behavior). Never remove the focus indicator.
- Text color on its background must meet WCAG AA contrast (4.5:1 for text under 18px) in every theme; theme colors change per site.
- Icons inside a labelled control are decorative (`aria-hidden`); an icon-only control needs an accessible name (`aria-label`).

## Where it is used

Scope: instances in the Figma file **MNG Web Design System** only (other files that use the library are not counted). Total: **4**.


**Built from:** Icons ×4
Icon variants: `content_copy` ×4.

## Production

No production selector recorded yet. Production gaps go in `design-vs-production.md`.

## Known issues

1. **Name swap (2026-10-02).** This documented set is `Button Action` (`7075:6357`). The older library set on the same page (`5417:3876`, formerly `Button Action`, kept for Reader Dashboard files) is now `Action Button`. The documentation frame keeps the page title "Action Button".
2. **Single-purpose reference.** This set only documents "Copy Link". The older `Action Button` library set bundles Resend Invitation, Link Copied, Share (Android/Apple/Unknown), Preview Most Recent, Save/Saved, Gift Article, Remove, Cancel and Delete as hidden layers, none exposed as variants. To render another action, swap the icon instance and the label text.
3. **Hidden trailing icon.** Every variant carries a hidden `Icon Right` (content_copy) after the label. It is never shown; ignore it when rendering.
4. **Margin not specified** (open spec gap, per the Figma Specifications column).

## Files

- `action-button.tokens.json`: component tokens (DTCG 2025.10).
- `action-button.html`: HTML/CSS skeleton of every variant, using the `dist/` CSS variables (open it in a browser).
- `previews/`: PNG of every variant @2x and the documentation frame.

*Generated 2026-10-14 by `scripts/component-export/export.py` (EXPORT-STANDARD.md section 7). Edit the text in `scripts/component-export/registry.json`, not here.*
