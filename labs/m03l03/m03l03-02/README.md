# m03l03-02 · Commands and events couple you differently

**Lesson:** [Queues, Events And Asynchronous Work](https://learnsome.tech/learn/systemdesign-course/m03l03) (lesson 3.3, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can decide what belongs on the request path and what belongs behind a queue, name the parts of a queue and what each one protects, and use Little's law to tell a buffering queue apart from a failing one.

In the lesson: There are two kinds of message and they are not interchangeable. A command is an instruction with a name and an owner: charge this card, send this email, resize this image. Exactly one consumer should carry it out, exactly once, and the producer knows what it is asking for. An event is a statement of fact in the past tense: an order was placed. It names no handler. Anybody may subscribe, nobody is obliged to, and the producer does not know or care who listens. That difference is the entire coupling story. Commands give you a clear owner and a tight dependency. Events let you add the fifth consumer of an order without touching the code that places orders, at the price that no single person can any longer tell you what happens when an order is placed.

## Files

- [`starter/commands-and-events-couple-you-differently.txt`](starter/commands-and-events-couple-you-differently.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/commands-and-events-couple-you-differently.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
