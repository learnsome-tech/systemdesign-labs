# m01l04 · Back Of The Envelope Estimation: Storage And Bandwidth

Module 1: Foundations And Estimation · lesson 1.4 · Free · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m01l04)

**Goal:** You can estimate stored bytes from a row size, a write rate and a retention window, apply index and replication multipliers, size shards from the result, and convert read traffic into egress bandwidth.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l04-02](m01l04-02/) | Estimate a row honestly, then stop refining it | Read along |
| [m01l04-03](m01l04-03/) | Rate, retention, indexes, replicas, shards | Graded |
| [m01l04-05](m01l04-05/) | Bandwidth: the bill nobody estimates | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Estimate storage for a photograph service

1. Assume ten million uploads a day, two megabytes each, kept for five years.
2. Compute raw bytes, then apply three copies and two thumbnail sizes.
3. Choose a shard count from a target rebuild time you state explicitly.
4. Estimate peak egress if each upload is viewed twenty times a year.

> **Hint:** Thumbnails are usually a small fraction of the original but there are several of them, and they are read far more often than the original, so they dominate bandwidth rather than storage.

## Check yourself

- What two multiplications and one question make up a storage estimate?
- Which two multipliers are most often left out of a first estimate?
- How should you choose a shard count, and what should you not choose it from?
- In the bandwidth example, why do images dominate, and what fixes it?
- Why is alerting on days of headroom better than alerting on percent of disk used?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
