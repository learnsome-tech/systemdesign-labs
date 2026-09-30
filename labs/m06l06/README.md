# m06l06 · Worked Design Three: Scaling The Metrics Pipeline

Module 6: Worked Designs End To End · lesson 6.6 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m06l06)

**Goal:** You can scale metrics ingestion with tenant quotas, partition-aware consumers, hot label controls, and backpressure while stating the final system trade-off.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l06-02](m06l06-02/) | Partition consumers by work, not by host count | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Stress the biggest tenant

1. Double one tenant's sample rate and find the first saturated resource.
2. Choose a quota, split, or sampling response.
3. State which query promise becomes weaker under pressure.

## Check yourself

- Which dimensions determine ingest and query capacity?
- Why does adding hosts not automatically add consumer parallelism?
- Where should cardinality limits be enforced?
- What is the final failure mode when tenant budgets are absent?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
