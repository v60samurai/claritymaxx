---
name: explain
description: Use when the user wants to understand something rather than change it - "explain this", "what is X", "how does this work", "why does this happen", "what is going on here", "what caused this", "walk me through", "break this down", "teach me", "help me make sense of this", "what am I missing" - about a concept, code, a system, an architecture, a paper, data, logs, or a process. Builds a correct mental model first, then explains it in the cheapest medium that works (prose, a diagram, an interactive HTML page, or a video).
---

# Explain

Understand first, then explain. A clear explanation of a wrong **model** does more harm than a rough explanation of a right one, so the model comes before the wording.

The **model** is the small set of parts, relationships, and conditions that lets the user predict what the subject does. A summary repeats what the source says. An explanation hands over the model.

The steps below are how you work. The reply contains the explanation only.

## 1. Fix the question

Decide what the user wants to be able to do or predict afterwards. If two readings of the request would produce materially different explanations and the context does not settle it, ask one question. Otherwise continue.

## 2. Build the model

Read the source before you form a view: the files, logs, paper, data, or documents that the question depends on. Follow each reference that the answer rests on. With no source material, your own knowledge is the source and the same bar applies.

This step is complete when you can do all three:

- State the model in a few sentences.
- Name the **load-bearing** parts: the few concepts and relationships that carry most of the difficulty. Other facts you found stay out unless they change the model.
- Sort every load-bearing claim as **observed** (the source shows it), **inferred** (you reasoned to it), or **unknown** (the source does not settle it).

## 3. Read the reader

Infer what the user already knows from their vocabulary, what they say they understand, and how specific the question is. Weigh that evidence above the difficulty of the topic.

- **Learn**: the user has no working model yet. Build from first principles, one new concept at a time, each resting on the one before. Add a concrete example where the idea turns abstract.
- **Inspect**: the user knows the domain. Start at the part they asked about. Cover relationships, why each part exists, unusual decisions, contradictions, failure modes, trade-offs, and what is observed versus inferred.

## 4. Choose the medium

Use the **cheapest medium** that carries the model. Stop at the first rung that works.

| Rung | Use it when | Before you build |
|------|-------------|------------------|
| Text | The model is a short chain of ideas. | |
| Diagram | The hard part is how things relate: flow, sequence, dependency, hierarchy, state, or cause. | Read `references/visual-explanations.md` |
| HTML | The reader must explore: several connected concepts, levels of abstraction, a path to step through, or an input to change. | Read `references/html-explainers.md` |
| Video | The model is a change over time that a still frame hides, or the user asks for video. | Read the Video section of `references/karpathy-output-ladder.md` |

A medium that the user names wins. When two rungs both seem right, read `references/karpathy-output-ladder.md` for the test at each rung.

## 5. Write

Match the length to the question. "Why does ice float?" gets a few sentences. A question about one concept gets a few short paragraphs with no headings, about 250 words at most, even when the user asks for it to be "really clear". Stop when the model is complete. A second example or a list of related facts makes the answer longer and the model no clearer.

- Lead with the model in one or two sentences, then build it up.
- Put one idea in each sentence. Name the actor. State cause and effect with "because", "so", and "if".
- Use the correct technical term, define it at first use, and keep that same term to the end.
- Say "inferred" or "unknown" in the sentence that carries such a claim, and say what would settle it.
- Mark each invented example as illustrative.

For more than a few paragraphs of prose, or when the user asks for ASD-STE100 or stricter controlled language, read `references/ste-style.md`.

### Edit once before you send

The text must read as if a careful person wrote it after they understood the subject. Apply this pass to every word the user reads: the reply, diagram labels and captions, the text in an HTML page, and video narration.

- **Fidelity.** Every sentence states something the source or your model supports. Add no opinion, cause, emphasis, or confidence to make the text sound stronger.
- **Plain words.** Write "use", "help", "many", "is", and "has". Replace "leverage", "utilize", "facilitate", "robust", "seamless", "crucial", "pivotal", "delve", "unlock", "landscape", "serves as", and "features" with the plain word. Technical terms stay.
- **Mechanism over mood.** Name what the thing does, or give the number. Replace an adverb with the measurement or a stronger verb.
- **Whole sentences.** Keep articles and verbs. In prose, write "then" or "so" in place of an arrow. Arrows belong in diagrams.
- **Punctuation.** End the sentence or use a comma where a dash would go. Use no em dash and no en dash, including in ranges and compound terms: write "2014 to 2017" and "encoder-decoder". Use a colon only before a list or an example. Use straight quotes.
- **Structure.** Prefer paragraphs. Use a list, a table, or a heading only when it helps the reader compare, follow steps, or scan. Write headings in sentence case. Bold a term where you define it and nowhere else. Use no decorative emoji.
- **Natural counts.** Give as many items as there are. Do not round a list up or down to three. State a point directly, without "not just X but Y".
- **No wrapper.** Start with the answer and stop when the point is clear. Leave out praise for the question, a closing summary, and an offer of more help.

## 6. Check the simplification

Compare the explanation with the model from step 2. Each load-bearing condition, dependency, caveat, distinction, uncertainty, and causal link is either present or was left out because it does not change what the user will predict. Restore anything that fails this test. Precision wins over simplicity: write the precise statement, then explain it.

## Gotchas

- **Wording before model.** You are polishing sentences and cannot yet state the model. Return to step 2.
- **Summary in place of explanation.** The draft lists what the source contains. Add why each part exists and what follows from it.
- **Parts without relationships.** Each component is described alone. The model lives in how the components connect, so explain the connections.
- **Everything you found.** The draft includes facts because they were discovered. Keep the load-bearing ones.
- **Certainty the source does not support.** An inferred or unknown claim reads like an observed one. Label it.
- **A term bent to sound simple.** "An embedding is a summary" is easier and wrong. Keep the true meaning and define the term.
- **A lost caveat.** The plain version dropped a condition, an edge case, or an exception that changes the prediction. Put it back.
- **A beginner answer for an expert.** The user showed domain knowledge and the draft teaches the basics. Switch to Inspect.
- **An invented example that looks real.** A made-up request, log line, or number sits next to real ones without a label. Label it.
- **Prose where a diagram fits.** Three paragraphs describe who calls whom. Draw it.
- **An artifact where prose fits.** Two paragraphs would answer the question. Write them.
- **A richer medium because it is available.** Each rung up needs a reason that comes from the model.
- **A handsome artifact that teaches nothing.** Every element and every interaction answers a question the reader has. Remove the rest.
- **A compliance claim.** The prose is inspired by ASD-STE100. Call it compliant only after a check against the standard that the user asked for.
- **"80% STE" as a score.** The phrase names a style direction and measures nothing.
