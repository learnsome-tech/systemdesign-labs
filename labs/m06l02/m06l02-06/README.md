# m06l02-06 · The scaled design, and where the lag becomes visible

**Lesson:** [Worked Design One: Scaling The Ticket Booking System](https://learnsome.tech/learn/systemdesign-course/m06l02) (lesson 6.2, module 6: Worked Designs End To End) · Pro  
**Check:** Read along

## Goal

You can size the opening minute of a ticket sale, choose admission control as the design rather than an add on, partition by event while admitting the hot shard it creates, and say exactly what the waiting room costs the people standing in it.

In the lesson: Here is the scaled design, with two additions and one honest problem. The additions are asynchrony and read scaling: confirmation email, ticket rendering and seat map refresh all move behind a queue, which is module three, and browsing moves to read replicas so the leader spends its capacity on commits. The honest problem is the one module two lesson six warned about. A buyer completes a purchase against the leader, refreshes the page, and the refresh lands on a replica that has not caught up, so the ticket they just bought is not there. They buy again. The fix is not more replicas, it is routing: after a write, read that user from the leader, or pin their session for a few seconds. Eventual consistency is fine until a person can see it.

## Files

- [`starter/the-scaled-design-and-where-the-lag-becomes-.txt`](starter/the-scaled-design-and-where-the-lag-becomes-.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-scaled-design-and-where-the-lag-becomes-.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l02-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
