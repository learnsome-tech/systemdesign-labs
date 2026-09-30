# m02l02-05 · One product, four stores, one ownership map

**Lesson:** [The Storage Decision: Key Value, Search And Blob](https://learnsome.tech/learn/systemdesign-course/m02l02) (lesson 2.2, module 2: Data, Storage And State) · Pro  
**Check:** Read along

## Goal

You can match exact lookup, text retrieval, and large immutable bytes to key value, search, and blob storage, while preserving a clear source of truth.

In the lesson: A practical ownership map can contain four stores without becoming mysterious. The relational database owns account and payment facts. Key value storage owns short lived sessions and leases. Search owns only its retrieval index. Blob storage owns immutable photo bytes, while SQL owns the row that says who may read them. Draw arrows from owners to projections, never arrows that imply two writers share authority. This is the same contract idea from the APIs course, applied to data: every boundary needs an owner, a failure response, and a way to retry without inventing a second truth.

## Files

- [`starter/one-product-four-stores-one-ownership-map.txt`](starter/one-product-four-stores-one-ownership-map.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/one-product-four-stores-one-ownership-map.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
