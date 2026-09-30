# m03l04-04 · Ordering exists inside a partition and nowhere else

**Lesson:** [The Difference Between A Queue And A Log](https://learnsome.tech/learn/systemdesign-course/m03l04) (lesson 3.4, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can say what a queue and a log each guarantee, choose between them from whether the message is a command or a fact, and explain why retention and consumer lag become design inputs once you pick a log.

In the lesson: A log gives you ordering, and the small print matters. A topic is divided into partitions because that is how you get more than one consumer working at once, and the ordering guarantee lives inside a partition only. Across partitions there is no order whatsoever. So the partition key is a real design decision: key by customer and every event for that customer is ordered against every other one, which is usually exactly what you want. It also means the parallelism you can reach is capped by the partition count, and it brings back the hot key problem from module two, because one very busy customer is one partition and therefore one consumer. Ordering and parallelism are traded against each other here, and the partition key is where you make the trade.

## Files

- [`starter/ordering-exists-inside-a-partition-and-nowhe.txt`](starter/ordering-exists-inside-a-partition-and-nowhe.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/ordering-exists-inside-a-partition-and-nowhe.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
