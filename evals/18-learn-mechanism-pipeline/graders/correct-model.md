---
type: llm
---

PASS if the reply, in any wording, is consistent with all of these and contradicts none:
1. The browser parses HTML into a tree of elements (the DOM) and CSS into style rules.
2. It combines the two to work out which style applies to each element, then computes the size and position of each element (layout).
3. It paints the elements into pixels, often in layers that are then composited.
4. JavaScript can change the DOM or the styles, which makes the browser repeat some of the later stages.

The reply may cover some of these only in a page it created. Do not fail it for brevity.
FAIL if the reply contradicts any of the four.
