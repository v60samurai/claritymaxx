---
type: llm
---

PASS if the reply, in any wording, is consistent with all of these and contradicts none:
1. Text is split into tokens, and each token becomes a vector.
2. Attention lets each position take in information from other positions.
3. The model repeats a block of attention and a feed-forward step many times, and each block updates the vectors.
4. The vector at the last position is turned into a score for every token in the vocabulary, the scores become probabilities, and one token is chosen.

The reply may cover some of these only in a page it created. Do not fail it for brevity.
FAIL if the reply states something that contradicts any of the four, for example that the model looks up the next token in a table or that it processes one word at a time like a recurrent network.
