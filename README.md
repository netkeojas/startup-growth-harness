# Startup Growth Harness

A small autonomous "agent harness" built on Claude Code: it researches a
trend, drafts a branded LinkedIn post + visual card, and publishes a new
insight to a live-feeling startup website — on its own, triggered by one
slash command.

This is the Phase 2 teaching artifact for the workshop: Phase 1 was a single
ChatGPT prompt; this is the same idea upgraded to "agent-as-code" — a shared,
version-controlled folder with specialist sub-agents, a house-style skill,
and a hard code-level guardrail instead of a polite instruction.

## Setup

```bash
cd startup-growth-harness
claude
```

Inside the Claude Code session, authenticate Canva (optional — the
`linkedin-creator` agent falls back to generating an SVG card if Canva isn't
connected, so the demo works either way):

```
/mcp
```
Select `canva` → Authenticate, and complete the browser login.

## Run it

Inside the session:

```
/weekly-campaign
```

This spawns three sub-agents in sequence (`trend-scout` →
`linkedin-creator` → `web-publisher`) and:
- drops a new post + visual into `drafts/`
- appends a new entry to `website/posts.js`
- logs a new row in `context/content_calendar.csv`

Just double-click `website/index.html` (or refresh it) to see the new card
appear on the feed — no local server needed. The data is loaded via
`<script src="posts.js">` rather than `fetch()`, specifically so this works
straight from the filesystem (`file://`) for non-technical students too.

## The guardrail demo

`website/index.html`, `context/brand_kit.md`, and `.claude/settings.json`
are hard-locked against edits **made by the agent** — a Python hook
(`.claude/hooks/guard_protected_files.py`) intercepts every `Edit`/`Write`
call and blocks these three paths with exit code 2, no matter how the agent
is asked.

Try it live:
```
Change the background color in website/index.html to bright red.
```
Watch it get blocked — including if you ask Claude to edit or disable
`settings.json` to get around it.

## Customizing for your own startup

The guardrail only blocks the **agent** — you're always free to hand-edit
any file yourself in your own editor. To adapt this harness to your startup:

1. Edit `context/brand_kit.md` directly (not through Claude) with your real
   pitch, ICP, and brand colors.
2. Add or tweak a sub-agent in `.claude/agents/` for your business (e.g. an
   Investor Scout, Competitor Tracker, or Customer Interview Analyzer).
3. Add a guardrail of your own in `.claude/settings.json` or
   `.claude/skills/brand-voice/SKILL.md`.
4. Run `/weekly-campaign` (or your own new slash command) and check
   `drafts/` and `website/posts.js` for the output.

## Folder map

| Path | Role |
|---|---|
| `CLAUDE.md` | The orchestrator / company handbook |
| `.claude/agents/` | Specialist sub-agents (trend-scout, linkedin-creator, web-publisher) |
| `.claude/skills/brand-voice/` | SOP / writing & visual style playbook |
| `.claude/settings.json` | Permissions + the guardrail hook wiring |
| `.claude/hooks/guard_protected_files.py` | The actual code-level guardrail |
| `.claude/commands/weekly-campaign.md` | The one slash command that runs the whole pipeline |
| `context/` | Brand kit + content calendar (the agent's shared memory) |
| `drafts/` | Generated LinkedIn posts + visual cards |
| `website/` | The "live" startup site the pipeline publishes to |
