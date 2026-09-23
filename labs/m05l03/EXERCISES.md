# Exercises — Capacity Planning As A Design Input

Lesson `m05l03` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m05l03)

## Exercise 1: Measure one node, then write the plan down

1. Load test one node to its knee. Record queries a second at your latency target.
2. Recompute the fleet for peak plus the loss of one zone, and round up.
3. Time your autoscaler end to end: alarm, schedule, start, warm, first useful work.
4. Write the monthly cost of that plan beside the cost of running hot.

> **Hint**: Per node capacity is the one number you may not estimate. Everything else in the plan is arithmetic on top of it, so a guess there propagates into every figure.


---

© LearnSome.tech · support@iwantto.learnsome.tech
