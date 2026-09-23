# Exercises — Latency Numbers Every Engineer Should Know

Lesson `m01l05` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m01l05)

## Exercise 1: Budget your own request path

1. Take one real endpoint. List its hops and give each a millisecond cost.
2. Mark which hops are serial and which genuinely run in parallel.
3. Compute the tail probability from the number of parallel calls it makes.
4. Name the one hop to remove, and say what removing it costs elsewhere.

> **Hint**: A hop you cannot cost is a hop you cannot defend. Measure it once, or label it a guess and mark it as the first thing to measure.


---

© LearnSome.tech · support@iwantto.learnsome.tech
