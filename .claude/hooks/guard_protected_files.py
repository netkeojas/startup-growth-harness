#!/usr/bin/env python3
"""PreToolUse guardrail: blocks the agent from writing to protected paths.

Students are free to hand-edit any of these files in their own editor —
this hook only intercepts tool calls made BY Claude.

Covers two routes to the filesystem:
  - Edit / Write: blocked if the target file_path/path matches a protected
    path, exactly as before.
  - Bash: blocked if the command string even *mentions* a protected path.
    This is intentionally broad (fail closed) — Bash can write files in
    ways Edit/Write never sees (`python3 -c "open(...).write(...)"`,
    `sed -i`, `echo ... > file`, `git checkout -- file`, etc.), and the
    project's settings allow Bash(python3:*) and Bash(git:*), so without
    this the hard-lock on Edit/Write alone is not airtight.
"""
import json
import re
import sys

PROTECTED_SUFFIXES = (
    "docs/index.html",
    "context/brand_kit.md",
    ".claude/settings.json",
)


def block(path: str) -> None:
    print(
        f"BLOCKED: '{path}' is protected by a hard guardrail and cannot be "
        "written to or referenced from a shell command by the agent. Edit "
        "it by hand in your editor instead.",
        file=sys.stderr,
    )
    sys.exit(2)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {}) or {}

    if tool_name in ("Edit", "Write", "MultiEdit"):
        file_path = tool_input.get("file_path") or tool_input.get("path") or ""
        normalized = file_path.replace("\\", "/")
        for suffix in PROTECTED_SUFFIXES:
            if normalized.endswith(suffix):
                block(suffix)

    elif tool_name == "Bash":
        command = tool_input.get("command", "") or ""
        for suffix in PROTECTED_SUFFIXES:
            # Match the path as a token, not as a substring of some longer
            # unrelated name (e.g. "my-context/brand_kit.md.bak" shouldn't
            # necessarily match, but "context/brand_kit.md" anywhere in the
            # command string should).
            if re.search(re.escape(suffix), command):
                block(suffix)

    sys.exit(0)


if __name__ == "__main__":
    main()
