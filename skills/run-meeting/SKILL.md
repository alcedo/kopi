---
name: run-meeting
description: Use when the user asks to prepare, schedule, add, update, reschedule, cancel, facilitate, document, or follow up on a meeting, review, workshop, or recurring forum.
---

# Run Meeting

Treat a meeting as a decision and coordination lifecycle, not just a calendar event.

## Choose the operation

- **Prepare:** purpose, participants, agenda, pre-read, and decisions needed.
- **Schedule or update:** calendar record plus preparation material.
- **Close:** decisions, dissent, actions, owners, dates, and approved follow-up writes.

Read [meeting contract](references/meeting-contract.md) before scheduling or closing a meeting. Read `kopi-mode`'s permissions reference before external writes.

## Prepare

Resolve the purpose and what should be different after the meeting. Gather relevant decisions, risks, work items, data, and prior notes. Use [agenda prompt](references/agenda-prompt.md) when the agenda needs synthesis.

Invite only people whose role in the meeting is clear. Mark each as decision owner, required contributor, facilitator, or informed observer. Recommend an asynchronous alternative when no live interaction is needed.

## Schedule

An explicit request to schedule, add, set up, move, or cancel authorizes that named calendar action. A request to draft or prepare does not.

Use an available calendar connector. Resolve identities and time zones, check availability, and search for an equivalent event before creating one. Never guess between ambiguous people or calendars. Include purpose, decision needed, agenda, location or conference link, and pre-read links when available.

Read the resulting event back. Verify its identifier, calendar, date, time zone, participants, recurrence, conferencing, and notification-sensitive changes. Do not retry an uncertain write until duplicate risk is resolved.

## Close

Separate decisions from discussion. Record dissent and unresolved questions. Every action has one owner and either a due date or an explicit missing-date flag. Tracker updates, messages, and document publication require their own explicit authorization.

Return what was prepared, what changed externally, the verified event link or identifier, and the open actions or gaps.

