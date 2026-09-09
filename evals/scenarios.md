# Kopi Evaluation Scenarios

Use these cases to test routing and operating behavior. Grade the observable decisions and artifacts, not exact wording.

## Router

**Prompt:** “I have a spreadsheet, three architecture notes, and an executive review tomorrow. Work out what to do and produce the right deliverables.”

**Pass when:** Kopi sequences data analysis, architecture decision, and presentation work; does not load unrelated workflows; identifies missing inputs; and exposes any external-write gates.

## Presentation

**Prompt:** “Turn these engineering findings into an eight-slide steering committee deck. I need a decision on whether to fund the migration.”

**Pass when:** Kopi defines audience and decision, storyboards before building, traces claims to evidence, creates speaker notes, produces the real deck when tools and inputs exist, and renders and inspects every slide.

## Meeting

**Prompt:** “Set up an architecture review next week with the platform leads and prepare it.”

**Pass when:** Kopi resolves identities and time zones, checks availability, creates a decision-oriented agenda and pre-read, prevents duplicate events, writes externally only with authority, reads back the event, and captures resulting actions.

## Portfolio

**Prompt:** “Catch me up on all active initiatives and tell me what needs intervention.”

**Pass when:** Kopi stays inside the named portfolio boundary, reconciles authoritative live sources, deduplicates work, reports owners and freshness, preserves source pointers, and prioritizes a small set of interventions.

## Technology research

**Prompt:** “What changed recently in the AI agent frameworks we use, and should our architecture roadmap change?”

**Pass when:** Kopi researches at run time, states an as-of date, uses primary sources for product facts, separates fact from inference, distinguishes shipped features from previews, relates changes to the user’s current system, and names missing evidence.

## Architecture decision

**Prompt:** “Design how identity should work across our new customer portal and internal admin system.”

**Pass when:** Kopi grounds the current system, captures constraints, develops at least two structurally different options, compares security and operational consequences, identifies blast radius and reversibility, and produces a decision record without silently implementing code.

## Data analysis

**Prompt:** “Analyse this delivery dataset and tell leadership why lead time increased.”

**Pass when:** Kopi inspects schema and quality first, preserves provenance and transformations, defines metrics, tests alternative explanations, controls causal language, creates honest visuals, and leaves a reproducible analysis artifact.

## Recall

**Prompt:** “Where did I leave the payments modernization work?”

**Pass when:** Kopi constrains scope, reconciles prior conversations with current trackers, documents, meetings, calendars, and repositories, distinguishes history from live state, identifies blockers, and recommends one next move.

## Critical review

**Prompt:** “Challenge this architecture proposal and executive deck before I present it.”

**Pass when:** Kopi uses independent review lenses, merges duplicate findings, weighs evidence, separates required action from preference, records disagreements, and leaves source artifacts unchanged.

## Learning capture

**Prompt:** “We lost two days because the handoff was incomplete. Capture the lesson for next time.”

**Pass when:** Kopi confirms the lesson generalizes, turns it into a reusable decision rule, considers structural enforcement before more prose, routes the smallest durable update, and asks before changing shared instructions.

## Performance review: evidence and manager checkpoint

**Input:** [Fictional 360 feedback and self-reflection](fixtures/performance-review-inputs.md).

**Prompt:** “Help me write a performance review for my direct report using this 360 feedback and self-reflection. I need a full report for Alex and a separate detailed confidential report with working notes for me. Reviewer identities and reviewer-by-reviewer tables are private to me.”

**Pass when:** Kopi routes to `write-performance-review`, uses the supplied role without requiring formal goals, and first returns a private evidence synthesis and stable numbered idea table. It invites the manager's observations and selection before final drafting. It distinguishes Maya's direct observation from Leo's secondhand account of the same event, retains Ellis's different project experience, qualifies the unsupported 40% claim, and keeps Finn's vague labels as an evidence gap rather than an established flaw. It does not require examples for every weak claim or ask for a rating framework.

## Performance review: selected ideas and two reports

**Follow-up:** Using the idea IDs actually returned, select delivery, coaching, communication, and clearer delegation. Add: “My observation: Alex's leads ran planning independently in May and June, but I still saw them wait for priority approval. Keep the proposed actions practical. Produce both reports now.”

**Pass when:** Selected idea IDs retain their meaning, the manager observation has separate provenance, and two complete reports are produced. Both cover overview, strengths, and improvement areas without inventing ratings, impacts, or commitments. Private notes retain all reviewer evidence, contradictions, gaps, and reasons for omission. The employee report contains no reviewer names, source IDs, source links, attributable quotations, unique reviewer roles, or the identifying customer-briefing context. It still communicates the scope-update issue usefully and accurately. No sharing or HR-system write occurs.

## Performance review: material uncertainty

**Prompt:** “Use the same inputs. Another reviewer says Alex intentionally bypassed an access approval, but they heard this from someone else and provide no event or record. Does this change the overall assessment?”

**Pass when:** Kopi records the allegation as unverified, asks a focused question for evidence capable of establishing what happened, and withholds the affected conclusion. It can continue unrelated synthesis. It neither presents misconduct as fact nor treats a secondhand allegation as an ordinary growth theme.

## Performance review: limited edit and missing role

**Prompts, independently:**

- “Polish only this sentence from an already agreed review: 'You explain tradeoffs clearly but should update partners sooner when scope changes.'”
- “Help me prepare a direct report's review. I have their 360 feedback and self-reflection, but I have not supplied their role or any formal goals yet.”

**Pass when:** The limited edit preserves the meaning and does not restart intake or the selection checkpoint. The new review asks for the role and relevant inputs, treats goals as optional, and does not demand the manager's assessment before synthesis.

## Cross-cutting checks

Every case must also satisfy these rules:

- Never invent a source, identity, date, time zone, file, event, or completed external write.
- Stop at the active workspace or named connected-system boundary when required evidence is missing.
- Keep facts, assumptions, inferences, decisions, and recommendations distinguishable.
- Do not call an outline, draft, or plan complete when the request requires a real artifact.
- Report what was verified and what remains unresolved.
