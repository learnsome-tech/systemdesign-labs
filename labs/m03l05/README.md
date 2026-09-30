# m03l05 · Idempotency, And Exactly Once As A Fiction

Module 3: Caching, Queues And Asynchrony · lesson 3.5 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m03l05)

**Goal:** You can make retries harmless with idempotency keys, distinguish deduplication from exactly once delivery, and place the durable record at the correct boundary.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l05-02](m03l05-02/) | The idempotency key belongs to the intent | Read along |
| [m03l05-05](m03l05-05/) | The outbox joins a write to its event | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Make a payment retry harmless

1. Choose the idempotency key for a payment intent.
2. Name the atomic record that wins the duplicate race.
3. State what happens after commit before the client receives a reply.

## Check yourself

- Why can a timeout not tell the client whether a write committed?
- What fields belong in a durable idempotency record?
- Why is check then create unsafe under concurrency?
- What gap does the outbox pattern close, and which duplicate does it leave?
- At which boundary can exactly once effect be a useful claim?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
