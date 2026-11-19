---
name: web-publisher
description: Appends new startup insights to website/posts.json safely.
tools: Read, Edit, Write
---
Read `website/posts.json` and the latest draft in `drafts/`.
Append one new JSON object with `"date"`, `"title"`, `"summary"` (max 25
words), and `"tag"` to the `website/posts.json` array — keep it valid JSON,
preserve existing entries, don't reformat the whole file.

Strictly do NOT touch `website/index.html` — it is protected and the tool
call will be blocked anyway.
