# Frame Bible v1: The Lovers, tree camera A

Annotated frame: `bible/FRAME_BIBLE_v1.png`
Camera model: `tools/camera.py`
Landmark traces: `tools/landmarks.py`

POV_MASTER stays the approved composition. This file measures what that image implies, so that every plate, storyboard panel and generated clip can be checked against numbers rather than against impressions.

## Camera A

| Value | Estimate | How it was measured |
|---|---|---|
| Lens height | about 3.6 m | Fence posts (assumed 1.2 m) and the hay wagon with driver (assumed 2.8 m) both land within 2–8 px of the model at this height |
| Neutral pitch | 14.7° down | Horizon sits at y = 125 px in a 941 px frame |
| Focal length | 1312 px, about 65° horizontal | Chosen to fit; height and focal length trade off, so treat both as ±20% |
| Allowed moves | Tilt −5° to +15°, yaw ±10° | Handover rule: head-like turns only |
| Used moves | Tilt +15° on beat 12 and +8° on beat 14 | Every other beat holds neutral |

The 3.6 m height agrees with the orange mark on CAMERA_LOCATION_MARKED and with the handover's 3–4 m.

These are estimates taken from an AI image, not survey numbers. If you change them, change them in `tools/camera.py` and re-render.

## What the measurement shows

**The couple in POV_MASTER are about 2.3 times too large.** They sit at roughly 5.6 m from the trunk. At that distance a seated adult should stand about 170 px tall in the frame; they are painted at about 400 px. The landscape was rendered from a high camera and the people from a low one. The board uses true scale. Faces will be small, which suits a watcher in a tree, but it means any beat that needs a readable face has to stage it (see the staging rule below).

**The ground under the tree is out of frame.** At neutral pitch the bottom edge of the frame lands 5.25 m from the trunk. Tilting to the +15° limit brings that in to about 3.3 m. Anyone touching the trunk is invisible.

**The carving cannot happen at the lens.** The lens is 3.6 m up, out of a standing person's reach. Decision: the carving is heard, not seen. They walk out of frame below the lens and come back.

**Any tilt or yaw exposes picture that isn't in the master.** A +15° tilt needs about 350 px of new ground below the current bottom edge, and a +8° tilt needs about 185 px. For that reason the board uses only the two tilts above and no yaw at all. Both tilts need a downward plate extension before video work.

## Locked landmarks

These must not move between plates or clips. Tolerance is about 6 px at 1672×941.

- **Horizon:** y = 125.
- **Fence:**
  - top rail runs from (0, 335) to (1340, 213)
  - 11 visible posts, listed in `landmarks.py`
  - post spacing is part of the lock
- **Road:**
  - near edge runs from (0, 690) to the bend at (1500, 255)
  - far edge runs from (0, 455) to (1360, 218)
  - the road bends right and back behind the right-hand tree line
- **Puddles:**
  - large: centred near (480, 545)
  - small: (590, 414)
  - right: (1090, 365)
  - puddles may fill and dry with weather, but their beds stay put
- **Distant hill:** fixed. The ruin on it is an image detail, not story canon.
- **Sun:** at (395, 80) in the master only. It moves with season and time of day.

## Ground plane

The blue grid in the annotated frame is the ground in metres from the trunk base. The table gives distances along the neutral view.

| Distance | Where it falls in the frame |
|---|---|
| 6 m | Just above the bottom edge |
| 8–11 m | The road's near edge on the left half of the frame |
| 20 m | The fence on the left |
| About 30 m | The wagon in the master |

Scale bars in the annotated frame show a 1.7 m standing adult and a 0.9 m seated adult at true size for several distances. Use them to reject generated frames where people are too big or too small.

## Stage zones

| Zone | Ground area | Use |
|---|---|---|
| Stage A | x −2.5 to +3.5, z 5.6 to 8.5 | Grass between the frame bottom and the road. All sitting scenes. |
| Stage B | x −2.0 to +1.5, z 9.0 to 10.5 | Road verge. Arrivals, departures, the argument. |
| Entry R | x +5 to +9, z 7 to 12 | His entrance across the grass in beats 11 and 15. |

## Staging rule for faces

The lens looks over the couple's backs toward the road. A person facing the road shows the camera the back of their head. The board therefore records a facing for every character in every beat:

- **cam:** faces the tree. Full face visible from above. Use sparingly. The first clear face is Maeve in beat 05, and it should feel earned.
- **L / R:** profile. The default for two-person scenes. Two people facing each other along the x axis both read in profile.
- **away:** back to the lens. Only for beats where the face doesn't matter.

## Rejecting a generated frame

Reject the frame if any of these happen:

- A tree trunk or framing leaves appear.
- The horizon, the fence posts or the road shift by more than about 6 px from the traces.
- People fall outside the scale bars for their distance by more than about 15%.
- The road changes direction.
- The puddle beds move.
- The camera tilts or turns where the beat card doesn't say so.
