# m03l01-03 · Five strategies, and where each one sends the bill

**Lesson:** [Caching Strategies And Topology](https://learnsome.tech/learn/systemdesign-course/m03l01) (lesson 3.1, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can place a cache at the right layer, choose a read and write strategy while naming what it costs, and size the origin for the miss rate instead of the hit ratio.

In the lesson: Five strategies, and each one sends the bill to a different place. Cache aside is the default: the application looks in the cache, misses, reads the database, and writes the value back. It is easy to reason about and it leaves the miss path fully exposed. Read through hides that by letting the cache fetch on your behalf, which means the cache now owns a connection to your origin. Write through writes both on every write, so the cache is never cold and every write pays a second round trip. Write behind writes to the cache and drains to the database later, which is the fastest option and the only one that can lose a write you already acknowledged. Refresh ahead warms a key before it expires and spends work on predictions that are sometimes wrong.

## Files

- [`starter/five-strategies-and-where-each-one-sends-the.txt`](starter/five-strategies-and-where-each-one-sends-the.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/five-strategies-and-where-each-one-sends-the.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
