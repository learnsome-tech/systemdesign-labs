# m05l03 · Capacity Planning As A Design Input

Module 5: Architecture And Operations · lesson 5.3 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m05l03)

**Goal:** You can explain why a queueing system is never run near saturation, size pools with Little's law, plan for peak plus the loss of one failure domain, and say what autoscaling cannot do for you.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l03-02](m05l03-02/) | The knee: why you never run a queue hot | Graded |
| [m05l03-03](m05l03-03/) | Little's law, and why pools exhaust without extra traffic | Read along |
| [m05l03-06](m05l03-06/) | A capacity plan you can defend | Graded |
| [m05l03-07](m05l03-07/) | Autoscaling cannot outrun its own reaction time | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Measure one node, then write the plan down

1. Load test one node to its knee. Record queries a second at your latency target.
2. Recompute the fleet for peak plus the loss of one zone, and round up.
3. Time your autoscaler end to end: alarm, schedule, start, warm, first useful work.
4. Write the monthly cost of that plan beside the cost of running hot.

> **Hint:** Per node capacity is the one number you may not estimate. Everything else in the plan is arithmetic on top of it, so a guess there propagates into every figure.

## Check yourself

- Using 1/(1-p), what is the relative wait at 80%, 90% and 99% utilisation?
- A pool of 200 threads serves 50 ms requests. What happens to concurrency when they take 200 ms?
- Why does planning across 3 zones cost 50% overhead while 2 zones costs 100%?
- Why can capacity for state not be added during the spike that needs it?
- Name each step in an autoscaler's reaction chain, and say why a spike outruns all of them.

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
