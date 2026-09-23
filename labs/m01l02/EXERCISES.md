# Exercises — Requirements: The Constraints That Shape The System

Lesson `m01l02` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m01l02)

## Exercise 1: Turn a product promise into constraints

1. Take a checkout flow. Write its latency target as a percentile and a number.
2. List its hard dependencies, then compute the ceiling their product gives you.
3. Pick one hard dependency and describe how to degrade without it.
4. State which data must be durable and which may be stale, and for how long.

> **Hint**: If degrading is impossible for a dependency, say so. A dependency that truly cannot be degraded is your availability ceiling, and it belongs at the top of the design document.


---

© LearnSome.tech · support@iwantto.learnsome.tech
