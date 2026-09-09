<div align="center">

# ☕ Kopi

**Agentic skills for project managers and software architects.**

Connecting evidence, decisions, meetings, delivery state, analysis, presentations, and performance reviews —
while keeping each workflow independently usable.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Codex Plugin](https://img.shields.io/badge/Codex-Plugin-blue.svg)](.codex-plugin/plugin.json)
[![Agent Plugins](https://img.shields.io/badge/Agent_Plugins-1.0-blue.svg)](plugin.json)
[![Skills](https://img.shields.io/badge/Skills-11-green.svg)](#-skill-catalog)
[![Validation](https://img.shields.io/badge/Validation-deterministic-brightgreen.svg)](#-validation)

</div>

---

The central router is [`kopi-mode`](skills/kopi-mode/SKILL.md). Start there when a request spans more than one deliverable. Invoke a specialist skill directly when the outcome is already clear.

## 📑 Contents

- [Layers](#-layers)
- [Installation](#-installation)
- [Skill catalog](#-skill-catalog)
- [Operating model](#-operating-model)
- [Example requests](#-example-requests)
- [Package map](#-package-map)
- [Validation](#-validation)
- [Intentional boundary](#-intentional-boundary)
- [License](#-license)

## 📦 Installation

Kopi packages the same eleven skills for **Claude Code, Claude chat/Cowork,
ChatGPT Work/Codex, and Cursor**. See the [installation guide](INSTALL.md) for
local installation, updates, prerequisites, and host smoke checks.

From the repository root, build the portable plugin ZIP and OpenAI local marketplace:

```bash
python3 scripts/package_plugin.py
```

Use `dist/kopi-0.1.2.zip` for Claude upload or extraction into Cursor's local
plugin folder. For ChatGPT Work/Codex, register the generated
`dist/kopi-openai-0.1.2` marketplace and install through the Plugins Directory.
Claude Code can also load this checkout directly with `claude --plugin-dir .`.

These are local distribution packages, not public marketplace listings. Host
and account capabilities determine which workflows can execute. Presentation,
spreadsheet, calendar, and source-access tools are supplied by your environment;
Kopi does not install libraries or connect accounts.

## 🧱 Layers

| # | Layer | Responsibility |
|:-:|---|---|
| 1 | **Router** | Chooses the smallest complete workflow and sequences connected work. |
| 2 | **Workflow skills** | Own one professional outcome each. |
| 3 | **Playbooks** | Describe the end-to-end path from request to verified deliverable. |
| 4 | **References & rubrics** | Provide schemas, prompts, source rules, and quality gates only when needed. |
| 5 | **Adapters** | Use available presentation, calendar, tracker, document, browser, and spreadsheet capabilities without binding the reasoning layer to one vendor. |
| 6 | **Evaluation** | Checks structure, routing, authority boundaries, and deliverable behavior. |

## 🧰 Skill catalog

| Skill | Use it for | Primary output |
|---|---|---|
| [`kopi-mode`](skills/kopi-mode/SKILL.md) | Connected or ambiguous requests | Routed workflow and coordinated deliverables |
| [`build-presentation`](skills/build-presentation/SKILL.md) | PowerPoint and executive narratives | Render-verified deck |
| [`run-meeting`](skills/run-meeting/SKILL.md) | Meeting preparation, scheduling, and closure | Agenda, pre-read, event, decisions, and actions |
| [`control-portfolio`](skills/control-portfolio/SKILL.md) | Multi-initiative visibility and intervention | Reconciled register and executive intervention view |
| [`research-technology`](skills/research-technology/SKILL.md) | Current tools, frameworks, releases, and AI capabilities | Time-stamped, cited research brief |
| [`decide-architecture`](skills/decide-architecture/SKILL.md) | Architecture options and target-state decisions | Decision record with tradeoffs and impact |
| [`analyze-data`](skills/analyze-data/SKILL.md) | Delivery, operational, and business datasets | Reproducible analysis and honest visuals |
| [`recall-work`](skills/recall-work/SKILL.md) | Catch-up, resume, and handoff | Current-state status capsule |
| [`challenge-deliverable`](skills/challenge-deliverable/SKILL.md) | Red-team review of plans, designs, and decks | Prioritized review findings without silent edits |
| [`capture-learning`](skills/capture-learning/SKILL.md) | Recurring workflow failures and lessons | Evidence-backed structural improvement proposal |
| [`write-performance-review`](skills/write-performance-review/SKILL.md) | Direct-report reviews from 360 feedback and self-reflection | Employee report and separate confidential manager report |

## 🔗 Operating model

Kopi follows a shared chain:

```text
research + data ─▶ architecture decisions ─▶ meetings + work items ─▶ portfolio ─▶ presentation
```

Each workflow can run alone. When composed, records retain source pointers and stable identities so claims can move into decisions, actions, metrics, and slides without being rewritten from memory.

Performance reviews start with the person's role, supplied 360 feedback, and
self-reflection; formal goals are optional. Kopi first presents a confidential
evidence synthesis and numbered ideas, then invites the manager's observations
and selection. It produces an employee report with reviewer identities protected
and a separate manager report containing attribution, disagreements, evidence
gaps, and working notes. The employee copy still needs the manager's check for
identifying context known only to the participants.

The [writing idea selection reference](skills/kopi-mode/references/compare-writing-ideas.md)
can also be composed by other writing workflows. It takes supported ideas and
returns a stable selection record for drafting; it does not require multiple
agents or activate a comparison step for every request.

> [!IMPORTANT]
> **External changes are gated.** Local analysis and drafts may proceed when in scope; sending invitations, changing trackers, posting messages, or updating shared systems requires explicit authority and destination checks. Create and update operations must be safe to retry and must be read back after execution.

## 💬 Example requests

- “Use `kopi-mode` to turn these delivery metrics and architecture notes into the right materials for tomorrow’s steering review.”
- “Build a decision deck from these findings and create the actual PowerPoint.”
- “Research recent changes in our agent frameworks and assess whether the architecture roadmap should change.”
- “Reconcile active initiatives and tell me which three need intervention.”
- “Prepare an architecture review; do not send invitations until I approve.”
- “Use `write-performance-review` for my direct report, an engineering manager. Here are their 360 feedback and self-reflection. Show me the evidence and numbered ideas before drafting the employee and confidential manager reports.”

## 🗂️ Package map

```text
kopi/
├── plugin.json
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── .codex-plugin/plugin.json
├── INSTALL.md
├── skills/
│   ├── kopi-mode/
│   │   ├── SKILL.md
│   │   ├── playbooks/
│   │   └── references/
│   └── <specialist-skill>/
│       ├── SKILL.md
│       └── references/
├── evals/
├── scripts/validate_pack.py
├── scripts/package_plugin.py
└── tests/
```

## ✅ Validation

Run the deterministic pack checks from the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_pack.py .
```

The validator checks cross-platform manifest consistency, Claude marketplace
resolution, skill metadata, resource reachability, internal links, unfinished
placeholders, and legacy implementation terms. Packaging tests also check clean,
reproducible archives and OpenAI marketplace resolution. These checks do not
replace a fresh install in each host. The behavioral cases and run records are
in [`evals/scenarios.md`](evals/scenarios.md) and [`evals/results.md`](evals/results.md).

## 🚧 Intentional boundary

Kopi is **not** a software-delivery agent. It does not carry over pull-request mechanics, worktree handling, CI monitoring, deployment workflows, TDD rules, language-specific coding conventions, or autonomous code repair. Once an architecture decision becomes implementation work, hand that scope to dedicated engineering skills.

The build creates distribution files under `dist/`. It does not install plugins,
modify personal marketplaces, or publish to shared directories.

## 📄 License

Released under the **MIT** License. See [`LICENSE`](LICENSE).
