# Exercises — Back Of The Envelope Estimation: Storage And Bandwidth

Lesson `m01l04` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m01l04)

## Exercise 1: Estimate storage for a photograph service

1. Assume ten million uploads a day, two megabytes each, kept for five years.
2. Compute raw bytes, then apply three copies and two thumbnail sizes.
3. Choose a shard count from a target rebuild time you state explicitly.
4. Estimate peak egress if each upload is viewed twenty times a year.

> **Hint**: Thumbnails are usually a small fraction of the original but there are several of them, and they are read far more often than the original, so they dominate bandwidth rather than storage.


---

© LearnSome.tech · support@iwantto.learnsome.tech
