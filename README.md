<p>
  <a href="https://learnsome.tech/courses/systemdesign-course">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/wordmark-inverse.svg">
      <img src=".github/assets/wordmark.svg" alt="LearnSome.tech" width="260">
    </picture>
  </a>
</p>

# Scalable System Design & Distributed Architecture

**Sharding, Replication, Event Streams & Microservice Contracts**

6 modules, 30 lessons: Foundations And Estimation; Data, Storage And State; Caching, Queues And Asynchrony; Resilience And Traffic Management; Architecture And Operations; Worked Designs End To End. Advanced level, about 2 hours.

This repository holds the labs of the LearnSome.tech course [Scalable System Design & Distributed Architecture](https://learnsome.tech/courses/systemdesign-course): each lab's starter files, a README with the goal, the steps and the expected output, and `./check`, which tests your work the way the site does.

## Start

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/learnsome-tech/systemdesign-labs?quickstart=1)

- **Codespaces:** the badge opens this repository in a dev container with Python 3.14.7, as in the site's lab sandbox.
- **On your machine:**

  ```sh
  git clone https://github.com/learnsome-tech/systemdesign-labs.git
  cd systemdesign-labs
  ./check m01l01-04
  ```

  You need Python 3 for `./check`, and for the labs themselves Python 3.14.7. Other versions mostly work, but only the sandbox's versions are sure to print what the site prints. VS Code's Dev Containers extension builds the same container as Codespaces (x86-64).

## Doing a lab

1. Open the lesson on LearnSome.tech and the lab folder beside it: `labs/<lesson>/<lab>/`. The lab README has the goal, the steps and the expected output.
2. Work in the lab's `starter/` folder.
3. From the repository root, run `./check <lab>` (for example `./check m01l01-04`), or `./check <lesson>` for all labs of a lesson, or `./check --all`. `./check --list` shows every lab and how it is checked.

`./check` runs your starter the way the site's lab sandbox does: in a scratch copy that is its working directory and `HOME`, with `LANG=C.UTF-8`, `TZ=UTC`, `input.txt` on standard input, 10 seconds and 256 KiB of output per stream. It then compares the output with the site's own rules, so a pass here is a pass on the site.

| Check | What `./check` does | Labs |
| --- | --- | --- |
| Graded | Runs the program and compares its output with `expected.txt`. | 30 |
| Read along | Nothing to run here: the site shows the listing read-only, and the lab README says honestly what it needs (Docker, a cluster, a cloud account...). | 40 |

## What is published, and what is not

Every lab's starter is the code the lesson shows on screen, which is also what the lab editor on the site opens with. Where that code is the whole program, such as a recorded shell session or a script from the video, it is published as it is: it is the lesson content. Nothing beyond the lesson is published. There are no reference solutions and no answers to the lesson exercises, and nothing the site keeps private.

Pro lessons' labs are here as starters too. LearnSome.tech runs and grades your labs in its sandbox, hosts the videos and keeps your progress; running and grading a Pro lab on the site needs Pro.

## Modules and lessons

### Module 1: Foundations And Estimation

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 1.1 | [What A Design Is For, And How To Run A Design Discussion](https://learnsome.tech/learn/systemdesign-course/m01l01) | [3 labs](labs/m01l01/) | Free |
| 1.2 | [Requirements: The Constraints That Shape The System](https://learnsome.tech/learn/systemdesign-course/m01l02) | [2 labs](labs/m01l02/) | Free |
| 1.3 | [Back Of The Envelope Estimation: Traffic And Throughput](https://learnsome.tech/learn/systemdesign-course/m01l03) | [2 labs](labs/m01l03/) | Free |
| 1.4 | [Back Of The Envelope Estimation: Storage And Bandwidth](https://learnsome.tech/learn/systemdesign-course/m01l04) | [3 labs](labs/m01l04/) | Free |
| 1.5 | [Latency Numbers Every Engineer Should Know](https://learnsome.tech/learn/systemdesign-course/m01l05) | [3 labs](labs/m01l05/) | Free |

### Module 2: Data, Storage And State

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 2.1 | [The Storage Decision: Relational Versus Document](https://learnsome.tech/learn/systemdesign-course/m02l01) | [2 labs](labs/m02l01/) | Pro |
| 2.2 | [The Storage Decision: Key Value, Search And Blob](https://learnsome.tech/learn/systemdesign-course/m02l02) | [2 labs](labs/m02l02/) | Pro |
| 2.3 | [Replication, Failover And Leader Election](https://learnsome.tech/learn/systemdesign-course/m02l03) | [1 lab](labs/m02l03/) | Pro |
| 2.4 | [Partitioning, Sharding And Hot Keys](https://learnsome.tech/learn/systemdesign-course/m02l04) | [1 lab](labs/m02l04/) | Pro |
| 2.5 | [Consistency, And The Truth About CAP](https://learnsome.tech/learn/systemdesign-course/m02l05) | [1 lab](labs/m02l05/) | Pro |
| 2.6 | [Eventual Consistency And What It Costs A Product](https://learnsome.tech/learn/systemdesign-course/m02l06) | [1 lab](labs/m02l06/) | Pro |

### Module 3: Caching, Queues And Asynchrony

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 3.1 | [Caching Strategies And Topology](https://learnsome.tech/learn/systemdesign-course/m03l01) | [4 labs](labs/m03l01/) | Pro |
| 3.2 | [Cache Invalidation And The Three Hard Cases](https://learnsome.tech/learn/systemdesign-course/m03l02) | [4 labs](labs/m03l02/) | Pro |
| 3.3 | [Queues, Events And Asynchronous Work](https://learnsome.tech/learn/systemdesign-course/m03l03) | [5 labs](labs/m03l03/) | Pro |
| 3.4 | [The Difference Between A Queue And A Log](https://learnsome.tech/learn/systemdesign-course/m03l04) | [4 labs](labs/m03l04/) | Pro |
| 3.5 | [Idempotency, And Exactly Once As A Fiction](https://learnsome.tech/learn/systemdesign-course/m03l05) | [2 labs](labs/m03l05/) | Pro |

### Module 4: Resilience And Traffic Management

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 4.1 | [Load Balancing And The Failure Modes It Introduces](https://learnsome.tech/learn/systemdesign-course/m04l01) | [3 labs](labs/m04l01/) | Pro |
| 4.2 | [Timeouts, And Avoiding Cascaded Failure](https://learnsome.tech/learn/systemdesign-course/m04l02) | [1 lab](labs/m04l02/) | Pro |
| 4.3 | [Retries, Backoff And Jitter](https://learnsome.tech/learn/systemdesign-course/m04l03) | [1 lab](labs/m04l03/) | Pro |
| 4.4 | [Circuit Breakers](https://learnsome.tech/learn/systemdesign-course/m04l04) | [1 lab](labs/m04l04/) | Pro |
| 4.5 | [Backpressure And Load Shedding](https://learnsome.tech/learn/systemdesign-course/m04l05) | [1 lab](labs/m04l05/) | Pro |

### Module 5: Architecture And Operations

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 5.1 | [Monolith Versus Services: The Honest Trade Offs](https://learnsome.tech/learn/systemdesign-course/m05l01) | [2 labs](labs/m05l01/) | Pro |
| 5.2 | [Observability As A Design Input](https://learnsome.tech/learn/systemdesign-course/m05l02) | [5 labs](labs/m05l02/) | Pro |
| 5.3 | [Capacity Planning As A Design Input](https://learnsome.tech/learn/systemdesign-course/m05l03) | [4 labs](labs/m05l03/) | Pro |

### Module 6: Worked Designs End To End

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 6.1 | [Worked Design One: Ticket Booking, Correctness First](https://learnsome.tech/learn/systemdesign-course/m06l01) | [3 labs](labs/m06l01/) | Pro |
| 6.2 | [Worked Design One: Scaling The Ticket Booking System](https://learnsome.tech/learn/systemdesign-course/m06l02) | [3 labs](labs/m06l02/) | Pro |
| 6.3 | [Worked Design Two: A Global Chat System](https://learnsome.tech/learn/systemdesign-course/m06l03) | [3 labs](labs/m06l03/) | Pro |
| 6.4 | [Worked Design Two: Scaling Chat Fan Out](https://learnsome.tech/learn/systemdesign-course/m06l04) | [1 lab](labs/m06l04/) | Pro |
| 6.5 | [Worked Design Three: A Metrics Ingestion Pipeline](https://learnsome.tech/learn/systemdesign-course/m06l05) | [1 lab](labs/m06l05/) | Pro |
| 6.6 | [Worked Design Three: Scaling The Metrics Pipeline](https://learnsome.tech/learn/systemdesign-course/m06l06) | [1 lab](labs/m06l06/) | Pro |

**Free** lessons are open to anyone with a free LearnSome.tech account; **Pro** lessons need a Pro membership to watch, run and grade on the site.

## Licence

- **Code** (starter files, `check` and `.learnsome/`, the dev container and the workflows) is under the [MIT licence](LICENSE).
- **Written text** (the READMEs, lab instructions, lesson text, exercises and questions) is under [CC BY-NC-SA 4.0](LICENSE-text.md): share and adapt it with attribution to LearnSome.tech, not commercially, under the same licence.
- The LearnSome.tech name and logo are not covered by either licence.

## Contributing and security

This repository is generated from the course. Report a broken lab or a content error [as an issue](../../issues/new/choose); see [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to [SECURITY.md](SECURITY.md).

© 2026 LearnSome.tech
