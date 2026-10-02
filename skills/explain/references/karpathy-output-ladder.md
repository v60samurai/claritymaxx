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

Karpathy orders the formats by richness. Claritymaxx adds one rule: climb only as far as the mental model needs. The **cheapest medium** is the lowest rung that still carries the model. Cost includes the reader's time, the time to build the artifact, and the number of things in it that can be wrong.

Ask these tests in order. Stop at the first rung that passes.

| Rung | It passes when |
|------|----------------|
| Text | The model is a short chain of ideas. A reader can hold it after one read. |
| Diagram | The hard part is how things relate: flow, sequence, dependency, hierarchy, state, cause, or position. Prose would make the reader build the picture in their head. |
| HTML | The reader must explore: several connected concepts, more than one level of abstraction, a path to step through, or a value to change and watch. A static page would be long or would force scrolling back and forth. |
| Video | The model is a change over time that a static frame hides: a transformation, moving information, geometry, or a causal progression. Or the user asked for a video. |

Two errors are equally bad. One is an artifact for a question that two paragraphs answer. The other is a wall of prose for a model that one small diagram shows.

Rungs combine. The usual good answer for a hard topic is one diagram plus a few sentences. An HTML page contains prose and diagrams. Pick the highest rung that is needed, then use the lower rungs inside it.

An explicit request for a medium overrides these tests. If the requested medium fits badly, build it anyway and say in one sentence which medium would have been enough.

## Video

Video is an optional branch. Take it only when the test above passes and a working toolchain is present.

1. Write a storyboard from the mental model first: one row for each beat, with what is on screen, what moves, and what the viewer should conclude. Paragraphs turned into slides are a slideshow, and a slideshow belongs on the HTML rung.
2. Give every motion a job: show a transformation, a sequence, a state change, information moving, geometry, time, or a causal progression.
3. Inspect what is installed before you choose tools. Programmatic animation tools such as Manim, Remotion, or Motion Canvas, plus ffmpeg, are common. Use what is there. If nothing is, say so and deliver the storyboard with an HTML step-through in its place.
4. Add narration only if it helps. Write narration and on-screen text to the writing rules and the edit pass in step 5 of `SKILL.md`. Prefer a local or free text-to-speech tool. Use a paid service only if the user asks for it and supplies the key through their environment. Read keys from the environment, and keep them out of files and commits.
5. Aim for the conceptual clarity of the best math explainers. Make the visual identity your own.
