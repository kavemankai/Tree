"""Zero-credit season/time placeholder grades of the empty plate.
Outputs storyboard/plates/PLATE_<NAME>.png. All share identical geometry by construction.
These are layout/mood placeholders for the board, not production plates.
"""
import os
import numpy as np
from PIL import Image, ImageFilter

SRC = 'storyboard/plates/PLATE_EMPTY_PLACEHOLDER.png'
DIR = 'storyboard/plates'
HORIZON = 128


def lum(a):
    return a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114


_SRC_L = None


def sky_mask(h, w):
    """Above-horizon pixels that are bright (sky, not the tree line)."""
    ys = np.arange(h)
    col = np.clip((HORIZON + 10 - ys) / 20, 0, 1)[:, None]
    bright = np.clip((_SRC_L - 135) / 50, 0, 1)
    return (col * bright)[..., None]


def grade(a, mul, add=(0, 0, 0), sat=1.0, contrast=1.0):
    L = lum(a)[..., None]
    a = L + (a - L) * sat
    a = (a - 128) * contrast + 128
    return a * np.array(mul) + np.array(add)


def summer(a):
    out = grade(a, (0.92, 1.02, 1.05), (0, 4, 10), sat=0.95, contrast=0.95)
    sky = np.zeros_like(a) + np.array([150, 190, 230])
    s = sky_mask(*a.shape[:2])
    return out * (1 - s * 0.55) + sky * s * 0.55


def autumn_late(a):
    L = lum(a)[..., None]
    g = a[..., 1:2] - (a[..., 0:1] + a[..., 2:3]) / 2  # greenness
    w = np.clip(g / 40, 0, 1)
    ochre = L * np.array([1.25, 0.95, 0.55])
    out = a * (1 - w * 0.75) + ochre * w * 0.75
    return grade(out, (1.0, 0.97, 0.9), sat=0.9)


def winter(a):
    h, w_, _ = a.shape
    L = lum(a)[..., None]
    g = a[..., 1:2] - (a[..., 0:1] + a[..., 2:3]) / 2
    ground = np.zeros((h, w_, 1), np.float32)
    ground[HORIZON + 5:] = 1
    snow_amt = np.clip(g / 25, 0, 1) * ground  # grassy ground takes snow
    snow = 205 + (L - 128) * 0.25 + np.array([0, 4, 12])
    out = grade(a, (0.85, 0.9, 1.0), (10, 14, 24), sat=0.35, contrast=0.85)
    out = out * (1 - snow_amt * 0.85) + snow * snow_amt * 0.85
    sky = np.zeros_like(a) + np.array([196, 202, 210])
    s = sky_mask(h, w_)
    return out * (1 - s * 0.8) + sky * s * 0.8


def rain(a):
    h, w_, _ = a.shape
    out = grade(a, (0.78, 0.84, 0.9), (12, 14, 18), sat=0.45, contrast=0.8)
    sky = np.zeros_like(a) + np.array([150, 156, 164])
    s = sky_mask(h, w_)
    out = out * (1 - s * 0.85) + sky * s * 0.85
    rng = np.random.default_rng(7)
    streak = np.zeros((h, w_), np.float32)
    for _ in range(2200):
        x, y, ln = rng.integers(0, w_), rng.integers(0, h), rng.integers(12, 34)
        for i in range(ln):
            yy, xx = y + i, x + i // 5
            if yy < h and xx < w_:
                streak[yy, xx] = 1
    streak = np.asarray(Image.fromarray((streak * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))) / 255.0
    return out * (1 - streak[..., None] * 0.35) + 225 * streak[..., None] * 0.35


def soft_afternoon(a):
    return grade(a, (1.0, 1.0, 0.97), (6, 8, 8), sat=0.85, contrast=0.88)


PLATES = {
    'AUTUMN_GOLD': lambda a: a,
    'SUMMER_DAY': summer,
    'AUTUMN_LATE': autumn_late,
    'WINTER_SNOW': winter,
    'SPRING_RAIN': rain,
    'SOFT_AFTERNOON': soft_afternoon,
}


def main():
    global _SRC_L
    a = np.asarray(Image.open(SRC).convert('RGB')).astype(np.float32)
    _SRC_L = lum(a)
    for name, fn in PLATES.items():
        out = np.clip(fn(a.copy()), 0, 255).astype(np.uint8)
        Image.fromarray(out).save(os.path.join(DIR, f'PLATE_{name}.png'))
        print('wrote', name)


if __name__ == '__main__':
    main()
