# m03l02-04 · The stale read after write, drawn on a timeline

**Lesson:** [Cache Invalidation And The Three Hard Cases](https://learnsome.tech/learn/systemdesign-course/m03l02) (lesson 3.2, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can tell expiry apart from invalidation, recognise the stampede, the stale read after write and the mass expiry in a running system, and apply single flight, versioned keys and jittered time to live to each.

In the lesson: This is the case people do not see coming, so walk the timeline. A reader misses, goes to the database, and reads version one. Then it is descheduled, because that is what threads do. Meanwhile a writer commits version two and deletes the cache key, which was the correct thing to do. Now the reader wakes up and writes what it read into the cache, so the cache holds version one and the database holds version two, and nothing will fix it until the key expires. The reader was correct at every single step. The SQL course explains why: its read was consistent when it happened, and staleness is not a transaction violation. The fixes are versioned keys, or write through, or a short time to live that bounds how long you are wrong.

## Files

- [`starter/the-stale-read-after-write-drawn-on-a-timeli.txt`](starter/the-stale-read-after-write-drawn-on-a-timeli.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-stale-read-after-write-drawn-on-a-timeli.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
