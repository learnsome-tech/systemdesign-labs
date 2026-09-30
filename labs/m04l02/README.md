# m04l02 · Timeouts, And Avoiding Cascaded Failure

Module 4: Resilience And Traffic Management · lesson 4.2 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m04l02)

**Goal:** You can budget timeouts from a request deadline, propagate the remaining budget across hops, and prevent a slow dependency from consuming every worker.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l02-02](m04l02-02/) | Budget a chain from the outside in | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Find the unbounded wait

1. Draw one request path and mark every serial and parallel hop.
2. Give the path a deadline and subtract each reservation.
3. Name the queue or connection that must be bounded.

## Check yourself

- Why should a deadline cross service boundaries?
- How do retries make a slow dependency worse?
- What should be bounded besides request duration?
- Which trace field explains a timeout on an otherwise healthy hop?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
