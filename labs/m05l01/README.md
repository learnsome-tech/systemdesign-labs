# m05l01 · Monolith Versus Services: The Honest Trade Offs

Module 5: Architecture And Operations · lesson 5.1 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m05l01)

**Goal:** You can argue the monolith and services decision from data ownership and team boundaries rather than fashion, price a split in latency and availability, and recognise a distributed monolith before you ship one.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l01-03](m05l01-03/) | And what it costs, itemised | Read along |
| [m05l01-05](m05l01-05/) | Price the split instead of arguing about it | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Extract one thing with the strangler pattern

1. Pick one module and name the tables only it writes. If none, stop here.
2. Put a facade in front, route one endpoint to a new service, leave the rest.
3. Write the contract first: request, response, errors, timeout, idempotency key.
4. Name what you can no longer do in one transaction, and what replaces it.

> **Hint:** The strangler pattern works because every step is reversible. If you cannot route one endpoint back to the monolith in a minute, you have cut in the wrong place.

## Check yourself

- Which of the four benefits of splitting are really about people rather than machines?
- Four services at 99.9% each: what is the composed availability, and how many minutes a month is that?
- Why does a shared database cancel the independent-deployment benefit you split to get?
- What two things should a service boundary follow, and which popular criterion should it ignore?
- Name three signs, visible during an outage, that you are running a distributed monolith.

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
