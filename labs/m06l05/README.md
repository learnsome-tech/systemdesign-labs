# m06l05 · Worked Design Three: A Metrics Ingestion Pipeline

Module 6: Worked Designs End To End · lesson 6.5 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m06l05)

**Goal:** You can design a metrics ingestion path from agents to durable partitions, choose retention and query stores, and preserve samples when consumers fall behind.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l05-02](m06l05-02/) | Separate admission, buffering, and storage | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Set the loss and lag contract

1. Choose which metric classes may be shed during overload.
2. Set a maximum ingest lag for an alerting stream.
3. Name the source used to rebuild a query projection.

## Check yourself

- Why batch samples before sending them?
- Which fields make a metrics batch idempotent?
- Why separate alerting workers from dashboard queries?
- How can a pipeline expose missing samples rather than only process health?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
