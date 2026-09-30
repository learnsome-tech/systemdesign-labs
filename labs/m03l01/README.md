# m03l01 · Caching Strategies And Topology

Module 3: Caching, Queues And Asynchrony · lesson 3.1 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m03l01)

**Goal:** You can place a cache at the right layer, choose a read and write strategy while naming what it costs, and size the origin for the miss rate instead of the hit ratio.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l01-02](m03l01-02/) | Six places a cache can live, from the user inwards | Read along |
| [m03l01-03](m03l01-03/) | Five strategies, and where each one sends the bill | Read along |
| [m03l01-04](m03l01-04/) | Latency slides, origin load falls off a cliff | Graded |
| [m03l01-06](m03l01-06/) | The cold cache spike nobody provisions for | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Find your real hit ratio, then your cold origin load

1. Measure one real cache hit ratio over a whole week, not over a good hour.
2. Compute origin queries a second at that ratio, and at ten points lower.
3. Decide whether the origin survives the cold number, and write the answer down.
4. Name the layer each cached value belongs in, and who is responsible for deleting it.

> **Hint:** If nobody can name who deletes a key, that value has no invalidation story and its time to live is the only safety net it has.

## Check yourself

- At a 90% hit ratio and 20,833 peak reads/s, how many reads/s still reach the origin?
- Which two strategies keep the cache warm, and what does each one charge you for it?
- Why can an in-process local cache not be invalidated reliably across 20 pods?
- What does the origin see during a rolling restart, and how do you size for that?
- Which cache layer can hold a price list but never a bank balance, and why?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
