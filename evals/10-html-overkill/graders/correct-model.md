---
type: llm
---

PASS if the reply does both:
1. Defines an idempotent operation as one where doing it several times leaves the same result as doing it once.
2. Gives a concrete example of an idempotent operation and of one that is not (for example setting a value versus adding to it, or HTTP PUT versus POST).

FAIL if either is missing.
