---
type: llm
---

PASS if the reply says all of these:
1. A hash map stores values by key.
2. A hash function turns the key into a position in an array, so a lookup goes to that position without a search through every item.
3. Two keys can land on the same position (a collision), and the map has a way to handle that.

FAIL if any of the three is missing.
