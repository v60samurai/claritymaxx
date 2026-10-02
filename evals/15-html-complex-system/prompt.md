---
tags: [html, architecture, under-escalation]
max_turns: 20
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

I take over Ferrywise next week and I have to review its design with the team. I know distributed systems. I did not build this. Help me form the right mental model, including last month's incident. Choose the format yourself.

```
FERRYWISE - DESIGN NOTES (ferry ticket platform)

Clients: web, mobile, and port kiosks. Kiosks work offline for up to
  20 minutes and upload their sales when the link returns.

edge-gateway: checks the session, applies rate limits, routes requests.

search-service: answers "which sailings have space". Reads a
  `sailing_index` in Elasticsearch. The index is rebuilt from
  inventory events and can be up to 90 s behind.

inventory-service: owns seat and vehicle-deck capacity in Postgres.
  It is the only writer. A hold lasts 10 minutes, then expires.

pricing-service: computes the fare from route, season, vehicle length,
  and remaining capacity. It reads remaining capacity from a Redis
  cache that inventory-service refreshes every 30 s.

booking-service: runs the purchase as a saga:
  hold capacity -> price -> take payment -> confirm -> issue ticket.
  Each step writes a row to `saga_log`. A failed step runs the
  compensations for the earlier steps in reverse order.

payments-adapter: calls the external payment provider. The provider
  sometimes answers after our 8 s timeout.

ticket-issuer: creates the QR ticket and puts a message on `ticket-events`.

notify-worker: reads `ticket-events`, sends email and SMS.

boarding-service: port staff scan QR codes. It keeps a local copy of
  the manifest for each sailing, synced every 60 s, so that scanning
  works when the port network drops.

admin-console: operations staff can cancel a sailing. A cancellation
  must release capacity, refund every booking, and notify every customer.

Trust zones: kiosks and port scanners are on port networks that we do
  not control. Payment card data must stay inside payments-adapter.

Team disagreement 1: one engineer says search may show stale capacity
  because inventory-service rejects the hold anyway. Another says stale
  search results are the top source of customer complaints.
Team disagreement 2: one engineer calls `saga_log` "our audit trail".
  Another says it only records enough to run compensations.

INCIDENT, 14 MARCH
 1. A storm closes the 18:00 sailing. Staff cancel it in admin-console.
 2. inventory-service releases the capacity for that sailing.
 3. A kiosk that was offline uploads 6 sales for the 18:00 sailing.
 4. booking-service accepts them. The capacity check passes, because
    the capacity was just released.
 5. payments-adapter charges 6 cards. Two calls time out, and
    booking-service retries them. Both cards are charged twice.
 6. ticket-issuer issues 6 tickets for a sailing that does not exist.
 7. The refund job for the cancellation ran at step 1 and has finished.
    It does not see the 6 new bookings.
 8. boarding-service still has the old manifest. Nobody scans, so
    nothing raises an alarm.
 9. Every service reported success. The first report was labelled
    "kiosk sync bug".
```
