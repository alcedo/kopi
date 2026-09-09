---
name: kopi-mode
description: Use when project-management or software-architecture work spans presentations, meetings, portfolios, technology research, architecture decisions, data analysis, performance reviews, recall, or several connected deliverables.
---

# Kopi Mode

Kopi mode routes work by the artifact and decision the user needs. It keeps evidence, decisions, actions, metrics, meetings, and slides connected without loading every workflow at once.

Two layers do the work. Foundational playbooks own the moves every workflow repeats. Workflow playbooks own one artifact each and call the foundation rather than restating it.

## Start

For multi-step work, read [operating principles](references/operating-principles.md). When two or more workflows share information, also read the [artifact model](references/artifact-model.md). Before any external write, read [permissions and writes](references/permissions-and-writes.md).

Every request opens with [frame the request](playbooks/frame-request.md) and closes with [deliver the artifact](playbooks/deliver-artifact.md). Skip either only for a single-turn factual answer that produces no artifact.

Choose the smallest complete workflow. Do not create extra briefs, decks, meetings, or registers merely because a template exists.

Treat named but unavailable inputs as missing. Search only the active workspace and user-supplied or connected sources that match the request. Never widen into unrelated directories, projects, or records. If a required input is absent, state exactly what is missing and prepare only the useful structure that does not depend on it.

## Foundation

Read a foundational playbook when its trigger fires, whichever workflow is running. These are shared moves, not a fixed sequence.

| Foundational playbook | When it runs | Workflows it carries |
|---|---|---|
| [Frame the request](playbooks/frame-request.md) | Start of every request, before collecting or drafting | Every workflow |
| [Gather evidence](playbooks/gather-evidence.md) | Any claim that must stay traceable to a source | Research, data, portfolio, recall, architecture, performance review |
| [Sketch options](playbooks/sketch-options.md) | A structure, layout, framing, or definition fork that observation can settle | Presentation, data analysis, architecture, meeting |
| [Compare options](playbooks/compare-options.md) | A consequential or hard-to-reverse choice | Architecture, portfolio intervention, integrated program |
| [Delegate work](playbooks/delegate-work.md) | Work fans out to parallel workers | Research, data, architecture, critical review, integrated program |
| [Verify the deliverable](playbooks/verify-deliverable.md) | Before any workflow declares done | Every workflow |
| [Deliver the artifact](playbooks/deliver-artifact.md) | End of every request | Every workflow |
| [Pause safely](playbooks/pause-safely.md) | Explicit pause, going offline, or losing session context | Every workflow, paired with Recall on resume |
| [Follow through](playbooks/follow-through.md) | The artifact shipped and other people must now act | Meeting, portfolio, integrated program |
| [Autonomous run](playbooks/autonomous-run.md) | Work must run to completion without checking in | Any multi-step workflow |
| [Author a playbook](playbooks/author-playbook.md) | A workflow recurs often enough to encode | Learning capture |

## Route

| User intent | Playbook | Required skill |
|---|---|---|
| PowerPoint, presentation, slides, executive narrative | [Presentation](playbooks/presentation.md) | `build-presentation` |
| Schedule, prepare, or close a meeting | [Meeting](playbooks/meeting.md) | `run-meeting` |
| Status across initiatives, risks, dependencies, intervention | [Portfolio](playbooks/portfolio.md) | `control-portfolio` |
| Latest tools, frameworks, releases, AI capabilities | [Technology research](playbooks/technology-research.md) | `research-technology` |
| Architecture options, target state, design decision | [Architecture decision](playbooks/architecture-decision.md) | `decide-architecture` |
| Dataset, spreadsheet, metrics, trends, causes | [Data analysis](playbooks/data-analysis.md) | `analyze-data` |
| Catch up, resume, handoff, where work stopped | [Recall](playbooks/recall.md) | `recall-work` |
| Challenge, stress-test, red-team, find blind spots | [Critical review](playbooks/critical-review.md) | `challenge-deliverable` |
| Retrospective lesson or recurring workflow correction | [Learning capture](playbooks/learning-capture.md) | `capture-learning` |
| Direct-report performance review, 360 feedback, manager assessment | [Performance review](playbooks/performance-review.md) | `write-performance-review` |
| Several connected deliverables or workstreams | [Integrated program](playbooks/integrated-program.md) | Route to each required skill in dependency order |

## Compose

Sequence workflows by dependency. Data and research produce evidence. Architecture work turns evidence into a decision. Meetings resolve or assign decisions. Portfolio control tracks resulting work. Presentations communicate the result.

Parallelize only independent evidence collection or option generation, under [delegate work](playbooks/delegate-work.md). Give each worker a distinct source, question, or artifact. Aggregate before making a decision.

For writing that calls for user selection among themes or framings, compose
[compare writing ideas](references/compare-writing-ideas.md). The owning skill
supplies evidence and audience boundaries, then drafts from the selected IDs.
Keep confidential performance-review evidence out of other deliverables unless
the user explicitly includes it in that scope and the destination audience is appropriate.

## Finish

Close through [deliver the artifact](playbooks/deliver-artifact.md). Return the requested artifact, the evidence that supports it, what was verified, and any unresolved decision or external-write gate. A plan is not completion when the user requested a real file, event, update, or analysis.
