---
name: decide-architecture
description: Use when the user asks to design or assess system architecture, choose boundaries or ownership, compare technical options, define a target state, write an ADR, evaluate migration impact, or explain where a capability should live.
---

# Decide Architecture

Settle the shape of a system before implementation makes the decision expensive.

## Ground

Trace the current system from entry points through data, control, ownership, integrations, and operational surfaces. Inspect code, diagrams, decisions, incidents, tickets, and discussions available inside scope. Distinguish observed behavior from historical rationale and present-day inference.

Write the stakeholder, caller, and operator experience first. Name constraints, quality attributes, invariants, trust boundaries, failure modes, and decisions the design must keep reversible.

## Explore

For a consequential decision, generate at least two structurally different options. Use [option runner prompt](references/option-runner-prompt.md) for independent candidates. Give each candidate the same grounding and success criteria, and separate their writable artifacts.

Reject options that merely rename components, leak internal rules to callers, duplicate authority, scatter state, or organize modules by execution phase rather than domain ownership.

## Decide

Compare options on fitness to constraints, interface depth, data ownership, security, operability, failure recovery, performance, cost, migration path, blast radius, reversibility, and reader load. Prefer the smallest public surface that hides meaningful complexity.

Read [architecture rubric](references/architecture-rubric.md). Select a recommendation and state its accepted tradeoffs, evidence, confidence, unresolved risks, and conditions that would reverse it. Do not average incompatible designs.

## Record

Use [decision record](references/decision-record.md). Include current and target views plus only the diagrams needed to explain boundaries or flow. When implementation is requested, finish the architecture artifact first and hand the chosen contract to the implementation workflow. Do not silently change the architecture while coding around friction; repeated deviations trigger redesign.

Return the decision record, option comparison, diagrams, evidence, and open risks. Leave implementation untouched when the request is design or review only.

