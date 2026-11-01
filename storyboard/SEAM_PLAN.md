# The Lovers: seam plan v1

The film has to read as one unbroken observation. In practice it's built from short generated clips, and the joins are hidden. This plan places every join where it is easiest to hide: when the frame is empty, when someone is holding still, or behind a passing wagon.

## Rules

1. **Every clip starts and ends on a known frame.** Either the empty plate for that season, or the last frame of the previous accepted clip. Use first-frame/last-frame conditioning. Never let a model invent the opening frame.
2. **Fast-forward is done in the edit.**
   - Generate normal-speed footage, then speed it up.
   - Never prompt a video model for "time-lapse". It gives you smear and morphing, which the handover rejects.
3. **Each fast-forward has two layers:**
   - The seasons and light come from interpolating between season plates. This can run at any speed.
   - The action (wagon, walkers, brief visits) comes from 1x clips composited on top.
4. **Wagons and walkers play at 4–8x, slower than the seasons.** See the decision below.
5. **Ageing happens off screen.** A character leaves the frame at one age and comes back at the next. No on-screen morphing.
6. **The camera moves only in beats 12 and 14.** Those two clips need a plate extended downward first (about 350 px and about 185 px).

## Decided: wagons and walkers play at 4–8x

A wagon takes roughly 8 seconds to cross the frame at walking pace. At 32x it would be on screen for a quarter of a second, which reads as a flicker, not as "a horse pulling a wagon with turning wheels".

So the two layers run at different rates. The season and light layer runs at 24–48x. The wagon layer plays at 4–8x, putting it on screen for 1–2 seconds with readable hooves and turning wheels. Strictly this is not one playback rate, but it reads as real footage sped up, which is what the handover asks for.

In practice:

- Generate each wagon pass at 1x, 8–10 s long, so there is enough footage to retime.
- Retime the wagon layer to 4–8x in the edit. Use the slower end when the wagon is nearer the lens.
- The wagon's lighting has to match the season plate underneath it at the moment it crosses. Don't let it drift through the season change.

Walkers and other travellers on foot get the same treatment. Someone walking along the road takes about 20 seconds to cross the frame at 1x, so at 4–8x they are on screen for 3–5 seconds and their steps read. The same rules apply:

- A 20-second crossing is longer than one Kling clip (10 s maximum), so either chain two clips joined at mid-frame, or have the walker cut the corner on a diagonal so the crossing fits in about 10 s.
- Match their lighting to the season plate at the moment they cross.
- This applies only to strangers passing through. The couple's sped-up visits in beat 13 stay at 48x on purpose: they are meant to flicker by.

## Segments

Lengths are generation targets. Kling 3.0 clips run 5–10 s, so long beats are split into chains of clips.

| Seg | Beat | Start frame | End frame | Content | Est. 1x length | Seam type |
|---|---|---|---|---|---|---|
| S01 | 01 | Empty SUMMER | Empty SUMMER | Ambient only: wind in the grass, clouds | 8 s (loop or extend) | Empty frame |
| S02a | 02 | Empty SUMMER | M_T1 kneeling, E_T1 seated, both still | She enters from the left on the road and walks to Stage A; he is already seated | 10 s | Held stillness |
| S02b–d | 02 | Previous end | Both still | Conversation, laughter. Chain 3 clips | 30 s | Held stillness |
| S03 | 03 | S02d end | Empty SUMMER | They get up, chase, and run out of frame left | 10 s | Empty frame |
| S04-plate | 04 | Empty SUMMER | Empty WINTER | Plate interpolation SUMMER → AUTUMN_LATE → WINTER | n/a (made in the edit) | n/a |
| S04-wagon | 04 | Empty AUTUMN_LATE | Empty AUTUMN_LATE | Wagon crosses left to right at 1x; composited | 8 s | Wagon enters and exits frame |
| S05a–b | 05 | Empty SUMMER | Both seated, still | Older teens arrive and sit; she turns to face the tree | 20 s | Held stillness |
| S06 | 06 | Empty AUTUMN_GOLD | Both standing still | Kiss, laugh, push | 10 s | Held stillness (1 s handles) |
| S07-plate | 07 | Empty AUTUMN_GOLD | Empty SUMMER | Rain plate, then drying | n/a | n/a |
| S07-wagon | 07 | Empty SPRING_RAIN | Empty SPRING_RAIN | Same wagon, right to left, in rain | 8 s | Wagon in and out |
| S08a–c | 08 | Empty SUMMER | Empty SUMMER | Long visit, A1 ages. Chain 3 clips | 30 s | Held stillness, then exit |
| S09a | 09 | Empty AUTUMN_LATE | Him leaving at the left edge | Argument | 10 s | He crosses the left frame edge |
| S09b | 09 | S09a end | Empty AUTUMN_LATE | She holds, sits, then leaves | 10 s | Empty frame |
| S10 | 10 | Empty AUTUMN_LATE | Empty SUMMER | Winter interpolation; walker and wagon layers, both at 4–8x | n/a + 8 s wagon + 10–20 s walker | Empty frame |
| S11 | 11 | Empty SUMMER | Embrace held | Two entries, apology, embrace | 10 s | Held stillness |
| S12 | 12 | S11 end (needs the extended plate) | Empty AUTUMN_GOLD (tilted, then back to neutral) | They walk under the lens. Carving is sound only | 10 s | Empty frame |
| S13 | 13 | Empty AUTUMN_GOLD | Empty SOFT_AFTERNOON | Season cycles plus 3–4 short 1x visit clips sped up | n/a + 4 × 5 s | Empty frame between visits |
| S14 | 14 | Empty SOFT_AFTERNOON | M_A2P standing, looking up | Slow down on the empty frame, then she enters at 1x and passes under the lens (needs the extended plate) | 10–15 s | Held stillness |
| S15a | 15 | S14 end | Both standing, his hand on her stomach | Footsteps, his entrance from the right | 10 s | Held stillness |
| S15b | 15 | S15a end | Empty SOFT_AFTERNOON | They leave down the road; final hold on the empty clearing | 10 s + hold | End of film |

## What it costs to try

These are Higgsfield preflight prices quoted on 1 Nov 2026.

| Item | Price |
|---|---|
| 5 s Kling 3.0 image-to-video clip | 8.75 credits |
| 5 s Seedance 2.5 clip | 35 credits |
| One medium/2k plate edit (GPT Image 2.5) | 1 credit, but needs Higgsfield's Basic plan |
| FLUX 3 image edit | 2 credits at 1k, 3 at 2k |

Proof A (S02a) and proof B (S04-wagon plus the plate interpolation) need about 4 Kling clips, plus retries, plus 4 proper season plates and 2 plate extensions. Budget 60–80 credits.

The current balance is 2.08 credits on the free plan, which can't buy a single clip.
