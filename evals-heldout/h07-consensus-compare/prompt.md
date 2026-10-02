---
tags: [heldout, expect-html]
max_turns: 20
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

I am implementing a replicated log and I will keep coming back to this while I build it. Compare Multi-Paxos, Raft, and Viewstamped Replication across four stages: choosing a leader, replicating an entry, deciding that an entry is committed, and changing the cluster membership. For each stage I want to see what the three do the same, what they do differently, and which safety rule each one relies on.
