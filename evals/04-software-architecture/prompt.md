---
tags: [architecture, diagram]
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill]
---

Here are our architecture notes for Parcelboard. Explain how this system works and where requests move.

```
PARCELBOARD - ARCHITECTURE NOTES

Clients: web app and mobile app. Both call the API gateway over HTTPS.

API gateway: checks the session token, applies rate limits, routes by path.
  /orders/*    -> orders-service
  /tracking/*  -> tracking-service

orders-service: owns the `orders` Postgres database.
  On "create order" it writes the order row AND a row in the `outbox`
  table in one database transaction.

outbox-relay: a separate process. Polls `outbox` every 500 ms, publishes
  each row to the Kafka topic `order-events`, then marks the row as sent.

notifications-worker: consumes `order-events`, sends email and push.
  It stores processed event ids so that a repeated event sends nothing.

tracking-service: read only. Reads order status from a Redis cache.
  On a cache miss it calls orders-service and stores the result for 60 s.

orders-service deletes the Redis key for an order when the order changes.
```
