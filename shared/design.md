# AI Learning Program Design Guidelines

Use this document for composition, hierarchy, motion, and logo behavior. The [HeyGen brand kit](branding-kit/heygen-brand-kit.md) is the single source of truth for the course palette, typography, default canvas, motion-graphics setting, and primary-logo setting.

Do not copy color values into this file or introduce additional course colors. Apply the semantic roles defined in the branding kit: Primary, Secondary, Tertiary, Accent, and the default canvas.

## 1. Course visual concept

The course helps learners move through a practical progression:

```text
Chatbot answer
    ↓
Bounded agent task
    ↓
Verified artifact
    ↓
Reusable workflow or better work design
```

Visuals should make that progression concrete. Show the source, the agent action, the human review point, and the evidence of completion. Prefer familiar workplace artifacts over abstract AI imagery.

The overall tone is calm, credible, practical, and slightly challenging. Avoid futuristic interfaces, glowing brains, robots, generic circuit imagery, and visuals that imply full autonomy.

## 2. Brand system

### Colors

Use only the roles and values in the [branding kit](branding-kit/heygen-brand-kit.md) for course-owned graphics. Do not define local palettes, gradients, data-series colors, or status colors in `design.md`.

Third-party product marks are the exception: preserve the official fills embedded in the approved logo assets. Do not recolor a product logo to match the course palette.

### Typography

- Titles and major statements: use the title family and weight defined in the branding kit.
- Body copy, labels, captions, and annotations: use the body family defined in the branding kit.
- Terminal and code captures may use the authentic product monospace font inside the captured interface.
- Keep title lines short and use sentence case.

### Motion

- Use the motion-graphics setting defined in the branding kit for teaching graphics and transitions.
- Animate one instructional change at a time.
- Use motion to reveal a distinction, show progress, or connect an action to evidence.
- Keep terminal motion authentic and restrained; continuous motion should not compete with narration.
- Respect reduced-motion settings in interactive HTML.

## 3. Composition and hierarchy

- Use a clear title, one focal idea, and one supporting visual per frame.
- Keep the default canvas and contrast behavior defined by the branding kit.
- Use generous margins and keep essential text inside title-safe and action-safe areas.
- Prefer split frames for comparisons such as chatbot versus agent.
- Prefer short pipelines for sequences such as source → action → artifact → check.
- Use cards only when they group related information; do not turn every sentence into a box.
- Keep captions and labels readable at normal playback size.

## 4. Reusable teaching patterns

### Title card

Show the course and lesson title with a restrained divider or signal. Do not add a company or course logo; the branding kit specifies no primary logo.

### Side-by-side comparison

Use parallel language and balanced visual weight. Make the behavioral difference visible before adding detailed terminology.

### Framework or process

Reveal one step at a time, then show the complete sequence. Keep labels consistent with the course glossary and lesson script.

### Evidence and verification

Show the source and the evidence together whenever possible. A checkmark alone is not evidence; display the row count, cited value, test result, diff, or other observable proof.

### Warning or boundary

Use the branding kit's signal role sparingly. State the operational limit in plain language and avoid alarm-style decoration.

## 5. Logos and product marks

The branding kit specifies **Primary logo: None**. Do not add an Aledade, HeyGen, or course logo to title cards, teaching cards, or persistent corners.

Use third-party product logos only when the product is named or its connection is part of the lesson:

- Source approved glyphs from [app-logos.md](app-logos.md).
- Preview the available set in [logos.html](logos.html).
- Keep the official SVG fills; do not tint, invert, or redraw the marks.
- Place each mark on a light rounded chip when used in a connection or tool-stack frame.
- Pair unfamiliar marks with a text label.
- Prefer one logo at first meaningful mention. Avoid persistent corner bugs and decorative logo walls.
- Do not substitute a related product logo for a product that is named but not available in the approved asset set.

## 6. Claude Code and terminal scenes

Use [`cc-cli-refence/`](cc-cli-refence/) as the canonical visual reference for Claude Code terminal behavior. Copy or adapt that composition instead of rebuilding the interface from memory.

The terminal is an embedded product surface, not a second course brand. It may retain its authentic theme and semantic status treatment. The surrounding title, annotation, and teaching graphics must still follow the branding kit.

### Terminal behavior

- Use a monospace grid with minimal chrome.
- Keep the input prompt as the primary framed element.
- Render tool calls as compact verb-and-target rows.
- Show diffs as added, removed, and unchanged lines with clear gutters.
- Distinguish done, in-progress, and pending task states through shape, label treatment, and the terminal's authentic semantic styling.
- Use a restrained spinner or progress state as the only continuous motion.
- Keep transitions discrete and settled before the next narrated idea.

## 7. Accessibility and production checks

- Maintain readable contrast using the approved brand roles.
- Do not communicate status by color alone; add text, shape, or icon differences.
- Describe important visual changes in narration or captions.
- Keep captions clear of logos, controls, and important evidence.
- Verify product labels and interfaces against the approved environment before recording.
- Confirm that each visual supports the spoken lesson rather than introducing a new claim.
