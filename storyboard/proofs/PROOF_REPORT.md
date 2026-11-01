# Proof report: plates and first two clips (1 Nov 2026)

Spent 32 credits. Balance 40.08 (Basic plan).

| Item | Model | Credits | Result |
|---|---|---|---|
| Empty master plate | GPT Image 2.5, medium, 2k | 1 | Pass. Landmark offset 0 px |
| Season plates ×5 (summer, late autumn, winter, spring rain, soft afternoon) | GPT Image 2.5, medium, 2k | 5 | All pass, 0–3 px |
| S02a end frame (both teens placed at board positions) | GPT Image 2.5 with plate, character sheet and blocking panel as references | 1 | Pass, 2 px. True scale, correct costumes, profile faces |
| Proof A: teen meeting, 10 s | Kling 3.0 std, start = empty summer plate, end = composite | 12.5 | Camera locked (≤2 px). Entrances at wrong scale. Action rushed |
| Proof B: wagon pass, 10 s | Kling 3.0 std, start = end = empty late-autumn plate | 12.5 | Camera locked (≤1 px). Wagon about 2.5× too big |

Generated plates are in `storyboard/plates/GEN_*_2k.png` (2688×1520). Frame strips (one frame per second) are `PROOF_A_strip.jpg` and `PROOF_B_strip.jpg`. Checks are run with `tools/check_plate.py` and `tools/check_clip.py`.

## What works

**The camera lock works.** Landmark-based plate edits hold the geometry: fence, road and horizon all land within 3 px of the master. Kling with start and end frames never moved the camera, in either clip, across all 20 sampled frames. The project's biggest fear, the background drifting between clips, did not happen.

**A keyframe pins scale and identity.** Feeding GPT Image the blocking panel as a reference put the teens exactly where the board has them, at the size the camera model predicts. Wherever the clip is pinned by that frame, its people look right.

## What fails

**Scale between keyframes.** The video model thinks in eye-level shots:

- Anyone entering near the lens is drawn as a giant, about half the frame height, and shrinks as they move away. The boy entering in proof A and the whole wagon in proof B both do this.
- This is the same mistake as the couple in the original POV_MASTER.

**Pacing.** Ten seconds can't hold two entrances, a sit-down and a kneel. The model rushes all of it.

**Artifacts.** A stray piece of red skirt appears at the boy's feet in the second frame of proof A.

## What to change before spending more

1. **Pin every entrance with a keyframe at true scale.** Composite the character or wagon just inside the frame edge, at the size the camera model gives, and use that as the start frame. The empty plate should only be a keyframe for clips where nothing enters close to the lens.
2. **Bring people in from far away.** Prefer entrances along the road or across the back of Stage A. Avoid entering at the near right edge, where the model inflates scale most.
3. **One action per clip, 15 s maximum.** Split S02a into two clips: he arrives and sits; then she arrives and kneels. Each clip gets its own pinned start and end frames.
4. **For the wagon, composite a true-scale wagon at the left road edge as the start frame.** End on the empty plate. If it still inflates, add a mid-road keyframe and chain two clips.
5. **Kling pro mode needs the Plus plan.** Std mode was used here. Std is good enough to judge motion and scale; pro is worth it only for final takes.

## Cost of the next round

The reworked S02a (2 keyframes at 1 credit each, plus 2 clips at about 12.5–17.5 each) and the reworked wagon (1 keyframe plus 1 clip) come to about 45–55 credits. That is more than the current 40.08.
