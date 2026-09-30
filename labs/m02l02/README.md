# m02l02 · The Storage Decision: Key Value, Search And Blob

Module 2: Data, Storage And State · lesson 2.2 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m02l02)

**Goal:** You can match exact lookup, text retrieval, and large immutable bytes to key value, search, and blob storage, while preserving a clear source of truth.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l02-02](m02l02-02/) | Key value is narrow by design | Read along |
| [m02l02-05](m02l02-05/) | One product, four stores, one ownership map | Read along |

## Check yourself

- Why is an exact key lookup a better fit for key value storage than a filtered query?
- What lag does a search projection introduce, and who accepts it?
- Why should blob metadata and bytes have separate ownership?
- What makes a projection safe to delete and rebuild?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
