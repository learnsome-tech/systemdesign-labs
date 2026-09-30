# m02l05-02 · CAP applies during a partition

**Lesson:** [Consistency, And The Truth About CAP](https://learnsome.tech/learn/systemdesign-course/m02l05) (lesson 2.5, module 2: Data, Storage And State) · Pro  
**Check:** Read along

## Goal

You can describe consistency as a client visible guarantee, state CAP correctly during a partition, and choose where a product may trade freshness for availability.

In the lesson: CAP is about a network partition, when replicas cannot communicate. During that partition, a system cannot both guarantee that every read sees one consistent ordering and also guarantee that every request receives a useful response. It must choose which behavior to preserve. The slogan is not a claim that a system gets only two letters in normal operation, and it says nothing by itself about latency or durability. Outside a partition, you can often provide both consistency and availability. The design question is what the user sees while the link is broken.

## Files

- [`starter/cap-applies-during-a-partition.txt`](starter/cap-applies-during-a-partition.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/cap-applies-during-a-partition.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
