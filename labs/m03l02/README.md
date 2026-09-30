# m03l02 · Cache Invalidation And The Three Hard Cases

Module 3: Caching, Queues And Asynchrony · lesson 3.2 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m03l02)

**Goal:** You can tell expiry apart from invalidation, recognise the stampede, the stale read after write and the mass expiry in a running system, and apply single flight, versioned keys and jittered time to live to each.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l02-02](m03l02-02/) | The three hard cases, and the fix for each | Read along |
| [m03l02-03](m03l02-03/) | The stampede, and what single flight is worth | Graded |
| [m03l02-04](m03l02-04/) | The stale read after write, drawn on a timeline | Read along |
| [m03l02-05](m03l02-05/) | Mass expiry, and what jitter costs you | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Run the three cases against your own hottest key

1. Find your hottest cached key and count the requesters that would miss together.
2. Add single flight, then measure origin calls for that key before and after.
3. Jitter every bulk warmed time to live, and state the staleness window you accept.
4. Write down who deletes each key, and what breaks when that path is skipped.

> **Hint:** Test invalidation by writing and immediately reading in a loop from two clients: the stale read after write only appears under concurrency.

## Check yourself

- Why is DEL on a key safer than SET to the new value when two writers race?
- How does single flight change origin calls when 1,000 requesters share one expiry?
- Sketch the stale read after write: which participant behaved incorrectly?
- Why does jittering a TTL lower the peak without lowering total origin work?
- How do you tell an invalidation bug from a data bug during an incident?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
