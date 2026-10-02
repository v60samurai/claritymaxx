# Held-out cases

These cases test medium choice on prompts that were not used to write or tune the skill. They exist to catch overfitting: a change that improves the cases in `evals/` and does not improve these has learned the cases, not the behaviour.

## Rules

- Do not read these prompts, their transcripts, or their results while you edit anything in `skills/`. Run them only after an edit is finished, and read only the scores.
- Do not copy text from a held-out prompt or from a failing answer into the skill.
- When a held-out case has been read during an edit, it is no longer held out. Move it to `evals/` and write a replacement.

## The cases

A person judged the expected rung for each case before any run. The tag `expect-any` marks a case with no expected rung. Only the pairwise judge scores that one.

| Case | Expected | Why a person would choose that rung |
|------|----------|-------------------------------------|
| `h01-backpressure` | Text | One concept, one causal chain. |
| `h02-quic-hol` | Text | The reader is an expert and the answer is one contrast. |
| `h03-three-sentences` | Text | The subject has many parts, and the user set the length. Tagged `no-pairwise`, because a forced medium would contradict the prompt. |
| `h04-tls-handshake` | Diagram | One sequence between two parties. |
| `h05-git-rebase` | Diagram | One before and after picture of a commit graph. |
| `h06-pod-lifecycle` | Any | About six components and one failure path. It sits between the diagram rung and the HTML rung. |
| `h07-consensus-compare` | HTML | Three mechanisms across four stages, and the reader will come back to it. |
| `h08-lab-incident` | HTML | Ten components, two trust zones, two disagreements, and an incident that spreads through five of them. All names and events are invented. |

## Run

Rung checks, with the same graders the main suite uses:

```bash
claude plugin eval . --eval-dir evals-heldout --allow-tools Write
```

Blind pairwise judge:

```bash
python3 evals/pairwise.py
```

The judge prints one row per case: the expected rung, the rung the skill chose, the answer the judge preferred, and a label. A preference counts only when the judge picks the same medium with the two answers in either order. Before you trust a new judge model or a changed judge prompt, read a few verdicts in the results folder and check that you would have scored them the same way.
