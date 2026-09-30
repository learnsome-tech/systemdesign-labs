# m02l01-04 · Make the decision with a workload table

**Lesson:** [The Storage Decision: Relational Versus Document](https://learnsome.tech/learn/systemdesign-course/m02l01) (lesson 2.1, module 2: Data, Storage And State) · Pro  
**Check:** Read along

## Goal

You can choose between relational and document storage from access patterns, transaction boundaries, and change ownership, while naming the failure mode your choice creates.

In the lesson: Make the decision with a workload table. Put each entity on a row, then write its hottest read, its write rate, its size, and the invariant that must survive a crash. Checkout needs an order and a payment together, so relational storage is a natural fit. A profile owns its fields and is usually fetched whole, so a document is plausible. Search needs text analysis and filters, so it deserves its own index fed from a source of truth. The table exposes mixed systems honestly. One product can use several stores, as long as one store owns each fact and the repair path is explicit.

## Files

- [`starter/make-the-decision-with-a-workload-table.txt`](starter/make-the-decision-with-a-workload-table.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/make-the-decision-with-a-workload-table.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
