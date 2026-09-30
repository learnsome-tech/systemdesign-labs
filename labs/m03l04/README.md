# m03l04 · The Difference Between A Queue And A Log

Module 3: Caching, Queues And Asynchrony · lesson 3.4 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m03l04)

**Goal:** You can say what a queue and a log each guarantee, choose between them from whether the message is a command or a fact, and explain why retention and consumer lag become design inputs once you pick a log.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l04-01](m03l04-01/) | One deletes on acknowledgement, one keeps an offset | Read along |
| [m03l04-02](m03l04-02/) | The same ten records through both shapes | Graded |
| [m03l04-04](m03l04-04/) | Ordering exists inside a partition and nowhere else | Read along |
| [m03l04-05](m03l04-05/) | Consumer lag, compaction, and the health metric | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Classify your messages and price your retention

1. List your message types and mark each a command with an owner or a fact.
2. For each fact, say who might want to replay it and how far back.
3. Price the retention that allows that replay, in days and in gigabytes.
4. Chart consumer lag in records and in seconds for one real consumer.

> **Hint:** If a consumer bug would force you to write a backfill script from partial evidence, you needed a log and you chose a queue.

## Check yourself

- What happens to a record when a consumer acks it, in a queue and in a log?
- Why does adding a third consumer cost nothing in a log but steal work in a queue?
- Within what boundary is ordering guaranteed, and what caps your parallelism?
- Convert a lag of 1,200,000 records at 4,000/s into a lag in time.
- You have 7 d retention and notice a consumer bug after 9 d. What can you recover?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
