# m03l02-02 · The three hard cases, and the fix for each

**Lesson:** [Cache Invalidation And The Three Hard Cases](https://learnsome.tech/learn/systemdesign-course/m03l02) (lesson 3.2, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can tell expiry apart from invalidation, recognise the stampede, the stale read after write and the mass expiry in a running system, and apply single flight, versioned keys and jittered time to live to each.

In the lesson: Cache invalidation has a reputation for being hard, and it comes down to three specific cases. The stampede, where one hot key expires and every request that wanted it goes to the origin at the same instant. The stale read after write, where an invalidation and a cache fill arrive in the wrong order and the cache ends up holding a value the database has already replaced. And the mass expiry, where a batch of keys written together all expire together and the origin takes the whole batch as one spike. Notice what they have in common. Every one of them is a timing bug, which means every one of them is invisible when you test it and inevitable when you are busy.

## Files

- [`starter/the-three-hard-cases-and-the-fix-for-each.txt`](starter/the-three-hard-cases-and-the-fix-for-each.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-three-hard-cases-and-the-fix-for-each.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
