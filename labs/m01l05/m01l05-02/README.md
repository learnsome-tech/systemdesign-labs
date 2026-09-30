# m01l05-02 · The list, in one screen

**Lesson:** [Latency Numbers Every Engineer Should Know](https://learnsome.tech/learn/systemdesign-course/m01l05) (lesson 1.5, module 1: Foundations And Estimation) · Free  
**Check:** Read along

## Goal

You can recite the latency numbers that matter, compose a request budget from them, explain why the speed of light sets a floor no engineering removes, and show how fan out turns a good tail latency into a bad user experience.

In the lesson: Here is the list. A cache reference is about a nanosecond and a main memory reference about a hundred. Compressing a kilobyte is a couple of microseconds. Reading a megabyte from memory is about three microseconds, from flash about half a millisecond, and from a spinning disk about five milliseconds. A random read on flash is around a hundred microseconds, a disk seek is ten milliseconds, and a round trip inside one datacentre is about half a millisecond. And the last line, a round trip across an ocean, is a hundred and fifty milliseconds. Those ten lines are the whole vocabulary. Say them until the gaps between them feel obvious, because it is the gaps, not the values, that decide designs.

## Files

- [`starter/the-list-in-one-screen.txt`](starter/the-list-in-one-screen.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-list-in-one-screen.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
