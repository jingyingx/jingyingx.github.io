# Academic design preview

Isolated branch: `codex/academic-design-preview`. No publication or commit is needed.

Start from this worktree:

```sh
python3 scripts/preview.py --port 4000
```

Open http://127.0.0.1:4000. Stop the server with Ctrl-C.

The preview uses the actual HTML content and shared Jekyll layout/CSS. It substitutes the layout's title, description, and content fields without requiring the remote theme or Ruby dependencies. GitHub Pages can still render these pages through Jekyll; a full Jekyll build has not been run locally.

Review Home, Research, Publications, and Teaching & Mentoring at desktop width and at 390px / 375px mobile width. Check expandable project descriptions and presentations, publication topic links, CV downloads, and email links.

All original publication entries and presentation records are retained. Full project prose is in expandable sections; papers also appear chronologically on Publications. No defense date or teaching philosophy was invented. Add an exact defense date and a personally approved teaching statement/classroom example when available.

Validation: all 29 original research records were retained; local links and assets checked; desktop (1280px) and mobile (390px / 375px) inspected; disclosures and publication deep links tested.
