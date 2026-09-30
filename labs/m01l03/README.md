# m01l03 · Back Of The Envelope Estimation: Traffic And Throughput

Module 1: Foundations And Estimation · lesson 1.3 · Free · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m01l03)

**Goal:** You can turn a user count into mean and peak queries a second, apply a peak factor and a read to write ratio, convert throughput into a server count, and state every assumption you used out loud.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l03-03](m01l03-03/) | Two rounding rules that make this mental arithmetic | Read along |
| [m01l03-04](m01l03-04/) | From users to queries a second, and then to servers | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Estimate a system you use

1. Pick a product. State daily actives, reads and writes per user, and a peak factor.
2. Compute mean and peak queries a second using the hundred thousand seconds rule.
3. Convert peak reads into servers, then add headroom for one zone lost.
4. Say which single assumption changes the answer by ten times if you are wrong.

> **Hint:** Do it in your head first and write the answer down, then run the arithmetic. When the two disagree by more than a factor of three, find out why before you trust either.

## Check yourself

- How many seconds are in a day, what do you round it to, and what does a million a day become?
- Which of the four estimation inputs should be measured rather than guessed, and why?
- Why is capacity computed at exactly peak load a problem during a deployment?
- What does a ratio of fifteen reads to one write tell you to build, and what does it tell you not to bother with?
- Name the symptom of a system sized for the mean rather than the peak.

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
