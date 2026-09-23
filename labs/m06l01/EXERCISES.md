# Exercises — Worked Design One: Ticket Booking, Correctness First

Lesson `m06l01` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m06l01)

## Exercise 1: Guard one contended write in your own schema

1. Find a table where two writers can pick the same row. Name the row and its state.
2. Write the pessimistic guard: the locking read, and who waits for whom.
3. Write the optimistic guard: the version column, and what the loser is told.
4. State your hold expiry, and name the job that reclaims a hold nobody paid for.

> **Hint**: If you cannot name the process that reclaims expired holds, your inventory leaks. A scheduled sweep is an answer; having no answer is not.


---

© LearnSome.tech · support@iwantto.learnsome.tech
