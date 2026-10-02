# Diagrams

A diagram answers one question about how things relate. Write that question down before you draw. It becomes the diagram's title.

## Pick the job

| The hard part is | The question | A form that fits |
|------------------|--------------|------------------|
| Flow | What happens next? | Flowchart, one direction |
| Sequence | Who tells whom, in what order? | Sequence diagram with one lane for each actor |
| Dependency | What relies on what? | Directed graph. State what an arrow means. |
| Hierarchy | What contains what? | Tree or nested boxes |
| Lifecycle | How does this change over time? | Timeline or stages in a row |
| State | What changes when an event occurs? | State diagram with the event on each arrow |
| Architecture | Where does information move? | Boxes for components, labelled arrows for data |
| Comparison | How do two approaches differ? | Table with the same rows for both |
| Causality | What causes what? | Chain of causes with each link labelled |

If the question has two jobs, draw the one that is harder to say in words and write the other as a sentence.

## Rules

- Label every arrow with a verb or with the data that moves. An arrow with no label hides the relationship the diagram exists to show.
- Use the names from the source and from your prose. A box named `OrderService` in the code is `OrderService` in the diagram.
- Keep to about nine nodes. Group or drop the rest, and say what you dropped.
- Show certainty. Draw a relationship you inferred as a dashed line, mark an unknown with `?`, and add a one-line legend.
- Show the one path that matters when a system has many. Highlight it and fade the rest.
- Put two or three sentences after the diagram that tell the reader what to notice.
- One strong diagram is better than several weak ones.

## Render for the surface

- Terminal: draw with box characters, inline, at most 80 columns wide.
- A surface that renders Mermaid: use Mermaid.
- Too large for either, or the layout is spatial: write an SVG file, or go up one rung to HTML.

## Check

Read the finished diagram as a person who has not seen the source. The question in the title must be answerable from the diagram alone. If it is not, the diagram is decoration. Fix it or remove it.
