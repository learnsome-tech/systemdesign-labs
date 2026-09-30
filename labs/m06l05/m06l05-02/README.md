# m06l05-02 · Separate admission, buffering, and storage

**Lesson:** [Worked Design Three: A Metrics Ingestion Pipeline](https://learnsome.tech/learn/systemdesign-course/m06l05) (lesson 6.5, module 6: Worked Designs End To End) · Pro  
**Check:** Read along

## Goal

You can design a metrics ingestion path from agents to durable partitions, choose retention and query stores, and preserve samples when consumers fall behind.

In the lesson: Separate admission, buffering, and storage. The gateway authenticates the tenant, checks a rate limit, and rejects work that cannot fit before accepting a batch. A bounded queue absorbs a short burst, not an infinite deficit. Partitions use tenant and time bucket so writes spread while recent queries stay local. A recent store serves dashboards, while older samples compact into cheaper blob archives. Each layer has a capacity and a refusal path, so overload does not quietly turn into memory exhaustion.

## Files

- [`starter/separate-admission-buffering-and-storage.txt`](starter/separate-admission-buffering-and-storage.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/separate-admission-buffering-and-storage.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
