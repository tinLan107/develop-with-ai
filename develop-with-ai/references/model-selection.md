# Model-selection reminder

Use this reference only when the `SKILL.md` model-selection gate says an assessment is needed. It is a sparse confirmation mechanism, not a universal routing system and not an authorization mechanism.

## Current role mapping

Maintain concrete model names here, and use role names everywhere else:

| Role | Current model | Primary use |
| --- | --- | --- |
| `frontier_model` | GPT-5.6 Sol | High-consequence reasoning, hard uncertainty, release, migration, incident, or independent review |
| `default_model` | GPT-5.6 Terra | Ordinary planning, implementation, testing, and bounded integration work |
| `fast_model` | GPT-5.6 Luna | Independent, mechanical, low-risk bulk work that is easy to verify |

Do not claim to have verified the user's current model through technical means. Treat availability as user- or environment-provided information.

## Assess in this order

Use this order; do not choose a model merely from labels such as “planning”, “implementation”, “architecture”, “cross-module”, or “review”:

```text
consequence and reversibility
→ uncertainty and verification difficulty
→ complexity and blast radius
→ development stage
```

Default to `default_model` when information is incomplete. Keep one small vertical feature on the same model through normal implementation and testing where practical. Do not switch for a few minutes of low-risk work merely to optimize speed.

## Recommend `frontier_model` only for a substantive condition

Recommend `frontier_model` when one or more of these conditions materially applies:

- The decision is difficult to reverse or expensive to change.
- The task involves production data, money, permissions, secrets, security, or public behavior.
- Multiple options have an important long-term tradeoff.
- The change alters a core boundary or a confirmed contract.
- Root cause remains unknown after the current approach has not made material progress.
- The work is a database migration, production release, incident response, or independent final review.

Do not recommend it only because a prompt uses words such as “architecture”, “cross-module”, or “review”.

## Recommend `fast_model` only for bounded mechanical work

Recommend `fast_model` only when the task is independent, bulk, low-risk, easy to verify, and the switch saves meaningful time. Suitable examples include:

- Mechanical changes repeated across many files.
- Organizing a large amount of logs or test output.
- Documenting already-verified behavior.
- Drafting basic tests or fixtures from an established pattern.

`fast_model` must not independently decide business rules, security or permission boundaries, database migrations, money calculations, testing sufficiency, or release conclusions. Validate its output with `default_model` and the relevant tests.

## Use the confirmation gate only when a change is recommended

At an eligible assessment point:

1. Continue silently with `default_model` when it remains appropriate.
2. If `frontier_model` or `fast_model` is recommended, stop before the next tool call, command, or file change.
3. State the current phase, recommended role, and one short reason.
4. Wait for one of these user responses:
   - `已切换，继续`
   - `保持当前模型继续`
   - `目标模型不可用`
5. Record the choice for the current task and risk level. Do not ask again unless the risk level materially changes, a new or forked task begins, or the user asks to reassess.

Use concise wording, for example:

> 当前进入生产发布前审查，涉及不可逆部署与回滚判断；建议使用 `frontier_model`。请回复：已切换，继续／保持当前模型继续／目标模型不可用。

Do not create a “switch again after switching” loop. If the user says “本阶段不再提醒”, do not revisit the gate unless risk materially changes.

## Keep choice and authorization separate

Follow this order:

```text
confirm model selection
→ analyze or implement within existing authorization
→ show an accurate preview for a consequential operation
→ obtain separate operational confirmation
→ execute
→ read back and verify
```

Changing to `frontier_model` does not authorize file changes, database migration, deployment, deletion, platform writes, spending, publishing, messaging, or any other high-impact operation.

## When a target model is unavailable

- Continue ordinary work with `default_model`.
- For work that genuinely needs `frontier_model`, remain read-only, narrow the scope, increase the available model's reasoning effort where possible, or pause for the user.
- Never lower testing, approval, rollback, or recovery requirements because a target model is unavailable.

## Independent final review

For a consequential release, prefer a new or forked `frontier_model` task with an explicit review package:

- original requirement and acceptance criteria;
- confirmed decisions;
- explicit non-goals;
- code diff or deliverable;
- test results and validation level;
- data, permission, security, and external-write impact;
- known risks and rollback plan.

The independent reviewer gives an assessment; it does not grant release authority.
