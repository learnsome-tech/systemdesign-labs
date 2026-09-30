# m06l02 · Worked Design One: Scaling The Ticket Booking System

Module 6: Worked Designs End To End · lesson 6.2 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m06l02)

**Goal:** You can size the opening minute of a ticket sale, choose admission control as the design rather than an add on, partition by event while admitting the hot shard it creates, and say exactly what the waiting room costs the people standing in it.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l02-02](m06l02-02/) | Size the opening minute before choosing anything | Graded |
| [m06l02-04](m06l02-04/) | Three doors, one crowd, and the numbers each produces | Graded |
| [m06l02-06](m06l02-06/) | The scaled design, and where the lag becomes visible | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Design the door for a sale you have watched fail

1. Pick a real launch. Estimate arrivals in the first minute and the commit rate.
2. Choose bounded queue or waiting room, and write the number you tuned it to.
3. Say what a person sees while waiting, and what they see when refused.
4. Name the metric that proves the door is working rather than the system dying.

> **Hint:** The queue depth and the admission rate are the two numbers an operator needs during the sale. If neither is on a dashboard, nobody can tell a healthy wait from a stall.

## Check yourself

- Why does overload make the booking leader slower rather than just busier?
- What are the three doors, and what does each one do to the 1.1M people who miss out?
- Partitioning by event fixes what, and leaves what completely unfixed?
- Why does a buyer refreshing after purchase sometimes see no ticket, and what routing fixes it?
- Which two metrics distinguish a working waiting room from a system quietly stalling?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
