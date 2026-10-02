# Failure categories

Use these labels when you review a run by hand, and when you write a grader for a new case. One run can carry more than one label.

## Model

| Label | The run |
|-------|---------|
| `wrong_model` | States a mechanism that the source or the subject does not support. |
| `summary_not_model` | Repeats what the source says and gives no relationships or reasons. |
| `lost_caveat` | Drops a condition or exception that changes what the reader would predict. |
| `false_certainty` | Presents an inference, an unknown, or a recommended design as an observed fact. |
| `wrong_level` | Teaches the basics to an expert, or skips them for a beginner. |

## Medium

### `medium_under_escalation`

The skill chose a representation that can express the answer, and that representation costs the reader much more effort than a richer one would. A correct answer can still carry this label.

Signs:

- Long prose explains a mechanism with many stages.
- The answer has several diagrams with no link between them, where one page would connect them.
- The reader has to work out each change of state from the prose.
- The reader has to compare a normal flow and a failure flow by hand.
- Following one object through the stages would be much easier to see than to read.
- The subject has many interacting layers, and the reader has to rebuild relationships across sections.
- The skill rejected HTML because nothing needs input, because there is no control, because Markdown can hold the same content, or because the prompt was short.

Cases: `15-html-complex-system`, `17-learn-mechanism`, `18-learn-mechanism-pipeline`, `22-agent-system`. `evals/pairwise.py` assigns this label when the skill chose text and the blind judge preferred the HTML answer in both orders.

### `medium_over_escalation`

The skill created a rich artifact when a simpler medium gives the same mental model with comparable clarity.

Signs:

- HTML for a definition or a narrow concept.
- A page for two paragraphs of content.
- Several views where one diagram is enough.
- A control that has no explanatory purpose.
- Animation that shows no change of state.
- The skill escalated because the prompt was long.
- The skill ignored a length or format that the user named.

Cases: `01-simple-everyday`, `10-html-overkill`, `11-domain-expert`, `12-caveat-preserved`, `16-long-prompt-linear`, `19-learn-concept`, `20-explicit-length`, `21-simple-definition`. `evals/pairwise.py` assigns this label when the skill chose HTML and the blind judge preferred the text answer in both orders.

## Surface

The skill runs in chat on the web and in the desktop app, in Cowork, and in Claude Code. These surfaces differ in what they can create. A case with no `Write` in its `allowed_tools` stands in for a surface that cannot create a file.

| Label | The run |
|-------|---------|
| `false_artifact_claim` | Says that a file or a page was created when no tool call created it. |
| `structure_lost_on_fallback` | Could not create the page it chose, and gave a linear answer that drops the map, the second view, or the certainty labels. |

Case: `evals-surface/01-no-file-tool`. It lives in its own suite because `--allow-tools Write` applies to every case in a run. Run it with `claude plugin eval . --eval-dir evals-surface` and no `Write` grant.

## Writing

| Label | The run |
|-------|---------|
| `wrapper` | Opens with praise, or closes with a summary or an offer of help. |
| `dashes` | Contains an em dash or an en dash. |
| `unlabelled_example` | Shows an invented value next to real ones with no label. |

## Review record

The graders check invariants. They do not read a page the way a reader does, so review medium choice by hand as well. For each run you review, record:

| Field | What to write |
|-------|---------------|
| Selected medium | Text, diagram, HTML, or video |
| Why it fits | The shape of the model that the medium serves |
| Better medium | Another medium that would have cost the reader less, or "none" |
| Mental-model clarity | Whether a reader could state the model after one pass |
| Factual fidelity | Any claim that the source or the subject does not support |
| Audience fit | Whether the level matches what the user showed they know |
| Preserved nuance | Any caveat, condition, or uncertainty that was lost |
| Cognitive load | What the reader still has to assemble alone |
| Labels | `medium_under_escalation`, `medium_over_escalation`, and any other label from this file |

For a page, open it. Check that the first screen gives the model, that the stages or parts relate clearly, that the reader can follow one object through the system, that each control helps, and that the page loads nothing from the network.
