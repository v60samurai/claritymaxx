---
type: llm
---

The user gave architecture notes for a system with: API gateway, orders-service with a Postgres database and an outbox table, outbox-relay, a Kafka topic order-events, notifications-worker, tracking-service, and a Redis cache.

PASS if the reply does all of these:
1. Traces the "create order" path in the right order: client, API gateway, orders-service, database transaction that writes the order row and the outbox row, outbox-relay, Kafka topic, notifications-worker.
2. Explains WHY the outbox exists: the order and its event are saved in one transaction, so an order cannot be saved without its event (or an event published without its order).
3. Traces the read path: tracking-service reads Redis, and on a miss calls orders-service and caches the result.
4. Shows the paths as a diagram or as a clearly ordered flow, not only as a list of component descriptions.

FAIL if any of the four is missing.
FAIL if the reply states as fact a component that the notes do not contain, such as a load balancer, an auth service, or a second database.
