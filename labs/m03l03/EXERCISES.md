# Exercises — Queues, Events And Asynchronous Work

Lesson `m03l03` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l03)

## Exercise 1: Move one thing off your request path, and watch it

1. List one endpoint's work and mark what the user must see before you reply.
2. Move one item behind a queue, returning 202 with a status URL to poll.
3. Chart queue depth and oldest message age, and alert on age, not on depth.
4. Compute the drain rate you need so depth returns to zero between bursts.

> **Hint**: Alert on the age of the oldest unprocessed message: depth alone cannot tell a fast deep queue from a slow shallow one.


---

© LearnSome.tech · support@iwantto.learnsome.tech
