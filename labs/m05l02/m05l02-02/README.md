# m05l02-02 · Three signals, three different questions

**Lesson:** [Observability As A Design Input](https://learnsome.tech/learn/systemdesign-course/m05l02) (lesson 5.2, module 5: Architecture And Operations) · Pro  
**Check:** Read along

## Goal

You can decide at design time what a system must emit, choose labels that respect cardinality, record latency as a histogram rather than a mean, and turn a service level objective into an error budget with a burn rate.

In the lesson: Three signals, and they answer different questions, so arguing about which is best is a category error. A metric is an aggregate: a counter or a histogram, cheap and fixed in cost no matter how much traffic you have, and it tells you nothing about any individual request. A log is one specific event described in full, which is what you want when a named customer says their order vanished, and which becomes ruinous at high volume. A trace follows one request across a fan out and attributes the time to each hop, which is the only signal that answers where did the time go. Design by starting from the question you expect to ask while half awake, then choose the signal that can answer it, and emit that.

## Files

- [`starter/three-signals-three-different-questions.txt`](starter/three-signals-three-different-questions.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/three-signals-three-different-questions.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
