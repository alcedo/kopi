# Architecture Decision Rubric

## Grounding

- Current behavior, ownership, data flow, and constraints are supported by evidence.
- Historical rationale is not inferred from code shape alone.
- Unknowns and contradictions are visible.

## Option quality

- Consequential decisions compare structurally different options.
- Each option starts from stakeholder, caller, and operator usage.
- Boundaries hide meaningful complexity and keep authority clear.
- Data ownership, trust boundaries, invariants, and lifecycle are explicit.

## Fitness

- Security, privacy, reliability, operability, performance, cost, and delivery constraints are addressed in proportion to their importance.
- Failure, recovery, migration, rollback, and blast radius are credible.
- Complexity earns its place.

## Decision integrity

- The recommendation follows from evidence and constraints.
- Accepted tradeoffs and rejected alternatives are recorded.
- Reversal conditions, confidence, owners, and open risks are explicit.
- The record does not claim implementation or verification that did not occur.

Return `PASS`, `REVISE`, or `BLOCKED` with decision-changing findings first.
