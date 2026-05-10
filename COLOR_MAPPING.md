# Color Mapping: From Artist Palette to Zed Theme

This document explains how artist palette colors are mapped to Zed theme properties, using Van Gogh as an example.

## Source Palette

Each artist definition in `generate.py` holds raw colors — statistically-derived master palette values mapped to semantic roles:

```
bg:             #161210    (deep warm black — darkest tones)
editor_bg:      #1a1612
surface:        #221e18
elevated:       #2c2820
text:           #cdc4a2    (warm parchment — lightest tone)
text_muted:     #8e8870
border:         #383020
border_focused: #6e8bc8    (blue — the one cool outlier)

Syntax:
  keyword:      #6e8bc8    (blue)
  string:       #d2b45e    (golden yellow)
  function:     #7b9f6b    (olive green)
  type:         #c88a4a    (burnt orange)
  variable:     #a8aea9    (neutral gray-green)
  number:       #b9773a    (raw sienna)
  constant:     #d4c070    (warm gold)
  comment:      #666347    (muted olive)
  operator:     #a07d4a    (tawny brown)
  property:     #c4a060    (warm ochre)
  boolean:      #8bb07b    (sage green)
```

## Dark Theme — Direct Mapping

The dark theme uses the palette colors almost directly. `build_theme()` passes them straight through:

| Zed property | Source field | Value | Notes |
|---|---|---|---|
| `background` | `bg` | `#161210` | Direct |
| `editor.background` | `editor_bg` | `#1a1612` | Direct |
| `editor.foreground` | `text` | `#cdc4a2` | Direct |
| `text` | `text` | `#cdc4a2` | Direct |
| `text.muted` | `text_muted` | `#8e8870` | Direct |
| `border` | `border` | `#383020` | Direct |
| `border.focused` | `border_focused` | `#6e8bc8` | Direct |
| `syntax.keyword` | `keyword` | `#6e8bc8` | Direct |
| `syntax.string` | `string` | `#d2b45e` | Direct |
| `syntax.function` | `function` | `#7b9f6b` | Direct |
| `syntax.type` | `type` | `#c88a4a` | Direct |
| `syntax.number` | `number` | `#b9773a` | Direct |
| `syntax.comment` | `comment` | `#666347` | Direct + italic |

### Derived Colors

UI colors that need transparency or slight variation are derived using `lighten()`, `darken()`, and `with_alpha()`:

| Zed property | Derivation | Result |
|---|---|---|
| `editor.active_line.background` | `lighten(editor_bg, 0.04)` + alpha 80 | `#231f1b50` |
| `border.variant` | `lighten(border, 0.05)` | `#413a2b` |
| `text.disabled` | `darken(text_muted, 0.3)` | `#635f4e` |
| `element.active` | `accent` + alpha 60 | `#6e8bc83c` |
| `search.match_background` | `string` + alpha 50 | `#d2b45e32` |
| `syntax.comment.doc` | `lighten(comment, 0.1)` | `#757259` |
| `syntax.string.escape` | `lighten(string, 0.15)` | `#d8bf76` |
| `terminal.ansi.bright_*` | `lighten(ansi_*, 0.15)` | Brighter variants |
| `terminal.ansi.dim_*` | `darken(ansi_*, 0.25)` | Dimmer variants |

## Light Theme — `derive_light_artist()` Transformation

The light theme is derived entirely from the dark palette. The key insight: the dark theme's `text` color (`#cdc4a2`, warm parchment) becomes the basis for the light background, blended toward white at different intensities.

### Background Inversion

| Light property | Derivation | Result |
|---|---|---|
| `bg` | `blend_to_white(#cdc4a2, 0.80)` | `#f5f3ec` |
| `editor_bg` | `blend_to_white(#cdc4a2, 0.86)` | `#f8f6f1` |
| `surface` | `blend_to_white(#cdc4a2, 0.74)` | `#f2efe6` |
| `elevated` | `blend_to_white(#cdc4a2, 0.90)` | `#faf9f5` |

`blend_to_white(color, factor)` interpolates each RGB channel toward 255. The 0.74-0.90 range produces warm off-whites that retain Van Gogh's parchment tint — `#f5f3ec` is not pure white, it's subtly golden.

### Text Darkening

| Light property | Derivation | Result |
|---|---|---|
| `text` | `for_light_bg(#cdc4a2, max_lum=0.15)` | `#3c392f` |
| `text_muted` | `for_light_bg(#8e8870, max_lum=0.40)` | `#726d5a` |

`for_light_bg(color, max_lum)` scales RGB proportionally to bring luminance below the target. The original `#cdc4a2` (luminance ~0.74) gets darkened to `#3c392f` (luminance ~0.15) — a warm dark brown, not black.

### Syntax Color Darkening

Every syntax color gets run through `for_light_bg()` with different luminance targets to ensure readability on the light background:

| Token | Dark | Light | `max_lum` |
|---|---|---|---|
| keyword | `#6e8bc8` | `#4f6490` | 0.35 |
| string | `#d2b45e` | `#83713b` | 0.38 |
| function | `#7b9f6b` | `#4e6544` | 0.32 |
| type | `#c88a4a` | `#926536` | 0.38 |
| number | `#b9773a` | `#8f5c2d` | 0.36 |
| comment | `#666347` | `#666347` | 0.42 (already dark enough, unchanged) |
| constant | `#d4c070` | `#7f7343` | 0.38 |
| boolean | `#8bb07b` | `#576f4d` | 0.35 |
| property | `#c4a060` | `#7f683e` | 0.36 |
| variable | `#a8aea9` | `#666a67` | 0.35 |

The hue is preserved — `#6e8bc8` (blue) stays blue as `#4f6490`, `#d2b45e` (golden) stays golden as `#83713b` — but the brightness is pulled down for contrast on white.

### Terminal ANSI Swap

`ansi_black` is hardcoded to `#2a2520`, and `ansi_white` is set to the light `bg` value (`#f5f3ec`). Chromatic ANSI colors get the same `for_light_bg()` treatment.

### Direction Reversal in `build_theme()`

`build_theme()` detects `appearance == "light"` and reverses helper directions:

- `subtle_highlight()` calls `darken()` instead of `lighten()` (active lines are slightly darker than bg, not lighter)
- `fade_out()` calls `lighten()` instead of `darken()` (disabled text gets lighter, not darker)
- Alpha values for selections/highlights are lower (30 vs 50, 25 vs 40) since light backgrounds need less alpha for visibility
