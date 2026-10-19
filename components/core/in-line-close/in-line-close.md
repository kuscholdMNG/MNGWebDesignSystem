---
name: In-Line Close
slug: in-line-close
layer: core
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set: "Button In-Line Close"
figma_node: "5335:16200"
component_key: f0d7dc9ffa766ef6e54c1d46416a37d1405acaa6
variants: 4
tokens: in-line-close.tokens.json
skeleton: in-line-close.html
exported: 2026-10-14
---

# In-Line Close

> Close (X) button for in-line panels and alerts (InLineMessage, ModalsOffset). Bare 12px icon in a 40px hit area at rest; the 28px `Box` gets a white fill and 1px near-black border on Hover/Pressed.

## Figma

- File: **MNG Web Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Button In-Line Close` · 5335:16200](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16200) · key `f0d7dc9ffa766ef6e54c1d46416a37d1405acaa6`
- Documentation frame: [In-Line Close — Documentation](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7975) · overview: [previews/in-line-close--documentation.png](previews/in-line-close--documentation.png)

## Properties

| Property | Default | Options |
|---|---|---|
| State | Default | Default, Hover, Pressed, InFocus |

## Variants

| Variant | Size | Node | Instances | Preview |
|---|---|---|---|---|
| `Default` | 40×40 | [5335:16197](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16197) | 96 | ![](previews/in-line-close--default.png) |
| `Hover` | 40×40 | [5335:16198](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16198) | 2 | ![](previews/in-line-close--hover.png) |
| `Pressed` | 40×40 | [7078:7697](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7697) | 1 | ![](previews/in-line-close--pressed.png) |
| `InFocus` | 40×40 | [5335:16199](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16199) | 1 | ![](previews/in-line-close--infocus.png) |

## Anatomy

Default variant `Default` (hidden layers marked):

- **State=Default** `COMPONENT`: 40×40, horizontal, gap 8, padding 0/0/0/0, hug×hug
  - **Button** `FRAME`: 40×40, horizontal, gap 0, padding 0/0/0/0, fixed×fixed
    - **Box** `FRAME`: 28×28, horizontal, gap 8, padding 8/8/8/8, hug×hug
      - **Icon** `INSTANCE`: 12×12, horizontal, gap 8, padding 0/0/0/0, fixed×fixed, instance of Icons (Name=close)

InFocus variant `InFocus`:

- **State=InFocus** `COMPONENT`: 40×40, horizontal, gap 8, padding 0/0/0/0, hug×hug
  - **Button** `FRAME`: 40×40, horizontal, gap 0, padding 0/0/0/0, fixed×fixed
    - **Box** `FRAME`: 28×28, horizontal, gap 8, padding 8/8/8/8, hug×hug
      - **Icon** `INSTANCE`: 12×12, horizontal, gap 8, padding 0/0/0/0, fixed×fixed, instance of Icons (Name=close)
  - **Focus Ring** `FRAME`: 42×42, fixed×fixed, absolute

## Component tokens

From `in-line-close.tokens.json`. References point at system tokens (`tokens/core/`, `tokens/themes/`); the CSS variable is `--mng-` + the token path. A literal value means the Figma layer isn't bound to a token.

| Token | Value |
|---|---|
| `in-line-close.base.button.border-radius` | 40px |
| `in-line-close.base.button.height` | 40px |
| `in-line-close.base.button.width` | 40px |
| `in-line-close.base.button.box.background` | `{color.gray.max}` |
| `in-line-close.base.button.box.border-color` | `{color.gray.min}` |
| `in-line-close.base.button.box.border-radius` | `{radius.sm}` |
| `in-line-close.base.button.box.border-style` | solid |
| `in-line-close.base.button.box.border-width` | 1px |
| `in-line-close.base.button.box.padding-bottom` | `{spacing.100}` |
| `in-line-close.base.button.box.padding-left` | `{spacing.100}` |
| `in-line-close.base.button.box.padding-right` | `{spacing.100}` |
| `in-line-close.base.button.box.padding-top` | `{spacing.100}` |
| `in-line-close.base.button.box.icon.height` | 12px |
| `in-line-close.base.button.box.icon.icon-color` | `{color.gray.min}` |
| `in-line-close.base.button.box.icon.width` | 12px |
| `in-line-close.state-infocus.focus-ring.border-color` | `{color.gray.black}` |
| `in-line-close.state-infocus.focus-ring.border-radius` | `{radius.sm}` |
| `in-line-close.state-infocus.focus-ring.border-style` | solid |
| `in-line-close.state-infocus.focus-ring.border-width` | 2px |

## Behavior and breakpoints

No Breakpoint property: one size at every width.

- Single size at every breakpoint (40×40 hit area). No Breakpoint property.
- Every state has the same layers (`Button` › `Box` › `Icon`); the `Box` has no fill or border in Default and InFocus.
- Usually placed top-right of an InLineMessage panel, with the hit area aligned to the panel padding.
- **Focus ring:** InFocus adds one `Focus Ring` frame, absolutely positioned 1px outside the element, with a 2px OUTSIDE stroke bound to `color/gray/black`. It draws outside the component and never changes its size or moves anything inside or around it (the ring surrounds the 40px hit area with 4px corners, matching the Hover/Pressed box). In CSS: `outline: 2px solid var(--mng-color-gray-black); outline-offset: 1px;` or an absolutely positioned pseudo-element; never a border or padding change.

## Accessibility

- Keyboard focus: the `InFocus` variant shows the focus ring (see Behavior). Never remove the focus indicator.
- Text color on its background must meet WCAG AA contrast (4.5:1 for text under 18px) in every theme; theme colors change per site.
- Icons inside a labelled control are decorative (`aria-hidden`); an icon-only control needs an accessible name (`aria-label`).

## Where it is used

Scope: instances in the Figma file **MNG Web Design System** only (other files that use the library are not counted). Total: **100**.

Inside components: InLineMessage ×59, ModalsOffset ×9.
Placed on pages: In-Line Content Containers | 2026.01.02 ×5, Alerts and Icons ×3, Buttons | 2026.09.30 ×1.
17 instances are nested inside other instances.

**Built from:** Icons ×4
Icon variants: `close` ×4.

## Production

No production selector recorded yet. Production gaps go in `design-vs-production.md`.

## Known issues

1. **Margin not specified** (open spec gap, per the Figma Specifications column).
2. **Values not bound to a token** (literal in the component tokens): `base` button border-radius = 40px.

## Files

- `in-line-close.tokens.json`: component tokens (DTCG 2025.10).
- `in-line-close.html`: HTML/CSS skeleton of every variant, using the `dist/` CSS variables (open it in a browser).
- `previews/`: PNG of every variant @2x and the documentation frame.

*Generated 2026-10-14 by `scripts/component-export/export.py` (EXPORT-STANDARD.md section 7). Edit the text in `scripts/component-export/registry.json`, not here.*
