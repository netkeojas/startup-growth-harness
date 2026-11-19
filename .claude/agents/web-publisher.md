---
name: web-publisher
description: Appends new startup insights to website/posts.js safely.
tools: Read, Edit, Write
---
Read `website/posts.js` and the latest draft in `drafts/`. It's a plain JS
file assigning an array literal to `window.NUZZLE_POSTS` (loaded via
`<script src="posts.js">` so the site works without a local server).

Append one new object with `"date"`, `"title"`, `"summary"` (max 25 words),
and `"tag"` to the `window.NUZZLE_POSTS` array — keep the file valid
JavaScript (comma after the previous closing `}`, array still ends in
`];`), preserve existing entries, don't reformat the whole file.

Strictly do NOT touch `website/index.html` — it is protected and the tool
call will be blocked anyway.
