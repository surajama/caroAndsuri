# Landing page source

The `index*.html` pages in the repo root are **generated** — edit `template.html` here, then run:

```bash
python3 tools/landing/build.py
```

| File | What it is |
|---|---|
| `template.html` | Page markup, CSS and the animation script, with placeholders `__GEOM__`, `__LETTERS__`, `__SHOW_GRID__`, `__STAINED_GLASS__`, `__WOOD__` |
| `geom.json` | Logo artwork as SVG path data, centred on the flower (viewBox -540..540). One C+S petal (`cSolid`/`sSolid` plus the `cFill`/`sFill` pieces that bridge the over/under line breaks); the flower outline (five circular arcs); `holePath`, where the lattice is cut away; `panelPath`, the walnut panel |
| `letters.json` | Pen-stroke centrelines and widths for the complete standalone C and S shown at the start of the animation, which retract into the petal shapes |
| `build.py` | Injects the JSON and per-variant flags into the template and writes the four pages |

The logo was hand-traced from a photo of the original artwork, and one petal is rotated five times. These JSON files are now the master copy of the artwork.

Variants: `index.html` (white lattice, current front-runner), `index-no-grid.html`, `index-stained-glass.html`, `index-wood-and-glass.html` (wood/glass uses `wood.jpg`).
