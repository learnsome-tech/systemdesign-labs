# m03l03-03 · The parts of a queue, and one honest sentence

**Lesson:** [Queues, Events And Asynchronous Work](https://learnsome.tech/learn/systemdesign-course/m03l03) (lesson 3.3, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can decide what belongs on the request path and what belongs behind a queue, name the parts of a queue and what each one protects, and use Little's law to tell a buffering queue apart from a failing one.

In the lesson: The vocabulary is small. A producer puts messages in. A consumer group takes them out, and adding members to the group is how you scale consumption. When a consumer picks up a message the message becomes invisible to everyone else for a visibility timeout, so two workers do not do the same job, and if the worker dies without acknowledging, the message reappears. The acknowledgement is the only signal that work actually finished, which is why acknowledging on receipt rather than on completion is such a common and such an expensive mistake. A message that keeps failing goes to a dead letter queue so it stops blocking the line. And then the honest sentence, which people resist: a queue is a buffer. A buffer smooths a burst. It is not extra capacity.

## Files

- [`starter/the-parts-of-a-queue-and-one-honest-sentence.txt`](starter/the-parts-of-a-queue-and-one-honest-sentence.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-parts-of-a-queue-and-one-honest-sentence.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
