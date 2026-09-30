# m02l03-02 · Leader and followers make the route explicit

**Lesson:** [Replication, Failover And Leader Election](https://learnsome.tech/learn/systemdesign-course/m02l03) (lesson 2.3, module 2: Data, Storage And State) · Pro  
**Check:** Read along

## Goal

You can choose a replication shape, route reads and writes around a leader, and explain the recovery cost and failure mode each replica introduces.

In the lesson: The common shape is one leader and several followers. The leader orders writes, and followers copy that order and serve reads when their lag is within the product budget. A user who writes and immediately reads needs a rule: route that session to the leader, wait until the follower has caught up, or accept that the old value may appear. Promotion after failure is not merely pointing a name at a new machine. You must fence the old leader so it cannot continue writing, then establish which sequence the new leader owns.

## Files

- [`starter/leader-and-followers-make-the-route-explicit.txt`](starter/leader-and-followers-make-the-route-explicit.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/leader-and-followers-make-the-route-explicit.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
