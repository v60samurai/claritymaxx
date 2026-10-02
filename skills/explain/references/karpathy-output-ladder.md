# The output ladder

The source is a public note by Andrej Karpathy about understanding the outputs of language models. This file paraphrases the note, then gives the tests Claritymaxx uses to pick a rung. The tests are Claritymaxx's, not Karpathy's.

## The idea

Language models keep getting better, so they do more of the legwork on their own. More human work then moves up the abstractions, into oversight and understanding. Models can help with that work too. Intelligence and code are now abundant, so you can ask for a large, custom, discardable software artifact to answer one question. A web app or an explainer video built for one reader would not have been worth making before.

Karpathy lists four output formats. He introduces each one after the first as "even better" for hard material.

1. **Writing.** Ask for the explanation in ASD-STE100, a controlled language first written for aerospace maintenance documents. Its constraints produce clean, readable prose. The full specification is strict, so he sometimes asks for "80% of the way to ASD-STE100".
2. **Diagrams and images.** Ask for a diagram instead of writing. A diagram can be much easier to process, parse, and understand.
3. **Web pages.** Ask for the output "in HTML" to get an interactive page. Models are now good at frontend work.
4. **Explainer videos.** The format he is most bullish on: a bespoke video on any topic, for example in the teaching style of 3Blue1Brown, with narration from a text-to-speech service or from a free tool that runs on local compute.

His closing advice is to push the boundaries, because the results are surprising.

## How Claritymaxx uses the ladder

Karpathy orders the formats by richness. Claritymaxx adds one rule: pick the rung where the mental model is easiest to form, inspect, navigate, and remember. The **cheapest medium** is the lowest rung that does that well. Cost has two sides. One side is the time to build the artifact and the number of things in it that can be wrong. The other side is the reader's effort to hold the model in their head. A long answer that makes the reader rebuild the structure is expensive, even though it was cheap to write.

Markdown is one rung. It is not the baseline that a richer medium must beat by offering controls.

| Rung | It passes when |
|------|----------------|
| Text | One linear path is enough. A reader can hold the model in working memory after one read. |
| Diagram | One or two relationships are the main difficulty: sequence, hierarchy, dependency, cause, state, or architecture. Prose would make the reader build the picture in their head. |
| HTML | The subject has enough interacting structure that spatial layout, several linked views, or progressive disclosure reduces the reader's effort. The page can be mostly static. |
| Video | Motion itself carries the model, narration helps materially, a transformation over time is hard to show in still frames, or the user asked for a video. |

Start at text and stop at the first rung that passes. A subject that passes the HTML test does not also need a video.

### Cues for the HTML rung

These are cues for judgement. Do not count them into a score. Consider HTML strongly when several are true:

- More than five important components interact, or more than one system layer matters.
- A normal flow and a failure flow both need explanation.
- Several levels of abstraction matter, and the reader must move between overview and detail.
- State transitions, chronology, or provenance carry part of the model.
- Trust boundaries or security boundaries matter.
- People hold competing mental models of the subject, and the answer must compare them.
- The answer wants two or more diagrams, or two views of one system.
- The prose answer would be long, or the reader would have to connect sections that sit far apart.
- The explanation follows one item through the system, or shows a failure as it spreads through components.
- The reader is likely to come back to the explanation.

The cues describe the model you built in step 2 of `SKILL.md`. They do not describe the prompt. A long prompt about one linear idea stays on the text rung.

### Reasons that do not decide the rung

Each of these is true of many subjects that still belong on the HTML rung:

- Nothing needs user input.
- There is no control to operate.
- Markdown can technically hold the same information.
- The page would look better than the text.

Decide with one question: would a small page built for this subject make the model easier to form, inspect, navigate, or remember? If yes, build it.

### Calibration

| Subject | Usual rung |
|---------|------------|
| "Why does ice float?", "What is a hash map?", "What does idempotent mean?", embeddings in five minutes | Text |
| An OAuth login flow, a simple RAG pipeline, a request that moves through three services | Text with one diagram |
| A production architecture with many agents or services, a large codebase with several subsystems, an incident that spans services, a system with a normal flow, a failure flow, trust boundaries, state, and recovery, a paper that compares several mechanisms across stages, a business system with many dependent rules | HTML, strongly considered |

Two errors are equally bad:

- **Under-escalation.** Text or a small diagram for a model that a page would make much easier to use. The answer is correct and costly to use: very long, with several unconnected diagrams, and the reader has to rebuild the relationships.
- **Over-escalation.** A page or a video where a short answer or one diagram explains the subject as well. The artifact took more effort than the question deserved.

Rungs combine. An HTML page contains prose and diagrams. Pick the highest rung that is needed, then use the lower rungs inside it.

An explicit request for a medium, a length, or a format overrides these tests. "In five sentences" gets five sentences, however complex the subject is. If the requested medium fits badly, build it anyway and say in one sentence which medium would have been enough.

## Video

Video is an optional branch. Take it only when the video test above passes and a working toolchain is present. A subject that suits HTML is not a reason to make a video.

1. Write a storyboard from the mental model first: one row for each beat, with what is on screen, what moves, and what the viewer should conclude. Paragraphs turned into slides are a slideshow, and a slideshow belongs on the HTML rung.
2. Give every motion a job: show a transformation, a sequence, a state change, information moving, geometry, time, or a causal progression.
3. Inspect what is installed before you choose tools. Programmatic animation tools such as Manim, Remotion, or Motion Canvas, plus ffmpeg, are common. Use what is there, and install nothing without the user's agreement. If nothing is there, or the surface has no shell, say so and deliver the storyboard with an HTML step-through in its place.
4. Add narration only if it helps. Write narration and on-screen text to the writing rules and the edit pass in step 5 of `SKILL.md`. Prefer a local or free text-to-speech tool. Use a paid service only if the user asks for it and supplies the key through their environment. Read keys from the environment, and keep them out of files and commits.
5. Aim for the conceptual clarity of the best math explainers. Make the visual identity your own.
