# m04l03 · Retries, Backoff And Jitter

Module 4: Resilience And Traffic Management · lesson 4.3 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m04l03)

**Goal:** You can retry only safe failures, apply bounded exponential backoff with jitter, and show why synchronized retries become a second outage.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l03-02](m04l03-02/) | Jitter separates the retry wave | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Write the retry policy

1. Choose the errors that are safe to retry for one endpoint.
2. Set a cap, an attempt limit, and a total deadline.
3. Say where the idempotency key from module three is stored.

## Check yourself

- Which failures should not be retried?
- Why does a seeded generator matter in the simulation?
- What does full jitter change about synchronized callers?
- Why should nested libraries avoid their own hidden retry policy?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
