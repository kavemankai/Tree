"""Generate storyboard/LOVERS_BEATS.md from tools/beats.py.
Run from repo root:  python3 tools/cards.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from beats import BEATS, CAST, SPEED

FACE = {'cam': 'toward the tree (face visible)', 'away': 'toward the road (back to lens)',
        'L': 'profile, facing frame left', 'R': 'profile, facing frame right'}
REFS = {
    'T1': 'reference_images/CHARACTERS_ELIAS_MAEVE.png (exists), pose ref FIRST_MEETING_PERFORMANCE_REFERENCE.png',
    'T2': 'late-teen identity sheet (TO BUILD from the T1 sheet)',
    'A1': 'early-twenties identity sheet (TO BUILD)',
    'A2': 'about-thirty identity sheet (TO BUILD)',
    'A2P': 'about-thirty pregnant sheet (TO BUILD)',
}
STATE = {'N': 'normal (1x)', 'UP': 'accelerating', 'FF': 'accelerated', 'DOWN': 'decelerating'}


def main():
    L = ['# THE LOVERS: beat cards v1', '',
         'Generated from `tools/beats.py`. Edit the data there and re-run `python3 tools/cards.py` and `python3 tools/board.py`; do not hand-edit this file.', '',
         'Camera anchor for every beat: **A** (upper trunk at the branch junction, about 3.6 m up). XYZ never changes. '
         'Ground positions are metres from the trunk base: x to the right of the neutral view, z forward. See `bible/FRAME_BIBLE.md`.', '',
         'Panels: `storyboard/panels/BEAT_XX.jpg`. Contact sheet: `storyboard/LOVERS_BOARD_v1.jpg`.', '']
    for b in BEATS:
        L += [f"## {b['id']}  {b['title']}", '',
              f"- **Time state:** {STATE[b['speed']]}, playback {b['rate']}",
              f"- **Camera:** anchor A, yaw {b['yaw']:+d} deg, pitch {b['pitch']:+d} deg from neutral. {b['camera']}",
              f"- **Plate:** `PLATE_{b['plate']}` (placeholder grade)"]
        if b['figs']:
            L.append('- **People:**')
            for f in b['figs']:
                ghost = ' (sped-up visit, appears briefly)' if f.get('ghost') else ''
                L.append(f"  - `{f['who']}` {CAST[f['who']]['name']}: {f['pose']} at x={f['x']:+.1f} m, z={f['z']:.1f} m, {FACE[f['face']]}{ghost}")
        else:
            L.append('- **People:** none in frame')
        for p in b.get('paths', []):
            pts = ' -> '.join(f'({x:+.1f}, {z:.1f})' for x, z in p['pts'])
            L.append(f"- **Path `{p['who']}`:** {pts}")
        if b.get('wagon'):
            w = b['wagon']
            L.append(f"- **Wagon:** on the road, travelling {'left to right' if w['dir'] == 'R' else 'right to left'} (same wagon, horse and driver every time)")
        for p in b.get('props', []):
            L.append(f"- **Prop:** {p['kind']} at x={p['x']:+.1f}, z={p['z']:.1f}")
        L += [f"- **Action:** {b['action']}",
              f"- **Sound:** {b['audio']}",
              f"- **Seam / generation:** {b['seam']}"]
        ids = sorted({f['who'].split('_')[1] for f in b['figs']})
        if ids:
            L.append('- **Reference assets:** ' + '; '.join(f'{i}: {REFS[i]}' for i in ids))
        L.append('- **Accept / reject notes:** (fill in per take)')
        L.append('')
    with open('storyboard/LOVERS_BEATS.md', 'w') as fh:
        fh.write('\n'.join(L))
    print('wrote storyboard/LOVERS_BEATS.md')


if __name__ == '__main__':
    main()
