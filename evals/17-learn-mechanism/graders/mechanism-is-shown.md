---
type: llm
---

The user is a beginner who asked what happens inside a transformer from text in to next token out.

PASS if the reply does one of these:
(a) Says that a page or a file was created, and also states the mechanism in a few sentences in the reply itself.
(b) Contains a diagram, drawn in text characters or in Mermaid, that shows the stages in order and what passes from each stage to the next.

FAIL if the reply is prose or a numbered list with no diagram and no page. That is `medium_under_escalation`: the reader has to build the picture of the mechanism from words.
