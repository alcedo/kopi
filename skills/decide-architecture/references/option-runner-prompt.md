# Architecture Option Runner Prompt

## Inputs

- Problem and decision: `{problem}`
- Current system: `{current_system}`
- Stakeholder and caller experience: `{usage}`
- Constraints and quality attributes: `{constraints}`
- Evidence: `{evidence}`

## Task

Propose one coherent architecture that is structurally distinct from the other requested candidates. Start with usage, data ownership, trust boundaries, and invariants. Then define components, interfaces, data flow, lifecycle, operations, failure handling, and migration.

Show what complexity the design hides and what it exposes. Identify the strongest alternative you considered, the tradeoff this option accepts, its blast radius, and the evidence that could invalidate it.

Do not implement code. Do not invent constraints or pretend unknown current-state behavior is established.

