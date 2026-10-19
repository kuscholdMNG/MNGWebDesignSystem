---
name: Non-Button Hyperlink
slug: non-button-hyperlink
layer: core
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set: "Hyperlink"
figma_node: "6282:5568"
component_key: 121a469eea7d108efe028d82b734c60ffbbf6aab
variants: 4
tokens: non-button-hyperlink.tokens.json
skeleton: non-button-hyperlink.html
exported: 2026-10-14
---

# Non-Button Hyperlink

> Plain in-text hyperlink (not a button). Brand-primary text with a 1px bottom border: dashed at rest, solid on Hover/Pressed, 2px teal box on InFocus. Figma set name: `Hyperlink`.

## Figma

- File: **MNG Web Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Hyperlink` · 6282:5568](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5568) · key `121a469eea7d108efe028d82b734c60ffbbf6aab`
- Documentation frame: [Non-Button Hyperlink — Documentation](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-8121) · overview: [previews/non-button-hyperlink--documentation.png](previews/non-button-hyperlink--documentation.png)

## Properties

| Property | Default | Options |
|---|---|---|
| State | Default | Default, Hover, Pressed, InFocus |

## Variants

| Variant | Size | Node | Instances | Preview |
|---|---|---|---|---|
| `Default` | 133×23 | [6282:5569](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5569) | 4 | ![](previews/non-button-hyperlink--default.png) |
| `Hover` | 133×23 | [6282:5577](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5577) | 2 | ![](previews/non-button-hyperlink--hover.png) |
| `Pressed` | 133×23 | [7078:7681](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7681) | 1 | ![](previews/non-button-hyperlink--pressed.png) |
| `InFocus` | 133×25 | [6282:5585](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5585) | 1 | ![](previews/non-button-hyperlink--infocus.png) |

## Anatomy

Default variant `Default` (hidden layers marked):

- **State=Default** `COMPONENT`: 133×23, horizontal, gap 0, padding 0/0/1/0, hug×hug
  - **Label** `TEXT`: 133×22, hug×hug, "...hyperlink text...", Noto Sans Regular 16.5px

InFocus variant `InFocus`:

- **State=InFocus** `COMPONENT`: 133×25, horizontal, gap 0, padding 0/0/2/0, hug×hug
  - **Underline** `FRAME`: 133×23, horizontal, gap 0, padding 0/0/1/0, hug×hug
    - **Label** `TEXT`: 133×22, hug×hug, "...hyperlink text...", Noto Sans Regular 16.5px

## Component tokens

From `non-button-hyperlink.tokens.json`. References point at system tokens (`tokens/core/`, `tokens/themes/`); the CSS variable is `--mng-` + the token path. A literal value means the Figma layer isn't bound to a token.

| Token | Value |
|---|---|
| `non-button-hyperlink.base.label.color` | `{color.theme.primary}` |
| `non-button-hyperlink.base.label.font-family` | `{font.family.noto-sans}` |
| `non-button-hyperlink.base.label.font-size` | `{font.size.16-5}` |
| `non-button-hyperlink.base.label.font-weight` | `{font.weight.regular}` |
| `non-button-hyperlink.base.root.border-bottom-width` | 1px |
| `non-button-hyperlink.base.root.border-color` | `{color.theme.primary}` |
| `non-button-hyperlink.state-infocus.root.border-radius` | `{radius.sm}` |
| `non-button-hyperlink.state-infocus.root.border-style` | solid |
| `non-button-hyperlink.state-infocus.root.border-width` | 2px |
| `non-button-hyperlink.state-infocus.root.padding-bottom` | 2px |
| `non-button-hyperlink.state-infocus.underline.border-bottom-width` | 1px |
| `non-button-hyperlink.state-infocus.underline.border-color` | `{color.theme.primary}` |
| `non-button-hyperlink.state-infocus.underline.border-style` | dashed |
| `non-button-hyperlink.state-infocus.underline.padding-bottom` | 1px |
| `non-button-hyperlink.state-infocus.underline.label.color` | `{color.theme.primary}` |
| `non-button-hyperlink.state-infocus.underline.label.font-family` | `{font.family.noto-sans}` |
| `non-button-hyperlink.state-infocus.underline.label.font-size` | `{font.size.16-5}` |
| `non-button-hyperlink.state-infocus.underline.label.font-weight` | `{font.weight.regular}` |
| `non-button-hyperlink.state-default.root.border-style` | dashed |
| `non-button-hyperlink.state-default.root.padding-bottom` | 1px |
| `non-button-hyperlink.state-hover.root.border-style` | solid |
| `non-button-hyperlink.state-hover.root.padding-bottom` | 1px |
| `non-button-hyperlink.state-pressed.root.border-style` | solid |
| `non-button-hyperlink.state-pressed.root.padding-bottom` | 1px |

## Behavior and breakpoints

No Breakpoint property: one size at every width.

- Hugs its text at every breakpoint. No Breakpoint property.
- Implement the underline as `border-bottom`, not `text-decoration` (that is how Figma builds it).
- **Intentional, matches production (Karl, 2026-10-02):** 16.5px text, a teal (color/theme/primary) 2px focus box with 4px corners instead of the black ring, and the dashed underline kept inside the InFocus box (`Underline` › `Label`). Because the focus box is part of the layout, InFocus is 2px taller (25 vs 23px). Do not "fix" these.

## Accessibility

- Keyboard focus: the `InFocus` variant shows the focus ring (see Behavior). Never remove the focus indicator.
- Text color on its background must meet WCAG AA contrast (4.5:1 for text under 18px) in every theme; theme colors change per site.
- Icons inside a labelled control are decorative (`aria-hidden`); an icon-only control needs an accessible name (`aria-label`).

## Where it is used

Scope: instances in the Figma file **MNG Web Design System** only (other files that use the library are not counted). Total: **8**.

Inside components: InLineMessage ×3.

**Built from:** no nested components.

## Production

No production selector recorded yet. Production gaps go in `design-vs-production.md`.

## Known issues

1. **Values not bound to a token** (literal in the component tokens): `state-default` root padding-bottom = 1px; `state-hover` root padding-bottom = 1px; `state-pressed` root padding-bottom = 1px; `state-infocus` root padding-bottom = 2px; `state-infocus` underline padding-bottom = 1px.

## Files

- `non-button-hyperlink.tokens.json`: component tokens (DTCG 2025.10).
- `non-button-hyperlink.html`: HTML/CSS skeleton of every variant, using the `dist/` CSS variables (open it in a browser).
- `previews/`: PNG of every variant @2x and the documentation frame.

*Generated 2026-10-14 by `scripts/component-export/export.py` (EXPORT-STANDARD.md section 7). Edit the text in `scripts/component-export/registry.json`, not here.*
