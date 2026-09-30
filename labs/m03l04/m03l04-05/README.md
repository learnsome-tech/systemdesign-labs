# m03l04-05 · Consumer lag, compaction, and the health metric

**Lesson:** [The Difference Between A Queue And A Log](https://learnsome.tech/learn/systemdesign-course/m03l04) (lesson 3.4, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can say what a queue and a log each guarantee, choose between them from whether the message is a command or a fact, and explain why retention and consumer lag become design inputs once you pick a log.

In the lesson: The health metric for a log is consumer lag: the end of the log minus the offset your consumer has committed. Report it two ways. Lag in records is the number you alarm on, and lag in time is the number you can discuss with a product owner, because saying five minutes behind is a sentence anybody can act on. This is exactly the observability lesson applied to asynchrony: the queue depth of the previous lesson and the consumer lag here are the same reading in different clothes. Compaction is the other idea worth knowing. A compacted topic keeps the newest record per key and discards older ones, which turns a stream of changes into a rebuildable table, so a new service can construct current state from history without querying anybody.

## Files

- [`starter/consumer-lag-compaction-and-the-health-metri.txt`](starter/consumer-lag-compaction-and-the-health-metri.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/consumer-lag-compaction-and-the-health-metri.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l04-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
