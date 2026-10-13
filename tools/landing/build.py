"""Builds the landing page variants from template.html.

Usage (from the repo root):  python3 tools/landing/build.py

template.html holds the page, styles and animation code. geom.json and letters.json
hold the hand-traced logo artwork (SVG path data and pen-stroke points); they are
injected into the template along with per-variant feature flags. Edit the template,
not the generated index*.html files.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

# Output file -> feature flags
VARIANTS = {
    'index.html':                {'SHOW_GRID': 'true',  'STAINED_GLASS': 'false', 'WOOD': 'false'},
    'index-no-grid.html':        {'SHOW_GRID': 'false', 'STAINED_GLASS': 'false', 'WOOD': 'false'},
    'index-stained-glass.html':  {'SHOW_GRID': 'true',  'STAINED_GLASS': 'true',  'WOOD': 'false'},
    'index-wood-and-glass.html': {'SHOW_GRID': 'true',  'STAINED_GLASS': 'true',  'WOOD': 'true'},
}

geom = json.dumps(json.loads((HERE / 'geom.json').read_text()),
                  separators=(',', ':')).replace('","', '",\n      "')
letters = json.dumps(json.loads((HERE / 'letters.json').read_text()),
                     separators=(',', ':')).replace('],"', '],\n      "')
base = (HERE / 'template.html').read_text().replace('__GEOM__', geom).replace('__LETTERS__', letters)

for name, flags in VARIANTS.items():
    html = base
    for flag, value in flags.items():
        html = html.replace(f'__{flag}__', value)
    (ROOT / name).write_text(html)
    print(name, len(html))
