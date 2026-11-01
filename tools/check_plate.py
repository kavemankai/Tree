"""Check a plate's geometry against the locked landmarks.
Usage: python3 tools/check_plate.py PLATE.png OUT_OVERLAY.png
Resizes the plate to 1672x941, draws the landmark traces over it, and reports
how far strong edges near the traced fence and road lines sit from the traces.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import landmarks as lm

W, H = 1672, 941


def edge_map(im):
    g = np.asarray(im.convert('L').filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)
    gx = np.abs(np.diff(g, axis=1, prepend=g[:, :1]))
    gy = np.abs(np.diff(g, axis=0, prepend=g[:1]))
    return gx + gy


def sample_line(pts, step=4):
    out = []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        n = max(1, int(np.hypot(x1 - x0, y1 - y0) / step))
        for i in range(n):
            out.append((x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n))
    return out


def offset_score(e_ref, e_new, pts, search=12):
    """For each sampled point, find the vertical shift (+/-search) that best aligns
    a small edge patch in the new plate with the reference. Returns median |shift|."""
    shifts = []
    for x, y in pts:
        x, y = int(x), int(y)
        if not (20 <= x < W - 20 and search + 10 <= y < H - search - 10):
            continue
        ref = e_ref[y - 8:y + 9, x - 12:x + 13]
        if ref.std() < 2:
            continue
        best, bs = None, 0
        for dy in range(-search, search + 1):
            new = e_new[y - 8 + dy:y + 9 + dy, x - 12:x + 13]
            c = np.corrcoef(ref.ravel(), new.ravel())[0, 1]
            if best is None or c > best:
                best, bs = c, dy
        if best is not None and best > 0.3:
            shifts.append(bs)
    return (float(np.median(np.abs(shifts))) if shifts else None), len(shifts)


def main(path, out):
    ref = Image.open('reference_images/POV_MASTER.png').convert('RGB')
    new = Image.open(path).convert('RGB').resize((W, H), Image.LANCZOS)
    er, en = edge_map(ref), edge_map(new)
    report = {}
    report['fence'] = offset_score(er, en, sample_line(lm.FENCE_TOP_RAIL))
    report['road_far'] = offset_score(er, en, sample_line(lm.ROAD_FAR_EDGE))
    report['road_near'] = offset_score(er, en, sample_line(lm.ROAD_NEAR_EDGE[:5]))
    report['horizon'] = offset_score(er, en, [(x, lm.HORIZON_Y) for x in range(40, 1240, 20)])
    d = ImageDraw.Draw(new)
    d.line([(0, lm.HORIZON_Y), (W, lm.HORIZON_Y)], fill=(255, 255, 255), width=1)
    d.line(lm.FENCE_TOP_RAIL, fill=(255, 200, 60), width=2)
    d.line(lm.ROAD_NEAR_EDGE, fill=(255, 110, 60), width=2)
    d.line(lm.ROAD_FAR_EDGE, fill=(255, 110, 60), width=2)
    for x, yt, yb in lm.FENCE_POSTS:
        d.line([(x, yt), (x, yb)], fill=(255, 200, 60), width=2)
    new.save(out)
    for k, (med, n) in report.items():
        print(f'{k:10s} median |dy| = {med} px over {n} samples')
    worst = max((m for m, _ in report.values() if m is not None), default=None)
    print('PASS' if worst is not None and worst <= 6 else 'CHECK BY EYE')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
