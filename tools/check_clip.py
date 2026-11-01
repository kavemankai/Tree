"""Check a generated clip against the locked landmarks.
Usage: python3 tools/check_clip.py CLIP.mp4 OUT_DIR
Extracts 1 frame per second with ffmpeg, runs the plate geometry check on each,
and writes a contact strip OUT_DIR/strip.jpg. Any frame whose landmark offset
exceeds 6 px means the camera drifted or the model redrew the scene.
"""
import os, subprocess, sys, glob
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
import numpy as np
import check_plate as cp
import landmarks as lm


def main(clip, out):
    os.makedirs(out, exist_ok=True)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', clip, '-vf', 'fps=1',
                    os.path.join(out, 'f_%03d.png')], check=True)
    frames = sorted(glob.glob(os.path.join(out, 'f_*.png')))
    ref = Image.open('reference_images/POV_MASTER.png').convert('RGB')
    er = cp.edge_map(ref)
    worst_all = 0
    for f in frames:
        im = Image.open(f).convert('RGB').resize((cp.W, cp.H), Image.LANCZOS)
        en = cp.edge_map(im)
        res = {
            'fence': cp.offset_score(er, en, cp.sample_line(lm.FENCE_TOP_RAIL)),
            'road_far': cp.offset_score(er, en, cp.sample_line(lm.ROAD_FAR_EDGE)),
            'horizon': cp.offset_score(er, en, [(x, lm.HORIZON_Y) for x in range(40, 1240, 20)]),
        }
        vals = [m for m, _ in res.values() if m is not None]
        worst = max(vals) if vals else None
        worst_all = max(worst_all, worst or 0)
        print(os.path.basename(f), ' '.join(f'{k}={m}' for k, (m, _) in res.items()))
    thumbs = [Image.open(f).convert('RGB').resize((418, 235)) for f in frames]
    cols = 4
    rows = (len(thumbs) + cols - 1) // cols
    strip = Image.new('RGB', (418 * cols, 235 * rows))
    for i, t in enumerate(thumbs):
        strip.paste(t, ((i % cols) * 418, (i // cols) * 235))
    strip.save(os.path.join(out, 'strip.jpg'), quality=88)
    print('worst offset', worst_all, 'PASS' if worst_all <= 6 else 'FAIL / CHECK')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
