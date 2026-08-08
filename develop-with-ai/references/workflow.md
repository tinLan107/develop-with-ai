# AI-assisted development workflow

## Contents

1. Delivery loop
2. Authorization gate
3. Section challenge gate
4. Requirements discovery gate
5. Phase gates
6. Request modes
7. Environment and release model
8. Measurement and review

## Delivery loop

Use this sequence for product features, automations, integrations, data systems, AI capabilities, refactors, and releases:

```text
Problem
→ Outcome
→ Specification
→ Risk probe
→ Thin vertical slice
→ Automated feedback
→ Controlled real-world validation
→ Progressive release
→ Observation
→ Continue, change, or remove
```

Do not force every task through heavyweight documents. A small reversible fix can express each gate in a few lines. Increase rigor with ambiguity, blast radius, irreversibility, security sensitivity, financial impact, and external dependencies.

## Authorization gate

This workflow is a reference standard, not implementation authorization.

- Select the request mode from the user's latest explicit action and target.
- Invoking `$develop-with-ai` only selects this standard; it does not select implementation mode.
- Explanation, analysis, audit, review, planning, design, and recommendation requests remain non-mutating.
- Implementation, operation, deployment, or external writes require explicit authorization for that scope.
- “Continue” inherits the last authorized mode and scope without expanding either one.
- When ambiguity would change state, choose the less-mutating mode or ask one blocking question.

## Section challenge gate

Apply this gate while designing. A design unit is a part that can be accepted independently: one page, user-journey step, state model, API contract, data-ownership rule, automation boundary, or release step. Do not run the loop sentence by sentence.

For every unit:

1. Draft the smallest design that satisfies the confirmed outcome.
2. Challenge it against these lenses:
   - user outcome and necessity;
   - conflicts with confirmed requirements, data ownership, authorization, or security;
   - normal, empty, failure, timeout, duplicate, cancellation, and recovery paths;
   - unnecessary fields, states, steps, components, or scope;
   - feasibility, testability, observability, rollback, and compatibility;
   - consistency with already accepted units;
   - human decisions versus automated decisions.
3. Record each issue with its exact location, failure scenario, impact, severity, and proposed correction. Reject vague criticism.
4. Revise blocker and important issues. Handle normal issues only when they stay in scope. Record preferences without letting them block.
5. Regression-check that the revision did not break confirmed behavior.
6. Mark the unit accepted or stop for a user decision.

Classify issues as:

- **Blocker**: a confirmed-rule conflict, security or data-loss risk, irreversible ambiguity, or failure of the primary job.
- **Important**: material ambiguity, a missing failure or recovery path, harmful duplication, or inability to verify the design.
- **Normal**: a safe, in-scope maintainability or experience simplification.
- **Preference**: wording, styling, or future ideas with no material effect.

Stop the challenge loop when:

- no blocker or important issue remains;
- normal issues are fixed or consciously accepted;
- remaining items are preferences, future scope, or explicitly recorded low-risk unknowns;
- the last revision passes regression against accepted units.

Use one round for a routine low-risk unit, at most two rounds by default, and at most three for money, permissions, deletion, migration, production data, or external writes. If the same blocker persists for two rounds or requires an unconfirmed business choice, ask the user. Never invent work merely to keep finding issues.

After all units pass, run one cross-section integration review for broken handoffs, conflicting terms or states, duplicated responsibilities, failure propagation, and one final Occam pass.

Keep the user-facing trace compact: material issues resolved, remaining risks, decisions needed, and pass or block status. Do not dump performative self-critique. The challenge gate does not authorize implementation.

## Requirements discovery gate

Use this gate before design and implementation when the work adds persistent state, async behavior, multiple modules, batch actions, external systems, migration, deletion, permissions, broad UI, or difficult rollback.

Do not rely on feature brainstorming alone. Reconstruct representative real work, inspect existing and remote data, model actors, objects, actions, lifecycles, historical takeover, and architecture-significant scenarios, then validate high-impact assumptions. Use risk-proportional depth rather than exhaustive combinations.

Read [requirements-discovery.md](requirements-discovery.md) and return PASS, CONDITIONAL, or BLOCKED. A saved medium- or high-impact packet must pass `scripts/validate_design_packet.py` structurally; structural success does not replace substantive review or user acceptance.

## Phase gates

### Gate 1: Problem and outcome

Required:

- current user or operator workflow;
- concrete pain or risk;
- measurable desired outcome;
- primary user;
- evidence that the problem exists.

Stop when the request is only a broad solution idea without a confirmed problem.

### Gate 2: Requirements discovery

Required in proportion to risk:

- representative real-work evidence and quantities;
- actors, core objects, consequential actions, ownership, and history;
- lifecycles, identities, sources of truth, and existing-data treatment;
- duplicate, interruption, restart, partial-success, uncertain-result, and multi-target behavior where relevant;
- high-impact assumptions with evidence or explicit blockers;
- low-fidelity walkthrough findings;
- traceability and gate status.

Do not advance when a remaining unknown can invalidate the primary workflow, data model, state machine, historical-data handling, external path, or recovery.

### Gate 3: Compact specification

Required:

- user journey;
- inputs and outputs;
- source of truth;
- business rules;
- human and automation boundary;
- failure and recovery behavior;
- acceptance criteria;
- non-goals.

Prefer examples over abstract prose. One valid example and one failure example often reveal missing rules.

### Gate 4: Feasibility and risk

Rank unknowns by:

```text
risk = probability of being wrong × cost of discovering it late
```

Probe the highest-risk assumption first. For external systems, verify each endpoint and token type independently. For AI, evaluate representative inputs before designing automation around the model.

### Gate 5: Minimal design

Confirm:

- stable identity for each entity;
- ownership of every datum;
- state transitions;
- idempotency;
- compatibility;
- security boundary;
- observability;
- rollback.

Reject data or components that do not serve the current vertical slice.

### Gate 6: Vertical implementation

Deliver one complete path. Avoid building all screens, tables, endpoints, or adapters in advance.

Use ports and adapters:

- keep business logic pure and independently testable;
- isolate database, file, network, platform, and model I/O;
- normalize external failures at the boundary while retaining sanitized raw evidence;
- keep irreversible actions behind explicit commands.

### Gate 7: Verification

Use the fastest feedback first:

1. formatting and static checks;
2. unit tests;
3. state and database tests;
4. contract and integration tests;
5. UI critical-path tests;
6. production build;
7. one-object real validation;
8. full regression.

Do not use an end-to-end test to compensate for untested business logic.

### Gate 8: Controlled rollout

Use the smallest meaningful blast radius:

- one record before a batch;
- one account before all accounts;
- one device before the network;
- one user before general access;
- recommendation before automatic action.

Expose freshness and uncertainty. Do not represent eventual synchronization as real time or estimated values as settled truth.

### Gate 9: Operate and learn

Observe:

- adoption and completed jobs;
- manual steps removed;
- lead time from idea to validated value;
- change failure rate;
- recovery time;
- duplicate or uncertain operations;
- support and explanation burden;
- rework caused by late discovery.

If a feature is not used, simplify or remove it rather than expanding it.

## Request modes

### Planning

Output:

- objective;
- user journey;
- scope and non-goals;
- data ownership;
- dependencies and assumptions;
- failure paths;
- acceptance criteria;
- staged implementation order;
- blocking decisions.

Do not change code or external state unless separately authorized.

### Implementation

Output before changing:

- intended behavior;
- affected components;
- verification plan;
- assumptions within scope.

Then implement the smallest complete slice, test it, inspect the diff, and report evidence.

### External integration

Maintain a capability matrix:

| Capability | Application | Credential type | Scope | Read | Write | Readback | Last verified |
| --- | --- | --- | --- | --- | --- | --- | --- |

Treat authentication, authorization, resource visibility, write permission, and cross-account sharing as separate claims.

### AI feature

Define:

- role: draft, classify, extract, recommend, or act;
- representative evaluation set;
- quality threshold;
- abstention and fallback;
- cost and latency ceiling;
- sensitive data policy;
- human review boundary;
- monitoring for model or prompt drift.

Start with offline evaluation, then shadow or recommendation mode, then bounded action only when justified.

### Automation

Define:

- trigger;
- immutable input snapshot;
- idempotency key;
- states and transitions;
- partial-success semantics;
- remote reconciliation;
- retry ownership;
- cancellation;
- audit trail;
- human takeover.

### Release or migration

Use expand-and-contract for incompatible data changes:

1. add backward-compatible structures;
2. deploy code that handles old and new;
3. migrate and verify;
4. switch reads and writes;
5. remove old structures in a later release.

Never bundle an unrelated external business-data migration into a routine software upgrade.

## Environment and release model

Recommended minimal model:

```text
main                  always releasable
short-lived branch    one bounded change
development           isolated ports, data, config, logs
pilot                 smallest real target
production            immutable versioned release
```

Keep mutable state outside release directories:

```text
releases/
current
data/
secrets/
logs/
backups/
```

For solo or local software, a repeatable local verification command is sufficient before adding hosted CI. Add infrastructure only when it removes a demonstrated bottleneck.

## Measurement and review

Use metrics to improve the system, not to reward output volume:

- validated user outcomes;
- cycle time;
- deployment frequency;
- change failure rate;
- recovery time;
- escaped defects;
- rework ratio;
- manual steps and minutes removed;
- feature usage and retention.

Run blameless reviews. Separate:

- direct cause;
- contributing conditions;
- why detection was late;
- recovery quality;
- corrective action;
- prevention;
- work to stop doing.
