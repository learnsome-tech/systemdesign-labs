# Exercises — Load Balancing And The Failure Modes It Introduces

Lesson `m04l01` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m04l01)

## Exercise 1: Audit the balancer you already run

1. Name the algorithm your balancer uses today, and find out who chose it and why.
2. Read the health check handler: does it touch the dependencies a real request needs?
3. Work out how much capacity one unhealthy verdict removes, as a fraction of the pool.
4. Find the key that stickiness pins to one backend, and say what its failure looks like.

> **Hint**: If the check and a real request do not touch the same dependencies, write down the outage the difference allows, then make the check touch one of them.


---

© LearnSome.tech · support@iwantto.learnsome.tech
