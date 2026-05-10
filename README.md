# Palette Masters — Zed Themes

A collection of 46 Zed editor themes inspired by the master palettes of history's most influential painters. Each theme is derived from real color analysis of the artist's body of work, sourced from [paletteinspiration.com](https://paletteinspiration.com).

Every artist comes in **dark** and **light** variants.

## Artists

| Artist | Dark Theme | Light Theme |
|---|---|---|
| Claude Monet | Monet — Water Lilies | Monet Light — Water Lilies |
| Vincent van Gogh | Van Gogh — Starry Night | Van Gogh Light — Starry Night |
| Henri Matisse | Matisse — The Dance | Matisse Light — The Dance |
| Pierre-Auguste Renoir | Renoir — Luncheon of the Boating Party | Renoir Light — Luncheon of the Boating Party |
| Camille Pissarro | Pissarro — Boulevard Montmartre | Pissarro Light — Boulevard Montmartre |
| Nicholas Roerich | Roerich — Himalayas | Roerich Light — Himalayas |
| John Singer Sargent | Sargent — Madame X | Sargent Light — Madame X |
| Ivan Aivazovsky | Aivazovsky — The Ninth Wave | Aivazovsky Light — The Ninth Wave |
| Paul Cezanne | Cezanne — Mont Sainte-Victoire | Cezanne Light — Mont Sainte-Victoire |
| Edgar Degas | Degas — The Ballet Class | Degas Light — The Ballet Class |
| Leonardo da Vinci | Da Vinci — Mona Lisa | Da Vinci Light — Mona Lisa |
| Rembrandt | Rembrandt — The Night Watch | Rembrandt Light — The Night Watch |
| Pablo Picasso | Picasso — Guernica | Picasso Light — Guernica |
| Johannes Vermeer | Vermeer — Girl with a Pearl Earring | Vermeer Light — Girl with a Pearl Earring |
| J.M.W. Turner | Turner — The Fighting Temeraire | Turner Light — The Fighting Temeraire |
| Gustav Klimt | Klimt — The Kiss | Klimt Light — The Kiss |
| Wassily Kandinsky | Kandinsky — Composition VIII | Kandinsky Light — Composition VIII |
| Paul Gauguin | Gauguin — Where Do We Come From? | Gauguin Light — Where Do We Come From? |
| Caravaggio | Caravaggio — Judith Beheading Holofernes | Caravaggio Light — Judith Beheading Holofernes |
| Raphael | Raphael — The School of Athens | Raphael Light — The School of Athens |
| Edvard Munch | Munch — The Scream | Munch Light — The Scream |
| Diego Velazquez | Velazquez — Las Meninas | Velazquez Light — Las Meninas |
| Katsushika Hokusai | Hokusai — The Great Wave | Hokusai Light — The Great Wave |

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
    "dark": "Monet — Water Lilies",
    "light": "Monet Light — Water Lilies"
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
