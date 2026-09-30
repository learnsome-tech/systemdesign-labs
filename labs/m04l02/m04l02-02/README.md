# m04l02-02 · Budget a chain from the outside in

**Lesson:** [Timeouts, And Avoiding Cascaded Failure](https://learnsome.tech/learn/systemdesign-course/m04l02) (lesson 4.2, module 4: Resilience And Traffic Management) · Pro  
**Check:** Read along

## Goal

You can budget timeouts from a request deadline, propagate the remaining budget across hops, and prevent a slow dependency from consuming every worker.

In the lesson: Budget a chain from the outside in. Start with the user visible tail target, reserve time for queueing and serialization, then divide what remains among serial and parallel calls. Parallel calls share one deadline, so the slowest one controls the result. A serial write spends the budget after the reads have already consumed theirs. Leave a margin for variance rather than allocating every millisecond. If the sum does not fit, remove a hop, make the work asynchronous, or change the product promise. A timeout cannot make an impossible path possible.

## Files

- [`starter/budget-a-chain-from-the-outside-in.txt`](starter/budget-a-chain-from-the-outside-in.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/budget-a-chain-from-the-outside-in.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
