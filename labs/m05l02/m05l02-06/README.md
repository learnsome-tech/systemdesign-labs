# m05l02-06 · Two things that must be threaded through at build time

**Lesson:** [Observability As A Design Input](https://learnsome.tech/learn/systemdesign-course/m05l02) (lesson 5.2, module 5: Architecture And Operations) · Pro  
**Check:** Read along

## Goal

You can decide at design time what a system must emit, choose labels that respect cardinality, record latency as a histogram rather than a mean, and turn a service level objective into an error budget with a burn rate.

In the lesson: Two pieces of plumbing have to exist from the first day, because retrofitting them is a rewrite. The first is a request identifier, created at the edge and carried through every hop, including the ones that are not calls: a message on a queue, a scheduled job, a retry. Without it, a trace has holes exactly where the asynchronous work from module three happens. The second is a deadline. Not a timeout per hop, which the resilience module covered, but the remaining time carried with the request, so a service that receives it with two hundred milliseconds left can decline to start work that takes five hundred. Both of these travel in headers, both need the same treatment as an idempotency key from the APIs course, and both are free at design time and impossible later.

## Files

- [`starter/two-things-that-must-be-threaded-through-at-.py`](starter/two-things-that-must-be-threaded-through-at-.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/two-things-that-must-be-threaded-through-at-.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l02-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
