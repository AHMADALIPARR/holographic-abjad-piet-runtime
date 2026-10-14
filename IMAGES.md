# Piet Program Images

The holographic front-end images are the Piet programs themselves. All images in `images/` are valid PNG files with canonical Piet palette colors.

## Images

| File | Size | Description |
|------|------|-------------|
| `holographic-primary.png` | 8×8 codels, 640×640px | Primary holographic square. Outer dark (Jalāl), inner light (Jamāl), center white equilibrium (53/106). |
| `holographic-secondary.png` | 6×6 codels, 480×480px | Secondary square. Four corner pillars framing the center. Red hue cycle. |
| `piet_4x4_clean.png` | 4×4 codels, 400×400px | Clean 4×4 grid covering all Piet hue/lightness cycles. |
| `wafq-3x3.png` | 3×3 codels, 360×360px | Minimal 3×3 Wafq Allāh (constant 33). Values [[8,1,24],[15,11,7],[10,21,2]] mapped to Piet colors. |

## Piet Palette

All images use canonical Piet colors (18 hues + black + white):
- **Hues:** Red, Yellow, Green, Cyan, Blue, Magenta
- **Lightness:** Light, Normal, Dark (3 per hue)
- **Special:** White (slide), Black (wall)

## How to Run

1. Save the image (PNG)
2. Use npiet, the online Piet interpreter, or any compatible runner
3. Set codel size appropriately (often 1 or auto-detect)
4. Observe stack operations on Abjad values, equilibrium, and kenoma/pleroma branch

## Previously Referenced (Removed)

The following files were referenced in an earlier README but did not exist or were corrupt:
- `piet_abjad_holographic_2d.gif` — did not exist
- `holographic-primary.jpg` — did not exist (replaced with `.png`)
- `holographic-secondary.jpg` — did not exist (replaced with `.png`)
- `holographic-render-1.jpg` — did not exist
- `holographic-render-2.jpg` — did not exist
- `piet_abjad_wafq_3x3.png` — did not exist (replaced with `wafq-3x3.png`)

All README image references now point to files that exist and are valid PNGs.
