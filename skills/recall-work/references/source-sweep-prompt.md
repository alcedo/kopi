# Recall Source Sweep Prompt

## Scope

- Topic or initiative: `{topic}`
- Workspace or organization: `{workspace}`
- Time window: `{window}`
- Assigned source: `{source}`

## Task

Find evidence about current state, what changed, decisions made, work attempted, reversals, recurring problems, blockers, ownership, and next actions. Search only the assigned source and scope.

Order records by real event or modification time. Distinguish current records from historical statements. Do not infer completion from a plan, message, or draft.

## Return

For each workstream, return source pointer, source date, goal, current status, latest verified change, owner, blocker or risk, open decision, and next action. Include contradictions, stale records, and searches that returned no result.

