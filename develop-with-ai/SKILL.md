---
name: develop-with-ai
description: Use as a reference standard for discovering requirements, planning, implementing, testing, integrating, releasing, operating, reviewing, or improving software with evidence-first phase gates and small vertical slices. Apply it to software products, workflow redesigns, automations, APIs, data systems, AI features, websites, internal tools, refactors, migrations, deployments, incidents, and technical roadmaps—especially when late requirements, legacy data, external systems, or repeated rework could invalidate the design. Explicit invocation selects this standard only; it never by itself authorizes code changes, execution, deployment, or external writes.
---

# Develop with AI

Build software through evidence, small vertical slices, automated feedback, controlled real-world validation, and reversible releases. Treat AI as an implementation accelerator, not the authority for product decisions, security boundaries, or high-impact external actions.

## Treat this skill as a reference standard

Use this skill to govern how work is handled, not to decide what work the user authorized.

- Derive the operating mode from the user's latest explicit request, not from the skill name, skill link, invocation chip, description, or default prompt.
- Treat invoking `$develop-with-ai` by itself as permission to apply this standard and perform relevant read-only inspection only.
- Do not infer permission to edit files, write data, run state-changing commands, restart services, deploy, publish, or call external write APIs merely because this skill was invoked.
- Keep requests to explain, analyze, audit, review, assess, summarize, design, plan, or recommend non-mutating unless the user separately asks for a change.
- Enter implementation only when the user explicitly asks to implement, fix, modify, create, build, execute, deploy, release, or otherwise change a clearly scoped target.
- Treat “continue” as continuing only the most recently authorized mode and scope. It does not promote planning into implementation or broaden prior authorization.
- If the requested verb or target is materially ambiguous, ask one concise question or remain in the less-mutating mode while providing useful analysis.

## Establish authority and context

Before any task:

1. Read the nearest repository instructions completely, including `AGENTS.md` and files it requires.
2. Inspect the relevant source, tests, documentation, Git state, runtime boundaries, and existing releases.
3. Apply this authority order when sources conflict:
   - latest explicit user decision;
   - repository and directory instructions;
   - confirmed specifications and decision records;
   - current implementation and tests;
   - generic engineering guidance in this skill.
4. Stop and identify the conflict if resolving it would change confirmed business rules, data models, formulas, public behavior, security boundaries, or irreversible external state.
5. Preserve user changes and the currently working production version.

## Classify the request

Choose the smallest applicable mode from the user's operative request. Never promote the request to a more mutating mode because the skill contains implementation guidance.

- **Explain or audit**: inspect and report evidence; do not mutate.
- **Discover requirements**: observe real work, inventory existing objects and data, expose architecture-changing unknowns, and define the readiness gate; remain read-only unless artifact writes are separately requested.
- **Discover or plan**: define the problem, scope, workflow, risks, acceptance criteria, and excluded work; do not treat the plan as implementation authorization.
- **Implement or fix**: deliver the smallest complete vertical slice and verify it.
- **Integrate an external system**: prove credentials, scope, identity mapping, read capability, write capability, and readback separately.
- **Release or operate**: protect data, secrets, service availability, rollback, and traceability.
- **Review an incident or project**: separate symptom, root cause, contributing conditions, wasted effort, corrective action, and prevention.

Integration and release requests are not blanket write authorization. Keep reads, previews, local verification, writes, and rollout as separate authorization steps when their effects differ.

For detailed phase gates and outputs, read [references/workflow.md](references/workflow.md).

## Evaluate model selection sparingly

Treat model selection as a risk-control reminder inside this workflow, not as a separate skill or an authorization gate.

- Evaluate it only at the start of a new software task, after a material rise in risk or uncertainty, before a migration, production operation, formal release, or independent final review, or when the user explicitly asks to reassess.
- Keep the current/default model for ordinary work without interruption. Do not recommend a change for brief documentation, log inspection, simple edits, or a small vertical slice that can remain coherent on one model.
- If the assessment recommends a non-default role, stop before the next tool call, command, or file change; state the phase, recommendation, and one-sentence reason; then wait for the user's choice. Do not claim to have detected the user's active model.
- Keep model choice separate from operational authorization. A model change never authorizes a file edit, migration, deployment, deletion, external write, or other consequential action.

Read [references/model-selection.md](references/model-selection.md) when an assessment is required. It defines the current role mapping, decision order, confirmation wording, unavailable-model behavior, and independent-review package.

## Discover before proposing solutions

Do not attempt to elicit a complex workflow by asking only what features the user wants. Requirements that can invalidate the architecture are often implicit in habitual work, existing remote objects, historical failures, batch scale, interruptions, and recovery.

For medium- or high-impact work, complete a requirements discovery gate before technical design or implementation:

1. Observe or reconstruct the current job with representative real examples.
2. Inventory actors, persistent objects, actions, systems, existing data, and ownership.
3. Model each core object's creation, use, change, interruption, reconciliation, retirement, and historical takeover.
4. Define behavior for normal, empty, existing, duplicate, failure, timeout, cancellation, restart, partial-success, uncertain-result, batch, and multi-target cases in proportion to risk.
5. Record confirmed facts, inferences, assumptions, evidence, and blocking unknowns separately.
6. Validate the highest-impact external or technical assumptions before building around them.
7. Walk a low-fidelity flow with a normal example, an existing-data example, and the highest-risk recovery example.

Do not seek an impossible guarantee that every future preference is known. Seek evidence that remaining unknowns cannot overturn the core workflow, identity model, state machine, data ownership, or external execution path.

Read [references/requirements-discovery.md](references/requirements-discovery.md) for risk tiers, discovery passes, operation coverage, the design-packet template, late-requirement handling, and exit criteria. For a saved medium- or high-impact design packet, run `scripts/validate_design_packet.py <packet.md>` before implementation.

## Start from one user outcome

Express the work in one sentence:

> A specific user can complete a specific job with a measurable improvement.

Define:

- current workflow and pain;
- desired outcome and success measure;
- one primary capability for this version;
- explicit non-goals;
- human decisions versus automated decisions;
- irreversible or high-impact actions;
- the smallest real example that proves value.

Do not begin with tables, frameworks, services, agents, or future feature lists. Keep work in progress to one primary feature unless independent parallel work is explicitly requested.

## Write a compact specification

Before implementation, establish:

- entry point and user journey;
- inputs, outputs, and source of truth;
- stable identities and cross-system mappings;
- states and allowed transitions;
- failure, partial-success, timeout, retry, cancellation, and recovery behavior;
- idempotency key or duplicate-prevention rule;
- security and privacy boundaries;
- acceptance criteria;
- excluded work.

Trace each architecture-significant requirement to its evidence, scenario, state or rule, implementation surface, and acceptance check. Do not treat an accepted page draft as acceptance of unspecified data, recovery, migration, or external behavior.

Ask only questions whose answers materially change the result or risk. Otherwise state reasonable assumptions and continue.

Use the readiness checklist in [references/checklists.md](references/checklists.md) for complex or high-risk work.

## Handle late requirements explicitly

When a requirement appears after design or implementation has started, classify it before changing code:

- **Local clarification**: changes wording, presentation, or a reversible local rule without changing identity, persistence, states, external contracts, or accepted workflows. Keep it in the current slice after updating acceptance.
- **Bounded capability**: adds an operation inside the accepted model. Update the operation matrix, affected design units, traceability, tests, and regression scope first.
- **Foundational discovery**: changes a core object, source of truth, lifecycle, state machine, historical-data treatment, external execution path, security boundary, or recovery semantics. Stop the affected implementation and return to discovery and design. Do not disguise it as a small patch.

Measure escaped foundational discoveries and their causes. Update the discovery gate when the same class recurs; do not respond by accumulating one-off edge-case rules.

## Challenge each design section

Treat each independently decidable design unit—such as one page, workflow, state model, interface, or release step—as a review gate.

For each unit:

```text
draft
→ challenge
→ classify issues
→ revise material issues
→ regression-check confirmed decisions
→ accept or escalate
```

Challenge user value, confirmed rules, normal and failure paths, recovery, unnecessary complexity, feasibility, testability, rollback, cross-section consistency, and human-versus-automation boundaries. Do not advance while a blocker or important issue remains unresolved.

Stop when no material issue remains, not when no subjective criticism is imaginable. Use at most two rounds by default and three for high-risk design. If the same blocker persists or requires a business decision, stop and ask the user instead of looping or expanding scope.

After all units pass, run one whole-design integration and Occam review. Report only material resolved issues, remaining risks, required decisions, and gate status. This review never authorizes implementation.

Read [references/workflow.md](references/workflow.md) for severity definitions and detailed stop conditions.

## Attack uncertainty before volume

Identify the assumption most likely to invalidate the design and test it first.

Examples:

- Does the API endpoint actually work with this exact application and token?
- Is the required field type supported by the write API, not merely by the UI?
- Can the deployed host reach the file, database, callback, or device?
- Can names be mapped uniquely, or are platform IDs required?
- Is AI output accurate, stable, affordable, and safe enough for the intended role?

Use a disposable probe, test table, sample record, mock, sandbox, or one-object read-only call. Record sanitized evidence. Do not build the full system around an unverified assumption.

## Build a thin vertical slice

Use this section only after implementation, integration, or release work has been explicitly authorized.

Prefer one end-to-end path over complete horizontal layers:

```text
one user
→ one object
→ one action
→ one persisted result
→ one visible outcome
→ one recoverable failure
```

Implement in this order when applicable:

1. pure business logic;
2. state and persistence;
3. external read adapter;
4. user preview;
5. internal task or command;
6. explicitly confirmed external write;
7. readback and reconciliation;
8. failure recovery and observability.

Expand to batches, multiple accounts, automation, AI, and optimization only after the single-object path is proven.

## Keep architecture proportional

Prefer the existing stack and the fewest moving parts that satisfy current requirements.

- Put a capability in the existing project when it shares users, master data, workflow, deployment, and lifecycle.
- Prototype an uncertain API, model, or data source in an isolated module or sandbox, then integrate it.
- Create a separate project or service only when ownership, data, security, scaling, deployment, or lifecycle is genuinely independent.
- Do not add microservices, queues, caches, orchestrators, agents, or configuration systems without a demonstrated constraint.
- Reuse stable modules; do not duplicate master data merely for interface convenience.

## Separate development from production

Keep the stable release usable while developing:

- production runs a versioned, immutable release;
- development uses an isolated branch or worktree, ports, configuration, data, and logs;
- development disables real external writes by default;
- secrets and live data remain outside source and release artifacts;
- schema changes are backward compatible until the new version is verified;
- rollback is designed before deployment.

Use short-lived branches and small self-contained changes. Keep the default branch releasable.

## Verify continuously

Match verification to risk:

- pure logic: normal, empty, invalid, boundary, and divide-by-zero cases;
- state: transitions, duplicates, cancellation, retries, restarts, and concurrency;
- database: constraints, migrations, rollback compatibility, and representative data;
- external APIs: sanitized contract fixtures, permission errors, expiry, rate limits, timeouts, partial success, and response drift;
- UI: critical user actions, loading, empty, blocked, success, partial-success, and failure states;
- security: input validation, secret redaction, least privilege, and dependency review;
- release: clean build, checksums, configuration templates, health checks, backup, restore, and rollback.

Run the narrow tests during iteration and the full relevant regression before release. Never claim a real integration or write succeeded based only on mocks, static checks, or a successful HTTP transport code.

## Control consequential actions

For money, publishing, deletion, messaging, account permissions, production data, or external platform writes:

```text
prepare
→ show exact preview
→ obtain explicit confirmation
→ execute once
→ read back
→ classify as succeeded, failed, partial, or uncertain
```

Use stable idempotency keys. If a write times out or its result is uncertain, query the remote system before retrying. Never silently broaden the target set, change parameters, repair review failures, or retry irreversible work.

Pause for confirmation when the work would:

- change confirmed business meaning or scope;
- add, delete, rename, or reinterpret important data;
- modify formulas, permissions, security boundaries, or public interfaces;
- perform external writes, deletions, spending, publishing, or messaging not already authorized;
- choose among ambiguous business objects;
- retry an uncertain external result;
- expose services or data beyond the confirmed trust boundary.

## Release progressively

Release in increasing scopes:

1. local automated verification;
2. isolated development integration;
3. one user, account, record, device, or tenant;
4. readback and observation;
5. wider rollout.

Before release:

- back up state;
- record version, source revision, dependencies, build time, tests, migrations, and artifact digest;
- verify health and readiness;
- confirm secrets and business data are excluded;
- define rollback;
- preserve the previous release.

After release, measure actual use, manual steps removed, failure rate, recovery time, rework, and support burden. Expand only when evidence shows value.

## Use AI with explicit guardrails

Give AI bounded tasks with context, examples, acceptance criteria, allowed files, forbidden changes, and required tests.

Use AI freely for:

- repository research;
- implementation planning;
- repetitive code;
- tests and fixtures;
- local diagnostics;
- documentation aligned to verified behavior;
- review and refactoring inside confirmed boundaries.

Reserve human judgment for:

- problem selection and priority;
- ambiguous business rules;
- security and privacy tradeoffs;
- credentials and permission expansion;
- financial or reputational actions;
- destructive or irreversible changes;
- acceptance of real-world results.

Validate all AI-generated work. A plausible explanation, generated test, or green mock is not evidence of production correctness.

## Finish with a decision-ready handoff

Report:

- outcome delivered;
- scope and explicit non-goals;
- changed artifacts;
- tests and validation tier;
- external reads and writes;
- data or schema impact;
- release and rollback status;
- remaining risks or blockers;
- the single next recommended step.

Use [references/checklists.md](references/checklists.md) for the final definition of done. Read [references/standards.md](references/standards.md) only when explaining, reviewing, or updating the engineering principles behind this workflow.
