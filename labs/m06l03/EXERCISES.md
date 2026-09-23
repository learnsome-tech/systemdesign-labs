# Exercises — Worked Design Two: A Global Chat System

Lesson `m06l03` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m06l03)

## Exercise 1: Write the message contract for one client

1. Define the send payload: conversation, client identifier, body, sender clock.
2. Define the accept response: the assigned sequence and the server timestamp.
3. Say what the client does on a timeout, and why that cannot duplicate.
4. Say how a client that was offline for a week catches up without a full scan.

> **Hint**: Catch up is a range read on the conversation sequence, not a time range. Store the last sequence each client acknowledged, per device.


---

© LearnSome.tech · support@iwantto.learnsome.tech
