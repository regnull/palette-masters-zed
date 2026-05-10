# Palette Masters — Zed Themes

A collection of 46 Zed editor themes inspired by the master palettes of history's most influential painters. Each theme is derived from real color analysis of the artist's body of work, sourced from [paletteinspiration.com](https://paletteinspiration.com).

Every artist comes in **dark** and **light** variants.

![Van Gogh — Veiled Tawny (dark)](screenshots/van-gogh-starry-night-dark.png)

## Artists

| Artist | Dark Theme | Light Theme |
|---|---|---|
| Claude Monet | Monet — Veiled Parchment | Monet Light — Veiled Parchment |
| Vincent van Gogh | Van Gogh — Veiled Tawny | Van Gogh Light — Veiled Tawny |
| Henri Matisse | Matisse — Muted Tawny | Matisse Light — Muted Tawny |
| Pierre-Auguste Renoir | Renoir — Muted Caramel | Renoir Light — Muted Caramel |
| Camille Pissarro | Pissarro — Veiled Tawny | Pissarro Light — Veiled Tawny |
| Nicholas Roerich | Roerich — Dimmed Parchment | Roerich Light — Dimmed Parchment |
| John Singer Sargent | Sargent — Shadowed Tawny | Sargent Light — Shadowed Tawny |
| Ivan Aivazovsky | Aivazovsky — Veiled Parchment | Aivazovsky Light — Veiled Parchment |
| Paul Cezanne | Cézanne — Penumbral Tawny | Cézanne Light — Penumbral Tawny |
| Edgar Degas | Degas — Shadowed Gamboge | Degas Light — Shadowed Gamboge |
| Leonardo da Vinci | Da Vinci — Veiled Tawny | Da Vinci Light — Veiled Tawny |
| Rembrandt | Rembrandt — Shadowed Bister | Rembrandt Light — Shadowed Bister |
| Pablo Picasso | Picasso — Muted Tawny | Picasso Light — Muted Tawny |
| Johannes Vermeer | Vermeer — Shadowed Bister | Vermeer Light — Shadowed Bister |
| J.M.W. Turner | Turner — Veiled Tawny | Turner Light — Veiled Tawny |
| Gustav Klimt | Klimt — Muted Tawny | Klimt Light — Muted Tawny |
| Wassily Kandinsky | Kandinsky — Muted Tawny | Kandinsky Light — Muted Tawny |
| Paul Gauguin | Gauguin — Shadowed Caramel | Gauguin Light — Shadowed Caramel |
| Caravaggio | Caravaggio — Nocturnal Bister | Caravaggio Light — Nocturnal Bister |
| Raphael | Raphael — Shadowed Tawny | Raphael Light — Shadowed Tawny |
| Edvard Munch | Munch — Muted Tawny | Munch Light — Muted Tawny |
| Diego Velazquez | Velázquez — Nocturnal Bister | Velázquez Light — Nocturnal Bister |
| Katsushika Hokusai | Hokusai — Soft Ecru | Hokusai Light — Soft Ecru |

## Installation

### From source

```bash
git clone https://github.com/regnull/palette-masters-zed.git
cd palette-masters-zed
make install
```

### One-liner (no clone)

```bash
mkdir -p ~/.config/zed/themes && \
  curl -sL https://github.com/regnull/palette-masters-zed/archive/refs/heads/main.tar.gz | \
  tar xz --strip-components=2 -C ~/.config/zed/themes "palette-masters-zed-main/themes/"
```

Then open Zed (or restart it), press `Cmd+K Cmd+T` (macOS) or `Ctrl+K Ctrl+T` (Linux), and search for **"Palette Masters"** or any artist name.

### Uninstall

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
