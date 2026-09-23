# Exercises — Monolith Versus Services: The Honest Trade Offs

Lesson `m05l01` · [Watch](https://learnsome.tech/courses/systemdesign-course/watch?lesson=m05l01)

## Exercise 1: Extract one thing with the strangler pattern

1. Pick one module and name the tables only it writes. If none, stop here.
2. Put a facade in front, route one endpoint to a new service, leave the rest.
3. Write the contract first: request, response, errors, timeout, idempotency key.
4. Name what you can no longer do in one transaction, and what replaces it.

> **Hint**: The strangler pattern works because every step is reversible. If you cannot route one endpoint back to the monolith in a minute, you have cut in the wrong place.


---

© LearnSome.tech · support@iwantto.learnsome.tech
