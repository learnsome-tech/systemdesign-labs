# m04l04 · Circuit Breakers

Module 4: Resilience And Traffic Management · lesson 4.4 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m04l04)

**Goal:** You can use a circuit breaker to stop repeated work against a failing dependency, choose a safe probe policy, and explain the degraded behavior it exposes.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l04-02](m04l04-02/) | The breaker changes the shape of failure | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Choose the degraded response

1. Pick a dependency and define its closed, open, and half open behavior.
2. Name the fallback that is safe for the product.
3. State which error must never be hidden by a fallback.

## Check yourself

- What work does an open breaker prevent?
- Why is a breaker local knowledge rather than a global truth?
- What makes a half open probe safe?
- Which product errors must not be hidden by fallback data?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
