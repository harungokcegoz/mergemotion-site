#!/usr/bin/env python3
"""Regenerate brand images in the new orange palette."""
import math
import sys

sys.path.insert(0, '/home/harun/.local/lib/python3.12/site-packages')

from PIL import Image, ImageDraw, ImageFont

LATO_BOLD = '/usr/share/fonts/truetype/lato/Lato-Bold.ttf'
LATO_SEMI = '/usr/share/fonts/truetype/lato/Lato-Semibold.ttf'

INK        = (11, 11, 13)         # #0B0B0D
ORANGE     = (255, 138, 76)       # #FF8A4C
ORANGE_DRK = (255, 107, 61)       # #FF6B3D
MUTED      = (184, 184, 189)      # #B8B8BD
WHITE      = (255, 255, 255)


# ---------------------------------------------------------------------------
# Helper: draw a radial glow blob
# ---------------------------------------------------------------------------
def draw_glow(draw, cx, cy, radius, color_rgb, max_alpha=90, steps=60):
    for i in range(steps, 0, -1):
        r = int(radius * i / steps)
        alpha = int(max_alpha * (i / steps) ** 1.5)
        x0, y0 = cx - r, cy - r
        x1, y1 = cx + r, cy + r
        draw.ellipse([x0, y0, x1, y1], fill=color_rgb + (alpha,))


# ---------------------------------------------------------------------------
# og-image.png  1200×630
# ---------------------------------------------------------------------------
def make_og():
    W, H = 1200, 630
    img = Image.new('RGB', (W, H), INK)

    # Glow layer (RGBA composite)
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    # Main centre-left orange glow
    draw_glow(gd, 300, 280, 380, ORANGE, max_alpha=70)
    # Secondary smaller glow top-right
    draw_glow(gd, 950, 120, 220, ORANGE_DRK, max_alpha=50)
    img_rgba = img.convert('RGBA')
    img_rgba = Image.alpha_composite(img_rgba, glow)
    img = img_rgba.convert('RGB')

    draw = ImageDraw.Draw(img)

    # Top accent bar (orange gradient simulation via filled rects with gradient)
    bar_h = 6
    for x in range(W):
        t = x / W
        r = int(ORANGE[0] * (1 - t) + ORANGE_DRK[0] * t)
        g = int(ORANGE[1] * (1 - t) + ORANGE_DRK[1] * t)
        b = int(ORANGE[2] * (1 - t) + ORANGE_DRK[2] * t)
        draw.line([(x, 0), (x, bar_h - 1)], fill=(r, g, b))

    # "Merge" wordmark
    font_title = ImageFont.truetype(LATO_BOLD, 110)
    draw.text((80, 160), 'Merge', font=font_title, fill=WHITE)

    # Tagline
    font_tag = ImageFont.truetype(LATO_SEMI, 38)
    draw.text((80, 300), 'Turn any photo into an AI motion video.', font=font_tag, fill=MUTED)

    img.save('/home/harun/mergemotion-site/public/assets/og-image.png', 'PNG')
    print(f'og-image.png: {img.size}')


# ---------------------------------------------------------------------------
# apple-touch-icon.png  180×180 — orange gradient rounded square, white "M"
# ---------------------------------------------------------------------------
def make_apple_touch():
    SIZE = 180
    RADIUS = 40

    # Create gradient base
    img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw gradient rounded rect (135° = top-left → bottom-right)
    # Approximate with per-pixel gradient inside a mask
    grad = Image.new('RGBA', (SIZE, SIZE))
    gd = ImageDraw.Draw(grad)
    diag = math.sqrt(2) * SIZE
    for i in range(SIZE):
        for j in range(SIZE):
            # 135° direction: t = (i+j) / (diag)
            t = min(1.0, (i + j) / (SIZE * 1.4))
            r = int(ORANGE[0] * (1 - t) + ORANGE_DRK[0] * t)
            g = int(ORANGE[1] * (1 - t) + ORANGE_DRK[1] * t)
            b = int(ORANGE[2] * (1 - t) + ORANGE_DRK[2] * t)
            grad.putpixel((i, j), (r, g, b, 255))

    # Rounded rect mask
    mask = Image.new('L', (SIZE, SIZE), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, SIZE - 1, SIZE - 1], radius=RADIUS, fill=255)

    img = Image.composite(grad, img, mask)

    # White "M"
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(LATO_BOLD, 100)
    bbox = draw.textbbox((0, 0), 'M', font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (SIZE - tw) // 2 - bbox[0]
    ty = (SIZE - th) // 2 - bbox[1]
    draw.text((tx, ty), 'M', font=font, fill=WHITE)

    out = img.convert('RGB')
    out.save('/home/harun/mergemotion-site/public/assets/apple-touch-icon.png', 'PNG')
    print(f'apple-touch-icon.png: {out.size}')


# ---------------------------------------------------------------------------
# favicon.ico — same orange "M" mark, multi-size
# ---------------------------------------------------------------------------
def make_favicon():
    SIZE = 256
    RADIUS = int(SIZE * 0.22)

    # Build same gradient rounded square at 256x256
    img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    grad = Image.new('RGBA', (SIZE, SIZE))
    for i in range(SIZE):
        for j in range(SIZE):
            t = min(1.0, (i + j) / (SIZE * 1.4))
            r = int(ORANGE[0] * (1 - t) + ORANGE_DRK[0] * t)
            g = int(ORANGE[1] * (1 - t) + ORANGE_DRK[1] * t)
            b = int(ORANGE[2] * (1 - t) + ORANGE_DRK[2] * t)
            grad.putpixel((i, j), (r, g, b, 255))

    mask = Image.new('L', (SIZE, SIZE), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, SIZE - 1, SIZE - 1], radius=RADIUS, fill=255)

    img = Image.composite(grad, img, mask)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(LATO_BOLD, 160)
    bbox = draw.textbbox((0, 0), 'M', font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (SIZE - tw) // 2 - bbox[0]
    ty = (SIZE - th) // 2 - bbox[1]
    draw.text((tx, ty), 'M', font=font, fill=WHITE)

    # Save as ICO with multiple sizes
    img.save(
        '/home/harun/mergemotion-site/public/assets/favicon.ico',
        format='ICO',
        sizes=[(16, 16), (32, 32), (48, 48)],
    )
    print(f'favicon.ico: generated with sizes 16,32,48')


if __name__ == '__main__':
    make_og()
    make_apple_touch()
    make_favicon()
    print('All images generated OK.')
