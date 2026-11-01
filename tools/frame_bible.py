"""Render bible/FRAME_BIBLE_v1.png: POV_MASTER with ground grid, landmarks and stage zones.
Run from repo root:  python3 tools/frame_bible.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw, ImageFont
import camera as cam
import landmarks as lm

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONTB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def poly(d, pts, col, w=3):
    d.line([tuple(p) for p in pts], fill=col, width=w, joint='curve')


def ground_line(d, pts_world, col, w=1):
    px = [cam.project(x, 0, z) for x, z in pts_world]
    px = [p for p in px if p]
    if len(px) > 1:
        d.line(px, fill=col, width=w)


def main():
    base = Image.open('reference_images/POV_MASTER.png').convert('RGB')
    # dim the image so annotation reads
    im = Image.blend(base, Image.new('RGB', base.size, (20, 20, 20)), 0.35)
    ov = Image.new('RGBA', im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    f = ImageFont.truetype(FONT, 15)
    fb = ImageFont.truetype(FONTB, 17)

    # ground grid
    for z in [6, 8, 10, 12, 15, 20, 30, 50]:
        ground_line(d, [(x / 2, z) for x in range(-80, 81)], (120, 220, 255, 150))
        p = cam.project(-0.0, 0, z)
        if p and p[1] < cam.H:
            d.text((p[0] + 4, p[1] - 16), f'{z} m', fill=(170, 235, 255, 255), font=f)
    for x in range(-20, 21, 2):
        ground_line(d, [(x, z / 4) for z in range(21, 400)], (120, 220, 255, 90))

    # landmarks
    d.line([(0, lm.HORIZON_Y), (cam.W, lm.HORIZON_Y)], fill=(255, 255, 255, 200), width=2)
    d.text((10, lm.HORIZON_Y - 20), 'HORIZON y=%d (locked)' % lm.HORIZON_Y, fill=(255, 255, 255, 255), font=fb)
    poly(d, lm.FENCE_TOP_RAIL, (255, 200, 60, 255), 3)
    for x, ytop, ybot in lm.FENCE_POSTS:
        d.line([(x, ytop), (x, ybot)], fill=(255, 200, 60, 255), width=5)
    d.text((40, 300), 'FENCE (post spacing locked)', fill=(255, 210, 90, 255), font=fb)
    poly(d, lm.ROAD_NEAR_EDGE, (255, 120, 60, 255), 3)
    poly(d, lm.ROAD_FAR_EDGE, (255, 120, 60, 255), 3)
    d.text((300, 640), 'ROAD near edge', fill=(255, 150, 100, 255), font=fb)
    for name, box in lm.PUDDLES.items():
        d.ellipse(box, outline=(120, 200, 255, 255), width=2)
    x0, y0, x1, y1 = lm.CASTLE_BOX
    d.rectangle(lm.CASTLE_BOX, outline=(255, 255, 255, 255), width=2)
    d.text((x0, y0 - 20), 'RUIN (image detail, not canon)', fill=(255, 255, 255, 255), font=f)
    sx, sy = lm.SUN_XY
    d.ellipse((sx - 14, sy - 14, sx + 14, sy + 14), outline=(255, 240, 120, 255), width=2)
    d.text((sx + 18, sy - 8), 'sun (master only; moves per plate)', fill=(255, 240, 150, 255), font=f)

    # stage zones on the ground
    for name, (xa, xb, za, zb, col) in lm.ZONES.items():
        pts = [(xa, za), (xb, za), (xb, zb), (xa, zb)]
        px = [cam.project(x, 0, z) for x, z in pts]
        d.polygon(px, outline=col + (255,), fill=col + (55,))
        cxp = cam.project((xa + xb) / 2, 0, (za + zb) / 2)
        d.text((cxp[0] - 60, cxp[1] - 10), name, fill=col + (255,), font=fb)

    # scale figures: standing 1.7 m and seated 0.9 m at a few distances
    for x, z in [(-1.5, 6), (2.5, 9), (-3.5, 14), (6, 20)]:
        for h, col in [(1.7, (255, 255, 255, 230)), (0.9, (255, 170, 220, 230))]:
            a, b = cam.project(x, 0, z), cam.project(x, h, z)
            off = 0 if h > 1 else 10
            d.line([(a[0] + off, a[1]), (b[0] + off, b[1])], fill=col, width=4)
        a = cam.project(x, 0, z)
        d.text((a[0] + 14, a[1] - 14), f'{z} m', fill=(255, 255, 255, 255), font=f)

    out = Image.alpha_composite(im.convert('RGBA'), ov).convert('RGB')
    # footer legend
    leg = Image.new('RGB', (cam.W, 120), (17, 27, 33))
    dl = ImageDraw.Draw(leg)
    dl.text((16, 10), 'FRAME BIBLE v1  /  THE LOVERS  /  tree camera A (upper trunk, branch junction)', fill=(235, 235, 225), font=fb)
    dl.text((16, 38), f'Lens ~{cam.CAM_H} m above ground  |  neutral pitch {round(cam.PITCH*57.2958,1)} deg down  |  f = {int(cam.F)} px (~65 deg HFOV)  |  '
                      'allowed: yaw +/-10 deg, pitch -5..+15 deg, no XYZ change, no zoom', fill=(200, 210, 210), font=f)
    dl.text((16, 62), 'Blue grid = ground plane in metres from the trunk base.  White bars = 1.7 m standing adult, pink = 0.9 m seated, at true scale for this camera.',
            fill=(200, 210, 210), font=f)
    dl.text((16, 86), 'Ground nearer than 5.25 m is OUT OF FRAME at neutral pitch. The painted couple in POV_MASTER are ~2.3x oversized; ignore their scale.',
            fill=(255, 170, 120), font=f)
    final = Image.new('RGB', (cam.W, cam.H + 120))
    final.paste(out, (0, 0)); final.paste(leg, (0, cam.H))
    final.save('bible/FRAME_BIBLE_v1.png')
    print('wrote bible/FRAME_BIBLE_v1.png')


if __name__ == '__main__':
    main()
