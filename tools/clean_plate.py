"""Local, zero-credit paint-out of the couple, basket and wagon from POV_MASTER.
Output: storyboard/plates/PLATE_EMPTY_PLACEHOLDER.png
This is a storyboard placeholder, NOT a video start frame. Replace with a proper
generative clean plate once a paid plan is active.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SRC = 'reference_images/POV_MASTER.png'
OUT = 'storyboard/plates/PLATE_EMPTY_PLACEHOLDER.png'

COUPLE = [(596, 600), (640, 578), (790, 578), (845, 520), (875, 462), (985, 455),
          (1060, 520), (1100, 535), (1215, 405), (1355, 410), (1445, 560), (1460, 860),
          (1300, 870), (1140, 925), (640, 935), (596, 780)]
WAGON = [(1148, 158), (1300, 158), (1302, 296), (1148, 296)]


def mask(poly, size, blur):
    m = Image.new('L', size, 0)
    ImageDraw.Draw(m).polygon(poly, fill=255)
    return m.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(blur))


def fill_rows_from_right(a, m):
    """Fill masked span of each row by mirroring the unmasked grass to its right."""
    out = a.copy()
    H, W, _ = a.shape
    hard = m > 8
    for y in range(H):
        xs = np.where(hard[y])[0]
        if xs.size == 0:
            continue
        x0, x1 = xs.min(), xs.max()
        span = x1 - x0 + 1
        src = a[y, x1 + 1:]
        if src.shape[0] < 8:
            continue
        # right-hand source, mirrored outward from the patch edge
        right = np.concatenate([src[::-1], src] * (span // (2 * src.shape[0]) + 2))[:span][::-1]
        if y >= 700 and x0 > 40:
            # lower rows: the left side is grass too; mirror it inward and crossfade
            lsrc = a[y, :x0]
            left = np.concatenate([lsrc[::-1], lsrc] * (span // (2 * lsrc.shape[0]) + 2))[:span]
            w = np.linspace(0, 1, span)[:, None]
            w = np.clip((w - 0.3) / 0.4, 0, 1)
            out[y, x0:x1 + 1] = left * (1 - w) + right * w
        else:
            out[y, x0:x1 + 1] = right
    return out


def main():
    im = Image.open(SRC).convert('RGB')
    a = np.asarray(im).astype(np.float32)
    mc = mask(COUPLE, im.size, 6)
    filled = fill_rows_from_right(a, np.asarray(mc))
    # break up row-copy streaks with a light vertical blur inside the patch only
    fimg = Image.fromarray(filled.astype(np.uint8))
    fimg = Image.blend(fimg, fimg.filter(ImageFilter.BoxBlur(1)), 0.5)
    alpha = np.asarray(mc).astype(np.float32)[..., None] / 255
    a = a * (1 - alpha) + np.asarray(fimg).astype(np.float32) * alpha

    # wagon: copy the strip 160 px to the left (trees, fence, verge, road)
    mw = mask(WAGON, im.size, 4)
    shifted = np.roll(a, 160, axis=1)
    alpha = np.asarray(mw).astype(np.float32)[..., None] / 255
    a = a * (1 - alpha) + shifted * alpha

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(OUT)
    print('wrote', OUT)


if __name__ == '__main__':
    main()
