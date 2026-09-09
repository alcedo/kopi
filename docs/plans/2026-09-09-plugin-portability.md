# Plugin portability implementation plan

**Goal:** Make Kopi distributable to Claude, ChatGPT/Codex, and Cursor without duplicating its skills or requiring OpenAI-only artifact skills.

**Architecture:** Keep `skills/` canonical. Add a portable Agent Plugins root manifest and Claude metadata; retain the Codex compatibility manifest. Build a clean plugin ZIP and a separate OpenAI local marketplace bundle, with no writes to personal settings. Use host capabilities for artifact generation while preserving verification gates.

**Tech stack:** Markdown, JSON, Python standard library, unittest.

The user approved this approach in the repository assessment follow-up. Separate platform copies would drift; an MCP service would introduce unnecessary hosting for instruction-only skills.

1. Add regression tests for cross-platform manifest consistency, malformed JSON, renamed checkouts, marketplace resolution, and clean/extractable release archives.
2. Add portable and Claude manifests plus a Claude repository marketplace. Extend local validation to check identity/version consistency and marketplace paths.
3. Build deterministic release archives from an explicit file allowlist. Stage the OpenAI marketplace under the output directory so repository and personal configuration are untouched.
4. Replace named mandatory presentation/spreadsheet sub-skills with host capability selection and precise missing-capability handling. Compare baseline and revised scenarios using an independent agent.
5. Add installation, update, prerequisite, and smoke-test instructions; fix README validation commands.
6. Run regression tests, build/extract validation, available native manifest validators, and inspect the final diff. Record host tests that were not performed; do not claim marketplace publication or live installations.
