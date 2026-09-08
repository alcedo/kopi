---
name: challenge-deliverable
description: Use when the user asks to challenge, red-team, stress-test, critique, pressure-test, find blind spots, or independently review a plan, proposal, architecture, presentation, roadmap, meeting pack, portfolio report, or data analysis.
---

# Challenge Deliverable

Find weaknesses that could change a decision or damage trust. Do not maximize comment count and do not edit the source artifact unless separately asked.

## Frame

State the artifact, intended audience, intended decision or outcome, constraints, and what failure would look like. Gather the artifact and the minimum surrounding evidence needed to judge it. If intent is uncertain, infer from the artifact and label the inference.

Select independent lenses from [review lenses](references/review-lenses.md). Use only lenses relevant to the artifact. A presentation and architecture proposal may need both narrative and architecture lenses; a data readout may need evidence, analysis, and visual lenses.

## Review

When independent agents are available, give each the same artifact, intent, evidence, and [reviewer prompt](references/reviewer-prompt.md), with one distinct lens. Run them in parallel and keep them read-only. When delegation is unavailable, run the lenses separately and disclose that the review lacks model independence.

Every finding needs a location, claim, evidence, impact, and optional correction. Reject findings based only on personal style, hypothetical scale, or missing context the artifact was never meant to cover.

## Judge

Merge duplicate findings and record genuine disagreement. Apply lead judgment:

- **Act on:** blocks the intended decision or creates material correctness, security, delivery, or trust risk.
- **Consider:** valid concern whose benefit may not justify the cost now.
- **Noted:** true context or low-impact limitation that needs no action.
- **Dismissed:** wrong, unsupported, irrelevant, duplicated, or preference-only.

Weight independent agreement, but verify findings against the source. One well-evidenced dissent can outweigh weak consensus.

## Return

Give the intent, lenses used, act-on findings first, consider items, compact noted and dismissed sections, disagreements, evidence gaps, and a final verdict. Preserve the original artifact. If the user then asks for changes, route the edits through the skill that owns that artifact.

