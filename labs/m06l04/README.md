# m06l04 · Worked Design Two: Scaling Chat Fan Out

Module 6: Worked Designs End To End · lesson 6.4 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m06l04)

**Goal:** You can scale the chat design with connection gateways, per conversation partitions, offline inboxes, and bounded fan out while naming the consistency cost.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l04-02](m06l04-02/) | Partition conversations, then protect the hot ones | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Choose the fan out boundary

1. Set a room size at which write fan out becomes unsafe.
2. Name the durable record that lets a reconnect replay safely.
3. Choose a sequence or timestamp rule and defend it.

## Check yourself

- Why should gateways avoid owning durable messages?
- When does read fan out beat write fan out?
- Why is a sequence safer than a timestamp for conversation order?
- What bounded resource protects delivery during a large room burst?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
