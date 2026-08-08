# Requirements discovery gate

## Contents

1. Purpose and stopping rule
2. Scale rigor by risk
3. Three discovery passes
4. Evidence and traceability
5. Operation coverage
6. Prototype and assumption probes
7. Design packet
8. Late requirements
9. Gate decision

## Purpose and stopping rule

Discover requirements that would be expensive to learn after implementation: changes to the primary job, object identity, source of truth, lifecycle, state machine, historical-data treatment, external contract, security boundary, or recovery semantics.

Do not promise exhaustive future requirements. Stop discovery when:

- the primary job is demonstrated end to end;
- core objects and consequential actions are known;
- architecture-significant scenarios have defined behavior;
- high-impact assumptions have evidence or remain explicit blockers;
- representative examples pass a low-fidelity walkthrough;
- remaining unknowns are local extensions rather than architecture-breaking discoveries.

## Scale rigor by risk

Classify the work before choosing artifacts.

### Low impact

Use a concise inline discovery note for reversible local changes with no persistent-state, cross-module, external-write, migration, security, or broad UI effect.

Confirm the user outcome, current behavior, desired behavior, one normal example, one boundary example, and acceptance check.

### Medium impact

Use a compact design packet for features that add persistent state, async behavior, multiple screens or modules, a new user workflow, batch actions, or compatibility concerns.

Require real examples, actor-object-action inventory, lifecycle and operation coverage, assumptions, low-fidelity walkthrough, traceability, and regression scope.

### High impact

Use a full design packet for external writes, money, deletion, migration, production data, permissions, account sharing, unknown remote results, broad architecture replacement, or difficult rollback.

Also require an external capability probe, legacy-data migration or isolation, idempotency and reconciliation, kill switch, rollback, pilot scope, and explicit user authorization boundaries.

## Three discovery passes

### Pass 1: Reconstruct real work

Use evidence instead of feature brainstorming.

Collect the minimum relevant set of:

- direct observation, screen recording, or step-by-step demonstration;
- representative real records, files, object counts, and batch sizes;
- historical failures, retries, manual repairs, logs, support questions, and screenshots;
- current code, data, caches, platform objects, and operating instructions;
- one simplest example, one common example, and the highest-risk example.

Separate:

- **AS-IS**: what happens today;
- **pain**: why it needs to change;
- **TO-BE**: the desired job;
- **invariants**: business facts that must remain true;
- **incidental constraints**: limitations of the current tool that need not be copied.

### Pass 2: Model the requirement surface

Inventory:

- actors and responsibility boundaries;
- persistent and remote objects;
- user, scheduled, and external-event actions;
- source of truth and stable identity for every datum;
- existing, legacy, duplicate, deleted, disabled, stale, or orphaned objects;
- normal lifecycle, retirement, archival, takeover, and reconciliation;
- cross-day, cross-device, cross-account, and multi-target behavior where relevant.

For every core object, cover creation, discovery, viewing, selection, change, enable or disable, retirement, history, and takeover of existing data. Mark an operation explicitly unnecessary rather than leaving it unexamined.

### Pass 3: Simulate and disprove

Walk representative jobs through a low-fidelity flow. Use the user's real vocabulary and realistic quantities.

Include:

- one normal new-object path;
- one existing or legacy-data path;
- one duplicate or repeated-action path;
- one interruption or restart path;
- one partial-success or uncertain-result path for multi-step external work;
- the largest common batch and target count;
- a cross-device or deployment environment when the product requires it.

Run a premortem: assume the feature failed after release and identify likely causes, silent corruption, duplicate effects, unrecoverable states, misleading success, and manual escape routes.

## Evidence and traceability

Label requirement statements as:

- **confirmed**: explicitly decided by the authorized user or repository rule;
- **observed**: directly evidenced in real work, data, code, logs, or platform behavior;
- **inferred**: a reasoned interpretation that still needs confirmation;
- **assumed**: temporarily adopted to proceed, with impact and validation plan;
- **unknown**: unresolved and either blocking or consciously deferred.

Trace every architecture-significant requirement:

```text
evidence
→ user outcome
→ rule or scenario
→ identity/state/data impact
→ implementation surface
→ acceptance check
```

Do not use percentages such as “100% requirements covered” unless the denominator is explicit. Report uncovered high-risk assumptions and escaped foundational discoveries instead.

## Operation coverage

Use the full operation card only for consequential operations: persistent writes, external calls, async tasks, batch actions, deletion, migration, permissions, and uncertain results.

```text
Operation:
Actor and entry:
Preconditions:
Inputs and immutable snapshot:
Source of truth and stable identities:
Automatic resolution:
Human decision:
Writes and side effects:
Normal result:
Empty or no-match result:
Already-existing or duplicate result:
Validation failure:
Timeout or uncertain result:
Partial success:
Cancellation:
Refresh, restart, and resume:
Multi-object isolation:
Idempotency and reconciliation:
Audit and observability:
Rollback or manual takeover:
Acceptance checks:
```

For low-risk read-only UI actions, use a short interaction check: discoverability, empty, loading, error, keyboard or pointer behavior, and recovery.

Avoid Cartesian scenario explosion. Cover each relevant dimension once, then combine only high-probability or high-impact pairs:

- quantity: zero, one, common batch, limit;
- time: current, delayed, expired, cross-day;
- state: new, existing, disabled, deleted, stale;
- result: success, failure, partial, uncertain;
- repetition: duplicate object, repeated click, retry;
- interruption: refresh, crash, network loss, service restart;
- scope: one and multiple users, tenants, devices, accounts, or targets;
- consistency: local-only, remote-only, mismatched, externally modified.

## Prototype and assumption probes

Do not use polished visuals before workflow and states stabilize. Progress through:

1. text flow;
2. object, state, and operation model;
3. low-fidelity wireframe;
4. task walkthrough;
5. visual system.

During walkthrough, avoid coaching the user. Treat hesitation, missing next actions, unexpected navigation, and “what now?” questions as discovery evidence.

Rank assumptions by:

```text
late-discovery risk = probability of being wrong × cost of discovering it late
```

Probe the highest score first. Keep external tests read-only or preview-only until real writes are separately authorized. Distinguish documentation evidence, mock behavior, single real success, recovery evidence, scale evidence, and release evidence.

## Design packet

For medium- and high-impact work, save or present these sections before implementation:

```markdown
# Design packet: <outcome>

## Authorization and current phase
## User outcome and success measure
## Scope and non-goals
## Evidence and representative examples
## AS-IS workflow and pain
## TO-BE workflow
## Actors, objects, actions, and ownership
## Sources of truth and stable identities
## Object lifecycles and historical data
## Consequential operation matrix
## States, transitions, and invariants
## External capabilities and assumptions
## Failure, duplicate, interruption, and recovery
## Low-fidelity walkthrough findings
## Architecture and change boundaries
## Migration, retirement, rollback, and kill switch
## Acceptance and evidence levels
## Traceability and regression scope
## Open decisions and gate status
```

Keep sections compact and use links to authoritative project artifacts instead of copying them. A section may state “not applicable” with a reason; do not silently omit it.

## Late requirements

Classify a late discovery before implementation continues.

### Local clarification

Keep it in the current slice after updating the scenario and acceptance check. Examples: copy, presentation, a safe default, or a reversible local preference.

### Bounded capability

Pause the affected unit. Update operation coverage, traceability, tests, and regression scope. Resume only after its design unit passes challenge.

### Foundational discovery

Stop the affected implementation. Return to discovery and design when the discovery changes a core object, identity, source of truth, lifecycle, state machine, history, external execution, security boundary, migration, or recovery.

Perform impact analysis before editing code. List affected data, states, interfaces, pages, jobs, tests, running releases, migration, and rollback. Do not patch around the old design.

## Gate decision

Return one status:

- **PASS**: no unresolved blocker or important discovery issue; remaining unknowns cannot invalidate the core design.
- **CONDITIONAL**: implementation may proceed only on an explicitly isolated slice; list assumptions, boundaries, and stop conditions.
- **BLOCKED**: a business decision, external capability, identity, historical-data rule, security boundary, or recovery behavior remains unresolved.

Report:

```text
Current phase:
Authorized mode and scope:
Evidence available:
Gate status:
Unresolved material items:
Permitted next step:
Forbidden actions:
```
