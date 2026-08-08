# Standards and evidence base

## Contents

1. DORA
2. Secure development
3. Software supply chain
4. OAuth
5. AI coding agents
6. How to apply these sources

Use this file when reviewing or explaining the principles behind the skill. Recheck current official sources before making claims that may have changed.

## DORA

Official sources:

- DORA 2025 State of AI-assisted Software Development: <https://dora.dev/research/2025/dora-report/>
- Working in small batches: <https://dora.dev/capabilities/working-in-small-batches/>
- Continuous integration: <https://dora.dev/capabilities/continuous-integration/>
- Trunk-based development: <https://dora.dev/capabilities/trunk-based-development/>
- Continuous delivery: <https://dora.dev/capabilities/continuous-delivery/>

Applied principles:

- AI amplifies the quality or dysfunction of the surrounding delivery system.
- Small changes and fast feedback reduce integration risk.
- Keep the mainline releasable and branches short-lived.
- Delivery speed and stability are improved together through technical capabilities, not traded blindly.
- Measure outcomes, flow, stability, and recovery rather than code volume.

## Secure development

Official source:

- NIST Secure Software Development Framework 1.1: <https://csrc.nist.gov/projects/ssdf>

Applied principles:

- Align security practices to mission, risk tolerance, and resources.
- Maintain secure development environments.
- Track security requirements, risks, and design decisions.
- Protect software and release integrity.
- Respond to vulnerabilities and prevent recurrence.

## Software supply chain

Official sources:

- SLSA specification 1.2: <https://slsa.dev/spec/v1.2/>
- SLSA provenance: <https://slsa.dev/spec/v1.2/provenance>

Applied principles:

- Trace artifacts to source revision and build process.
- Record build inputs, builder, dependencies, and digest.
- Verify provenance rather than only generating it.
- Adopt the lowest useful level before adding expensive controls.

## OAuth

Official source:

- RFC 9700, OAuth 2.0 Security Best Current Practice: <https://www.rfc-editor.org/info/rfc9700/>

Applied principles:

- Prefer authorization code flows over exposing access tokens in authorization responses.
- Validate redirects and protect state or PKCE as supported.
- Restrict token scope and audience.
- Protect access and refresh tokens from leakage and replay.
- Keep distinct clients, issuers, callbacks, and token stores distinguishable.
- Use end-to-end TLS and avoid credentials in URLs and logs.

## AI coding agents

Official sources:

- GitHub best practices for coding-agent tasks: <https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks>
- GitHub repository custom instructions: <https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-copilot-overview>

Applied principles:

- Give agents clear, bounded tasks and acceptance criteria.
- Research and plan before broad changes.
- Keep repository instructions current.
- Let agents build, test, and validate in an isolated environment.
- Review generated work, especially complex, sensitive, ambiguous, or production-critical changes.

## How to apply these sources

These sources provide compatible principles, not one mandatory universal process. Tailor rigor to risk:

- a local reversible script needs less ceremony than a financial write path;
- a solo project can use one repeatable verification command instead of an enterprise CI platform;
- a private local application does not need public SaaS infrastructure;
- a high-impact external automation needs stronger preview, identity, idempotency, readback, and human-control gates.

Prefer the simplest control that produces the required evidence and recovery capability.
