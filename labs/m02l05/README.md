# m02l05 · Consistency, And The Truth About CAP

Module 2: Data, Storage And State · lesson 2.5 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m02l05)

**Goal:** You can describe consistency as a client visible guarantee, state CAP correctly during a partition, and choose where a product may trade freshness for availability.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l05-02](m02l05-02/) | CAP applies during a partition | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Choose the partition behavior

1. For a payment, choose refusal or stale response and defend it.
2. For a social count, choose a fallback and name its limit.
3. Write the sentence a product manager should see during a partition.

## Check yourself

- What event makes CAP relevant?
- Why is availability a response policy rather than only an uptime percentage?
- How do read and write quorums reduce divergence?
- Why can one product choose different partition behavior for payments and counts?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
