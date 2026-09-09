# Pause Safely

**Invoked on an explicit pause, on going offline, or when the session is about to lose context.** It owns the checkpoint a cold start can resume from. Its complement is [recall](recall.md).

This playbook is explicit only. On "keep going" or "run until done", do not pause. Route to [autonomous run](autonomous-run.md).

1. Stop at a safe boundary. Finish the current step or back out of it cleanly. Never stop on a half-edited artifact, a partly written record, or an external write in an unknown state. Start nothing new and cancel pending workers.
2. Take no irreversible action in order to pause. Do not send, schedule, publish, or file anything that was not already authorized and in flight.
3. Resolve every in-flight external write to a known state before writing the note. Read the record back and capture its identifier and state, or record that its state is unknown and exactly how to check it.
4. Make the work durable. Save drafts and partial artifacts to real paths. Say in one line which are incomplete and where each breaks off.
5. Write the checkpoint: the frame, what is done and verified, what is drafted and unverified, the current state and path of each artifact, missing inputs, open decisions, source pointers, and the first action on resume. Point at an existing trail instead of duplicating it.
6. Reply with where you stopped, what is on disk versus still unwritten, the checkpoint path, and the first action on resume.

This is a pause, not a final report. Do not dress a checkpoint up as a completed deliverable.
