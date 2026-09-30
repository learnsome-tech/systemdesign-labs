# m05l03-07 · Autoscaling cannot outrun its own reaction time

**Lesson:** [Capacity Planning As A Design Input](https://learnsome.tech/learn/systemdesign-course/m05l03) (lesson 5.3, module 5: Architecture And Operations) · Pro  
**Check:** Read along

## Goal

You can explain why a queueing system is never run near saturation, size pools with Little's law, plan for peak plus the loss of one failure domain, and say what autoscaling cannot do for you.

In the lesson: Autoscaling is a cost control, not a resilience mechanism, and the reason is its reaction time. Trace the chain: a metric is scraped and averaged, a threshold is crossed, a decision is made, an instance is scheduled, a process starts, connections are established, and only then does a cache warm up enough for that instance to be worth as much as its neighbours. That is minutes. A spike is seconds. So the new capacity arrives after the incident, and worse, while it is warming it is slower than the machines it came to help, so adding it briefly raises your latency. Autoscaling is excellent at following a daily shape and at shrinking overnight, which is real money. What absorbs the spike is headroom, and what protects you when the headroom runs out is shedding.

## Files

- [`starter/autoscaling-cannot-outrun-its-own-reaction-t.txt`](starter/autoscaling-cannot-outrun-its-own-reaction-t.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/autoscaling-cannot-outrun-its-own-reaction-t.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l03-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
