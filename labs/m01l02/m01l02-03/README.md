# m01l02-03 · Each constraint rules out a family of designs

**Lesson:** [Requirements: The Constraints That Shape The System](https://learnsome.tech/learn/systemdesign-course/m01l02) (lesson 1.2, module 1: Foundations And Estimation) · Free  
**Check:** Read along

## Goal

You can separate functional requirements from the non-functional constraints that actually shape a system, turn an availability target into a monthly downtime budget, and show why availability multiplies along a chain of hard dependencies.

In the lesson: The useful way to read a requirement is to ask what it forbids. A tail latency target of one hundred milliseconds forbids a synchronous call to another continent, because the speed of light has already spent most of your budget. A promise never to lose a payment forbids acknowledging that payment from memory before it is durably stored. A statement that reads may be a few seconds stale permits replicas, caches and asynchronous fan out, all at once, and that single sentence is often worth more than every other requirement combined. Requirements are not a wish list to be satisfied. They are a set of constraints that shrink the space of possible designs until the remaining space is small enough to reason about.

## Files

- [`starter/each-constraint-rules-out-a-family-of-design.txt`](starter/each-constraint-rules-out-a-family-of-design.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/each-constraint-rules-out-a-family-of-design.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
