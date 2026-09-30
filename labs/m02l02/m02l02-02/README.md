# m02l02-02 · Key value is narrow by design

**Lesson:** [The Storage Decision: Key Value, Search And Blob](https://learnsome.tech/learn/systemdesign-course/m02l02) (lesson 2.2, module 2: Data, Storage And State) · Pro  
**Check:** Read along

## Goal

You can match exact lookup, text retrieval, and large immutable bytes to key value, search, and blob storage, while preserving a clear source of truth.

In the lesson: Key value storage is narrow by design. The key is the access pattern, and the value is whatever the application can replace or decode quickly. Sessions, rate limit counters, short lived leases, and connection registries fit because they are found by exact key and often expire. Conditional writes can protect a small invariant, such as acquiring a lock only when it is free. The cost is equally clear: asking for every value matching a property is not the store's job. Add another index or change the query, rather than turning a key value system into an accidental database.

## Files

- [`starter/key-value-is-narrow-by-design.txt`](starter/key-value-is-narrow-by-design.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/key-value-is-narrow-by-design.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
