---
name: research-technology
description: Use when the user asks for latest or recent changes, release comparisons, technology radar updates, framework or tool evaluation, AI capability research, version impact, adoption advice, or roadmap implications.
---

# Research Technology

Produce a date-aware decision brief grounded in current primary evidence. “Latest” requires a fresh web search during the run.

## Frame

Identify the technologies, current versions or practices, decision being considered, architecture context, constraints, and decision horizon. Inspect local manifests or documentation when they establish the user's actual baseline. Do not assume that a named tool is deployed.

Record the research as-of timestamp. Read [source policy](references/source-policy.md) before searching.

## Investigate

Partition work by technology or independent evidence source. Give every investigator the [investigator prompt](references/investigator-prompt.md), one bounded question, the known baseline, and the same cutoff date. Run independent searches in parallel when available, then inspect the cited sources yourself before synthesis.

Separate:

- released and documented behavior;
- announced or preview behavior;
- deprecations and migration requirements;
- measured third-party findings;
- community opinion;
- inference about the user's system.

Search for contradictions and evidence that would reverse the recommendation. Empty or inaccessible source categories are findings, not permission to guess.

## Decide

Map changes to the user's architecture, roadmap, operating model, security, migration cost, and reversibility. Recommend `adopt`, `trial`, `assess`, `hold`, or `retire` only when the user needs a radar decision. Otherwise answer the question directly.

Propose an experiment only when sources cannot settle a material uncertainty. Name the hypothesis, smallest probe, metric, and decision rule.

## Report

Read [research rubric](references/research-rubric.md). Include as-of time, current baseline, change matrix, implications, recommendation, confidence, contradictions, gaps, and direct links near the claims they support. Never cite a search-results page or fabricate a source.

