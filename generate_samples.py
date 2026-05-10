#!/usr/bin/env python3
"""Generate SVG code sample images for each Palette Masters theme."""

import html
import os
import re

from generate import ARTISTS

SAMPLES_DIR = os.path.join(os.path.dirname(__file__), "samples")

# Python RSI calculation snippet — exercises many syntax token types.
CODE_SNIPPET = '''\
import pandas as pd

def calculate_rsi(
    prices: pd.Series,
    period: int = 14,
) -> pd.Series:
    """Compute the Relative Strength Index."""
    delta = prices.diff()

    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    rsi = 100.0 - (100.0 / (1.0 + rs))

    return rsi.rename("RSI")

# Example usage
if __name__ == "__main__":
    data = pd.read_csv("prices.csv")
    close = data["close"].astype(float)
    result = calculate_rsi(close, period=20)
    print(result.dropna().head(5))
'''

# --- Token categories ---
KEYWORDS = {
    "import", "from", "def", "return", "if", "else", "elif", "for", "while",
    "with", "as", "in", "not", "and", "or", "is", "class", "try", "except",
    "finally", "raise", "yield", "pass", "break", "continue", "del", "assert",
    "lambda", "global", "nonlocal", "async", "await",
}
BUILTINS = {
    "print", "len", "range", "int", "float", "str", "list", "dict", "set",
    "tuple", "bool", "type", "isinstance", "hasattr", "getattr", "setattr",
    "open", "enumerate", "zip", "map", "filter", "sorted", "reversed",
    "min", "max", "sum", "abs", "round", "input", "super", "property",
    "staticmethod", "classmethod", "None",
}
BOOLEANS = {"True", "False"}
CONSTANTS = {"__name__", "__main__"}

# Patterns applied in order. First match wins.
TOKEN_PATTERNS = [
    ("comment",   re.compile(r'#[^\n]*')),
    ("string",    re.compile(r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|"[^"\n]*"|\'[^\'\n]*\'')),
    ("number",    re.compile(r'\b\d+\.?\d*\b')),
    ("operator",  re.compile(r'->|[+\-*/%=<>!&|^~]+')),
    ("punctuation", re.compile(r'[(){}\[\]:;,.]')),
    ("word",      re.compile(r'\b[A-Za-z_]\w*\b')),
    ("whitespace", re.compile(r'[ \t]+')),
    ("newline",   re.compile(r'\n')),
]


def tokenize(code):
    """Split code into (category, text) tokens for syntax highlighting."""
    tokens = []
    pos = 0
    while pos < len(code):
        best = None
        for cat, pat in TOKEN_PATTERNS:
            m = pat.match(code, pos)
            if m:
                best = (cat, m.group())
                break
        if best is None:
            tokens.append(("text", code[pos]))
            pos += 1
            continue

        cat, text = best
        pos += len(text)

        # Refine word tokens into more specific categories.
        if cat == "word":
            cat = classify_word(text, tokens)

        tokens.append((cat, text))
    return tokens


def classify_word(text, preceding_tokens):
    """Classify an identifier into a syntax category based on context."""
    if text in KEYWORDS:
        return "keyword"
    if text in BOOLEANS:
        return "boolean"
    if text in CONSTANTS:
        return "constant"

    # Check what came just before (skipping whitespace).
    prev_cat, prev_text = None, None
    for cat, txt in reversed(preceding_tokens):
        if cat != "whitespace":
            prev_cat, prev_text = cat, txt
            break

    # After 'def' keyword → function definition.
    if prev_text == "def":
        return "function"

    # After a dot → property/method.
    if prev_text == ".":
        return "property"

    # Type annotations: after ':', '->', or as PascalCase.
    if prev_text in (":", "->"):
        return "type"

    # Builtins used as function calls.
    if text in BUILTINS:
        return "function"

    return "variable"


def get_color(category, artist):
    """Map a token category to a hex color from the artist palette."""
    color_map = {
        "keyword":     artist["keyword"],
        "string":      artist["string"],
        "comment":     artist["comment"],
        "function":    artist["function"],
        "type":        artist["type"],
        "variable":    artist["variable"],
        "number":      artist["number"],
        "constant":    artist["constant"],
        "operator":    artist["operator"],
        "punctuation": artist["punctuation"],
        "boolean":     artist["boolean"],
        "property":    artist["property"],
        "text":        artist["text"],
        "whitespace":  None,
        "newline":     None,
    }
    return color_map.get(category, artist["text"])


# --- SVG rendering ---

FONT_FAMILY = "'JetBrains Mono','SF Mono','Fira Code',monospace"
CHAR_WIDTH = 8.8
LINE_HEIGHT = 22
FONT_SIZE = 14
PADDING_X = 24
PADDING_Y = 16
LINE_NUM_WIDTH = 36
TITLE_BAR_HEIGHT = 38
DOT_RADIUS = 6
DOT_GAP = 20
CORNER_RADIUS = 10


def build_svg(artist):
    """Build an SVG string showing syntax-highlighted code for one artist."""
    tokens = tokenize(CODE_SNIPPET)

    # Split tokens into lines for rendering.
    lines = [[]]
    for cat, text in tokens:
        if cat == "newline":
            lines.append([])
        else:
            lines[-1].append((cat, text))

    num_lines = len(lines)
    code_x = PADDING_X + LINE_NUM_WIDTH
    width = 680
    height = TITLE_BAR_HEIGHT + PADDING_Y + num_lines * LINE_HEIGHT + PADDING_Y

    bg = artist["editor_bg"]
    muted = artist["text_muted"]
    border = artist["border"]

    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}">'
    )

    # Background rounded rect.
    parts.append(
        f'<rect width="{width}" height="{height}" rx="{CORNER_RADIUS}" '
        f'fill="{bg}" />'
    )

    # Title bar.
    parts.append(
        f'<rect width="{width}" height="{TITLE_BAR_HEIGHT}" rx="{CORNER_RADIUS}" '
        f'fill="{artist["surface"]}" />'
    )
    # Bottom-cover rect to square off the title bar bottom corners.
    parts.append(
        f'<rect y="{TITLE_BAR_HEIGHT - CORNER_RADIUS}" '
        f'width="{width}" height="{CORNER_RADIUS}" '
        f'fill="{artist["surface"]}" />'
    )
    # Title bar separator line.
    parts.append(
        f'<line x1="0" y1="{TITLE_BAR_HEIGHT}" '
        f'x2="{width}" y2="{TITLE_BAR_HEIGHT}" '
        f'stroke="{border}" stroke-width="1" />'
    )

    # macOS window dots.
    dot_y = TITLE_BAR_HEIGHT // 2
    dot_colors = ["#ff5f57", "#febc2e", "#28c840"]
    for i, color in enumerate(dot_colors):
        cx = PADDING_X + i * DOT_GAP
        parts.append(
            f'<circle cx="{cx}" cy="{dot_y}" r="{DOT_RADIUS}" fill="{color}" />'
        )

    # Theme name in title bar.
    title_x = PADDING_X + len(dot_colors) * DOT_GAP + 12
    parts.append(
        f'<text x="{title_x}" y="{dot_y + 5}" '
        f'font-family="{FONT_FAMILY}" font-size="13" '
        f'fill="{muted}">{html.escape(artist["theme_name"])}</text>'
    )

    # Code lines.
    y_start = TITLE_BAR_HEIGHT + PADDING_Y + LINE_HEIGHT
    for line_idx, line_tokens in enumerate(lines):
        y = y_start + line_idx * LINE_HEIGHT

        # Line number.
        line_num = str(line_idx + 1)
        ln_x = PADDING_X + LINE_NUM_WIDTH - 12
        parts.append(
            f'<text x="{ln_x}" y="{y}" '
            f'font-family="{FONT_FAMILY}" font-size="{FONT_SIZE}" '
            f'fill="{muted}" text-anchor="end">{line_num}</text>'
        )

        # Render each token as a tspan.
        if line_tokens:
            spans = []
            for cat, text in line_tokens:
                color = get_color(cat, artist)
                escaped = html.escape(text)
                if color:
                    spans.append(f'<tspan fill="{color}">{escaped}</tspan>')
                else:
                    spans.append(escaped)
            parts.append(
                f'<text x="{code_x}" y="{y}" '
                f'xml:space="preserve" '
                f'font-family="{FONT_FAMILY}" font-size="{FONT_SIZE}" '
                f'fill="{artist["text"]}">'
                + "".join(spans)
                + "</text>"
            )

    parts.append("</svg>")
    return "\n".join(parts)


def main():
    os.makedirs(SAMPLES_DIR, exist_ok=True)
    for artist in ARTISTS:
        svg = build_svg(artist)
        path = os.path.join(SAMPLES_DIR, f"{artist['id']}.svg")
        with open(path, "w") as f:
            f.write(svg)
        print(f"  {path}")
    print(f"\nGenerated {len(ARTISTS)} SVG samples in {SAMPLES_DIR}/")


if __name__ == "__main__":
    main()
