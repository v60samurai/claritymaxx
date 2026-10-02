---
type: llm
---

PASS if the reply does all of these:
1. Contains a diagram drawn in text characters or in Mermaid, not only prose and not only a numbered list.
2. The diagram shows at least these actors: the user or browser, the client application, and the authorization server.
3. The diagram shows the messages in order, and the arrows or steps are labelled with what is sent.
4. The reply says the client creates a code_verifier and sends a code_challenge derived from it in the first request, and that the authorization server checks the code_verifier against the code_challenge when the client exchanges the authorization code for tokens.

FAIL if any of the four is missing.
