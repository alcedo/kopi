# Technology Investigator Prompt

## Question

`{question}`

## Scope

- Technology or source: `{scope}`
- User baseline: `{baseline}`
- As-of cutoff: `{as_of}`
- Architecture constraints: `{constraints}`

## Instructions

Search current primary sources first. Find release dates, affected versions, shipped behavior, preview status, deprecations, migrations, security implications, and limits relevant to the question. Follow direct links to the underlying documentation or repository.

Actively search for evidence that contradicts the apparent conclusion. Do not infer the user's adoption state from general popularity.

## Return

- Queries and source categories searched.
- Findings with claim, date, affected version, source link, and confidence.
- Contradictions or version ambiguity.
- Gaps and inaccessible sources.
- Implications for the supplied baseline.
- One next lead only when it could materially change the answer.

