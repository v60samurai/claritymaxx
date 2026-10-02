# HTML explainers

An HTML explainer is an interface to a mental model. The reader uses it to explore the model. A report with styling is still a report, and a report belongs on the text rung.

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

Every interaction must teach something. If you remove a control and the reader loses nothing, remove it. The page must be less complex than its subject.

## Build

- One self-contained file: inline CSS and JavaScript, inline SVG for diagrams, no network requests, no build step. The file must open from disk.
- Put the model in the first screen: one sentence and the overview diagram. A reader who stops there still leaves with the right idea.
- Use the prose rules from `ste-style.md` for all text on the page.
- Use motion only to show a change of state or the movement of information.
- Make it readable at phone width and in light and dark themes. Make every control reachable from the keyboard.

## Ground it

- Build from the real code, logs, data, and documents when they exist. Use real names, real values, and real paths.
- Label every invented value where the reader sees it, for example "Illustrative example". An invented request that looks like a log line will be read as an observation.
- Show certainty the same way the prose does: mark inferred relationships and unknowns in the page itself.

## Deliver

Save the file in the current working directory under a descriptive name, unless the user names another place. Give the path. If the directory is a git repository, say that the file is new and untracked. Open it in the browser if a tool for that is available. In the reply, state the model in two or three sentences so the reader has the answer before they open the page.

## Check

Open the file, or read it top to bottom if you cannot render it. Every control works. Every claim on the page appears in the model you built. Nothing on the page is there only because HTML made it possible.
