---
name: analyze-data
description: Use when the user asks to inspect a dataset or spreadsheet, calculate metrics, explain a trend, compare groups or periods, find drivers, create charts, test a hypothesis, or turn quantitative evidence into a decision brief.
---

# Analyze Data

Produce a reproducible analysis artifact and decision-ready findings. A confident narrative without a traceable calculation is not complete.

## Select available capabilities

For spreadsheet inputs or outputs, use the host's spreadsheet skill or tools, such as `spreadsheets:Spreadsheets` in OpenAI environments, an available `xlsx` skill in Claude, or a connected spreadsheet application. Discover actual capabilities; a particular skill name is not a prerequisite. Follow the selected tool's dependency and verification instructions.

If no spreadsheet skill is available, use available file or code tools that can read and produce the requested format. Preserve formulas, data types, and formatting when editing workbooks. Verify saved output by reopening it; recalculate formulas with an available spreadsheet engine when formulas change or cached values may be stale. Writing a formula string does not prove that its displayed value is correct.

Do not assume libraries, a calculation engine, or connectors are installed, and do not install software or connect accounts merely because this skill mentions it. If a required capability is missing, identify the blocked operation. Continue useful analysis from accessible data, but never claim a workbook was created, recalculated, or visually verified without performing that step. Label any generated file with incomplete verification as a draft and state the remaining checks.

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
