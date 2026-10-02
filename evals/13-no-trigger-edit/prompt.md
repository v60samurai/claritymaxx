---
tags: [trigger, negative]
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill]
---

Rename the variable `tmp` to `retry_count` in this function and give me back the updated code.

```python
def bump(state):
    tmp = state.get("retries", 0)
    tmp += 1
    state["retries"] = tmp
    return state
```
