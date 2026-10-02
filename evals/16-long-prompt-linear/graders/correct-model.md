---
type: llm
---

The prompt is long, and the question is one linear concept.

PASS if the reply does both:
1. Explains that a float holds a fixed number of significant bits, so each addition rounds its result, and the rounding error depends on the sizes of the two numbers that are added.
2. Concludes that a different order produces different intermediate sums, so different rounding, so floating-point addition is not associative. The result is deterministic for a given order. It is not random.

FAIL if either is missing.
FAIL if the reply explains the user's architecture, Kafka, or the warehouses.
