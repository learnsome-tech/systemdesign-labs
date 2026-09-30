# m02l03 · Replication, Failover And Leader Election

Module 2: Data, Storage And State · lesson 2.3 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m02l03)

**Goal:** You can choose a replication shape, route reads and writes around a leader, and explain the recovery cost and failure mode each replica introduces.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l03-02](m02l03-02/) | Leader and followers make the route explicit | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Write the failover story

1. Name the write authority and the fence that prevents two leaders.
2. Choose what a user reads immediately after a successful write.
3. State how recovery handles a follower that missed the last writes.

## Check yourself

- What does synchronous replication buy, and what does it cost?
- Why must failover fence an old leader before promoting a follower?
- When is a stale read acceptable product behavior?
- How does split brain turn a network partition into data loss?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
