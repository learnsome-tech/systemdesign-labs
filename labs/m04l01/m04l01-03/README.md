# m04l01-03 · Four algorithms, and how each really behaves

**Lesson:** [Load Balancing And The Failure Modes It Introduces](https://learnsome.tech/learn/systemdesign-course/m04l01) (lesson 4.1, module 4: Resilience And Traffic Management) · Pro  
**Check:** Read along

## Goal

You can choose a balancing algorithm and a health check policy on evidence, say what layer four and layer seven each can see, and name the failure modes the balancer itself adds to the system.

In the lesson: Four algorithms cover almost every deployment. Round robin takes turns. It is fair in the number of requests and blind to the cost of them, which is fine when every request costs the same and is a problem the moment they do not. Least connections sends work to the shortest queue, which tracks real load, but it needs live state and that state is per balancer, so several balancers can agree to overload the same backend. Least request with two random choices picks two backends at random and sends to the lighter one, and it needs no coordination at all. Consistent hashing sends the same key to the same backend every time, which is how you keep a cache warm. Next, measure them.

## Files

- [`starter/four-algorithms-and-how-each-really-behaves.txt`](starter/four-algorithms-and-how-each-really-behaves.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/four-algorithms-and-how-each-really-behaves.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
