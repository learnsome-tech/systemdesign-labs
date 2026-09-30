# m06l04-02 · Partition conversations, then protect the hot ones

**Lesson:** [Worked Design Two: Scaling Chat Fan Out](https://learnsome.tech/learn/systemdesign-course/m06l04) (lesson 6.4, module 6: Worked Designs End To End) · Pro  
**Check:** Read along

## Goal

You can scale the chat design with connection gateways, per conversation partitions, offline inboxes, and bounded fan out while naming the consistency cost.

In the lesson: Partition conversations by conversation ID so one thread has one ordering authority. A large room can still create a fan out hotspot, so separate durable append from recipient delivery. Append one message, then deliver it in bounded batches through gateway owners. Offline recipients receive a row in their inbox and replay it on reconnect. The message is ordered once in the conversation; delivery order at each gateway may lag and can be retried. This split keeps history correct while allowing delivery capacity to scale.

## Files

- [`starter/partition-conversations-then-protect-the-hot.txt`](starter/partition-conversations-then-protect-the-hot.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/partition-conversations-then-protect-the-hot.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
