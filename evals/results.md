# Kopi Evaluation Results

**Behavioral runs:** 2026-09-03 to 2026-09-04  
**Latest deterministic verification:** 2026-09-04  
**Pack version:** 0.1.0

## Deterministic checks

| Check | Result |
|---|---|
| Plugin manifest validator | Pass |
| Skill metadata validation | Pass for all ten skills |
| Internal link and resource reachability | Pass |
| Pack validator unit tests | Pass, 5 of 5 |
| Legacy implementation term scan | Pass within operating skills |

## Behavioral checks

| Scenario | Result | Observation |
|---|---|---|
| Router | Pass after refinement | Initial run widened into unrelated temporary directories. The router now stops at the active workspace and treats named but unavailable inputs as missing. |
| Presentation | Pass at boundary behavior | With source material and a presentation runtime deliberately unavailable, the skill did not claim a finished deck; it identified the missing requirements and preserved the real-artifact and render-verification gates. |
| Meeting | Pass | Produced decision-oriented preparation and respected the no-write condition and missing identity facts. |
| Portfolio | Pass after refinement | Initial run treated plugin files as possible portfolio evidence. The skill now excludes its own implementation and stops when the active portfolio boundary is empty. |
| Technology research | Pass after runner recovery | With framework names and deployed versions absent, the skill blocked a roadmap recommendation, supplied the as-of date, required fresh primary evidence, and did not invent sources. |
| Architecture decision | Inconclusive | The evaluator loaded the skill and decision references, but its response stream reset and then stalled. The bounded run was stopped without a final decision artifact. Deterministic validation passed. |
| Data analysis | Pass | Quantified the observed change, exposed aggregate-data limits, tested alternative explanations, and blocked unsupported causal attribution. |
| Recall | Pass | Refused to mine unrelated projects or treat memory as live state, then requested one in-scope source of truth. |
| Critical review | Pass | Produced deduplicated multi-lens findings, action categories, evidence gaps, and a verdict without editing the supplied artifact. |
| Learning capture | Pass | Converted the repeated failure into required handoff fields and a completion validator, rejected reminder-only fixes, and preserved the approval gate. |

## Baseline improvements encoded

The original no-Kopi baseline commonly stopped at outlines, blurred authority for external writes, omitted read-back and duplicate prevention, weakened freshness and citation controls, jumped to a single architecture design, and treated project recall as code archaeology. The implemented pack adds explicit controls for each of those failure modes.

The incomplete architecture row is recorded rather than reported as a pass. Re-run that case from [`scenarios.md`](scenarios.md) when the isolated execution service is stable.

## Portability update — 2026-09-09, version 0.1.1

The earlier behavioral results above belong to version 0.1.0. This update adds
portable/Claude packaging and capability-based artifact adapters.

- Eleven deterministic unit tests pass, including renamed checkouts, malformed
  metadata, version drift, clean/reproducible ZIPs, extracted resource integrity,
  OpenAI marketplace resolution, and protection against replacing changed output.
- Root manifest passes the official Agent Plugins 1.0.0 JSON Schema.
- Claude plugin and marketplace manifests pass the installed Claude CLI's strict
  validator. The Codex compatibility manifest passes the plugin-creator validator.
- Independent instruction-level scenarios found that the old named requirements
  blocked equivalent host tools. Revised instructions allow available PPTX/XLSX
  skills or equivalent tools, block missing generation capabilities, and label
  artifacts with missing visual verification/recalculation as drafts.
- Independent code review identified a repeat-install symlink hazard in the Cursor
  guide. The guide now checks both existing files and symlinks before creating one.

These are structural checks and instruction-level scenarios, not live workflow
runs in Claude, ChatGPT, or Cursor. Fresh host installation, connector access,
artifact generation/rendering, and formula recalculation remain user-environment
smoke checks described in INSTALL.md. No public marketplace publication occurred.
