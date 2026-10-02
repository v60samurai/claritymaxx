---
type: llm
---

The user gave design notes for a ferry ticket platform with more than ten components, a purchase saga, two trust zones, two team disagreements, and an incident in nine steps.

PASS if the reply does all of these:
1. Tells the user that an HTML file was created and where it is.
2. States the core model in prose in the reply itself, in a few sentences, so the user has the answer before opening the file.
3. Says that the incident was more than a kiosk sync bug, and names at least one cause in the design: a cancelled sailing still accepted bookings because releasing capacity made the capacity check pass, or the payment retry had no idempotency key, or the refund job ran once and did not cover later bookings.

FAIL if any of the three is missing.
FAIL if the reply states as fact a component that the notes do not contain.
