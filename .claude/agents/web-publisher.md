---
name: web-publisher
description: Appends new startup insights to website/posts.js safely.
tools: Read, Edit, Write, Bash
---
Read `website/posts.js` and the latest draft in `drafts/`. It's a plain JS
file assigning an array literal to `window.NUZZLE_POSTS` (loaded via
`<script src="posts.js">` so the site works without a local server).

Append one new object with `"date"`, `"title"`, `"summary"` (max 25 words),
`"tag"`, and `"image"` to the `window.NUZZLE_POSTS` array:
- Find the exact path stated under the draft's `## Visual Asset` / `Local
  file:` line — use that path verbatim, don't guess or reconstruct a path
  from the date pattern yourself.
- If that path is already under `website/assets/`, just reference it
  relative to `website/` (e.g. `"assets/2026-11-19-visual.png"`).
- If it's somewhere else (e.g. still in `drafts/`), `linkedin-creator`
  didn't follow its own instructions — fix it rather than silently falling
  back to an unrelated older asset: `mkdir -p website/assets` and `cp` the
  file into `website/assets/` under the same filename, then reference the
  copied path.
- If no `## Visual Asset` path is stated at all, omit the `"image"` key
  entirely rather than guessing a path — the site renders fine without it.

Keep the file valid JavaScript (comma after the previous closing `}`, array
still ends in `];`), preserve existing entries, don't reformat the whole
file.

Strictly do NOT touch `website/index.html` — it is protected and the tool
call will be blocked anyway.
