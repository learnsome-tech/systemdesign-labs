# m06l03 · Worked Design Two: A Global Chat System

Module 6: Worked Designs End To End · lesson 6.3 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m06l03)

**Goal:** You can design a chat system from written requirements and a connection estimate, route a message through a gateway registry to a partitioned store, order a conversation with a per conversation sequence instead of a clock, and make a client resend harmless with an idempotency key.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l03-02](m06l03-02/) | Estimate connections, then everything follows | Graded |
| [m06l03-03](m06l03-03/) | The design on one screen: gateways, registry, store | Read along |
| [m06l03-06](m06l03-06/) | Same five arrivals, ordered two different ways | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Write the message contract for one client

1. Define the send payload: conversation, client identifier, body, sender clock.
2. Define the accept response: the assigned sequence and the server timestamp.
3. Say what the client does on a timeout, and why that cannot duplicate.
4. Say how a client that was offline for a week catches up without a full scan.

> **Hint:** Catch up is a range read on the conversation sequence, not a time range. Store the last sequence each client acknowledged, per device.

## Check yourself

- Why is the connection count, not the 92k messages a second, the number that shapes this design?
- What does per-conversation ordering promise, and what does it deliberately refuse?
- Why is a sender's timestamp a bad sort key, and what replaces it?
- Where does the client-generated message ID come from, and what does it make safe?
- A gateway pod crashes: what is wrong with the registry for the next few seconds?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
