# m03l03 · Queues, Events And Asynchronous Work

Module 3: Caching, Queues And Asynchrony · lesson 3.3 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m03l03)

**Goal:** You can decide what belongs on the request path and what belongs behind a queue, name the parts of a queue and what each one protects, and use Little's law to tell a buffering queue apart from a failing one.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l03-02](m03l03-02/) | Commands and events couple you differently | Read along |
| [m03l03-03](m03l03-03/) | The parts of a queue, and one honest sentence | Read along |
| [m03l03-04](m03l03-04/) | Little's law is all the queue theory you need | Read along |
| [m03l03-05](m03l03-05/) | A healthy queue: bursty, never empty, always bounded | Graded |
| [m03l03-06](m03l03-06/) | Change one constant and the queue stops being a buffer | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Move one thing off your request path, and watch it

1. List one endpoint's work and mark what the user must see before you reply.
2. Move one item behind a queue, returning 202 with a status URL to poll.
3. Chart queue depth and oldest message age, and alert on age, not on depth.
4. Compute the drain rate you need so depth returns to zero between bursts.

> **Hint:** Alert on the age of the oldest unprocessed message: depth alone cannot tell a fast deep queue from a slow shallow one.

## Check yourself

- A queue holds 1,200 messages and drains at 50/s: how far behind is a new arrival?
- Why is acknowledging on receipt rather than on completion a data loss bug?
- What does a visibility timeout protect, and what happens when it is too short?
- Which is a command and which is an event: "charge card" and "order placed"?
- Why alert on oldest message age instead of on queue depth?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
