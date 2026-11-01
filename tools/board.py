"""Render perspective-locked panels and the contact sheet for THE LOVERS.
Run from repo root:  python3 tools/board.py
Outputs: storyboard/panels/BEAT_XX.jpg  and  storyboard/LOVERS_BOARD_v1.jpg
"""
import math, os, sys, textwrap
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw, ImageFont
import camera as cam
import landmarks as lm
from beats import BEATS, CAST, SPEED

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONTB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SKIN = (226, 186, 160)
DIRS = {'L': (-1, 0), 'R': (1, 0), 'cam': (0, -1), 'away': (0, 1)}
PATH_COL = {'E': (120, 200, 255), 'M': (255, 140, 110)}


class View:
    def __init__(self, pitch):
        self.pitch = pitch

    def p(self, x, y, z):
        return cam.project(x, y, z, 0, self.pitch)

    def s(self, x, z):
        a, b = self.p(x, 0, z), self.p(x, 1.0, z)
        return a[1] - b[1]


def tilted_plate(plate, pitch):
    """Shift plate for a downward tilt; uncovered band is hatched (needs outpaint)."""
    if pitch == 0:
        return plate.copy(), 0
    dv = int(round(cam.F * math.tan(math.radians(pitch))))
    out = Image.new('RGB', plate.size, (40, 40, 44))
    out.paste(plate.crop((0, dv, plate.width, plate.height)), (0, 0))
    d = ImageDraw.Draw(out)
    top = plate.height - dv
    for x in range(-plate.height, plate.width, 28):
        d.line([(x, plate.height), (x + dv, top)], fill=(70, 70, 76), width=6)
    f = ImageFont.truetype(FONTB, 26)
    d.text((24, top + dv / 2 - 14), f'NOT IN MASTER PLATE: tilt +{pitch} deg needs ~{dv} px downward extension',
           fill=(255, 190, 120), font=f)
    return out, top


def draw_shadow(d, v, x, z, r):
    pts = [v.p(x + r * math.cos(t), 0, z + r * 0.6 * math.sin(t)) for t in [i * math.pi / 10 for i in range(20)]]
    d.polygon(pts, fill=(0, 0, 0, 70))


def draw_figure(d, v, f):
    c = CAST[f['who']]
    x, z, pose, face = f['x'], f['z'], f['pose'], f['face']
    alpha = 120 if f.get('ghost') else 255
    A = lambda col: tuple(col) + (alpha,)
    s = v.s(x, z)
    u0, v0 = v.p(x, 0, z)
    dx, dz = DIRS[face]
    girl = 'skirt' in c
    H = c['h']
    draw_shadow(d, v, x, z, 0.35 if pose != 'lie' else 0.9)

    def head(cx, cy, r):
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=A(SKIN))
        hair = A(c['hair'])
        if face == 'away':
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=hair)
            if girl:
                d.line([(cx, cy), (cx + r * 0.2, cy + r * 3)], fill=hair, width=max(2, int(r * 0.6)))
        elif face == 'cam':
            d.pieslice((cx - r * 1.05, cy - r * 1.1, cx + r * 1.05, cy + r * 0.9), 180, 360, fill=hair)
        else:
            back = 0 if face == 'L' else 180  # hair on the back of the head
            d.pieslice((cx - r * 1.05, cy - r * 1.05, cx + r * 1.05, cy + r * 1.05), back - 100, back + 100, fill=hair)
            if girl:
                bx = cx + (r * 0.9 if face == 'L' else -r * 0.9)
                d.line([(bx, cy), (bx, cy + r * 3)], fill=hair, width=max(2, int(r * 0.5)))

    w = 0.42 * s  # shoulder width (front); narrower in profile
    if face in ('L', 'R'):
        w *= 0.6
    if pose in ('stand', 'walk'):
        hip = v0 - 0.85 * s * H / 1.7
        sh = v0 - 1.40 * s * H / 1.7
        hr = 0.12 * s
        if girl:
            d.polygon([(u0 - w * 0.45, sh + 0.12 * s), (u0 + w * 0.45, sh + 0.12 * s), (u0 + w * 0.9, v0 - 0.08 * s),
                       (u0 - w * 0.9, v0 - 0.08 * s)], fill=A(c['skirt']))
            d.rectangle((u0 - w * 0.5, sh, u0 + w * 0.5, hip - 0.1 * s), fill=A(c['vest']))
            d.rectangle((u0 - w * 0.6, sh, u0 + w * 0.6, sh + 0.12 * s), fill=A(c['top']))
        else:
            step = 0.12 * s if pose == 'walk' else 0.05 * s
            d.line([(u0 - w * 0.2, hip), (u0 - step, v0)], fill=A(c['legs']), width=max(2, int(0.13 * s)))
            d.line([(u0 + w * 0.2, hip), (u0 + step, v0)], fill=A(c['legs']), width=max(2, int(0.13 * s)))
            d.rectangle((u0 - w * 0.55, sh, u0 + w * 0.55, hip), fill=A(c['top']))
            d.rectangle((u0 - w * 0.45, sh + 0.04 * s, u0 + w * 0.45, hip), fill=A(c['vest']))
        if c.get('pregnant'):
            bx = u0 + (dx * w * 0.6 if face in ('L', 'R') else 0)
            bw = 0.13 * s if face in ('L', 'R') else 0.2 * s
            d.ellipse((bx - bw, hip - 0.24 * s, bx + bw, hip + 0.02 * s), fill=A(c['vest']))
        head(u0, sh - hr * 1.1, hr)
    elif pose in ('sit', 'kneel'):
        top_h = 0.9 if pose == 'sit' else 1.15
        sh = v0 - (top_h - 0.32) * s
        hr = 0.12 * s
        # legs/skirt on the ground in facing direction
        fx, fy = v.p(x + dx * 0.75, 0, z + dz * 0.75)
        if girl:
            d.polygon([(u0 - w * 0.9, v0), (u0 + w * 0.9, v0), (fx + w * 0.6, fy), (fx - w * 0.6, fy)], fill=A(c['skirt']))
        else:
            d.line([(u0, v0 - 0.1 * s), (fx, fy - (0.35 * s if pose == 'sit' else 0))], fill=A(c['legs']), width=max(3, int(0.16 * s)))
        d.rectangle((u0 - w * 0.5, sh, u0 + w * 0.5, v0 - 0.08 * s), fill=A(c['top']))
        d.rectangle((u0 - w * 0.4, sh + 0.04 * s, u0 + w * 0.4, v0 - 0.08 * s), fill=A(c['vest']))
        head(u0, sh - hr * 1.1, hr)
    elif pose == 'lie':
        ex, ey = v.p(x + dx * 1.5, 0, z + dz * 1.5)
        d.line([(u0, v0 - 0.08 * s), (ex, ey - 0.08 * s)], fill=A(c.get('skirt', c.get('legs'))), width=max(3, int(0.3 * s)))
        hr = 0.12 * s
        hx, hy = v.p(x - dx * 0.15, 0.1, z - dz * 0.15)
        head(hx, hy, hr)
    # facing arrow on the ground
    a0 = v.p(x, 0.02, z)
    a1 = v.p(x + dx * 0.7, 0.02, z + dz * 0.7)
    d.line([a0, a1], fill=(255, 255, 255, 200), width=2)
    ang = math.atan2(a1[1] - a0[1], a1[0] - a0[0])
    for da in (2.6, -2.6):
        d.line([a1, (a1[0] + 9 * math.cos(ang + da), a1[1] + 9 * math.sin(ang + da))], fill=(255, 255, 255, 200), width=2)
    # label
    lf = ImageFont.truetype(FONTB, max(13, int(0.11 * s)))
    d.text((u0 + 0.3 * s, v0 - 0.4 * s), f['who'], fill=(255, 255, 255, alpha), font=lf, stroke_width=2, stroke_fill=(0, 0, 0, alpha))


def road_point(t):
    """t in 0..1 along road centre line (pixel space), left->right."""
    near, far = lm.ROAD_NEAR_EDGE[:7], lm.ROAD_FAR_EDGE[:7]
    mid = [((a[0] + b[0]) / 2, (a[1] + b[1]) / 2) for a, b in zip(near, far)]
    seg = t * (len(mid) - 1)
    i = min(int(seg), len(mid) - 2)
    k = seg - i
    return (mid[i][0] * (1 - k) + mid[i + 1][0] * k, mid[i][1] * (1 - k) + mid[i + 1][1] * k)


def draw_wagon(d, v, w):
    u, vv = road_point(w['t'])
    gx, gz = cam.ground_from_pixel(u, vv)
    s = v.s(gx, gz)
    u, vv = v.p(gx, 0, gz)
    sg = 1 if w['dir'] == 'R' else -1
    wood, horse = (110, 80, 52, 255), (92, 56, 36, 255)
    d.polygon([(u - 1.3 * s, vv - 0.6 * s), (u + 1.1 * s, vv - 0.6 * s), (u + 1.1 * s, vv - 1.3 * s), (u - 1.3 * s, vv - 1.3 * s)], fill=wood)
    d.ellipse((u - 1.2 * s, vv - 1.6 * s, u + 1.0 * s, vv - 1.1 * s), fill=(200, 170, 90, 255))  # hay
    for wx in (-0.8, 0.6):
        d.ellipse((u + wx * s - 0.45 * s, vv - 0.9 * s, u + wx * s + 0.45 * s, vv), outline=(50, 36, 26, 255), width=max(2, int(0.08 * s)))
    hx = u + sg * 2.2 * s
    d.ellipse((hx - 0.9 * s, vv - 1.5 * s, hx + 0.9 * s, vv - 0.9 * s), fill=horse)
    d.polygon([(hx + sg * 0.7 * s, vv - 1.3 * s), (hx + sg * 1.3 * s, vv - 1.9 * s), (hx + sg * 1.5 * s, vv - 1.7 * s), (hx + sg * 0.9 * s, vv - 1.1 * s)], fill=horse)
    for lx in (-0.6, -0.3, 0.4, 0.7):
        d.line([(hx + lx * s, vv - 1.0 * s), (hx + lx * s, vv)], fill=horse, width=max(2, int(0.1 * s)))
    d.ellipse((u + sg * 0.6 * s - 0.15 * s, vv - 2.1 * s, u + sg * 0.6 * s + 0.15 * s, vv - 1.8 * s), fill=SKIN + (255,))
    d.rectangle((u + sg * 0.6 * s - 0.17 * s, vv - 1.8 * s, u + sg * 0.6 * s + 0.17 * s, vv - 1.3 * s), fill=(70, 66, 60, 255))
    ax = u + sg * 3.6 * s
    d.line([(u + sg * 3.0 * s, vv - 0.5 * s), (ax, vv - 0.5 * s)], fill=(255, 255, 255, 230), width=3)
    d.polygon([(ax, vv - 0.5 * s - 7), (ax + sg * 12, vv - 0.5 * s), (ax, vv - 0.5 * s + 7)], fill=(255, 255, 255, 230))


def draw_prop(d, v, p):
    s = v.s(p['x'], p['z'])
    u, vv = v.p(p['x'], 0, p['z'])
    d.ellipse((u - 0.25 * s, vv - 0.3 * s, u + 0.25 * s, vv), fill=(150, 110, 60, 255))
    d.arc((u - 0.2 * s, vv - 0.55 * s, u + 0.2 * s, vv - 0.15 * s), 180, 360, fill=(120, 86, 50, 255), width=max(2, int(0.05 * s)))


def draw_path(d, v, pth):
    col = PATH_COL[pth['who'][0]] + (230,)
    pts = [v.p(x, 0.03, z) for x, z in pth['pts']]
    pts = [p for p in pts if p]
    for a, b in zip(pts, pts[1:]):
        n = int(math.dist(a, b) / 14) + 1
        for i in range(0, n, 2):
            p0 = (a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n)
            p1 = (a[0] + (b[0] - a[0]) * (i + 1) / n, a[1] + (b[1] - a[1]) * (i + 1) / n)
            d.line([p0, p1], fill=col, width=4)
    a, b = pts[-2], pts[-1]
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    d.polygon([b, (b[0] - 18 * math.cos(ang - 0.45), b[1] - 18 * math.sin(ang - 0.45)),
               (b[0] - 18 * math.cos(ang + 0.45), b[1] - 18 * math.sin(ang + 0.45))], fill=col)


def render_beat(b):
    plate = Image.open(f"storyboard/plates/PLATE_{b['plate']}.png").convert('RGB')
    img, _ = tilted_plate(plate, b['pitch'])
    v = View(b['pitch'])
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for pth in b.get('paths', []):
        draw_path(d, v, pth)
    if b.get('wagon'):
        draw_wagon(d, v, b['wagon'])
    for p in b.get('props', []):
        draw_prop(d, v, p)
    for f in sorted(b['figs'], key=lambda f: -f['z']):  # far first
        draw_figure(d, v, f)
    if b['speed'] != 'N':
        fb = ImageFont.truetype(FONTB, 44)
        d.text((cam.W - 300, 24), b['rate'], fill=(255, 220, 150, 255), font=fb, stroke_width=3, stroke_fill=(0, 0, 0, 200))
    out = Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')
    os.makedirs('storyboard/panels', exist_ok=True)
    out.save(f"storyboard/panels/BEAT_{b['id']}.jpg", quality=90)
    return out


def card(b, pw, img):
    f = ImageFont.truetype(FONT, 15)
    fs = ImageFont.truetype(FONT, 13)
    fb = ImageFont.truetype(FONTB, 17)
    ih = int(img.height * pw / img.width)
    act = textwrap.wrap(b['action'], 92)[:3]
    camw = textwrap.wrap('CAMERA: ' + b['camera'], 105)[:2]
    aud = textwrap.wrap('SOUND: ' + b['audio'], 105)[:1]
    capt_h = 14 + 20 * len(act) + 17 * (len(camw) + len(aud)) + 10
    H = 34 + ih + capt_h
    c = Image.new('RGB', (pw, H), (240, 240, 232))
    d = ImageDraw.Draw(c)
    d.rectangle((0, 0, pw, 34), fill=(34, 56, 64))
    d.text((12, 7), f"{b['id']}   {b['title']}", fill=(240, 240, 230), font=fb)
    label, col = SPEED[b['speed']]
    if b['speed'] != 'N':
        label = f"{b['rate']}  {label}"
    tw = d.textlength(label, font=fs) + 24
    d.rounded_rectangle((pw - tw - 10, 7, pw - 10, 27), 6, fill=col)
    d.text((pw - tw + 2, 9), label, fill=(30, 30, 30), font=fs)
    c.paste(img.resize((pw, ih), Image.LANCZOS), (0, 34))
    y = 34 + ih + 8
    for line in act:
        d.text((12, y), line, fill=(25, 25, 25), font=f); y += 20
    for line in camw + aud:
        d.text((12, y), line, fill=(95, 95, 95), font=fs); y += 17
    d.text((pw - 230, 34 + ih - 22), f"plate: {b['plate']}", fill=(255, 255, 255), font=fs, stroke_width=2, stroke_fill=(0, 0, 0))
    return c


def main():
    panels = [card(b, 760, render_beat(b)) for b in BEATS]
    cols, gap, margin = 3, 18, 26
    ph = max(p.height for p in panels)
    W = margin * 2 + cols * 760 + (cols - 1) * gap
    rows = math.ceil(len(panels) / cols)
    H = 120 + rows * ph + (rows - 1) * gap + 90
    sheet = Image.new('RGB', (W, H), (17, 27, 33))
    d = ImageDraw.Draw(sheet)
    d.text((margin, 22), 'THE LOVERS  /  Perspective-locked storyboard v1', fill=(240, 240, 230), font=ImageFont.truetype(FONTB, 40))
    d.text((margin, 74), "Look Who's Barking  •  15 beats, one tree camera (A: upper trunk, ~3.6 m), true character scale from tools/camera.py",
           fill=(170, 185, 190), font=ImageFont.truetype(FONT, 20))
    for i, p in enumerate(panels):
        x = margin + (i % cols) * (760 + gap)
        y = 120 + (i // cols) * (ph + gap)
        sheet.paste(p, (x, y))
    fy = H - 78
    fnt = ImageFont.truetype(FONT, 17)
    d.text((margin, fy), 'CAMERA: one mounting point, no translation, no cuts, no zoom. Only moves: tilt down on 12 (+15) and 14 (+8). Hatched band = plate extension needed.',
           fill=(220, 225, 220), font=fnt)
    d.text((margin, fy + 26), 'PLACEHOLDER plates: local paint-out + colour grades of POV_MASTER. Figures are blocking glyphs at true scale; arrows on the ground = facing. Blue/red dashes = Elias/Maeve paths.',
           fill=(220, 225, 220), font=fnt)
    d.text((margin, fy + 52), 'Fast-forward = 1x footage sped up in the edit (seasons 24-48x, wagon layer 4-8x). Never ask the video model for time-lapse.',
           fill=(255, 190, 120), font=fnt)
    sheet.save("storyboard/LOVERS_BOARD_v1.jpg", quality=92)
    print('wrote storyboard/LOVERS_BOARD_v1.jpg', sheet.size)


if __name__ == '__main__':
    main()
