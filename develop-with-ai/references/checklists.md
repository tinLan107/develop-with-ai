# Delivery checklists

## Contents

1. Definition of ready
2. Requirements discovery gate
3. External API checklist
4. AI feature checklist
5. Automation checklist
6. Data and schema checklist
7. UI checklist
8. Security checklist
9. Release checklist
10. Definition of done

Use only the sections relevant to the current task.

## Definition of ready

- [ ] The user and problem are concrete.
- [ ] The desired outcome is measurable.
- [ ] The current workflow is understood.
- [ ] One primary capability is selected.
- [ ] Non-goals are explicit.
- [ ] Inputs, outputs, and sources of truth are known.
- [ ] Stable identities and mappings are defined.
- [ ] Human decisions and automated actions are separated.
- [ ] Failure, timeout, partial-success, cancellation, and recovery behavior are defined.
- [ ] Acceptance criteria contain a normal and failure example.
- [ ] The largest uncertainty has a probe plan.
- [ ] External writes and destructive actions have an approval boundary.
- [ ] Each independently decidable design unit passed the section challenge gate, or unresolved blocker and important issues are explicit.

## Requirements discovery gate

Use this full section for medium- and high-impact work; keep low-risk reversible changes concise.

- [ ] Representative real work was observed or reconstructed from evidence rather than feature brainstorming alone.
- [ ] The simplest, common, existing-data, and highest-risk examples were considered in proportion to risk.
- [ ] AS-IS behavior, pain, TO-BE behavior, invariants, and incidental current-tool constraints are separated.
- [ ] Actors, persistent objects, consequential actions, systems, and ownership are inventoried.
- [ ] Every core object has creation, use, change, interruption, reconciliation, retirement, and historical-takeover behavior where applicable.
- [ ] Stable identities, sources of truth, legacy data, duplicates, stale data, and externally modified objects are addressed.
- [ ] Consequential operations define normal, empty, existing, duplicate, invalid, timeout, partial, uncertain, cancellation, restart, multi-target, idempotency, and recovery behavior in proportion to risk.
- [ ] Confirmed, observed, inferred, assumed, and unknown statements are distinguished.
- [ ] High-impact assumptions have evidence or explicit blocker status.
- [ ] A low-fidelity walkthrough covered normal, existing-data, duplicate, interruption, and highest-risk recovery examples as applicable.
- [ ] Architecture-significant requirements trace to evidence, scenario or rule, state or data impact, implementation surface, and acceptance check.
- [ ] Remaining unknowns cannot invalidate the core workflow, identity model, state machine, data ownership, external execution path, security boundary, or recovery semantics.
- [ ] The gate is explicitly PASS, CONDITIONAL, or BLOCKED; CONDITIONAL states the isolated slice and stop conditions.

## External API checklist

- [ ] Official current documentation was checked.
- [ ] Exact application, environment, host, endpoint, and API version are known.
- [ ] Credential type and account or tenant scope are known.
- [ ] Required permissions are listed by endpoint.
- [ ] Read capability was proven with sanitized evidence.
- [ ] Write capability was proven separately on one target when authorized.
- [ ] The result was read back from the remote system.
- [ ] Pagination, rate limits, expiry, refresh, and clock assumptions are handled.
- [ ] Timeout and uncertain-write reconciliation are defined.
- [ ] Response fixtures are sanitized and covered by contract tests.
- [ ] Cross-account or shared-resource behavior was proven, not inferred.

## AI feature checklist

- [ ] AI has a defined role and is not used where deterministic logic is sufficient.
- [ ] Representative evaluation inputs and expected qualities exist.
- [ ] Accuracy, stability, cost, and latency thresholds are defined.
- [ ] Unsupported or uncertain cases can abstain.
- [ ] Human review is required for high-impact outputs.
- [ ] Sensitive data and retention boundaries are defined.
- [ ] Prompts, model, parameters, and evaluation version are traceable.
- [ ] Model failure cannot silently trigger irreversible action.
- [ ] Drift and user feedback can be observed.
- [ ] A non-AI fallback exists where the workflow requires continuity.

## Automation checklist

- [ ] Trigger conditions are explicit.
- [ ] Input is snapshotted before execution.
- [ ] A stable idempotency key exists.
- [ ] States and allowed transitions are defined.
- [ ] Duplicate delivery is harmless.
- [ ] Partial success is represented explicitly.
- [ ] A timeout does not cause blind retry.
- [ ] Remote state can be reconciled.
- [ ] Retry requires the correct owner and approval.
- [ ] Cancellation behavior is defined.
- [ ] Original error evidence is retained without secrets.
- [ ] Human takeover is possible.

## Data and schema checklist

- [ ] Each field has one source of truth.
- [ ] Names are not used as unique identity unless guaranteed.
- [ ] Derived data is not duplicated without a synchronization owner.
- [ ] The current schema cannot already support the need.
- [ ] New data has an owner, update frequency, retention rule, and deletion rule.
- [ ] Constraints and indexes express real invariants.
- [ ] Migrations are backward compatible or have a proven stop-the-world plan.
- [ ] Backfill is idempotent and auditable.
- [ ] Rollback and mixed-version behavior are known.
- [ ] Raw technical history is separated from human-facing business data.

## UI checklist

- [ ] The page follows the user's job, not the database schema.
- [ ] Technical identifiers are automatically resolved.
- [ ] Defaults are safe and explainable.
- [ ] Empty, loading, blocked, success, partial-success, failure, and uncertain states are visible.
- [ ] Consequential actions show an exact preview.
- [ ] Confirmation text states target, quantity, and effect.
- [ ] Repeated clicks cannot duplicate work.
- [ ] Recovery or next action is clear.
- [ ] Accessibility and keyboard behavior match the product's needs.
- [ ] The critical path is covered by an automated interaction test.

## Security checklist

- [ ] Secrets are outside source, logs, fixtures, release packages, and business tables.
- [ ] Development and production credentials are separated.
- [ ] Least privilege is used.
- [ ] Untrusted input is validated and output is safely encoded.
- [ ] Authentication and authorization are tested independently.
- [ ] OAuth state, redirect, application identity, token refresh, and token storage are protected.
- [ ] Dependencies are locked and reviewed.
- [ ] Logs are useful but redact credentials and sensitive data.
- [ ] Backups are protected and restore was tested.
- [ ] Network exposure matches the confirmed trust boundary.

## Release checklist

- [ ] The change is a bounded versioned unit.
- [ ] Relevant automated tests pass.
- [ ] Production build succeeds.
- [ ] Migrations are rehearsed and versioned.
- [ ] Backup completed.
- [ ] Secrets and live data are excluded from the artifact.
- [ ] Artifact digest and source revision are recorded.
- [ ] Health and readiness checks pass.
- [ ] One-target smoke test passes.
- [ ] Rollback is documented and feasible.
- [ ] Previous release remains available.
- [ ] Post-release observation owner and period are defined.

## Definition of done

- [ ] The specified user outcome works end to end.
- [ ] Explicit non-goals remain out of scope.
- [ ] Acceptance criteria pass.
- [ ] Normal, boundary, failure, duplicate, and recovery paths are verified in proportion to risk.
- [ ] Validation tier is stated honestly: static, mock, integration, pilot, or production.
- [ ] External reads and writes are listed.
- [ ] Data, schema, permission, and secret impacts are listed.
- [ ] Documentation describes verified current behavior, not aspirations.
- [ ] Git or source status is known.
- [ ] Release and rollback status are known.
- [ ] Remaining risks and the single next step are clear.
- [ ] The whole-design integration and Occam review found no unresolved material issue.
