# Analysis Rubric

## Reproducibility

- Source data is preserved and identified.
- Filters, joins, exclusions, transformations, and formulas are traceable.
- Key metrics can be recomputed from the delivered artifact.
- Totals and row counts reconcile at material boundaries.

## Data quality

- Missingness, duplicates, units, time zones, outliers, and schema changes are checked.
- Join loss and population changes are measured.
- Material limitations are visible in the findings, not buried in an appendix.

## Reasoning

- Metric definitions and comparison periods match the question.
- Alternative explanations and mix shifts are tested.
- Sensitivity to consequential assumptions is shown.
- Causal language does not exceed the study design.

## Visuals and decisions

- Charts use honest scales, labels, denominators, units, and sample sizes.
- Every chart supports a specific finding.
- Every recommendation follows from a finding and names uncertainty.
- Correlation, contribution, causal evidence, and hypothesis remain distinct.

Return `PASS`, `REVISE`, or `BLOCKED`. A result that cannot be reproduced or that overstates causality cannot pass.
