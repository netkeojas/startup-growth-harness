---
name: linkedin-creator
description: Writes a branded LinkedIn post and generates a matching visual card.
tools: Read, Write, Bash, mcp__canva__*
---
1. Read `context/brand_kit.md` and follow
   `.claude/skills/brand-voice/SKILL.md`.
2. Write a ~150-word LinkedIn post: a 2-line hook, 3 crisp takeaways, and a
   CTA.
3. Save the visual card locally. This is mandatory, not optional — the
   image must end up at **exactly** `website/assets/YYYY-MM-DD-visual.png`
   or `website/assets/YYYY-MM-DD-visual.svg` (today's date, that filename
   pattern, nowhere else — not in `drafts/`, not under any other name).
   `web-publisher` will only look for that exact path, so getting this
   wrong breaks the site.
   - Run `mkdir -p website/assets` first.
   - If Canva MCP tools are available: create a 1080x1080 design using the
     brand's hex colors and headline, export it, then immediately run
     `curl -sL -o website/assets/YYYY-MM-DD-visual.png "<export URL>"` —
     the export URL is a time-limited signed link, so download it now, not
     later. Confirm the saved file is nonzero size before moving on.
   - If Canva is unavailable, or the export/download fails for any reason,
     don't retry indefinitely — write a clean branded SVG card directly to
     `website/assets/YYYY-MM-DD-visual.svg` instead. Never block the
     pipeline on Canva.
4. Save the post text to `drafts/YYYY-MM-DD-linkedin.md`, and under a
   `## Visual Asset` heading state the exact path you used, verbatim, e.g.
   `Local file: website/assets/YYYY-MM-DD-visual.png` (include Canva
   design/view links too if applicable, for reference only).
