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

# Photo backgrounds. scale = image width in logo widths; aspect = height / width; cx, cy = the point of
# the image (as fractions) that sits under the flower's centre.
GLASS_WALL = json.dumps({  # 8x8 tile wall; centre = junction of the middle four tiles of a 4x4 block
    'image': "url('glass-wall.jpg')", 'colour': '#8a5d3b', 'repeat': 'repeat',
    'scale': '2.062', 'aspect': str(1160 / 1136), 'cx': '0.4946', 'cy': '0.5033'})
CEILING = json.dumps({  # venue ceiling, cropped centred on its twelve-pointed star; petals reach just past the gilded rosette
    'image': "url('ceiling.jpg')", 'colour': '#3a2a1c', 'repeat': 'no-repeat',
    'scale': '4.16', 'aspect': str(2800 / 2400), 'cx': '0.5', 'cy': '0.5'})

# Output file -> feature flags
VARIANTS = {
    'index.html':                {'SHOW_GRID': 'true',  'STAINED_GLASS': 'false', 'WOOD': 'false', 'PHOTO_BACKGROUND': 'false', 'OUTLINE_FROM_START': 'false', 'FLOWER_FILL': '#e9b949', 'OUTLINE_COLOUR': '#fff', 'BACKGROUND': '{}'},
    'index-no-grid.html':        {'SHOW_GRID': 'false', 'STAINED_GLASS': 'false', 'WOOD': 'false', 'PHOTO_BACKGROUND': 'false', 'OUTLINE_FROM_START': 'false', 'FLOWER_FILL': '#e9b949', 'OUTLINE_COLOUR': '#fff', 'BACKGROUND': '{}'},
    'index-stained-glass.html':  {'SHOW_GRID': 'true',  'STAINED_GLASS': 'true',  'WOOD': 'false', 'PHOTO_BACKGROUND': 'false', 'OUTLINE_FROM_START': 'false', 'FLOWER_FILL': '#e9b949', 'OUTLINE_COLOUR': '#fff', 'BACKGROUND': '{}'},
    'index-wood-and-glass.html': {'SHOW_GRID': 'true',  'STAINED_GLASS': 'true',  'WOOD': 'true',  'PHOTO_BACKGROUND': 'false', 'OUTLINE_FROM_START': 'false', 'FLOWER_FILL': '#e9b949', 'OUTLINE_COLOUR': '#fff', 'BACKGROUND': '{}'},
    'index-glass-panel.html':    {'SHOW_GRID': 'false', 'STAINED_GLASS': 'false', 'WOOD': 'false', 'PHOTO_BACKGROUND': 'true', 'OUTLINE_FROM_START': 'true', 'FLOWER_FILL': '#e9b949', 'OUTLINE_COLOUR': '#fff',
                                  'BACKGROUND': GLASS_WALL},
    'index-ceiling.html':        {'SHOW_GRID': 'false', 'STAINED_GLASS': 'false', 'WOOD': 'false', 'PHOTO_BACKGROUND': 'true', 'OUTLINE_FROM_START': 'true', 'FLOWER_FILL': '#e9b949', 'OUTLINE_COLOUR': '#fff',
                                  'BACKGROUND': CEILING},
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
