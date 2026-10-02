---
type: llm
---

PASS if the reply does all of these:
1. Says what came before: sequence models built on recurrent networks (RNN, LSTM, or GRU), often with an attention mechanism added on top. Mentioning convolutional sequence models as well is fine.
2. Says what changed: the Transformer removes recurrence and uses attention (self-attention) as the main mechanism.
3. Gives a consequence of that change: positions can be processed in parallel during training, or distant tokens are connected by a short path.
4. Says the model needs positional encodings (or positional information) because attention alone does not know token order.

FAIL if any of the four is missing.
FAIL if the reply is only a section-by-section summary of the paper with no comparison to earlier models.
