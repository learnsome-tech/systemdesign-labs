# m06l06-02 · Partition consumers by work, not by host count

**Lesson:** [Worked Design Three: Scaling The Metrics Pipeline](https://learnsome.tech/learn/systemdesign-course/m06l06) (lesson 6.6, module 6: Worked Designs End To End) · Pro  
**Check:** Read along

## Goal

You can scale metrics ingestion with tenant quotas, partition-aware consumers, hot label controls, and backpressure while stating the final system trade-off.

In the lesson: Consumer parallelism is bounded by the number of partitions, not by the number of hosts you happen to run. Rebalancing moves ownership and loses local cache warmth, so it is a cost during an incident. A hot tenant may need a split across buckets or a quota that protects other tenants. Watch lag per partition and make it drive admission: when the lag budget is exceeded, shed low value samples or slow the tenant before the queue consumes every worker.

## Files

- [`starter/partition-consumers-by-work-not-by-host-coun.txt`](starter/partition-consumers-by-work-not-by-host-coun.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/partition-consumers-by-work-not-by-host-coun.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l06-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
