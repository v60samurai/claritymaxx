# HTML explainers

An HTML explainer is an interface to a mental model. It earns its place through structure: spatial layout, linked views, and detail on demand. Controls are optional, and a page can be mostly static. A report with styling is still a report, and a report belongs on the text rung.

## Start from the model

List the parts and relationships that carry the model. Each one gets a place on the page. Then decide what the reader does:

| The reader needs to | Technique |
|---------------------|-----------|
| See the whole before the parts | Overview first, detail on demand |
| Follow one request, record, or event | Step-through with next and back, one path highlighted |
| Know what a term means without leaving the page | Definition on hover or tap |
| Move between "what it does" and "how it does it" | Toggle for the level of abstraction |
| Compare two designs or two moments | Before and after, side by side, same layout |
| See how an output depends on an input | A control that changes the input and redraws the result |
| Place events in time | Timeline |
| Find where a part sits in a system | Clickable architecture map |
| See a normal flow and a failure flow in one system | Two views on the same map, with the path that differs highlighted |
| See where a failure started and how it spread | The path through the components, with the step that lost or changed information marked |
| Compare competing views of one thing | A table with the same rows for each view, and what each view gets right |

Choose the smallest set of views that carries the model. Every view, element, and control must teach something. If you remove one and the reader loses nothing, remove it. The page must be less complex than its subject.

## Build

- One self-contained file: inline CSS and JavaScript, inline SVG for diagrams, no network requests, no build step. The file must open from disk.
- Put the model in the first screen: one sentence and the overview diagram. A reader who stops there still leaves with the right idea.
- All text on the page follows the writing rules and the edit pass in step 5 of `SKILL.md`. That includes headings, labels, button text, and captions.
- Use motion only to show a change of state or the movement of information.
- Make it readable at phone width and in light and dark themes. Make every control reachable from the keyboard.

## Ground it

- Build from the real code, logs, data, and documents when they exist. Use real names, real values, and real paths.
- Label every invented value where the reader sees it, for example "Illustrative example". An invented request that looks like a log line will be read as an observation.
- Show certainty the same way the prose does: mark inferred relationships and unknowns in the page itself.
- Where a design you recommend sits next to a fact from the source, mark each one with a small visible label, for example "From the source", "Inferred", and "Recommended". Use the same labels across the whole page and explain them once.

## Deliver

Save the file in the current working directory under a descriptive name, unless the user names another place. Give the path. If the directory is a git repository, say that the file is new and untracked. Open it in the browser if a tool for that is available. In the reply, state the model in two or three sentences so the reader has the answer before they open the page.

## Check

Open the file, or read it top to bottom if you cannot render it. Every control works. Each view answers a question the reader has. Every claim on the page appears in the model you built. Nothing on the page is there only because HTML made it possible.
