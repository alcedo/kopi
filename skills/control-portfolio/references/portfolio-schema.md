# Portfolio Schema

## Initiative

| Field | Rule |
|---|---|
| `id` | Preserve the authoritative system identifier |
| `name` | Use the source title, not a rewritten synonym |
| `outcome` | Describe the result, not the activity |
| `owner` | One accountable person or explicit `unassigned` |
| `status` | `not-started`, `in-progress`, `blocked`, `at-risk`, `done`, `paused`, or `cancelled` |
| `milestone` | Next observable delivery point |
| `due_at` | Source date and time zone where relevant |
| `dependencies` | Stable IDs or resolvable names |
| `risks` | Risk IDs or short evidence-backed risks |
| `decision_needed` | Decision, owner, and needed-by date |
| `last_updated_at` | Timestamp from the source |
| `next_action` | One action, owner, and date or gap |
| `source` | Resolvable record or document pointer |

## Reconciliation

- Exact source ID match is the strongest duplicate evidence.
- A similar title is not enough. Check owner, outcome, dates, and links.
- A completed initiative is not active because an old report still lists it.
- A stale status remains stale even when repeated in a newer summary that cites no new evidence.
- Derived health never replaces source status. Keep both when they differ.

