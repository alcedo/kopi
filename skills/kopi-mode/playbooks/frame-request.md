# Frame the Request

**Invoked at the start of every other playbook.** It owns the boundary: who the output is for, what decision it serves, which inputs exist, and what counts as done.

1. Name the consumer and the decision. Write one sentence covering who reads or runs this and what they must understand, decide, approve, schedule, or do. If that sentence cannot be written, get it before building anything.
2. Classify the ask. Analyze, prepare, draft, review, and recommend produce artifacts. Create, update, send, schedule, invite, publish, and file are external writes and carry the gate in [permissions and writes](../references/permissions-and-writes.md).
3. Fix the scope boundary. Name the workspace, projects, records, people, and time window in scope. Everything outside stays out even when it shares a name. Record the as-of timestamp for anything time-sensitive.
4. Inventory inputs against that boundary. Mark each named input found, found but stale, or missing. A named input that is not present is missing. Do not substitute a similarly named file, project, dataset, or record.
5. State the done condition and the smallest artifact set that meets it. One artifact per decision. Do not add a brief, deck, register, or meeting because a template exists.
6. Return the frame in a few lines before the work starts: consumer and decision, scope boundary and as-of, missing inputs, done condition. Then proceed on every part that does not depend on a missing input.

A frame is cheap to write and expensive to skip. Every later step cites it.
