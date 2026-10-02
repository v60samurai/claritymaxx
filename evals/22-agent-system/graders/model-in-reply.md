---
type: llm
---

The user described a production AI agent system with an orchestrator, a planner, a router, workers, three kinds of information, an incident in eleven steps, and several team disagreements. The user did not name a format.

PASS if the reply does all of these:
1. Tells the user that an HTML file or page was created and where it is.
2. States the core model in prose in the reply itself, organised around a small number of underlying ideas and not as a summary of each section of the prompt.
3. Says that "LLM hallucination" is the wrong or an incomplete diagnosis of the strategy incident, and names a cause in the design: two internal sources disagreed and nothing compared them, or the summary dropped the source, the time, and the disagreement, or the approver saw a diff with no provenance.

FAIL if any of the three is missing.
