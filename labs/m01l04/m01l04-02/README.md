# m01l04-02 · Estimate a row honestly, then stop refining it

**Lesson:** [Back Of The Envelope Estimation: Storage And Bandwidth](https://learnsome.tech/learn/systemdesign-course/m01l04) (lesson 1.4, module 1: Foundations And Estimation) · Free  
**Check:** Read along

## Goal

You can estimate stored bytes from a row size, a write rate and a retention window, apply index and replication multipliers, size shards from the result, and convert read traffic into egress bandwidth.

In the lesson: To size one record, count its fields and be honest but quick. An identifier is about sixteen bytes, a timestamp eight, a short text body a couple of hundred, a handful of flags a few more. Add roughly a third on top for row overhead, alignment and the small bookkeeping every storage engine does, then stop refining. The difference between three hundred and four hundred bytes will not change a single design decision, while the difference between four hundred bytes and four hundred kilobytes changes everything, and that is the mistake to look for. Large binary objects are counted separately, because pictures and video do not belong inside the row in the first place.

## Files

- [`starter/estimate-a-row-honestly-then-stop-refining-i.txt`](starter/estimate-a-row-honestly-then-stop-refining-i.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/estimate-a-row-honestly-then-stop-refining-i.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
