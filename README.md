# Look Who's Barking

A collection of short films seen entirely from one old tree. The tree is the camera. This repo holds the development material.

## Where things are

- `bible/HANDOVER.md`: the full creative and production handover. Its locked rules still apply.
- `bible/FRAME_BIBLE.md` and `bible/FRAME_BIBLE_v1.png`: camera A measured from the approved master frame (height, pitch, ground grid, locked landmarks, stage zones, staging rule for faces).
- `storyboard/LOVERS_BOARD_v1.jpg`: the perspective-locked contact sheet for The Lovers, 15 beats.
- `storyboard/LOVERS_BEATS.md`: one card per beat (positions, facing, camera, plate, sound, seam notes). Generated from code.
- `storyboard/SEAM_PLAN.md`: how the film splits into generated clips with hidden joins, plus costs.
- `storyboard/plates/`: the empty plate and the season grades. All of them are **placeholders**: a local paint-out and colour grades of POV_MASTER, not generated plates.
- `storyboard/panels/`: full-resolution panels.
- `reference_images/`: the original concept images. Read the handover to see which are approved and which are historical.
- `tools/`: the Python (PIL and numpy) that produces all of the above.

## Rebuild

```
python3 tools/frame_bible.py   # annotated frame bible
python3 tools/clean_plate.py   # empty placeholder plate
python3 tools/plates.py        # season placeholder grades
python3 tools/board.py         # panels and contact sheet
python3 tools/cards.py         # beat cards
```

Beats, positions and facings live in `tools/beats.py`. The camera numbers live in `tools/camera.py`. Change them there and re-run.
