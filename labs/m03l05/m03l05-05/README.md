# m03l05-05 · The outbox joins a write to its event

**Lesson:** [Idempotency, And Exactly Once As A Fiction](https://learnsome.tech/learn/systemdesign-course/m03l05) (lesson 3.5, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can make retries harmless with idempotency keys, distinguish deduplication from exactly once delivery, and place the durable record at the correct boundary.

In the lesson: The outbox pattern joins a business write to its event. In one SQL transaction, update the order and insert an outbox row. A relay reads unsent rows, publishes the event, and records progress. If the relay crashes after publishing, it publishes again, which is acceptable because the consumer stores a unique event identifier before applying its effect. The outbox removes the gap between a committed state change and a missing event. It does not remove duplicates downstream, and it adds a table that must be drained, indexed, and monitored.

## Files

- [`starter/the-outbox-joins-a-write-to-its-event.txt`](starter/the-outbox-joins-a-write-to-its-event.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-outbox-joins-a-write-to-its-event.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l05-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
