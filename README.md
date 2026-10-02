<p align="center">
  <img src="assets/claritymaxx-banner.svg" alt="Claritymaxx. Understand difficult things." width="100%">
</p>

# Claritymaxx

Understand difficult things.

Claritymaxx is a Claude Code plugin with skills for understanding hard material: code, systems, papers, data, logs, and processes. Models now do more of the implementation work. More of your work is to inspect what they did, judge it, and decide what matters. Claritymaxx helps with that part.

It has one skill today: `explain`.

## Inspiration

Claritymaxx started from [a post by Andrej Karpathy](https://x.com/karpathy/status/2105819303471976479) about understanding the outputs of language models. His observation: as models do more of the implementation work on their own, more human work moves up into oversight and understanding.

He described a progression of output formats for that work:

- **Clear writing.** Ask for prose in the style of ASD-STE100, a controlled language from aerospace maintenance. The full standard is strict, so he suggests a softer target, "80% of the way to ASD-STE100".
- **Diagrams and images**, when structure is easier to see than to read.
- **Interactive HTML pages**, when exploring helps.
- **Bespoke explainer videos**, the format he is most optimistic about.

The larger idea is that intelligence and code are getting cheap. A custom, disposable artifact made to answer one question was too expensive to build before. Now it is a reasonable thing to ask for.

Both the ladder of output formats and the ASD-STE100 writing style in this project come from that post. Claritymaxx is our implementation and extension of the idea: a reusable skill that builds the mental model first, then chooses the simplest medium that explains the topic well. Karpathy is not involved in this project and has not reviewed or endorsed it.

## What `explain` does

`explain` builds a mental model of the subject before it writes a word of explanation. It reads the source, finds the few parts and relationships that carry most of the difficulty, and separates what the source shows from what it inferred. Then it presents that model in the cheapest medium that works.

```text
> why does this service read from both the cache and the database?
```

`explain` reads the code first. Then it answers the question you asked: which reads go where, why two sources exist, and where they can disagree. It says which parts of that answer it saw in the code and which parts it inferred. If the hard part is the flow of requests, you get a small diagram and a few sentences in place of a page of prose.

It adapts to the reader without a mode switch:

- **Learn.** You have no working model yet. It builds one from first principles, one concept at a time.
- **Inspect.** You know the domain. It skips the basics and goes to relationships, odd decisions, failure modes, and what is known versus inferred.

## Install

In Claude Code:

```text
/plugin marketplace add v60samurai/claritymaxx
/plugin install claritymaxx@claritymaxx
```

Or from a shell:

```bash
claude plugin marketplace add v60samurai/claritymaxx
claude plugin install claritymaxx@claritymaxx
```

Start a new session, or run `/reload-plugins`. To try it without installing, clone the repository and run `claude --plugin-dir ./claritymaxx`.

## Use

Ask in your own words. The skill loads when you want to understand something:

```text
explain how this repo handles retries
what is an embedding?
walk me through the OAuth PKCE flow
I know MVCC. Why does one long transaction bloat tables it never touched?
```

Or call it by name: `/claritymaxx:explain <what you want to understand>`.

## The ladder

```text
text  →  diagram  →  interactive HTML  →  video (optional)
```

This ladder is Karpathy's progression of output formats (see [Inspiration](#inspiration)). He presents each format as better than the one before for hard material. Claritymaxx adds one rule of its own: it climbs only as far as the mental model needs. The conditions in the table below are ours.

| Medium | Chosen when |
|--------|-------------|
| Text | The model is a short chain of ideas. |
| Diagram | The hard part is how things relate: flow, sequence, dependency, state, cause. |
| Interactive HTML | You need to explore: several connected concepts, levels of abstraction, a path to step through, an input to change. |
| Video | The model is a change over time that a still frame hides, or you ask for one. No paid service is required. |

"Why does ice float?" gets a few sentences. A request to play with consistent hashing gets a small page with a ring you can add nodes to. If you name a medium, you get that medium.

## Writing style

The prose is inspired by [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/), a controlled language written for aerospace maintenance documents: familiar words, short sentences, one term for one thing, explicit cause and effect. Using it for explanations is Karpathy's suggestion, and so is the target: "80% of the way to ASD-STE100".

That phrase names a style. It is not a score. Claritymaxx does not check text against the standard and does not claim that its output complies with ASD-STE100. Correct technical terms stay, and when precision and simplicity conflict, precision wins.

## What is in the repository

```text
.claude-plugin/        plugin and marketplace manifests
skills/explain/        SKILL.md, four reference files, one reference image
evals/                 14 eval cases for `claude plugin eval`
```

`SKILL.md` is short. The reference files for diagrams, HTML explainers, the ladder, and the writing style load only when a request needs them.

Run the evals from a clone:

```bash
claude plugin eval . --scaffold --allow-tools Write
```

`--scaffold` lets one case create a small fixture repository, and `--allow-tools Write` lets one case write an HTML file. The cases check invariants such as factual fidelity, medium choice, kept caveats, and stated uncertainty. They do not check wording.

## Later

More focused skills for understanding may follow, for example for codebases, systems, research, and data. They will be added when real use shows a need.

## License

[MIT](LICENSE)
