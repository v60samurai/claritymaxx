---
tags: [heldout, expect-html]
max_turns: 20
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

I am the new engineering lead for Brightline and I chair the incident review on Friday. I know distributed systems. I did not build this. Help me form the right mental model of the system and of the incident.

```
BRIGHTLINE - HOSPITAL LAB RESULTS PIPELINE, DESIGN NOTES

order-intake: receives lab orders from the hospital record system (EHR)
  as HL7 messages. Assigns an order id.

sample-tracker: staff scan the tube barcode at collection, at transport,
  and at the lab. Each scan is an event on the `sample-events` topic.

analyzer-bridge: one process per analyzer machine. Reads results from
  the machine over a serial link and publishes them to `raw-results`.
  If the link drops, it buffers on local disk and replays on reconnect.
  Replay keeps the original measurement time, not the send time.

results-store: consumes `raw-results`. Writes one row per order and
  test. A newer message for the same order and test overwrites the row.
  "Newer" means it arrived later.

corrections-ui: a lab technician can correct a result after a rerun.
  The correction is published to `raw-results` with `corrected: true`.

rules-engine: runs on every write to results-store. If a value is
  outside the critical range, it creates a critical alert. It keeps an
  alert key per order and test for 24 h so that it does not alert twice.

notifier: pages the on-call clinician for each critical alert and
  expects an acknowledgement within 15 minutes. No acknowledgement
  escalates to the charge nurse.

ehr-sync: every 2 minutes, copies changed rows from results-store to
  the EHR, where clinicians read them.

audit-log: records who viewed or changed a result. It does not record
  machine writes.

Trust zones: analyzers and analyzer-bridge are on the lab network.
  The EHR belongs to the hospital and we cannot change it.

Team disagreement 1: one engineer says "last write wins" is correct
  because corrections always come after originals. Another says
  arrival order and measurement order are different things.
Team disagreement 2: one engineer says the 24 h alert key prevents
  alert fatigue. Another says it hides real changes.

INCIDENT, 9 JUNE
 1. 02:10 Analyzer 3 measures potassium 6.9 mmol/L for a patient
    (critical high). Its serial link has been down since 02:05, so
    analyzer-bridge buffers the result.
 2. 02:20 The technician sees 6.9 on the analyzer screen, suspects a
    damaged sample, and reruns it: 4.1 mmol/L (normal).
 3. 02:24 The technician enters 4.1 in corrections-ui. results-store
    writes 4.1. rules-engine sees a normal value. No alert.
 4. 02:31 The link returns. analyzer-bridge replays the buffered 6.9.
 5. results-store overwrites 4.1 with 6.9, because 6.9 arrived later.
 6. rules-engine creates a critical alert. notifier pages the clinician.
 7. ehr-sync copies 6.9 to the EHR.
 8. 02:40 The clinician orders treatment for high potassium.
 9. 03:15 The technician notices the EHR shows 6.9 and corrects it
    again. results-store writes 4.1. rules-engine has an alert key for
    this order, so it does nothing. Nobody is paged about the change.
10. Every service reported success. The first report was labelled
    "technician data entry error".
```
