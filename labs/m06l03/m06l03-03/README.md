# m06l03-03 · The design on one screen: gateways, registry, store

**Lesson:** [Worked Design Two: A Global Chat System](https://learnsome.tech/learn/systemdesign-course/m06l03) (lesson 6.3, module 6: Worked Designs End To End) · Pro  
**Check:** Read along

## Goal

You can design a chat system from written requirements and a connection estimate, route a message through a gateway registry to a partitioned store, order a conversation with a per conversation sequence instead of a clock, and make a client resend harmless with an idempotency key.

In the lesson: Here is the design. Gateway pods terminate the sockets and hold no durable state, which is what lets you restart them. A registry maps a user to the gateway currently holding their connection, and it is a key value store with short lived entries, which is module two lesson two making a very specific choice: this data is small, hot, looked up by exact key, and worthless after a minute. The message service writes to a conversation store partitioned by conversation, so everything one thread needs lands in one place. A recipient who is connected gets a push through their gateway. A recipient who is not gets a row in a per user inbox and collects it when they return. Every arrow on that diagram is either a socket, a lookup, or an append.

## Files

- [`starter/the-design-on-one-screen-gateways-registry-s.txt`](starter/the-design-on-one-screen-gateways-registry-s.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-design-on-one-screen-gateways-registry-s.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
