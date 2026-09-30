# m03l03-04 · Little's law is all the queue theory you need

**Lesson:** [Queues, Events And Asynchronous Work](https://learnsome.tech/learn/systemdesign-course/m03l03) (lesson 3.3, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can decide what belongs on the request path and what belongs behind a queue, name the parts of a queue and what each one protects, and use Little's law to tell a buffering queue apart from a failing one.

In the lesson: One equation covers this. The number of items in a system equals the arrival rate times the time each item spends there, which people know as Little's law. Turn it round and it becomes the only monitoring rule you need: the wait is the depth divided by the drain rate. Twelve hundred messages draining at fifty a second means anything arriving now is twenty four seconds behind, and you can read that off a dashboard without a stopwatch. The second consequence matters more. If the depth is flat your consumers are keeping up and the queue is doing its job. If the depth is rising, your consumers are slower than your producers, and no queue length in the world fixes that, because the queue was never the thing doing the work.

## Files

- [`starter/little-s-law-is-all-the-queue-theory-you-nee.py`](starter/little-s-law-is-all-the-queue-theory-you-nee.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/little-s-law-is-all-the-queue-theory-you-nee.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
