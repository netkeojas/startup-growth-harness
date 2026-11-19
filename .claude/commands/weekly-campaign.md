Run our weekly startup growth campaign:
1. Read `context/content_calendar.csv` to see which **topics/titles** are
   already covered — dedupe by subject matter, never by date. It's normal
   and expected for multiple rows to share the same date (e.g. this
   command being re-run more than once in a day, such as during a demo).
   Never skip, refuse, or short-circuit a run just because today's date
   already has an entry — only skip if the actual topic would be a
   near-duplicate of one already logged.
2. Spawn `trend-scout` to find 1 high-signal industry trend from the last 7
   days relevant to `context/brand_kit.md`, that is a genuinely different
   topic/angle from every title already in the calendar (compare by
   subject, not by date).
3. Spawn `linkedin-creator` to write the LinkedIn post and generate a visual
   card in `drafts/` (use Canva MCP tools if available; otherwise generate a
   branded SVG card).
4. Spawn `web-publisher` to append the new insight card to
   `docs/posts.js`.
5. Append today's date, the chosen topic, and status "Drafted" as a new row
   to `context/content_calendar.csv` — always add a new row, even if other
   rows already share today's date.
6. Report a short summary of what was created and where.
