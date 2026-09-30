# m01l02 · Requirements: The Constraints That Shape The System

Module 1: Foundations And Estimation · lesson 1.2 · Free · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m01l02)

**Goal:** You can separate functional requirements from the non-functional constraints that actually shape a system, turn an availability target into a monthly downtime budget, and show why availability multiplies along a chain of hard dependencies.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l02-03](m01l02-03/) | Each constraint rules out a family of designs | Read along |
| [m01l02-04](m01l02-04/) | An availability target is a downtime budget | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Turn a product promise into constraints

1. Take a checkout flow. Write its latency target as a percentile and a number.
2. List its hard dependencies, then compute the ceiling their product gives you.
3. Pick one hard dependency and describe how to degrade without it.
4. State which data must be durable and which may be stale, and for how long.

> **Hint:** If degrading is impossible for a dependency, say so. A dependency that truly cannot be degraded is your availability ceiling, and it belongs at the top of the design document.

## Check yourself

- Why do functional requirements rarely decide an architecture?
- Name the six non-functional constraints, and say what a latency target forbids.
- Five hard dependencies at ninety nine point nine percent give you what, and why?
- What is the difference between a hard and a soft dependency, in one sentence?
- Which two constraints are most often left unwritten, and what spends them?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
