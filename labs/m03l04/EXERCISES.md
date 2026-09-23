# Exercises — The Difference Between A Queue And A Log

Lesson `m03l04` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l04)

## Exercise 1: Classify your messages and price your retention

1. List your message types and mark each a command with an owner or a fact.
2. For each fact, say who might want to replay it and how far back.
3. Price the retention that allows that replay, in days and in gigabytes.
4. Chart consumer lag in records and in seconds for one real consumer.

> **Hint**: If a consumer bug would force you to write a backfill script from partial evidence, you needed a log and you chose a queue.


---

© LearnSome.tech · support@iwantto.learnsome.tech
