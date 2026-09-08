---
name: recall-work
description: Use when the user asks to catch up, resume, reconstruct context, find where work stopped, review recent activity, understand current project state, or prepare a handoff across conversations and shared systems.
---

# Recall Work

Reconstruct the smallest trustworthy current-state brief needed to resume or decide.

## Bound the recall

Fix the topic, project or workspace, and time window. Default “recent” to seven days and state it. Never search unrelated projects or private histories outside the active boundary. If the user supplied a handoff containing paths, decisions, state, and next steps, use it before wider mining.

## Gather history

Search available task or conversation history for the user's goal, decisions, attempts, corrections, artifacts, open questions, and stated next steps. For a large history, partition by time or workstream and keep raw transcripts out of the main synthesis.

Use [source sweep prompt](references/source-sweep-prompt.md) to inspect shared records in parallel when a named initiative, subsystem, vendor, or decision has live state elsewhere. Relevant sources may include trackers, documents, meeting notes, calendars, repositories, dashboards, and messages.

## Reconcile current state

History is evidence of what someone believed or attempted. Check surfaced records against their live state. Preserve source dates and distinguish:

- completed and verified;
- in progress;
- blocked or at risk;
- planned but not started;
- paused, cancelled, reverted, or superseded;
- unknown or conflicting.

Do not redo completed investigation. Verify only the claims needed to know where to resume.

## Report

Follow [status capsule](references/status-capsule.md). Lead with a five-bullet maximum capsule, then one line per workstream, recurring problems, evidence gaps, and one best next move. Cite source identifiers or links. Cut detail before cutting active workstreams.

If no in-scope evidence exists, return `BLOCKED` with the exact missing source. Do not turn a project-management recall into code archaeology unless code state is relevant to the named work.

