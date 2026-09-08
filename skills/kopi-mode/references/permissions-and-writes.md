# Permissions and External Writes

## Authority test

An explicit request to create, update, send, schedule, invite, publish, or file authorizes that named action and its necessary fields. A request to analyze, prepare, draft, review, or recommend does not authorize an external write.

When authority is absent, prepare a draft or preview and stop before the write. Do not hide the pending action inside a long report.

## Validate before writing

- Resolve people, teams, destinations, dates, time zones, and record identifiers from available context or connected systems.
- Surface ambiguous matches. Never guess an identity or destination.
- Show the meaningful effect when the request could target multiple records or audiences.
- Preserve user-provided wording and scope unless a safety or correctness issue requires correction.

## Retry safety

Before creating, search for an existing equivalent record. Prefer updating the intended record over creating a duplicate. Use stable source identifiers when tools support them.

After writing, read the resulting record and verify its identifier, destination, participants, content, and state. Report partial success precisely. Do not retry an uncertain write until duplicate risk is resolved.

## Higher-risk actions

Cancellation, deletion, broad reassignment, publication to a large audience, or changes that notify people unexpectedly require exact target confirmation when the user's request leaves room for doubt.

