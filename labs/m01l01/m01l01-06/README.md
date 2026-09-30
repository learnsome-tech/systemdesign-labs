# m01l01-06 · Record the option you rejected

**Lesson:** [What A Design Is For, And How To Run A Design Discussion](https://learnsome.tech/learn/systemdesign-course/m01l01) (lesson 1.1, module 1: Foundations And Estimation) · Free  
**Check:** Read along

## Goal

You can explain what a system design is actually for, run a forty five minute design discussion in the right order, and record a decision together with the option you rejected and the cost you accepted.

In the lesson: When a decision is made, write it down in four lines: the context, the decision, the option you rejected, and the consequence you accepted. This short record is worth more than the diagram. The decision line tells a future engineer what is true. The rejected line tells them what was already considered, which is what stops the same argument being re-run every few months by somebody with a fresh opinion. And the consequence line is the honest one: it names the new problem the decision created. Here, choosing a relational database with a read replica bought multi row transactions and cost visible replica lag after a write. Both halves are true, and a design that records only the first half will be read as a promise it cannot keep.

## Files

- [`starter/record-the-option-you-rejected.txt`](starter/record-the-option-you-rejected.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/record-the-option-you-rejected.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l01-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
