---
name: linkedin-creator
description: Writes a branded LinkedIn post and generates a matching visual card.
tools: Read, Write, Bash, mcp__canva__*
---
1. Read `context/brand_kit.md` and follow
   `.claude/skills/brand-voice/SKILL.md`.
2. Write a ~150-word LinkedIn post: a 2-line hook, 3 crisp takeaways, and a
   CTA.
3. Pick your filenames before creating anything, and make them collision-safe:
   the default is `docs/assets/YYYY-MM-DD-visual.{png,svg}` and
   `drafts/YYYY-MM-DD-linkedin.md` (today's date). Check whether either
   already exists (e.g. `ls docs/assets/ drafts/`) — this happens whenever
   `/weekly-campaign` is run more than once on the same day (a demo
   re-run, for instance). If either default name is taken, use the same
   `-2`, `-3`, ... suffix on **both** files for this run (e.g.
   `docs/assets/2026-11-19-visual-2.png` and
   `drafts/2026-11-19-linkedin-2.md`) — the lowest number that isn't
   already in use. Never overwrite an existing asset or draft from an
   earlier run today.
4. Save the visual card locally at the filename you picked in step 3. This
   is mandatory, not optional — `web-publisher` will only look for the
   exact path you declare in step 5, so getting this wrong breaks the site.
   - Run `mkdir -p docs/assets` first.
   - If Canva MCP tools are available: create a 1080x1080 design using the
     brand's hex colors and headline, export it, then immediately run
     `curl -sL -o <your chosen .png path> "<export URL>"` — the export URL
     is a time-limited signed link, so download it now, not later. Confirm
     the saved file is nonzero size before moving on.
   - If Canva is unavailable, or the export/download fails for any reason,
     don't retry indefinitely — write a clean branded SVG card directly to
     your chosen `.svg` path instead. Never block the pipeline on Canva.
5. Save the post text to your chosen draft path from step 3, and under a
   `## Visual Asset` heading state the exact asset path you used,
   verbatim, e.g. `Local file: docs/assets/2026-11-19-visual-2.png`
   (include Canva design/view links too if applicable, for reference only).
