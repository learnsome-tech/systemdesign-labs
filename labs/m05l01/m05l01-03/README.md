# m05l01-03 · And what it costs, itemised

**Lesson:** [Monolith Versus Services: The Honest Trade Offs](https://learnsome.tech/learn/systemdesign-course/m05l01) (lesson 5.1, module 5: Architecture And Operations) · Pro  
**Check:** Read along

## Goal

You can argue the monolith and services decision from data ownership and team boundaries rather than fashion, price a split in latency and availability, and recognise a distributed monolith before you ship one.

In the lesson: Now the bill. Every call you move across a boundary becomes a network call, which means it can be slow, it can time out, and it can half succeed. The single commit you relied on in the SQL course does not cross the boundary, so a workflow that used to be one transaction becomes a saga with compensating steps, or becomes nothing at all and you live with inconsistency. Testing changes shape: answering one question now needs four things running. And the operational surface grows, because you need distributed tracing, per service dashboards and correlated logs before you can answer where did the time go. That is not extra credit. Everything the observability course taught becomes a prerequisite rather than a nice habit.

## Files

- [`starter/and-what-it-costs-itemised.txt`](starter/and-what-it-costs-itemised.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/and-what-it-costs-itemised.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
