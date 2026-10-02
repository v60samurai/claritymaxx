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

Karpathy orders the formats by richness. Claritymaxx adds one rule: pick the rung where the mental model is easiest to form, inspect, navigate, and remember, and go no higher. The ladder is an order of escalation for understanding. It is not an order of polish.

Cost has two sides. One side is the time to build the artifact and the number of things in it that can be wrong. The other side is the reader's effort to hold the model in their head. A long answer that makes the reader rebuild the structure is expensive, even though it was cheap to write.

Text is one rung with its own test. It is not the baseline that a richer medium must beat.

| Rung | It passes when |
|------|----------------|
| Text | The difficulty is a definition or one line of reasoning. A reader can hold the model in working memory after one read. |
| Diagram | One relationship is the main difficulty: sequence, hierarchy, dependency, cause, state, or flow. Prose would make the reader build the picture in their head. |
| HTML | The reader must see several connected pictures of one model, so spatial layout, linked views, or progressive disclosure reduces the reader's effort. The page can be mostly static. |
| Video | Motion itself carries the model, narration helps materially, a transformation over time is hard to show in still frames, or the user asked for a video. |

Start at text and stop at the first rung that passes. A subject that passes the HTML test does not also need a video.

### The shape of the difficulty

Two things decide the rung: how much there is, and what **shape** it has. Shape matters more. Name the shape of the model from step 2 of `SKILL.md`, then read the rung from this table.

| The difficulty is | The reader needs to | Usual rung |
|-------------------|---------------------|------------|
| A definition, a property, or one reason | Read it once | Text |
| One relationship: order, dependency, containment, cause, or state | See one picture | Text with one diagram |
| A transformation in stages: one input changes form several times before it becomes the output | Follow one example through every stage and see its form at each stage | HTML step-through. One diagram when the stages are few and the form changes little. |
| Several levels of abstraction | Move between the overview and the detail | HTML |
| Change over time: state, a feedback loop, or a procedure that repeats | See the state before and after each step | HTML step-through. Video only when still frames hide the motion. |
| Geometry or position | See where things are and how far apart | Diagram. HTML when the reader must vary an input to see the effect. |
| A system of interacting parts | See the map, then follow one request across it | HTML |
| Two paths over the same parts, such as a normal flow and a failure flow | Compare the paths on one layout | HTML |
| Competing views of one thing | Compare the views row by row | Table. HTML when each view needs its own picture. |

A model can have two shapes. Take the higher rung and use the lower rung inside it.

### Cues when the reader is learning

A reader in Learn mode has no picture to hang the words on, so prose that describes a mechanism makes this reader build the picture and understand it at the same time. When the user wants to know how something works, as opposed to what it is, find what the user cannot yet picture. Consider HTML strongly when several of these are true:

- The explanation follows one object as it changes representation.
- Each stage uses the output of the stage before, and there are more than about four stages.
- The mechanism has more than one level, and the reader must connect the levels.
- State changes over time, or a loop feeds a result back in.
- A cause in one stage has its effect several stages later.
- Position, distance, or geometry carries part of the idea.

A concept with one central relationship stays lower. An idea that turns on one triangle of cause, one comparison, or one sequence of a few messages gets text with one diagram.

### Cues when the subject is a system

Make one check first. Draw, in your head, one diagram of every path that the user asked about. If it has about nine nodes or fewer and every arrow fits, the rung is Diagram, and the cues below do not apply. Count only what the user asked about. A failure case or an open question that you noticed yourself gets a sentence under the diagram, and it is not a reason for a page.

When one diagram cannot hold it, consider HTML strongly when several of these are true:

- More than five important components interact, or more than one system layer matters.
- A normal flow and a failure flow both need explanation.
- Several levels of abstraction matter, and the reader must move between overview and detail.
- State transitions, chronology, or provenance carry part of the model.
- Trust boundaries or permission boundaries matter.
- More than one path reaches the same data or the same action.
- People hold competing mental models of the subject, or make competing claims about it, and the answer must compare them.
- The answer wants two or more diagrams, or two views of one system.
- The prose answer would be long, or the reader would have to connect sections that sit far apart.
- The explanation follows one request through the system, or shows one incident as it spreads through components.
- The subject is easier to hold as a map than as a list of sections.
- The reader is likely to come back to the explanation.

All of these cues are for judgement. Do not count them into a score. They describe the model you built in step 2 of `SKILL.md`. They do not describe the prompt. A long prompt about one linear idea stays on the text rung.

### Reasons that do not decide the rung

Each of these is true of many subjects that still belong on the HTML rung:

- Nothing needs user input.
- There is no control to operate.
- Markdown can technically hold the same information.
- The steps can be written as a numbered list.
- The prompt is short, or the subject has one name.
- The page would look better than the text.

Decide with one question: would a small page built for this subject make the model easier to form, inspect, navigate, or remember? If yes, build it.

### Calibration

| Subject | Usual rung |
|---------|------------|
| "Why does ice float?", "What is a hash map?", "What does idempotent mean?", embeddings in five minutes | Text |
| An OAuth login flow, a simple RAG pipeline, a request that moves through three services, what a confounder does to a correlation | Text with one diagram |
| A mechanism that a learner must watch work, in which one input changes form across many stages: a compiler from source text to machine code, a diffusion model from noise to image | HTML, strongly considered |
| A production architecture with many agents or services, a large codebase with several subsystems, an incident that spans services, a system with a normal flow, a failure flow, trust boundaries, state, and recovery, a paper that compares several mechanisms across stages, a business system with many dependent rules | HTML, strongly considered |

Two errors are equally bad:

- **Under-escalation.** The representation can express the answer, and it costs the reader much more effort than a richer one would. Examples: long prose for a mechanism with many stages, several unconnected diagrams in place of one page, prose that makes the reader work out each change of state, a normal flow and a failure flow that the reader must compare by hand. A correct answer can still fail here.
- **Over-escalation.** A rich artifact where a simpler medium gives the same model with comparable clarity. Examples: a page for a definition, a page for two paragraphs of content, a control or an animation that explains nothing, several views where one diagram is enough.

The examples in this file illustrate shapes. Decide from the shape of the model in front of you, not from a match with an example.

Rungs combine. An HTML page contains prose and diagrams. Pick the highest rung that is needed, then use the lower rungs inside it.

An explicit request for a medium, a length, or a format overrides these tests. "In five sentences" gets five sentences, however complex the subject is. If the requested medium fits badly, build it anyway and say in one sentence which medium would have been enough.

## Video

Video is an optional branch. Take it only when the video test above passes and a working toolchain is present. A subject that suits HTML is not a reason to make a video.

1. Write a storyboard from the mental model first: one row for each beat, with what is on screen, what moves, and what the viewer should conclude. Paragraphs turned into slides are a slideshow, and a slideshow belongs on the HTML rung.
2. Give every motion a job: show a transformation, a sequence, a state change, information moving, geometry, time, or a causal progression.
3. Inspect what is installed before you choose tools. Programmatic animation tools such as Manim, Remotion, or Motion Canvas, plus ffmpeg, are common. Use what is there, and install nothing without the user's agreement. If nothing is there, or the surface has no shell, say so and deliver the storyboard with an HTML step-through in its place.
4. Add narration only if it helps. Write narration and on-screen text to the writing rules and the edit pass in step 5 of `SKILL.md`. Prefer a local or free text-to-speech tool. Use a paid service only if the user asks for it and supplies the key through their environment. Read keys from the environment, and keep them out of files and commits.
5. Aim for the conceptual clarity of the best math explainers. Make the visual identity your own.
