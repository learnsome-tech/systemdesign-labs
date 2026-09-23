# Exercises — Cache Invalidation And The Three Hard Cases

Lesson `m03l02` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l02)

## Exercise 1: Run the three cases against your own hottest key

1. Find your hottest cached key and count the requesters that would miss together.
2. Add single flight, then measure origin calls for that key before and after.
3. Jitter every bulk warmed time to live, and state the staleness window you accept.
4. Write down who deletes each key, and what breaks when that path is skipped.

> **Hint**: Test invalidation by writing and immediately reading in a loop from two clients: the stale read after write only appears under concurrency.


---

© LearnSome.tech · support@iwantto.learnsome.tech
