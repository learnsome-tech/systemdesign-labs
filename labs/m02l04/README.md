# m02l04 · Partitioning, Sharding And Hot Keys

Module 2: Data, Storage And State · lesson 2.4 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m02l04)

**Goal:** You can partition state by a stable key, estimate the limits of one shard, and recognise hot keys before they turn a balanced fleet into one overloaded machine.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l04-02](m02l04-02/) | Good keys spread work and preserve a useful local view | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Find the hot partition

1. Pick a partition key for a feed or chat workload.
2. Name the single key that could receive half the traffic.
3. Choose salt, split, replication, or queue, and state the new cost.

## Check yourself

- What does a partition key decide besides data placement?
- Why can a hash still produce a hot partition?
- What costs can salting a hot key introduce?
- What must be true before a resharding cutover?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
