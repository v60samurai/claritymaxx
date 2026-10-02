---
tags: [expert, inspect]
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill]
---

I run Postgres in production and I'm comfortable with MVCC, xmin/xmax and how vacuum works. What I don't get: why does one long-running transaction cause bloat in tables it never touched?
