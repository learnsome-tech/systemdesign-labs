# m05l02-03 · Cardinality is the constraint that decides your labels

**Lesson:** [Observability As A Design Input](https://learnsome.tech/learn/systemdesign-course/m05l02) (lesson 5.2, module 5: Architecture And Operations) · Pro  
**Check:** Read along

## Goal

You can decide at design time what a system must emit, choose labels that respect cardinality, record latency as a histogram rather than a mean, and turn a service level objective into an error budget with a burn rate.

In the lesson: Here is the constraint nobody mentions until the bill arrives. A metric costs one stored series for every combination of its label values, so the cost is the product, not the sum. Three hundred combinations is nothing. Add a customer identifier with two hundred thousand values and you have sixty million series, which will take down your metrics system faster than your outage would have. So metrics get labels with small, bounded sets: service, endpoint, status class, region, customer tier. Anything unbounded, such as a user identifier, a request identifier or a raw path with numbers in it, belongs in a log or a trace where you pay per event instead of per combination. And this is a design decision, because the labels you choose now decide which questions are answerable later.

## Files

- [`starter/cardinality-is-the-constraint-that-decides-y.txt`](starter/cardinality-is-the-constraint-that-decides-y.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/cardinality-is-the-constraint-that-decides-y.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
