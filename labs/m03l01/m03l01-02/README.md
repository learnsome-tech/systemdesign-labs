# m03l01-02 · Six places a cache can live, from the user inwards

**Lesson:** [Caching Strategies And Topology](https://learnsome.tech/learn/systemdesign-course/m03l01) (lesson 3.1, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can place a cache at the right layer, choose a read and write strategy while naming what it costs, and size the origin for the miss rate instead of the hit ratio.

In the lesson: There are six places a cache can live, and they line up from the user inwards. The browser holds a copy you cannot reach once you have sent it. A content delivery network edge holds public bytes near the user, which is why it serves images and a price list beautifully and must never serve a bank balance. A reverse proxy in front of your own servers can hold whole responses. Inside the process, a plain dictionary is the fastest cache that exists. Then a shared remote cache, usually Redis, which every server can see and every server can delete from. And finally the database itself, which has been caching pages in its buffer pool the entire time you were arguing about the others. Each step outwards is faster and less controllable, and that trade is the whole topology decision.

## Files

- [`starter/six-places-a-cache-can-live-from-the-user-in.txt`](starter/six-places-a-cache-can-live-from-the-user-in.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/six-places-a-cache-can-live-from-the-user-in.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
