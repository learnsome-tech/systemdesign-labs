# m05l03-03 · Little's law, and why pools exhaust without extra traffic

**Lesson:** [Capacity Planning As A Design Input](https://learnsome.tech/learn/systemdesign-course/m05l03) (lesson 5.3, module 5: Architecture And Operations) · Pro  
**Check:** Read along

## Goal

You can explain why a queueing system is never run near saturation, size pools with Little's law, plan for peak plus the loss of one failure domain, and say what autoscaling cannot do for you.

In the lesson: Little's law is the other piece of arithmetic you need, and it is one line: the number of things inside a system equals the rate they arrive times the time each one spends inside. Apply it to a thread pool. Two hundred threads, fifty milliseconds a request, and you can serve four thousand requests a second. Now a dependency gets slower and each request spends two hundred milliseconds instead of fifty. Traffic has not changed at all, but the concurrency you need has quadrupled, so your pool of two hundred is full, arrivals queue behind it, and the queue makes the time in the system longer still. That is why saturation of pools is a golden signal, and why the timeouts from the resilience module are what stop this loop.

## Files

- [`starter/little-s-law-and-why-pools-exhaust-without-e.py`](starter/little-s-law-and-why-pools-exhaust-without-e.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/little-s-law-and-why-pools-exhaust-without-e.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
