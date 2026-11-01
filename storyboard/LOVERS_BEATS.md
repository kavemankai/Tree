# THE LOVERS: beat cards v1

Generated from `tools/beats.py`. Edit the data there and re-run `python3 tools/cards.py` and `python3 tools/board.py`; do not hand-edit this file.

Camera anchor for every beat: **A** (upper trunk at the branch junction, about 3.6 m up). XYZ never changes. Ground positions are metres from the trunk base: x to the right of the neutral view, z forward. See `bible/FRAME_BIBLE.md`.

Panels: `storyboard/panels/BEAT_XX.jpg`. Contact sheet: `storyboard/LOVERS_BOARD_v1.jpg`.

## 01  Opening hold

- **Time state:** normal (1x), playback 1x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Neutral. Establish road, fence, horizon. No movement at all.
- **Plate:** `PLATE_SUMMER_DAY` (placeholder grade)
- **People:** none in frame
- **Action:** Empty clearing in summer afternoon light. Nothing happens for a long breath.
- **Sound:** Wind in leaves (close, above lens), birds, distant cicadas.
- **Seam / generation:** Seg S01 start frame = empty SUMMER_DAY plate.
- **Accept / reject notes:** (fill in per take)

## 02  First meeting

- **Time state:** normal (1x), playback 1x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Neutral. Both in PROFILE to each other so faces read in 3/4-profile from above.
- **Plate:** `PLATE_SUMMER_DAY` (placeholder grade)
- **People:**
  - `E_T1` Elias (teen): sit at x=+1.7 m, z=6.4 m, profile, facing frame left
  - `M_T1` Maeve (teen): kneel at x=-0.4 m, z=6.7 m, profile, facing frame right
- **Path `M_T1`:** (-6.0, 9.6) -> (-3.0, 8.5) -> (-0.6, 6.9)
- **Prop:** basket at x=-1.1, z=6.6
- **Action:** She comes off the road with the flower basket; he is already sitting. She kneels, leans toward him. Teasing, laughter, a long unhurried talk.
- **Sound:** Their voices at a distance of ~7 m (not close-mic), grass, birds.
- **Seam / generation:** Seg S02 starts on S01 end frame (empty). She enters from frame left on the road.
- **Reference assets:** T1: reference_images/CHARACTERS_ELIAS_MAEVE.png (exists), pose ref FIRST_MEETING_PERFORMANCE_REFERENCE.png
- **Accept / reject notes:** (fill in per take)

## 03  Early friendship

- **Time state:** normal (1x), playback 1x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Neutral. Let them run out of frame left; the camera does not follow.
- **Plate:** `PLATE_SUMMER_DAY` (placeholder grade)
- **People:**
  - `E_T1` Elias (teen): walk at x=-1.2 m, z=9.6 m, profile, facing frame left
  - `M_T1` Maeve (teen): walk at x=+1.0 m, z=8.0 m, profile, facing frame left
- **Path `M_T1`:** (+2.5, 7.0) -> (+1.0, 8.0) -> (-2.5, 10.0)
- **Path `E_T1`:** (+0.5, 8.5) -> (-1.2, 9.6) -> (-4.5, 10.6)
- **Action:** They muck around: chase along the verge, throw something, sit, get up again. Unimportant time.
- **Sound:** Running steps on grass, shouts, laughter fading toward the road.
- **Seam / generation:** Natural seam: both exit frame left along the road. Frame empty = cut point S03/S04.
- **Reference assets:** T1: reference_images/CHARACTERS_ELIAS_MAEVE.png (exists), pose ref FIRST_MEETING_PERFORMANCE_REFERENCE.png
- **Accept / reject notes:** (fill in per take)

## 04  Ramp 1: the world continues

- **Time state:** accelerated, playback 32x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Neutral, locked. Plate cross-interpolates SUMMER -> AUTUMN_LATE -> WINTER.
- **Plate:** `PLATE_AUTUMN_LATE` (placeholder grade)
- **People:** none in frame
- **Wagon:** on the road, travelling left to right (same wagon, horse and driver every time)
- **Action:** Empty clearing sped up: clouds race, light swings, leaves turn, first snow. A wagon crosses left to right more slowly than the world around it (4-8x), so hooves and wheels read.
- **Sound:** Ambience ramps with speed: wind gusts compress, hooves become a rapid patter then gone.
- **Seam / generation:** Generate wagon pass at 1x (8-10 s) on AUTUMN_LATE. Season layer runs at 32x; wagon layer is retimed to 4-8x so it reads (1-2 s on screen).
- **Accept / reject notes:** (fill in per take)

## 05  Older teens

- **Time state:** normal (1x), playback 1x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Neutral. Her face toward the lens = the first time we see a face clearly. Earned, not default.
- **Plate:** `PLATE_SUMMER_DAY` (placeholder grade)
- **People:**
  - `E_T2` Elias (late teen): sit at x=+0.2 m, z=6.3 m, profile, facing frame right
  - `M_T2` Maeve (late teen): sit at x=+1.3 m, z=6.6 m, toward the tree (face visible)
- **Action:** Same spot, a year or two on. They sit closer and talk less. She has turned to face the tree, he watches her.
- **Sound:** Quiet talk, long pauses, a bee.
- **Seam / generation:** Enter on empty frame after S04 decelerates. Age change happened offscreen.
- **Reference assets:** T2: late-teen identity sheet (TO BUILD from the T1 sheet)
- **Accept / reject notes:** (fill in per take)

## 06  First kiss

- **Time state:** normal (1x), playback 1x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Profile two-shot from above. No push-in. Hold through the laugh.
- **Plate:** `PLATE_AUTUMN_GOLD` (placeholder grade)
- **People:**
  - `E_T2` Elias (late teen): stand at x=+0.9 m, z=7.2 m, profile, facing frame left
  - `M_T2` Maeve (late teen): stand at x=+0.4 m, z=7.2 m, profile, facing frame right
- **Action:** Standing at the edge of Stage A in golden light. Hesitation, a shy kiss, a laugh, she pushes him away playfully.
- **Sound:** Wind drops right before the kiss. Laughter breaks the hush.
- **Seam / generation:** Single generated performance segment; start and end on both standing still for 1 s (clean seam handles).
- **Reference assets:** T2: late-teen identity sheet (TO BUILD from the T1 sheet)
- **Accept / reject notes:** (fill in per take)

## 07  Ramp 2: more time

- **Time state:** accelerated, playback 32x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Locked neutral.
- **Plate:** `PLATE_SPRING_RAIN` (placeholder grade)
- **People:** none in frame
- **Wagon:** on the road, travelling right to left (same wagon, horse and driver every time)
- **Action:** Rain sweeps through, puddles fill and dry, the same wagon returns right to left. One distant dog crosses the field.
- **Sound:** Rain hiss compressed, wagon creak, then dry wind.
- **Seam / generation:** Wagon return generated at 1x (8-10 s) on SPRING_RAIN plate, same wagon/driver refs as beat 04. Wagon layer at 4-8x over the 32x season layer.
- **Accept / reject notes:** (fill in per take)

## 08  Young adults

- **Time state:** normal (1x), playback 1x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Neutral. His face to lens, hers in profile, both readable.
- **Plate:** `PLATE_SUMMER_DAY` (placeholder grade)
- **People:**
  - `E_A1` Elias (20s): sit at x=+0.8 m, z=6.3 m, toward the tree (face visible)
  - `M_A1` Maeve (20s): lie at x=-0.3 m, z=6.0 m, profile, facing frame right
- **Prop:** basket at x=+1.9, z=6.5
- **Action:** A long comfortable visit: he sits against nothing, facing the tree; she lies with her head near his knee. Plans, teasing, silence.
- **Sound:** Low conversation, mostly unintelligible, real silences.
- **Seam / generation:** Long take. Split into 2-3 generated segments with seams on still moments.
- **Reference assets:** A1: early-twenties identity sheet (TO BUILD)
- **Accept / reject notes:** (fill in per take)

## 09  Argument

- **Time state:** normal (1x), playback 1x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Neutral. Camera does not follow him out. Hold on her.
- **Plate:** `PLATE_AUTUMN_LATE` (placeholder grade)
- **People:**
  - `E_A1` Elias (20s): walk at x=-1.6 m, z=9.8 m, profile, facing frame left
  - `M_A1` Maeve (20s): stand at x=+0.8 m, z=7.0 m, profile, facing frame left
- **Path `E_A1`:** (+0.2, 7.2) -> (-1.6, 9.8) -> (-6.5, 10.8)
- **Action:** Disagreement grows. He walks off down the road to frame left; she stays standing, watching him go, then sits.
- **Sound:** Raised voices, then his footsteps on the road, then wind.
- **Seam / generation:** Seam when he passes frame-left edge. Her hold continues as one segment.
- **Reference assets:** A1: early-twenties identity sheet (TO BUILD)
- **Accept / reject notes:** (fill in per take)

## 10  Ramp 3: absence

- **Time state:** accelerated, playback 24x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Locked neutral.
- **Plate:** `PLATE_WINTER_SNOW` (placeholder grade)
- **People:** none in frame
- **Wagon:** on the road, travelling left to right (same wagon, horse and driver every time)
- **Action:** Neither of them. Snow comes and goes. A lone walker and the wagon pass more slowly than the world around them (4-8x), so their steps and wheels read.
- **Sound:** Snow-muffled ambience, sped wind, a crow.
- **Seam / generation:** Empty plate interpolation at 24x + composited walker and wagon layers, both retimed to 4-8x. Walker crossing generated at 1x, 10-20 s (chain two clips if needed).
- **Accept / reject notes:** (fill in per take)

## 11  Reconciliation

- **Time state:** normal (1x), playback 1x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Neutral. Profile embrace. No move.
- **Plate:** `PLATE_SUMMER_DAY` (placeholder grade)
- **People:**
  - `E_A1` Elias (20s): stand at x=+0.6 m, z=7.4 m, profile, facing frame left
  - `M_A1` Maeve (20s): stand at x=+0.2 m, z=7.4 m, profile, facing frame right
- **Path `M_A1`:** (-6.0, 10.2) -> (-2.5, 9.0) -> (+0.1, 7.5)
- **Path `E_A1`:** (+7.5, 9.0) -> (+3.5, 8.0) -> (+0.7, 7.5)
- **Action:** She arrives from the road, he from frame right across the grass. Hesitation, part of an apology, an embrace.
- **Sound:** Half-heard apology, then only wind and the embrace.
- **Seam / generation:** Start on empty frame; two entries generated together.
- **Reference assets:** A1: early-twenties identity sheet (TO BUILD)
- **Accept / reject notes:** (fill in per take)

## 12  The carving (heard)

- **Time state:** normal (1x), playback 1x
- **Camera:** anchor A, yaw +0 deg, pitch +15 deg from neutral. Tilt to the +15 limit as they approach, then hold on the empty clearing during the carving. Bottom band of tilted frame is NOT in the master plate: needs a generated ground extension.
- **Plate:** `PLATE_AUTUMN_GOLD` (placeholder grade)
- **People:** none in frame
- **Path `E_A1`:** (+0.5, 7.0) -> (+0.3, 5.0) -> (+0.1, 3.0)
- **Action:** They walk toward the trunk and pass out of frame below the lens. We hear the knife scrape bark, their murmurs and a laugh. They step back into view, look up at the tree, leave.
- **Sound:** Knife on bark, very close and loud: the tree feels it. Breathing, a laugh.
- **Seam / generation:** Empty-frame hold = ideal seam. Tilt-down shot needs an extended plate (outpaint downward ~350 px).
- **Accept / reject notes:** (fill in per take)

## 13  Ramp 4: years of ordinary life

- **Time state:** accelerated, playback 48x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Locked neutral.
- **Plate:** `PLATE_AUTUMN_LATE` (placeholder grade)
- **People:**
  - `E_A2` Elias (30): walk at x=+2.0 m, z=10.0 m, profile, facing frame left (sped-up visit, appears briefly)
  - `M_A2` Maeve (30): walk at x=+1.4 m, z=10.2 m, profile, facing frame left (sped-up visit, appears briefly)
- **Wagon:** on the road, travelling left to right (same wagon, horse and driver every time)
- **Action:** Seasons cycle repeatedly. Brief uncomplicated visits flicker by at speed: the two of them walking past, sitting, leaving. Ageing happens between visits.
- **Sound:** Compressed seasonal ambience; a few words of their voices sped up.
- **Seam / generation:** Short 1x visit clips, each sped 48x, separated by empty-plate interpolation. Wagon layer at 4-8x.
- **Reference assets:** A2: about-thirty identity sheet (TO BUILD)
- **Accept / reject notes:** (fill in per take)

## 14  She returns

- **Time state:** decelerating, playback 48x -> 1x
- **Camera:** anchor A, yaw +0 deg, pitch +8 deg from neutral. Tilt +8 as she approaches; return toward neutral when she steps back.
- **Plate:** `PLATE_SOFT_AFTERNOON` (placeholder grade)
- **People:**
  - `M_A2P` Maeve (30, pregnant): stand at x=+0.3 m, z=6.2 m, toward the tree (face visible)
- **Path `M_A2P`:** (-6.0, 10.4) -> (-2.0, 8.8) -> (+0.3, 6.2) -> (+0.2, 4.0)
- **Action:** Speed eases to real time as she comes off the road alone, visibly pregnant. She walks to the tree, passes below the lens (touching the carving, heard), steps back into view and stands looking up.
- **Sound:** Silence apart from wind and birds. Her hand on bark: a soft rasp, close.
- **Seam / generation:** Deceleration happens on an empty frame BEFORE she enters, so her performance is all 1x.
- **Reference assets:** A2P: about-thirty pregnant sheet (TO BUILD)
- **Accept / reject notes:** (fill in per take)

## 15  He enters; final hold

- **Time state:** normal (1x), playback 1x
- **Camera:** anchor A, yaw +0 deg, pitch +0 deg from neutral. Neutral. No zoom, no fade. End on empty frame.
- **Plate:** `PLATE_SOFT_AFTERNOON` (placeholder grade)
- **People:**
  - `M_A2P` Maeve (30, pregnant): stand at x=+0.3 m, z=6.3 m, profile, facing frame right
  - `E_A2` Elias (30): stand at x=+0.9 m, z=6.5 m, profile, facing frame left
- **Path `E_A2`:** (+8.0, 9.5) -> (+4.0, 7.6) -> (+1.0, 6.5)
- **Action:** Footsteps first, then he walks in from frame right. No drama: a smile, his hand on her stomach. They stay a while, then leave together down the road. The tree holds on the empty clearing.
- **Sound:** Footsteps on grass before he is visible. Then wind.
- **Seam / generation:** No wagon, no passers-by. Final segment ends on empty SOFT_AFTERNOON plate.
- **Reference assets:** A2: about-thirty identity sheet (TO BUILD); A2P: about-thirty pregnant sheet (TO BUILD)
- **Accept / reject notes:** (fill in per take)
