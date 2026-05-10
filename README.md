# Palette Masters — Zed Themes

A collection of 46 Zed editor themes inspired by the master palettes of history's most influential painters. Each theme is derived from real color analysis of the artist's body of work, sourced from [paletteinspiration.com](https://paletteinspiration.com).

Every artist comes in **dark** and **light** variants.

## Artists

| Artist | Dark Theme | Light Theme |
|---|---|---|
| Claude Monet | [Monet — Veiled Parchment](samples/monet.svg) | [Monet Light — Veiled Parchment](samples/monet-light.svg) |
| Vincent van Gogh | [Van Gogh — Veiled Tawny](samples/van-gogh.svg) | [Van Gogh Light — Veiled Tawny](samples/van-gogh-light.svg) |
| Henri Matisse | [Matisse — Muted Tawny](samples/matisse.svg) | [Matisse Light — Muted Tawny](samples/matisse-light.svg) |
| Pierre-Auguste Renoir | [Renoir — Muted Caramel](samples/renoir.svg) | [Renoir Light — Muted Caramel](samples/renoir-light.svg) |
| Camille Pissarro | [Pissarro — Veiled Tawny](samples/pissarro.svg) | [Pissarro Light — Veiled Tawny](samples/pissarro-light.svg) |
| Nicholas Roerich | [Roerich — Dimmed Parchment](samples/roerich.svg) | [Roerich Light — Dimmed Parchment](samples/roerich-light.svg) |
| John Singer Sargent | [Sargent — Shadowed Tawny](samples/sargent.svg) | [Sargent Light — Shadowed Tawny](samples/sargent-light.svg) |
| Ivan Aivazovsky | [Aivazovsky — Veiled Parchment](samples/aivazovsky.svg) | [Aivazovsky Light — Veiled Parchment](samples/aivazovsky-light.svg) |
| Paul Cezanne | [Cezanne — Penumbral Tawny](samples/cezanne.svg) | [Cezanne Light — Penumbral Tawny](samples/cezanne-light.svg) |
| Edgar Degas | [Degas — Shadowed Gamboge](samples/degas.svg) | [Degas Light — Shadowed Gamboge](samples/degas-light.svg) |
| Leonardo da Vinci | [Da Vinci — Veiled Tawny](samples/da-vinci.svg) | [Da Vinci Light — Veiled Tawny](samples/da-vinci-light.svg) |
| Rembrandt | [Rembrandt — Shadowed Bister](samples/rembrandt.svg) | [Rembrandt Light — Shadowed Bister](samples/rembrandt-light.svg) |
| Pablo Picasso | [Picasso — Muted Tawny](samples/picasso.svg) | [Picasso Light — Muted Tawny](samples/picasso-light.svg) |
| Johannes Vermeer | [Vermeer — Shadowed Bister](samples/vermeer.svg) | [Vermeer Light — Shadowed Bister](samples/vermeer-light.svg) |
| J.M.W. Turner | [Turner — Veiled Tawny](samples/turner.svg) | [Turner Light — Veiled Tawny](samples/turner-light.svg) |
| Gustav Klimt | [Klimt — Muted Tawny](samples/klimt.svg) | [Klimt Light — Muted Tawny](samples/klimt-light.svg) |
| Wassily Kandinsky | [Kandinsky — Muted Tawny](samples/kandinsky.svg) | [Kandinsky Light — Muted Tawny](samples/kandinsky-light.svg) |
| Paul Gauguin | [Gauguin — Shadowed Caramel](samples/gauguin.svg) | [Gauguin Light — Shadowed Caramel](samples/gauguin-light.svg) |
| Caravaggio | [Caravaggio — Nocturnal Bister](samples/caravaggio.svg) | [Caravaggio Light — Nocturnal Bister](samples/caravaggio-light.svg) |
| Raphael | [Raphael — Shadowed Tawny](samples/raphael.svg) | [Raphael Light — Shadowed Tawny](samples/raphael-light.svg) |
| Edvard Munch | [Munch — Muted Tawny](samples/munch.svg) | [Munch Light — Muted Tawny](samples/munch-light.svg) |
| Diego Velazquez | [Velazquez — Nocturnal Bister](samples/velazquez.svg) | [Velazquez Light — Nocturnal Bister](samples/velazquez-light.svg) |
| Katsushika Hokusai | [Hokusai — Soft Ecru](samples/hokusai.svg) | [Hokusai Light — Soft Ecru](samples/hokusai-light.svg) |

## Installation

### From Zed Extensions (recommended)

1. Open Zed
2. Open the Extensions panel (`Cmd+Shift+X` on macOS, `Ctrl+Shift+X` on Linux)
3. Search for **"Palette Masters"**
4. Click **Install**

### Manual install

```bash
git clone https://github.com/regnull/palette-masters-zed.git
cd palette-masters-zed
make install
```

### Uninstall (manual installs only)

```bash
make uninstall
```

### Auto Light/Dark Switching

To automatically switch between an artist's light and dark theme based on your system appearance, set both variants in your Zed `settings.json`:

```json
{
  "theme": {
    "mode": "system",
    "dark": "Monet — Veiled Parchment",
    "light": "Monet Light — Veiled Parchment"
  }
}
```

## About

Each theme uses the artist's **master palette** — a statistical color analysis across their entire body of work. The dark themes use the palette's darkest tones as backgrounds with lighter palette colors and derived accents for syntax highlighting. The light themes invert this relationship, placing darkened palette colors on warm, tinted near-white backgrounds.

All themes include:

- Full syntax highlighting (44 token types)
- Terminal ANSI colors (regular, bright, dim)
- Multiplayer cursor colors
- Complete UI styling (panels, tabs, status bar, scrollbar, etc.)
- Status indicators (error, warning, success, info, hints)

Color data sourced from [paletteinspiration.com](https://paletteinspiration.com).

## License

[MIT](LICENSE)
