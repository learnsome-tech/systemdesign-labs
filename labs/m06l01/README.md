# m06l01 · Worked Design One: Ticket Booking, Correctness First

Module 6: Worked Designs End To End · lesson 6.1 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m06l01)

**Goal:** You can design a ticket booking system that sells each seat exactly once, starting from written requirements and a spike estimate rather than a diagram, choosing relational storage for the multi row transaction, and guarding the seat row with either a row lock or a version column.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l01-02](m06l01-02/) | Estimate the spike, because the mean is a lie here | Graded |
| [m06l01-04](m06l01-04/) | The design on one screen | Read along |
| [m06l01-06](m06l01-06/) | The race, run twice: unguarded, then versioned | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Guard one contended write in your own schema

1. Find a table where two writers can pick the same row. Name the row and its state.
2. Write the pessimistic guard: the locking read, and who waits for whom.
3. Write the optimistic guard: the version column, and what the loser is told.
4. State your hold expiry, and name the job that reclaims a hold nobody paid for.

> **Hint:** If you cannot name the process that reclaims expired holds, your inventory leaks. A scheduled sweep is an answer; having no answer is not.

## Check yourself

- Why is the opening-minute spike, not the daily mean, the number this design is built around?
- Which parts of one sale must move together, and which store hands you that transaction?
- What is a lost update, and what are the two correct guards against it?
- What does an idempotency key on the payment call buy you, and what does it not buy?
- What does an operator actually observe when holds never expire?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
