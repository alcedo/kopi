---
name: analyze-data
description: Use when the user asks to inspect a dataset or spreadsheet, calculate metrics, explain a trend, compare groups or periods, find drivers, create charts, test a hypothesis, or turn quantitative evidence into a decision brief.
---

# Analyze Data

Produce a reproducible analysis artifact and decision-ready findings. A confident narrative without a traceable calculation is not complete.

For spreadsheet inputs or outputs, **REQUIRED SUB-SKILL:** Use `spreadsheets:Spreadsheets`. Load its workspace dependencies and follow its verification workflow.

## Frame

State the decision, population, metric definition, comparison, time window, and unit of analysis. Preserve the original data. Record source, retrieval time, filters, and any user-provided business definitions.

Read [analysis contract](references/analysis-contract.md). Inspect schema, types, ranges, missingness, duplicates, joins, units, time zones, outliers, selection effects, and definition changes before interpreting results.

## Analyze

1. Create a reproducible transformation path from source rows to each reported metric.
2. Establish the baseline before slicing for drivers.
3. Test mix shifts, data quality changes, and plausible alternative explanations.
4. Run sensitivity checks for assumptions that could change the conclusion.
5. Use causal language only when the design supports it. Otherwise state association, contribution, or hypothesis.

Do not discard inconvenient records silently. Explain exclusions and show their effect when material.

## Communicate

Choose charts by relationship, not decoration. Preserve scales, denominators, units, sample sizes, and comparison periods. Each chart should support one finding and one decision implication. Use `build-presentation` when the requested deliverable is a deck.

## Verify

Read [analysis rubric](references/analysis-rubric.md). Recompute key values independently or through a second path, inspect formulas and transformations, reconcile totals, and visually inspect charts. Check that every claim maps to a metric and every metric maps to source data.

Return the analysis file, findings, methods, assumptions, limitations, alternative explanations, and recommended next action. If required fields or data are absent, report what can and cannot be concluded.

