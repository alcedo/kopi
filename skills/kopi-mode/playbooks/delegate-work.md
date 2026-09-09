# Delegate Work

**Invoked when a playbook fans work out to parallel workers.** It owns the split and the merge: distinct slices in, one reconciled result out.

1. Split by source, question, or artifact so no two workers can produce the same row. Overlapping slices manufacture agreement that means nothing.
2. Parallelize evidence collection, option generation, and independent review. Do not parallelize a decision, a dependent sequence, or edits to one artifact.
3. Brief each worker with the frame's boundary plus its own slice: the question, the sources it may use, the scope it may not leave, the output shape, and the as-of timestamp. Pass pointers to source material instead of pasting the material.
4. Require the evidence row shape from the [artifact model](../references/artifact-model.md) from every worker so results merge without translation. Require unavailable sources and dead ends to be reported rather than dropped.
5. Aggregate before any decision or external write. Deduplicate by stable identifier, reconcile conflicting claims by source date and authority, and keep genuine disagreement visible.
6. Own the merged result. Re-check load-bearing claims against their sources yourself. A worker's summary is a report, not verification.

One worker is enough for most requests. Fan out to widen coverage, never to look thorough.
