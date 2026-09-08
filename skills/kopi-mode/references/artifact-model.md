# Shared Artifact Model

Use only the records needed by the active workflow. Preserve stable identifiers when a record already exists.

## Evidence

| Field | Meaning |
|---|---|
| `claim` | The statement the source supports |
| `source` | A resolvable file, URL, message, event, query, or record |
| `source_date` | When the source was published or changed |
| `retrieved_at` | When it was checked |
| `confidence` | Direct, supported, inferred, speculative, or unknown |
| `freshness` | Current, stale, or unknown for the decision being made |

## Decision

`id`, `question`, `constraints`, `options`, `choice`, `rationale`, `owner`, `decided_at`, `review_at`, `evidence`, `status`.

## Work item

`id`, `outcome`, `owner`, `status`, `due_at`, `milestone`, `dependencies`, `risks`, `last_updated_at`, `evidence`, `next_action`.

Status is one of `not-started`, `in-progress`, `blocked`, `at-risk`, `done`, `paused`, or `cancelled`. Do not invent a more precise status than the source supports.

## Risk

`id`, `event`, `cause`, `impact`, `likelihood`, `owner`, `mitigation`, `trigger`, `status`, `evidence`.

## Meeting

`id`, `purpose`, `decision_needed`, `participants`, `start`, `end`, `timezone`, `location`, `agenda`, `pre_read`, `decisions`, `actions`, `source_event`.

## Slide

`number`, `audience`, `message`, `evidence`, `visual`, `speaker_notes`, `source_footnote`.

## Metric

`name`, `definition`, `source`, `population`, `time_window`, `calculation`, `unit`, `assumptions`, `value`, `uncertainty`.

## Linking rules

- Evidence may support metrics, risks, decisions, and slide claims.
- Meeting actions become work items only when the user requests tracking or the active system already treats meeting actions as tracked work.
- Slides reference records. They do not become the source of truth.
- Portfolio summaries derive from work items, decisions, and risks. Do not maintain a second hand-edited status universe.

