# m04l01 · Load Balancing And The Failure Modes It Introduces

Module 4: Resilience And Traffic Management · lesson 4.1 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m04l01)

**Goal:** You can choose a balancing algorithm and a health check policy on evidence, say what layer four and layer seven each can see, and name the failure modes the balancer itself adds to the system.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l01-02](m04l01-02/) | What each layer can see, and what that buys | Read along |
| [m04l01-03](m04l01-03/) | Four algorithms, and how each really behaves | Read along |
| [m04l01-04](m04l01-04/) | Round robin is fine until service times vary | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Audit the balancer you already run

1. Name the algorithm your balancer uses today, and find out who chose it and why.
2. Read the health check handler: does it touch the dependencies a real request needs?
3. Work out how much capacity one unhealthy verdict removes, as a fraction of the pool.
4. Find the key that stickiness pins to one backend, and say what its failure looks like.

> **Hint:** If the check and a real request do not touch the same dependencies, write down the outage the difference allows, then make the check touch one of them.

## Check yourself

- What can a layer 7 balancer do that a layer 4 balancer cannot, and what does it cost?
- Why does least connections behave badly across 4 independent balancer instances?
- Why is a /health handler that returns 200 from memory worse than no check at all?
- Consistent hashing keeps caches warm: what does it do to a tenant with 10x the traffic?
- In a pool of 3, what fraction of capacity does one unhealthy verdict remove?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
