# m05l02 · Observability As A Design Input

Module 5: Architecture And Operations · lesson 5.2 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m05l02)

**Goal:** You can decide at design time what a system must emit, choose labels that respect cardinality, record latency as a histogram rather than a mean, and turn a service level objective into an error budget with a burn rate.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l02-02](m05l02-02/) | Three signals, three different questions | Read along |
| [m05l02-03](m05l02-03/) | Cardinality is the constraint that decides your labels | Read along |
| [m05l02-05](m05l02-05/) | What an average hides, in one sample | Graded |
| [m05l02-06](m05l02-06/) | Two things that must be threaded through at build time | Read along |
| [m05l02-07](m05l02-07/) | The error budget, and the burn rate that spends it | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Write the emission contract for one service

1. List the four golden signals for one service, with the exact metric names.
2. Write its label set, then count the series it produces at full cardinality.
3. Name one objective, its window, and the budget in minutes a month.
4. Write the question you asked in the last incident, and which signal answers it.

> **Hint:** If counting the series makes you nervous, move that label into the log line. Metrics answer how many; logs and traces answer which one.

## Check yourself

- Which signal answers 'where did the 2 seconds go?', and which answers 'what happened to order 4471'?
- Why does adding customer_id as a metric label cost the product of the label values, not the sum?
- A mean of 72 ms with a median of 40 ms: what fraction of requests are above the mean, and why?
- An objective of 99.9% a month is how many minutes of budget, and what is a 4x burn rate?
- Why can a request identifier and a deadline not be added during the incident that needs them?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
