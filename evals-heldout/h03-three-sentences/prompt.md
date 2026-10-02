---
tags: [heldout, expect-text, no-pairwise]
max_turns: 12
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

In three sentences: how does Kubernetes get a pod from `kubectl apply` to a running container, across the API server, etcd, the scheduler, the kubelet, and the container runtime?
