# m03l04-01 · One deletes on acknowledgement, one keeps an offset

**Lesson:** [The Difference Between A Queue And A Log](https://learnsome.tech/learn/systemdesign-course/m03l04) (lesson 3.4, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can say what a queue and a log each guarantee, choose between them from whether the message is a command or a fact, and explain why retention and consumer lag become design inputs once you pick a log.

In the lesson: These two are often sold as the same product and they are not the same thing at all. In a queue, consumers compete for messages. One of them wins, does the work, acknowledges, and the message is deleted, because in a queue an acknowledgement means destruction. In a log, nothing is deleted on reading. The log keeps its records in order for a retention period, and each consumer holds an offset saying how far it has read. Two consequences follow and they decide everything else. A queue cannot be replayed, because the evidence is gone. And adding a consumer to a queue steals work from the others, while adding one to a log costs nobody anything, because it starts from an offset of its own choosing.

## Files

- [`starter/one-deletes-on-acknowledgement-one-keeps-an-.txt`](starter/one-deletes-on-acknowledgement-one-keeps-an-.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/one-deletes-on-acknowledgement-one-keeps-an-.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l04-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
