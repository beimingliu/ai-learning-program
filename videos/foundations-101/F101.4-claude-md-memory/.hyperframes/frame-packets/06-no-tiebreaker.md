# Frame packet: 06-no-tiebreaker

## Project inputs

- Project: /Users/beimingliu/beimingliu/ai-learning-program/videos/foundations-101/F101.4-claude-md-memory
- Design truth: /Users/beimingliu/beimingliu/ai-learning-program/videos/foundations-101/F101.4-claude-md-memory/frame.md
- RULES_DIR: /Users/beimingliu/.agents/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 6 — No tiebreaker

- status: outline
- src: compositions/06-no-tiebreaker.html
- rules: reactive-displacement, scale-swap-transition
- duration: 10.88s
- voiceover: "If two files disagree, there is no magical tiebreaker. Claude receives conflicting instructions. The fix is not a clever hierarchy. The fix is to delete the wrong line."
- transition_in: crossfade 0.4s
- blueprint: compose
- focal: two contradictory instructions and the corrective deletion
- roles: project instruction victim; subdirectory instruction intruder; no-tiebreaker warning; deletion correction
- sfx: none

Scene 1 (0.0–3.6s): Full frame. Put two equal CLAUDE.md evidence cards in direct opposition: project says "Use certified metric definition" and subdirectory says "Ignore certified metric definition." → Scene 2 (3.6–6.8s): Reactive-displacement collides the second instruction into the first and lands the orange warning "No tiebreaker." Both statements remain readable long enough to establish the contradiction. → Scene 3 (6.8–10.88s): Scale-swap the wrong line into a struck/deleted state and land "Delete the wrong line." Hold the corrected evidence for at least one second.

## Selected motion rule: reactive-displacement

---
name: reactive-displacement
description: Physical collision where an entering element's spring drives the exiting element's displacement — single source of truth makes the motion causally linked.
metadata:
  tags: transition, physics, collision, displacement, spring, causal
---

# Reactive Displacement

Exit animation of element A is mathematically DERIVED from the entry spring of element B — a causal link: "A moves _because_ B hit it." Distinct from [scale-swap-transition.md](scale-swap-transition.md) (which overlaps but isn't causal) and [card-morph-anchor.md](card-morph-anchor.md) (one container morphing).

A single 0→1 driver tween (the "entry spring") feeds three concurrent derived motions in one `onUpdate`:

- **Intruder** (B, entering): position interpolated off-stage → settled over the full driver, plus tilt settling to 0° and a sharp early opacity reveal.
- **Victim** (A, exiting): position interpolated settled → off-stage in the OPPOSITE direction, completing at `VICTIM_FRACTION` (~0.4–0.5) of the driver — NOT 1.0.

The victim finishing BEFORE the intruder's entry creates the "hit then settle" rhythm; sharing one eased driver makes the impact moment mathematically synchronized.

## Recipe

```js
// Both cards absolutely centered; overflow: hidden on the scene (off-stage travel);
// will-change: transform, opacity on both; intruder z-index ABOVE victim.
const INTRUDER_START_X = STAGE_W; // off-stage right
const VICTIM_END_X = -STAGE_W; // off-stage left — SAME axis, opposite direction

gsap.set("#victim", { x: 0, opacity: 1, rotation: 0 });
gsap.set("#intruder", { x: INTRUDER_START_X, opacity: 0, rotation: -INTRUDER_TILT });

const driver = { p: 0 };
tl.to(
  driver,
  {
    p: 1,
    duration: DRIVER_DUR,
    ease: `back.out(${BOUNCE_FACTOR})`, // the intruder spring
    onUpdate: () => {
      // Intruder: full 0→1 progress maps enter (off-stage → center)
      const intruderX = INTRUDER_START_X * (1 - driver.p);
      const intruderOpacity = Math.min(1, driver.p * FADE_IN_SHARPNESS);
      const intruderRot = -INTRUDER_TILT * (1 - driver.p); // settles to 0°
      const intruder = document.getElementById("intruder");
      intruder.style.transform = `translate(-50%, -50%) translateX(${intruderX}px) rotate(${intruderRot}deg)`;
      intruder.style.opacity = String(intruderOpacity);

      // Victim: completes its exit at VICTIM_FRACTION of the driver — by the
      // time the intruder centers, the victim is already off-stage.
      const victimP = Math.min(1, driver.p / VICTIM_FRACTION);
      const victimX = VICTIM_END_X * victimP;
      const victim = document.getElementById("victim");
      victim.style.transform = `translate(-50%, -50%) translateX(${victimX}px)`;
      victim.style.opacity = String(1 - victimP);
    },
  },
  DRIVER_AT,
);
// Climax dwell — intruder holds centered for ≥ DWELL_MIN before the scene ends.
```

## Variations

- **Impact rotation on victim** — the victim also rotates as it slides: `const victimRot = victimP * -VICTIM_KICK_DEG;` appended to its transform. `VICTIM_KICK_DEG` 15–25°, magnitude matched to the perceived intruder weight.
- **Vertical collision** — intruder from top, victim displaced downward; same math on Y. Reads as "weight dropped on it."
- **Wobble after settle** — after the intruder centers, a damped sine wobble (`±WOBBLE_AMP_DEG` rotation, linearly decaying over `WOBBLE_DUR` via a second `ease: "none"` driver at `DRIVER_AT + DRIVER_DUR`) before stillness — "impact aftermath."
- **Multi-victim ripple** — the intruder displaces multiple aligned cards, each victim's `victimP` on a slightly offset driver phase (cascade ripple).

## Values

| token             | range                  | notes                                                                                                      |
| ----------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| DRIVER_AT         | phase-dependent        | after the prior reading beat resolves; must leave ≥ DWELL_MIN of climax dwell before the scene ends        |
| DRIVER_DUR        | 0.6–1.4 s              | short = zippy punch, long = heavy landed impact; higher bounce on long durations reads as floaty           |
| BOUNCE_FACTOR     | 1.2–2.0 (typ. 1.4–1.6) | stay in the `back.out` family (or `elastic.out` for oscillation) — changing family rewrites the feel       |
| VICTIM_FRACTION   | 0.4–0.5                | <0.4 the victim disappears before the impact reads; >0.5 feels parallel, not causal; hard cap ~0.6         |
| STAGE_W           | ≥ composition width    | smaller leaves the off-stage element partially visible at start                                            |
| INTRUDER_TILT     | 5–15° (typ. ~10°)      | low = clean glide, high = "spin-and-plant"; sign consistent with entry direction (momentum transfer)       |
| FADE_IN_SHARPNESS | 3–8                    | intruder reaches opacity 1 at `1/FADE_IN_SHARPNESS` of progress; must be > 1 or it's transparent at center |
| DWELL_MIN         | ≥ 1.0 s (typ. 1.0–1.5) | post-impact dwell is where the new content gets read — do not skip                                         |

## Critical Constraints

- **Single driver = single source of truth** — both motions computed inside ONE driver's `onUpdate`, never separate `tl.to()` calls per element; independent tweens destroy the causal link (they'd merely be near each other in time).
- **Victim completes at a fraction of the driver** — the "hit" is the overlap moment; after it the victim is just vacating space the intruder will fill.
- **Directional momentum transfer** — same axis, opposite directions; different axes read as passing, not colliding.
- **Intruder z-index above victim** — explicit, not DOM order; otherwise the victim looks like it tunneled through.
- **Intruder enters tilted, settles flat** — small initial tilt → 0° reads as "spinning in then planting."
- **Climax dwell after impact** — the impact is the headline beat; hold the settled intruder ≥ DWELL_MIN.
- **`overflow: hidden` on the scene** — off-stage motion exceeds the frame.

## See also

`control-target-sync` (the live-editing mirror — repeated coupled edits, nothing exits) · `hacker-flip-3d` (intruder text reveal during entry) · `sine-wave-loop` (idle breathing during the dwell) · `vertical-spring-ticker` (a ticker that "shoves" the previous content out).

## Selected motion rule: scale-swap-transition

---
name: scale-swap-transition
description: Coordinated shrink-out + spring pop-in morph-like transition between two elements — no SVG path interpolation needed.
metadata:
  tags: transition, morph, scale, swap, spring, pop
---

# Scale-Swap Transition

Simulates a "morph" between two DOM elements by overlapping exit and entrance scale animations. Lighter weight than [card-morph-anchor.md](card-morph-anchor.md) (which morphs container dimensions — use that for SHAPE changes; this rule is for SAME-shape state swaps) and easier than SVG path interpolation.

At a single trigger, two coordinated tweens fire:

1. **Outgoing**: scale `1.0 → EXIT_SCALE` + opacity `1 → 0`, fast `power2.in` (rushing away).
2. **Incoming**: scale `EXIT_SCALE → 1.0` + opacity `0 → 1`, `back.out(BOUNCE_FACTOR)` (arriving with weight).

A small `OVERLAP` window during which both are mid-tween creates the morph illusion; the incoming sits on top via z-index so the outgoing's fade-tail doesn't bleed through.

## Recipe

```html
<!-- Both cards position: absolute; inset: 0 in one fixed-size wrapper — same
     footprint, same transform-origin: 50% 50%. Incoming starts opacity: 0,
     transform: scale(EXIT_SCALE), z-index above the outgoing. -->
<div class="swap-wrap">
  <div class="card outgoing" id="outgoing">{outgoingIcon} {outgoingLabel}</div>
  <div class="card incoming" id="incoming">
    {incomingIcon} {incomingLabel}
    <div class="sub" id="sub">{incomingSubline}</div>
  </div>
</div>
```

```js
// Outgoing: shrink + fade fast
tl.to(
  "#outgoing",
  { scale: EXIT_SCALE, opacity: 0, duration: EXIT_DUR, ease: "power2.in" },
  TRIGGER,
);

// Incoming: pops in with overshoot, starting OVERLAP before the exit finishes
tl.to(
  "#incoming",
  { scale: 1.0, opacity: 1, duration: ENTER_DUR, ease: `back.out(${BOUNCE_FACTOR})` },
  TRIGGER + EXIT_DUR - OVERLAP,
);

// Inner content reveals AFTER the incoming settles
tl.fromTo(
  "#sub",
  { opacity: 0, y: SUB_REVEAL_Y_PX },
  { opacity: 1, y: 0, duration: SUB_REVEAL_DUR, ease: "power3.out" },
  TRIGGER + EXIT_DUR + SUB_REVEAL_DELAY,
);
```

## Variations

- **Delayed inner content reveal** — the classic pattern above: morph the container, then reveal inner text once it settles; the 0.2–0.4 s gap lets the eye land on the new shape before reading.
- **Triple swap (3-state cycle)** — chain A→B→C with triggers `TRIGGER_AB` / `TRIGGER_BC`; each transition is its own tween pair, the previous incoming becoming the next outgoing. State-evolution narratives (early → mid → final labels).
- **Color-shift transition (no scale)** — for a flat morph between same-shape states, drop the scale and keep opacity + a brief background hue tween; less dramatic, more product-UI tone.

## Values

| token            | range                                 | notes                                                                                                  |
| ---------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| TRIGGER          | ≥ outgoing settled + a presence-dwell | the outgoing must "land" before transforming                                                           |
| EXIT_DUR         | 0.3–0.5 s                             |                                                                                                        |
| ENTER_DUR        | 0.45–0.7 s                            | longer than `EXIT_DUR` so the overshoot can settle                                                     |
| OVERLAP          | 0.1–0.2 s                             | >0.3 s both are clearly visible together (no morph); <0.05 s leaves a visible empty gap                |
| EXIT_SCALE       | 0.6–0.8                               | smaller exits feel dramatic but risk reading as "vanish" instead of "morph"                            |
| BOUNCE_FACTOR    | 1.4 soft · 1.8 firm · 2.2 cartoony    |                                                                                                        |
| SUB_REVEAL_DELAY | 0.2–0.4 s                             | reveals during the morph compete with the swap for attention                                           |
| BRAND_REVEAL_AT  | < TRIGGER                             | context (brand, eyebrow) sets the stage early; revealed AT the swap it competes with the headline beat |

## Critical Constraints

- **Incoming z-index ABOVE outgoing** — otherwise the outgoing's fade-tail (opacity 0.3–0.5) bleeds through and double-exposes the frame.
- **Both elements share `transform-origin: 50% 50%`** — different origins make the morph read as one thing teleporting elsewhere.
- **Bouncy ease ONLY on the incoming** — outgoing `power2.in`, incoming `back.out`; reversed, the swap feels mechanical.
- **Both cards `position: absolute; inset: 0`** in the same fixed-size wrapper (sized to fit both states; the wrap never resizes).
- **Don't `display: none` the outgoing** after the fade — leave it at `opacity: 0` so layout doesn't reflow.
- **Inner content reveals after the container settles**; **climax dwell ≥ 1 s** after the final state + subline land.

## See also

`press-release-spring` (a button press TRIGGERS the swap — cause and effect) · `card-morph-anchor` (shape-changing alternative) · `reactive-displacement` (when the replacement should read as a causal collision) · `sine-wave-loop` (idle breathing on the final state).
