#!/usr/bin/env python3
"""PreToolUse guardrail: blocks the agent from writing to protected paths.

Students are free to hand-edit any of these files in their own editor —
this hook only intercepts Edit/Write tool calls made BY Claude.
"""
import json
import sys

PROTECTED_SUFFIXES = (
    "website/index.html",
    "context/brand_kit.md",
    ".claude/settings.json",
)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    tool_input = payload.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path") or tool_input.get("path") or ""
    normalized = file_path.replace("\\", "/")

    for suffix in PROTECTED_SUFFIXES:
        if normalized.endswith(suffix):
            print(
                f"BLOCKED: '{suffix}' is protected by a hard guardrail and "
                "cannot be edited by the agent. Edit it by hand in your "
                "editor instead.",
                file=sys.stderr,
            )
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
