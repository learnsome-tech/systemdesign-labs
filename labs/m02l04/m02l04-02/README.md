# m02l04-02 · Good keys spread work and preserve a useful local view

**Lesson:** [Partitioning, Sharding And Hot Keys](https://learnsome.tech/learn/systemdesign-course/m02l04) (lesson 2.4, module 2: Data, Storage And State) · Pro  
**Check:** Read along

## Goal

You can partition state by a stable key, estimate the limits of one shard, and recognise hot keys before they turn a balanced fleet into one overloaded machine.

In the lesson: A good key spreads work while preserving a useful local view. Customer ID keeps one customer's history together and lets a read stay local. A random identifier spreads writes but makes a range scan expensive. A timestamp alone sends every newest write to the same partition, creating a moving hotspot. Compound keys can encode both ownership and time, as with a tenant plus time bucket for metrics. The right key is the one that makes the dominant query local without placing a popular tenant, event, or conversation on one machine forever.

## Files

- [`starter/good-keys-spread-work-and-preserve-a-useful-.txt`](starter/good-keys-spread-work-and-preserve-a-useful-.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/good-keys-spread-work-and-preserve-a-useful-.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
