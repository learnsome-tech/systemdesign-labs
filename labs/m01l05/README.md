# m01l05 · Latency Numbers Every Engineer Should Know

Module 1: Foundations And Estimation · lesson 1.5 · Free · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m01l05)

**Goal:** You can recite the latency numbers that matter, compose a request budget from them, explain why the speed of light sets a floor no engineering removes, and show how fan out turns a good tail latency into a bad user experience.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l05-02](m01l05-02/) | The list, in one screen | Read along |
| [m01l05-04](m01l05-04/) | Composing a request budget out of hops | Graded |
| [m01l05-06](m01l05-06/) | Fan out turns a good tail into a bad experience | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Budget your own request path

1. Take one real endpoint. List its hops and give each a millisecond cost.
2. Mark which hops are serial and which genuinely run in parallel.
3. Compute the tail probability from the number of parallel calls it makes.
4. Name the one hop to remove, and say what removing it costs elsewhere.

> **Hint:** A hop you cannot cost is a hop you cannot defend. Measure it once, or label it a guess and mark it as the first thing to measure.

## Check yourself

- Roughly how long is a main memory reference, an SSD random read, and a datacentre round trip?
- What are the three ratios, and which optimisation does each one justify?
- Why is a hundred and fifty milliseconds the honest figure for an intercontinental round trip?
- If one call in a hundred is slow, what fraction of hundred way fan out requests are slow, and why?
- What three fixes follow from budgeting at the tail rather than the median?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
