---
name: build-presentation
description: Use when the user asks for PowerPoint, PPTX, slides, a presentation deck, an executive review, a steering-committee narrative, or a data or architecture story meant to be presented.
---

# Build Presentation

Create the presentation file the audience will consume. A slide outline is an intermediate artifact, not completion.

## Select available capabilities

Use the host's presentation skill or tools for PowerPoint creation, rendering, and file-level verification. Examples include `presentations:Presentations` in OpenAI environments or an available `pptx` skill in Claude. Discover what is actually available; a particular skill name is not a prerequisite.

If no presentation skill is available, use available file-generation tools or libraries that can create a real `.pptx`, together with a renderer and image inspection. Follow the selected tool's setup instructions. Do not assume any library, renderer, or connector is installed, and do not install software or connect accounts merely because this skill mentions it.

Preserve every verification step below whichever tools are used. If generation is unavailable, state that the `.pptx` is blocked and name the missing capability. If generation succeeds but rendering or image inspection is unavailable, return the actual file as a draft with visual verification explicitly incomplete. Never report an outline as a completed deck or claim to have inspected slides you could not render and view.

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

When rendering and inspection are available, revise the actual deck and render again until it passes. When verification is complete, return the `.pptx`, any requested PDF, and a short note naming the audience, decision, sources, and verification performed. Otherwise follow the explicit draft or blocked handling above.

## Common failures

- Producing an outline when the user asked for a file.
- Repeating a report instead of building a decision narrative.
- Filling a requested slide count with weak material.
- Treating successful generation as visual verification.
- Inventing logos, colors, metrics, citations, or executive priorities.
