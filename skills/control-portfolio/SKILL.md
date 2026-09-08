---
name: control-portfolio
description: Use when the user needs a cross-project status, initiative portfolio, program dashboard, intervention list, dependency view, risk review, milestone health check, or coordinated tracking across many workstreams.
---

# Control Portfolio

Reconcile many workstreams into one decision view while leaving detailed truth in authoritative systems.

## Bound the portfolio

Define the initiatives, organization, time horizon, reporting date, and audience. If “all” is ambiguous, use the active workspace or named program and state that boundary.

Discover available trackers, planning documents, meeting records, calendars, repositories, and prior reports. Read only sources inside the boundary. Skill files and the plugin directory are instructions, never portfolio evidence. If the active boundary contains no initiative records and no connected source is in scope, report the missing sources and stop rather than widening the search. Use [portfolio schema](references/portfolio-schema.md) to normalize records without erasing source-specific detail.

## Reconcile

1. Resolve a stable identity for each initiative. Merge duplicates only with evidence.
2. Determine owner, outcome, status, milestone, due date, dependencies, risks, decisions, last update, and next action.
3. Treat source conflict as a finding. Prefer a named authoritative system; otherwise show both claims and their dates.
4. Apply a freshness threshold appropriate to the work cadence. State it instead of treating old status as current.
5. Flag intervention when work is blocked, ownerless, stale, slipping, dependency-bound, missing a decision, or carrying an unmitigated material risk.

Independent source collection may run in parallel. Each collector owns one source or portfolio slice and returns normalized records plus source pointers. Aggregate before judging status.

## Report

Read [portfolio rubric](references/portfolio-rubric.md). Lead with the few interventions requiring attention. Follow with a compact initiative table and explicit data gaps. Derive counts and summaries from the normalized records rather than hand-writing a second status narrative.

Tracker edits, assignments, dates, and messages require explicit user authorization. Search before creating and read back every changed record. Return the reporting boundary, as-of time, interventions, detailed register, conflicts, and writes performed.
