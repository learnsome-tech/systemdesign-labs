# m02l06 · Eventual Consistency And What It Costs A Product

Module 2: Data, Storage And State · lesson 2.6 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m02l06)

**Goal:** You can model an eventual consistency race, identify the product cost of stale state, and add read routing or reconciliation where the user cannot tolerate surprise.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l06-02](m02l06-02/) | A read can lose a write without losing data | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Spend a staleness budget

1. Choose a user journey and set its maximum visible age.
2. Name the route when a write is followed by a read.
3. Describe the message shown when the bound is exceeded.

## Check yourself

- What does eventual consistency promise, and what does it leave unspecified?
- How can a user create a duplicate from a stale read?
- Why is a read from the leader a useful post write rule?
- What measurements make a repair path operable?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
