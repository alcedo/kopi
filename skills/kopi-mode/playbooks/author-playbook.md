# Author a Playbook

**Invoked when a workflow recurs often enough to be worth encoding.** It owns the shape of new and edited instructions inside this pack.

1. Establish that it recurs. One occurrence is a task. A second occurrence of the same correction is the signal. Decide what should change through [learning capture](learning-capture.md) first.
2. Prefer structure over prose. A required field, a validation rule, a template slot, a routing condition, or an ownership rule beats another paragraph. Add prose only where judgment cannot be encoded.
3. Choose the layer. A recurring move several playbooks need is a foundational playbook. A named workflow with its own artifact is a routed playbook plus a skill. A contract, schema, or rubric shared across playbooks is a reference.
4. Write it in this pack's shape: what it owns in one line, the steps in order, and a closing rule that names the failure it prevents. Delegate to other playbooks and references by link rather than restating them.
5. Cut everything that does not change a decision. State the rule and skip the reason unless the rule is confusing without one.
6. Wire it in. Add the route so it is reachable, and link every new file so nothing is orphaned.
7. Validate and test. Run `scripts/validate_pack.py`, then check the change against a real scenario the old instructions handled badly.

Get approval before editing shared playbooks or skills. Record rejected and deferred proposals so the same case is not re-litigated.
