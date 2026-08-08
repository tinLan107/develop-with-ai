#!/usr/bin/env python3
"""Validate that a medium/high-impact design packet contains every gate section."""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path


REQUIRED_SECTIONS = (
    "Authorization and current phase",
    "User outcome and success measure",
    "Scope and non-goals",
    "Evidence and representative examples",
    "AS-IS workflow and pain",
    "TO-BE workflow",
    "Actors, objects, actions, and ownership",
    "Sources of truth and stable identities",
    "Object lifecycles and historical data",
    "Consequential operation matrix",
    "States, transitions, and invariants",
    "External capabilities and assumptions",
    "Failure, duplicate, interruption, and recovery",
    "Low-fidelity walkthrough findings",
    "Architecture and change boundaries",
    "Migration, retirement, rollback, and kill switch",
    "Acceptance and evidence levels",
    "Traceability and regression scope",
    "Open decisions and gate status",
)

GATE_STATUSES = ("PASS", "CONDITIONAL", "BLOCKED")


def _headings(text: str) -> set[str]:
    result: set[str] = set()
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            result.add(stripped[3:].strip())
    return result


def validate_text(text: str) -> list[str]:
    errors: list[str] = []
    if not any(line.strip().startswith("# Design packet:") for line in text.splitlines()):
        errors.append("missing '# Design packet: <outcome>' title")

    headings = _headings(text)
    for section in REQUIRED_SECTIONS:
        if section not in headings:
            errors.append(f"missing section: {section}")

    gate_section = ""
    marker = "## Open decisions and gate status"
    if marker in text:
        gate_section = text.split(marker, 1)[1]
    if not any(status in gate_section for status in GATE_STATUSES):
        errors.append("gate status must contain PASS, CONDITIONAL, or BLOCKED")
    return errors


def validate_file(path: Path) -> list[str]:
    if not path.is_file():
        return [f"file not found: {path}"]
    return validate_text(path.read_text(encoding="utf-8"))


def _valid_fixture() -> str:
    sections = []
    for section in REQUIRED_SECTIONS:
        body = "PASS" if section == "Open decisions and gate status" else "Not applicable: self-test."
        sections.append(f"## {section}\n\n{body}\n")
    return "# Design packet: self-test\n\n" + "\n".join(sections)


def run_self_test() -> int:
    with tempfile.TemporaryDirectory() as directory:
        valid = Path(directory) / "valid.md"
        invalid = Path(directory) / "invalid.md"
        valid.write_text(_valid_fixture(), encoding="utf-8")
        invalid.write_text("# Design packet: invalid\n", encoding="utf-8")
        valid_errors = validate_file(valid)
        invalid_errors = validate_file(invalid)
    if valid_errors:
        print("self-test failed: valid fixture rejected", file=sys.stderr)
        for error in valid_errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    if not invalid_errors:
        print("self-test failed: invalid fixture accepted", file=sys.stderr)
        return 1
    print("self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return run_self_test()
    if args.packet is None:
        parser.error("packet is required unless --self-test is used")

    errors = validate_file(args.packet)
    if errors:
        print(f"design packet is not ready: {args.packet}", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"design packet is structurally ready: {args.packet}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
