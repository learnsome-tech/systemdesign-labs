<img src="https://learnsome.tech/logo.png" width="48" alt="LearnSome.tech">

# Scalable System Design & Distributed Architecture

6 modules, 30 lessons: Foundations And Estimation; Data, Storage And State; Caching, Queues And Asynchrony; Resilience And Traffic Management; Architecture And Operations; Worked Designs End To End.

## Watch and read

- **Course page**: [https://learnsome.tech/courses/systemdesign-course](https://learnsome.tech/courses/systemdesign-course)
- **Video player**: [https://learnsome.tech/courses/systemdesign-course/watch](https://learnsome.tech/courses/systemdesign-course/watch)
- **Handbook PDF**: [https://learnsome.tech/handbooks/systemdesign/book.pdf](https://learnsome.tech/handbooks/systemdesign/book.pdf)
- **On-site handbook**: [https://learnsome.tech/courses/systemdesign-course/book](https://learnsome.tech/courses/systemdesign-course/book)

## What is in this repository

This repository contains code artifacts, exercises and reference files for the lessons in this course.
30 lessons include a `labs/<lessonId>/` folder.
Each folder is named after the lesson identifier (e.g. `labs/m01l01/`) and contains the
artifact files shown in the course video, an `EXERCISES.md` with hands-on tasks, and
sub-directories named by artifact reference (e.g. `m01l01-02/`).

## Lessons

| # | Lesson | Watch | Labs | Handbook |
|---|--------|-------|------|----------|
| | **Foundations And Estimation** | | | |
| 1 | What A Design Is For, And How To Run A Design Discussion | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m01l01) | [labs/m01l01/](labs/m01l01/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-1-1) |
| 2 | Requirements: The Constraints That Shape The System | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m01l02) | [labs/m01l02/](labs/m01l02/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-1-2) |
| 3 | Back Of The Envelope Estimation: Traffic And Throughput | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m01l03) | [labs/m01l03/](labs/m01l03/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-1-3) |
| 4 | Back Of The Envelope Estimation: Storage And Bandwidth | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m01l04) | [labs/m01l04/](labs/m01l04/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-1-4) |
| 5 | Latency Numbers Every Engineer Should Know | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m01l05) | [labs/m01l05/](labs/m01l05/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-1-5) |
| | **Data, Storage And State** | | | |
| 6 | The Storage Decision: Relational Versus Document | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m02l01) | [labs/m02l01/](labs/m02l01/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-2-1) |
| 7 | The Storage Decision: Key Value, Search And Blob | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m02l02) | [labs/m02l02/](labs/m02l02/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-2-2) |
| 8 | Replication, Failover And Leader Election | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m02l03) | [labs/m02l03/](labs/m02l03/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-2-3) |
| 9 | Partitioning, Sharding And Hot Keys | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m02l04) | [labs/m02l04/](labs/m02l04/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-2-4) |
| 10 | Consistency, And The Truth About CAP | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m02l05) | [labs/m02l05/](labs/m02l05/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-2-5) |
| 11 | Eventual Consistency And What It Costs A Product | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m02l06) | [labs/m02l06/](labs/m02l06/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-2-6) |
| | **Caching, Queues And Asynchrony** | | | |
| 12 | Caching Strategies And Topology | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l01) | [labs/m03l01/](labs/m03l01/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-3-1) |
| 13 | Cache Invalidation And The Three Hard Cases | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l02) | [labs/m03l02/](labs/m03l02/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-3-2) |
| 14 | Queues, Events And Asynchronous Work | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l03) | [labs/m03l03/](labs/m03l03/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-3-3) |
| 15 | The Difference Between A Queue And A Log | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l04) | [labs/m03l04/](labs/m03l04/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-3-4) |
| 16 | Idempotency, And Exactly Once As A Fiction | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l05) | [labs/m03l05/](labs/m03l05/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-3-5) |
| | **Resilience And Traffic Management** | | | |
| 17 | Load Balancing And The Failure Modes It Introduces | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m04l01) | [labs/m04l01/](labs/m04l01/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-4-1) |
| 18 | Timeouts, And Avoiding Cascaded Failure | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m04l02) | [labs/m04l02/](labs/m04l02/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-4-2) |
| 19 | Retries, Backoff And Jitter | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m04l03) | [labs/m04l03/](labs/m04l03/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-4-3) |
| 20 | Circuit Breakers | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m04l04) | [labs/m04l04/](labs/m04l04/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-4-4) |
| 21 | Backpressure And Load Shedding | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m04l05) | [labs/m04l05/](labs/m04l05/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-4-5) |
| | **Architecture And Operations** | | | |
| 22 | Monolith Versus Services: The Honest Trade Offs | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m05l01) | [labs/m05l01/](labs/m05l01/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-5-1) |
| 23 | Observability As A Design Input | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m05l02) | [labs/m05l02/](labs/m05l02/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-5-2) |
| 24 | Capacity Planning As A Design Input | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m05l03) | [labs/m05l03/](labs/m05l03/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-5-3) |
| | **Worked Designs End To End** | | | |
| 25 | Worked Design One: Ticket Booking, Correctness First | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m06l01) | [labs/m06l01/](labs/m06l01/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-6-1) |
| 26 | Worked Design One: Scaling The Ticket Booking System | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m06l02) | [labs/m06l02/](labs/m06l02/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-6-2) |
| 27 | Worked Design Two: A Global Chat System | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m06l03) | [labs/m06l03/](labs/m06l03/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-6-3) |
| 28 | Worked Design Two: Scaling Chat Fan Out | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m06l04) | [labs/m06l04/](labs/m06l04/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-6-4) |
| 29 | Worked Design Three: A Metrics Ingestion Pipeline | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m06l05) | [labs/m06l05/](labs/m06l05/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-6-5) |
| 30 | Worked Design Three: Scaling The Metrics Pipeline | [▶](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m06l06) | [labs/m06l06/](labs/m06l06/) | [§](https://learnsome.tech/courses/systemdesign-course/book#lesson-6-6) |

## Exercises

Each lesson folder contains an `EXERCISES.md` with hands-on tasks drawn directly from the course material.
Open the file for a lesson to see the tasks and, where provided, hints.

---

© LearnSome.tech · support@iwantto.learnsome.tech
