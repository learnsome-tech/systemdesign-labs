# m04l05 · Backpressure And Load Shedding

Module 4: Resilience And Traffic Management · lesson 4.5 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m04l05)

**Goal:** You can bound work in flight, shed low value load before queues exhaust resources, and explain why admission control is kinder than late timeouts.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l05-02](m04l05-02/) | A shedder keeps the useful work alive | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Design the admission policy

1. List three request classes and rank their value during overload.
2. Set a queue bound and an age limit for each class.
3. Write the response for a request that is shed.

## Check yourself

- Why is a queue a promise rather than free capacity?
- Which work should be shed first during overload?
- What metrics reveal a queue that is failing slowly?
- Why must every boundary have a refusal path?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
