#!/usr/bin/env bash
# Writes the fixture repository into the empty eval workspace.
set -euo pipefail
mkdir -p tinyqueue

cat > tinyqueue/README.md <<'FIXTURE_EOF'
# tinyqueue

A job queue in one SQLite file.

    python -m tinyqueue.cli enqueue send_email '{"to": "a@example.com"}'
    python -m tinyqueue.cli work
FIXTURE_EOF

: > tinyqueue/__init__.py

cat > tinyqueue/backoff.py <<'FIXTURE_EOF'
import random

BASE_SECONDS = 2
CAP_SECONDS = 300


def delay_for(attempts):
    ceiling = min(CAP_SECONDS, BASE_SECONDS * 2 ** attempts)
    return random.uniform(0, ceiling)
FIXTURE_EOF

cat > tinyqueue/cli.py <<'FIXTURE_EOF'
import json
import sys

from . import store, worker


@worker.handler("send_email")
def send_email(payload):
    print("sending email to", payload["to"])


def main(argv):
    db = store.connect()
    if argv[1] == "enqueue":
        store.enqueue(db, argv[2], json.loads(argv[3]))
    elif argv[1] == "work":
        worker.run_forever(db)


if __name__ == "__main__":
    main(sys.argv)
FIXTURE_EOF

cat > tinyqueue/store.py <<'FIXTURE_EOF'
import json
import sqlite3
import time

CLAIM_SECONDS = 30
MAX_ATTEMPTS = 5

SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    kind TEXT NOT NULL,
    payload TEXT NOT NULL,
    state TEXT NOT NULL DEFAULT 'pending',
    attempts INTEGER NOT NULL DEFAULT 0,
    run_after REAL NOT NULL DEFAULT 0,
    claimed_until REAL
);
"""


def connect(path="queue.db"):
    db = sqlite3.connect(path, isolation_level=None)
    db.execute(SCHEMA)
    return db


def enqueue(db, kind, payload):
    db.execute("INSERT INTO jobs (kind, payload) VALUES (?, ?)", (kind, json.dumps(payload)))


def claim(db, now=None):
    now = now or time.time()
    db.execute("BEGIN IMMEDIATE")
    row = db.execute(
        """
        SELECT id, kind, payload, attempts FROM jobs
        WHERE (state = 'pending' AND run_after <= ?)
           OR (state = 'claimed' AND claimed_until <= ?)
        ORDER BY id LIMIT 1
        """,
        (now, now),
    ).fetchone()
    if row is None:
        db.execute("COMMIT")
        return None
    db.execute(
        "UPDATE jobs SET state = 'claimed', claimed_until = ?, attempts = attempts + 1 WHERE id = ?",
        (now + CLAIM_SECONDS, row[0]),
    )
    db.execute("COMMIT")
    return {"id": row[0], "kind": row[1], "payload": json.loads(row[2]), "attempts": row[3] + 1}


def complete(db, job_id):
    db.execute("UPDATE jobs SET state = 'done', claimed_until = NULL WHERE id = ?", (job_id,))


def fail(db, job, delay):
    if job["attempts"] >= MAX_ATTEMPTS:
        db.execute("UPDATE jobs SET state = 'dead', claimed_until = NULL WHERE id = ?", (job["id"],))
        return
    db.execute(
        "UPDATE jobs SET state = 'pending', claimed_until = NULL, run_after = ? WHERE id = ?",
        (time.time() + delay, job["id"]),
    )
FIXTURE_EOF

cat > tinyqueue/worker.py <<'FIXTURE_EOF'
import time

from . import backoff, store

HANDLERS = {}


def handler(kind):
    def register(fn):
        HANDLERS[kind] = fn
        return fn
    return register


def run_once(db):
    job = store.claim(db)
    if job is None:
        return False
    try:
        HANDLERS[job["kind"]](job["payload"])
    except Exception:
        store.fail(db, job, backoff.delay_for(job["attempts"]))
    else:
        store.complete(db, job["id"])
    return True


def run_forever(db, idle_seconds=1.0):
    while True:
        if not run_once(db):
            time.sleep(idle_seconds)
FIXTURE_EOF
