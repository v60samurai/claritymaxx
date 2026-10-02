# HTML explainers

An HTML explainer is an interface to a mental model. It earns its place through structure: spatial layout, linked views, and detail on demand. Controls are optional, and a page can be mostly static. A report with styling is still a report, and a report belongs on the text rung.

## Start from the model

List the parts and relationships that carry the model. Each one gets a place on the page. Then decide what the reader does:

| The reader needs to | Technique |
|---------------------|-----------|
| See the whole before the parts | Overview first, detail on demand |
| Follow one request, record, or event | Step-through with next and back, one path highlighted |
| See how one input changes form across stages | A row of stages with one example carried through. Each stage shows the form of the example at that stage and what changed. |
| Know where a claim came from | A provenance trail: the claim, its source, its time, and each step that changed it |
| See what each boundary permits | The map with the trust zones drawn, and what crosses each line |
| Know what a term means without leaving the page | Definition on hover or tap |
| Move between "what it does" and "how it does it" | Toggle for the level of abstraction |
| Compare two designs or two moments | Before and after, side by side, same layout |
| See how an output depends on an input | A control that changes the input and redraws the result |
| Place events in time | Timeline |
| Find where a part sits in a system | Clickable architecture map |
| See a normal flow and a failure flow in one system | Two views on the same map, with the path that differs highlighted |
| See where a failure started and how it spread | The path through the components, with the step that lost or changed information marked |
| Compare competing views of one thing | A table with the same rows for each view, and what each view gets right |

Choose the smallest set of views that carries the model. Every view, element, and control must teach something. If you remove one and the reader loses nothing, remove it. The page must be less complex than its subject. Cards, metrics, panels, and animation that answer no question from the reader are decoration, so remove them.

## Build

- One self-contained file: inline CSS, inline SVG for diagrams, and a small amount of inline JavaScript only where a control needs it. Use no external library, font, image, or stylesheet, no network request, no package install, and no build step or local server. The file must work when it is opened from disk with no connection.
- Put the model in the first screen: one sentence and the overview diagram. A reader who stops there still leaves with the right idea.
- All text on the page follows the writing rules and the edit pass in step 5 of `SKILL.md`. That includes headings, labels, button text, and captions.
- Use motion only to show a change of state or the movement of information.
- Make it readable at phone width and in light and dark themes. The page itself must never scroll sideways: let rows of links, buttons, and cards wrap, and put a wide diagram or table in its own container that scrolls. Make every control reachable from the keyboard.

## Ground it

- Build from the real code, logs, data, and documents when they exist. Use real names, real values, and real paths.
- Label every invented value where the reader sees it, for example "Illustrative example". An invented request that looks like a log line will be read as an observation.
- Show certainty the same way the prose does: mark inferred relationships and unknowns in the page itself.
- Where a design you recommend sits next to a fact from the source, mark each one with a small visible label, for example "From the source", "Inferred", and "Recommended". Use the same labels across the whole page and explain them once.

## Deliver

Deliver the page with what this surface can do. Use the first case that applies:

- **The surface shows a page next to the conversation.** Create the page there.
- **You have a working directory.** Save the file there under a descriptive name, unless the user names another place. Give the path. If the directory is a git repository, say that the file is new and untracked. Open it in the browser if a tool for that is available.
- **You can create files and have no working directory.** Create the file and give it to the user as a download.
- **You cannot create a file.** Put the same structure in the reply: the overview diagram first, then one short section for each view the page would have, with a table where the page would compare. Keep the certainty labels. Say in one sentence that a page would hold this structure better and that this surface could not create one.

Say that a file or a page exists only after the tool call that created it succeeded. If that call failed, use the last case.

In the reply, state the model in two or three sentences so the reader has the answer before they open the page.

## Check

Open the page, or read it top to bottom if you cannot render it. Every control works. Each view answers a question the reader has. Every claim on the page appears in the model you built. Nothing on the page is there only because HTML made it possible.
