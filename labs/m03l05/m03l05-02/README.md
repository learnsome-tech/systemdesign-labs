# m03l05-02 · The idempotency key belongs to the intent

**Lesson:** [Idempotency, And Exactly Once As A Fiction](https://learnsome.tech/learn/systemdesign-course/m03l05) (lesson 3.5, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Read along

## Goal

You can make retries harmless with idempotency keys, distinguish deduplication from exactly once delivery, and place the durable record at the correct boundary.

In the lesson: The idempotency key belongs to the business intent, not to a network attempt. The client creates one key for one checkout, and the server stores that key with a request fingerprint, status, and result. The first request creates the payment and saves the result. A retry returns the saved result without creating another payment. Reusing the key with different input is a conflict, because silently accepting it would make the key mean two things. The record must live in durable storage for at least the longest retry and recovery window.

## Files

- [`starter/the-idempotency-key-belongs-to-the-intent.txt`](starter/the-idempotency-key-belongs-to-the-intent.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-idempotency-key-belongs-to-the-intent.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
