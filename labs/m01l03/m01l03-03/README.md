# m01l03-03 · Two rounding rules that make this mental arithmetic

**Lesson:** [Back Of The Envelope Estimation: Traffic And Throughput](https://learnsome.tech/learn/systemdesign-course/m01l03) (lesson 1.3, module 1: Foundations And Estimation) · Free  
**Check:** Read along

## Goal

You can turn a user count into mean and peak queries a second, apply a peak factor and a read to write ratio, convert throughput into a server count, and state every assumption you used out loud.

In the lesson: Two rules turn this into mental arithmetic. First, there are eighty six thousand four hundred seconds in a day, and you should call it a hundred thousand. That makes a million events a day about ten a second, a hundred million a day about a thousand a second, and a billion a day about ten thousand a second. Learn those three lines and most traffic questions are answered before you reach for anything. Second, work in powers of ten. Two hundred is a fine answer; two hundred and twelve is false precision that invites an argument about the wrong thing. Say which way you rounded, so nobody mistakes a convenient number for a measurement.

## Files

- [`starter/two-rounding-rules-that-make-this-mental-ari.txt`](starter/two-rounding-rules-that-make-this-mental-ari.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/two-rounding-rules-that-make-this-mental-ari.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
