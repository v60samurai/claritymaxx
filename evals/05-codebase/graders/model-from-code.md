---
type: llm
---

The repository is a small job queue backed by SQLite. Jobs move pending -> claimed -> done, or back to pending for a retry, or to dead.

PASS if the reply does all of these:
1. Describes the job lifecycle with the states pending, claimed, done, and dead.
2. Explains the visibility timeout: a claimed job becomes claimable again when its claim expires, which is how the queue recovers from a worker that died.
3. Explains retries: a failed job goes back to pending with a delay that grows with each attempt, and becomes dead after the maximum number of attempts.
4. Says that a job can run more than once (for example when a slow worker outlives its claim), or that handlers must be idempotent, or that delivery is at-least-once.
5. Names real files or functions from the repository (for example store.py, worker.py, backoff.py, claim, run_once).

FAIL if any of the five is missing.
FAIL if the reply only lists the files and what each contains without explaining how a job moves through them.
