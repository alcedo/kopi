# Analysis Contract

## Question

- What decision will the analysis inform?
- What outcome or metric is being explained?
- What is the population, unit of analysis, time window, and comparison?
- Which definition is authoritative when sources disagree?

## Provenance

Record source location, retrieval time, source owner, table or sheet names, row counts, filters, joins, transformations, and output path. Never overwrite the only copy of source data.

## Quality checks

- Types, units, currencies, categories, and time zones.
- Missing and impossible values.
- Duplicate entities or events.
- Join cardinality and unmatched records.
- Late-arriving data and changing definitions.
- Outliers and whether they are errors or real cases.
- Selection, survivorship, seasonality, and mix effects.

## Claim levels

- **Description:** what the observed data contains.
- **Association:** variables move together in the observed data.
- **Contribution:** a defined decomposition assigns part of a change to a segment or factor.
- **Causal evidence:** a credible design isolates an effect.
- **Hypothesis:** a plausible mechanism requiring more evidence.

Do not move up this ladder because the audience wants a stronger story.

