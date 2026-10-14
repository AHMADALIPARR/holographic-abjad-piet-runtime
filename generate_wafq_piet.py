#!/usr/bin/env python3
"""Generate the minimal 3x3 Wafq Allāh Piet-style image using canonical colors."""
from PIL import Image, ImageDraw

# Canonical Piet palette (subset)
colors = [
    (255, 192, 192), (255, 0, 0), (192, 0, 0),      # light/normal/dark red
    (255, 255, 192), (255, 255, 0), (192, 192, 0),  # yellows
    (192, 255, 192), (0, 255, 0), (0, 192, 0),      # greens
]

img = Image.new('RGB', (300, 300), (0, 0, 0))
draw = ImageDraw.Draw(img)

block_size = 80
positions = [(10,10), (110,10), (210,10),
             (10,110), (110,110), (210,110),
             (10,210), (110,210), (210,210)]
# Corresponding to Wafq: 8 1 24 / 15 11 7 / 10 21 2
for i, (x, y) in enumerate(positions):
    color = colors[i % len(colors)]
    draw.rectangle([x, y, x + block_size, y + block_size], fill=color)
    # Subtle highlight
    highlight = tuple(min(255, c + 40) for c in color)
    draw.rectangle([x + 5, y + 5, x + 25, y + 25], fill=highlight)

img.save('images/piet_abjad_wafq_3x3.png')
print('Generated images/piet_abjad_wafq_3x3.png')
