# m06l01-04 · The design on one screen

**Lesson:** [Worked Design One: Ticket Booking, Correctness First](https://learnsome.tech/learn/systemdesign-course/m06l01) (lesson 6.1, module 6: Worked Designs End To End) · Pro  
**Check:** Read along

## Goal

You can design a ticket booking system that sells each seat exactly once, starting from written requirements and a spike estimate rather than a diagram, choosing relational storage for the multi row transaction, and guarding the seat row with either a row lock or a version column.

In the lesson: Here is the design on one screen, and every box is something an earlier module already named. Browsing reads a cached seat map and a read replica, because a slightly stale map is acceptable and cheap. Buying goes through the booking API to the leader, because only the leader can commit the transaction that moves a seat from held to sold. The payment gateway sits outside your trust boundary, so the call to it carries an idempotency key, which is module three lesson five spent rather than described. Confirmation email and ticket rendering hang off a queue, because nobody needs a rendered ticket before the seat is theirs. In the language of the Kubernetes course, each of those boxes is a deployment, and the database is the one thing that is not.

## Files

- [`starter/the-design-on-one-screen.txt`](starter/the-design-on-one-screen.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-design-on-one-screen.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
