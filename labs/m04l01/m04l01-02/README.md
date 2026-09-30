# m04l01-02 · What each layer can see, and what that buys

**Lesson:** [Load Balancing And The Failure Modes It Introduces](https://learnsome.tech/learn/systemdesign-course/m04l01) (lesson 4.1, module 4: Resilience And Traffic Management) · Pro  
**Check:** Read along

## Goal

You can choose a balancing algorithm and a health check policy on evidence, say what layer four and layer seven each can see, and name the failure modes the balancer itself adds to the system.

In the lesson: Here is the honest comparison. The transport balancer makes one choice when the connection opens and then forwards bytes, which is close to free and is why it scales to enormous volumes. But it cannot retry a request, because it does not know where one request ends and the next begins, and a client that holds a connection open for an hour stays pinned to whichever backend it landed on. The application balancer parses, so it can route by path, retry an idempotent call, add a header for tracing, and refuse a request outright. You pay for that in latency and in memory. If you have met Kubernetes, you have used both already: the Service is the transport one and the Ingress is the application one.

## Files

- [`starter/what-each-layer-can-see-and-what-that-buys.txt`](starter/what-each-layer-can-see-and-what-that-buys.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/what-each-layer-can-see-and-what-that-buys.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
