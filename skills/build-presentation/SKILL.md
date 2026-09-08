---
name: build-presentation
description: Use when the user asks for PowerPoint, PPTX, slides, a presentation deck, an executive review, a steering-committee narrative, or a data or architecture story meant to be presented.
---

# Build Presentation

Create the presentation file the audience will consume. A slide outline is an intermediate artifact, not completion.

**REQUIRED SUB-SKILL:** Use `presentations:Presentations` for PowerPoint creation, rendering, and file-level verification. If it is unavailable, state that the `.pptx` is blocked rather than silently substituting prose.

## Frame

Determine the audience, decision or outcome, speaking setting, time available, source material, required format, and whether a template or brand system was supplied. Infer ordinary presentation choices when the context supports them. Ask only for a missing fact that would materially change the deck.

Treat a requested slide count as a maximum unless the user says it is exact. One slide carries one message.

## Build

1. Extract claim-level evidence and unresolved questions.
2. Draft the storyline as slide messages before choosing layouts. For a consequential or contested deck, use [storyboard prompt](references/storyboard-prompt.md) to compare two different narratives.
3. Choose a visual form that fits each message. Use charts for quantitative relationships, diagrams for systems or sequences, and prose only when neither visual improves comprehension.
4. Build the `.pptx` with concise on-slide text, source footnotes, and useful speaker notes.
5. Use the supplied template. Without one, use a restrained neutral theme and do not invent branding.

## Verify

Read [presentation rubric](references/presentation-rubric.md). Render every slide and inspect the images. Check overflow, clipping, alignment, hierarchy, contrast, font size, chart scales, legends, source footnotes, and consistency. Confirm that every major claim resolves to evidence and the final ask is explicit.

Revise the actual deck and render again until it passes. Return the `.pptx`, any requested PDF, and a short note naming the audience, decision, sources, and verification performed.

## Common failures

- Producing an outline when the user asked for a file.
- Repeating a report instead of building a decision narrative.
- Filling a requested slide count with weak material.
- Treating successful generation as visual verification.
- Inventing logos, colors, metrics, citations, or executive priorities.

