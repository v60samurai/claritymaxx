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

The skill chose text or a small diagram when a richer page built for the subject would materially improve understanding.

Signs:

- The answer is very long and linear.
- The answer has several diagrams with no link between them.
- The subject has many interacting layers.
- The reader has to rebuild relationships across sections.
- A second view of the same system would help.
- The reader cannot follow how a failure spreads.
- The explanation is correct and costly to use.
- The skill rejected HTML because nothing needs input, because there is no control, or because Markdown can hold the same content.

Case: `15-html-complex-system`. `evals/pairwise.py` assigns this label when the skill chose text and the blind judge preferred the HTML answer in both orders.

### `medium_over_escalation`

The skill created HTML, a video, or another large artifact when a short text answer or one diagram would explain the subject as well.

Signs:

- HTML for a narrow concept.
- Animation that shows no change of state.
- Many controls with little explanatory value.
- Interaction added for novelty.
- The artifact took more effort than the question deserved.
- The skill escalated because the prompt was long.
- The skill ignored a length or format that the user named.

Cases: `01-simple-everyday`, `10-html-overkill`, `11-domain-expert`, `12-caveat-preserved`, `16-long-prompt-linear`. `evals/pairwise.py` assigns this label when the skill chose HTML and the blind judge preferred the text answer in both orders.

## Surface

The skill runs in chat on the web and in the desktop app, in Cowork, and in Claude Code. These surfaces differ in what they can create. A case with no `Write` in its `allowed_tools` stands in for a surface that cannot create a file.

| Label | The run |
|-------|---------|
| `false_artifact_claim` | Says that a file or a page was created when no tool call created it. |
| `structure_lost_on_fallback` | Could not create the page it chose, and gave a linear answer that drops the map, the second view, or the certainty labels. |

Case: `17-no-file-surface`.

## Writing

| Label | The run |
|-------|---------|
| `wrapper` | Opens with praise, or closes with a summary or an offer of help. |
| `dashes` | Contains an em dash or an en dash. |
| `unlabelled_example` | Shows an invented value next to real ones with no label. |
