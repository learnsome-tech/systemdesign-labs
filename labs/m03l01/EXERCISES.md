# Exercises — Caching Strategies And Topology

Lesson `m03l01` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l01)

## Exercise 1: Find your real hit ratio, then your cold origin load

1. Measure one real cache hit ratio over a whole week, not over a good hour.
2. Compute origin queries a second at that ratio, and at ten points lower.
3. Decide whether the origin survives the cold number, and write the answer down.
4. Name the layer each cached value belongs in, and who is responsible for deleting it.

> **Hint**: If nobody can name who deletes a key, that value has no invalidation story and its time to live is the only safety net it has.


---

© LearnSome.tech · support@iwantto.learnsome.tech
