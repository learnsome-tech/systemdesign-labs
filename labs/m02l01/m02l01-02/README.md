# m02l01-02 · Relational storage earns its ceremony

**Lesson:** [The Storage Decision: Relational Versus Document](https://learnsome.tech/learn/systemdesign-course/m02l01) (lesson 2.1, module 2: Data, Storage And State) · Pro  
**Check:** Read along

## Goal

You can choose between relational and document storage from access patterns, transaction boundaries, and change ownership, while naming the failure mode your choice creates.

In the lesson: Relational storage earns its ceremony when shared facts must remain consistent. An order points to a customer, a payment points to an order, and a transaction can commit those changes together. Foreign keys and unique indexes turn an assumption into an enforced rule. That is why SQL from the earlier course remains the default for money, inventory, and identity. The cost is that joins cross pages, indexes consume memory and write work, and schema changes need a migration plan. A relational design is strongest when you can state the invariant in one sentence and let the engine guard it for you.

## Files

- [`starter/relational-storage-earns-its-ceremony.txt`](starter/relational-storage-earns-its-ceremony.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/relational-storage-earns-its-ceremony.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
