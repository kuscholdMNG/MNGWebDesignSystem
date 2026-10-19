---
name: Pop-Up Modal Close
slug: pop-up-modal-close
layer: core
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set: "Button Modal Close"
figma_node: "5335:16196"
component_key: 790ce7e08b7c4a4da2f4c22f29a5525fdcbea997
variants: 4
tokens: pop-up-modal-close.tokens.json
skeleton: pop-up-modal-close.html
exported: 2026-10-14
---

# Pop-Up Modal Close

> Circular 32px close (X) button for pop-up modals (ModalsCenter, Modals/*). Light-gray circle at rest, white on Hover/Pressed; InFocus keeps the Default look and adds the ring.

## Figma

- File: **MNG Web Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Button Modal Close` · 5335:16196](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16196) · key `790ce7e08b7c4a4da2f4c22f29a5525fdcbea997`
- Documentation frame: [Pop-Up Modal Close — Documentation](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7807) · overview: [previews/pop-up-modal-close--documentation.png](previews/pop-up-modal-close--documentation.png)

## Properties

| Property | Default | Options |
|---|---|---|
| State | Default | Default, Hover, Pressed, InFocus |

## Variants

| Variant | Size | Node | Instances | Preview |
|---|---|---|---|---|
| `Default` | 32×32 | [5335:16193](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16193) | 23 | ![](previews/pop-up-modal-close--default.png) |
| `Hover` | 32×32 | [5335:16194](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16194) | 1 | ![](previews/pop-up-modal-close--hover.png) |
| `Pressed` | 32×32 | [7078:7686](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7686) | 1 | ![](previews/pop-up-modal-close--pressed.png) |
| `InFocus` | 32×32 | [5335:16195](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16195) | 1 | ![](previews/pop-up-modal-close--infocus.png) |

## Anatomy

Default variant `Default` (hidden layers marked):

- **State=Default** `COMPONENT`: 32×32, horizontal, gap 0, padding 0/0/0/0, fixed×fixed
  - **Icon** `INSTANCE`: 12×12, horizontal, gap 8, padding 0/0/0/0, fixed×fixed, instance of Icons (Name=close)

InFocus variant `InFocus`:

- **State=InFocus** `COMPONENT`: 32×32, horizontal, gap 0, padding 0/0/0/0, fixed×fixed
  - **Icon** `INSTANCE`: 12×12, horizontal, gap 8, padding 0/0/0/0, fixed×fixed, instance of Icons (Name=close)
  - **Focus Ring** `FRAME`: 34×34, fixed×fixed, absolute

## Component tokens

From `pop-up-modal-close.tokens.json`. References point at system tokens (`tokens/core/`, `tokens/themes/`); the CSS variable is `--mng-` + the token path. A literal value means the Figma layer isn't bound to a token.

| Token | Value |
|---|---|
| `pop-up-modal-close.state-infocus.focus-ring.border-color` | `{color.gray.black}` |
| `pop-up-modal-close.state-infocus.focus-ring.border-radius` | 40px |
| `pop-up-modal-close.state-infocus.focus-ring.border-style` | solid |
| `pop-up-modal-close.state-infocus.focus-ring.border-width` | 2px |
| `pop-up-modal-close.state-infocus.root.background` | `{color.gray.600}` |
| `pop-up-modal-close.state-infocus.root.border-color` | `{color.gray.400}` |
| `pop-up-modal-close.base.icon.height` | 12px |
| `pop-up-modal-close.base.icon.icon-color` | `{color.gray.min}` |
| `pop-up-modal-close.base.icon.width` | 12px |
| `pop-up-modal-close.base.root.border-radius` | 40px |
| `pop-up-modal-close.base.root.border-style` | solid |
| `pop-up-modal-close.base.root.border-width` | 1px |
| `pop-up-modal-close.base.root.height` | 32px |
| `pop-up-modal-close.base.root.width` | 32px |
| `pop-up-modal-close.state-default.root.background` | `{color.gray.600}` |
| `pop-up-modal-close.state-default.root.border-color` | `{color.gray.400}` |
| `pop-up-modal-close.state-hover.root.background` | `{color.gray.max}` |
| `pop-up-modal-close.state-hover.root.border-color` | `{color.gray.500}` |
| `pop-up-modal-close.state-pressed.root.background` | `{color.gray.max}` |
| `pop-up-modal-close.state-pressed.root.border-color` | `{color.gray.500}` |

## Behavior and breakpoints

No Breakpoint property: one size at every width.

- Single size at every breakpoint (32×32 in every state). No Breakpoint property.
- Sits in the modal header, top-right; see ModalsCenter in the main file.
- **Focus ring:** InFocus adds one `Focus Ring` frame, absolutely positioned 1px outside the element, with a 2px OUTSIDE stroke bound to `color/gray/black`. It draws outside the component and never changes its size or moves anything inside or around it (the 32px circle reads as 38px with the ring). In CSS: `outline: 2px solid var(--mng-color-gray-black); outline-offset: 1px;` or an absolutely positioned pseudo-element; never a border or padding change.

## Accessibility

- Keyboard focus: the `InFocus` variant shows the focus ring (see Behavior). Never remove the focus indicator.
- Text color on its background must meet WCAG AA contrast (4.5:1 for text under 18px) in every theme; theme colors change per site.
- Icons inside a labelled control are decorative (`aria-hidden`); an icon-only control needs an accessible name (`aria-label`).

## Where it is used

Scope: instances in the Figma file **MNG Web Design System** only (other files that use the library are not counted). Total: **26**.

Inside components: Modals ×7, ModalsCenter ×6.
Placed on pages: Modal Panels | 2025.12.29 ×7.

**Built from:** Icons ×4
Icon variants: `close` ×4.

## Production

No production selector recorded yet. Production gaps go in `design-vs-production.md`.

## Known issues

1. **Margin not specified** (open spec gap, per the Figma Specifications column).
2. **Values not bound to a token** (literal in the component tokens): `state-infocus` focus-ring border-radius = 40px; `base` root border-radius = 40px.

## Files

- `pop-up-modal-close.tokens.json`: component tokens (DTCG 2025.10).
- `pop-up-modal-close.html`: HTML/CSS skeleton of every variant, using the `dist/` CSS variables (open it in a browser).
- `previews/`: PNG of every variant @2x and the documentation frame.

*Generated 2026-10-14 by `scripts/component-export/export.py` (EXPORT-STANDARD.md section 7). Edit the text in `scripts/component-export/registry.json`, not here.*
