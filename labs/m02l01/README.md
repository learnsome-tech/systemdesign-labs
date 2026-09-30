# m02l01 · The Storage Decision: Relational Versus Document

Module 2: Data, Storage And State · lesson 2.1 · Pro · [Open the lesson](https://learnsome.tech/learn/systemdesign-course/m02l01)

**Goal:** You can choose between relational and document storage from access patterns, transaction boundaries, and change ownership, while naming the failure mode your choice creates.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l01-02](m02l01-02/) | Relational storage earns its ceremony | Read along |
| [m02l01-04](m02l01-04/) | Make the decision with a workload table | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Choose a model from the invariant

1. Choose storage for a shopping cart and state its strongest invariant.
2. Name one query that becomes easier and one write that becomes harder.
3. Say which fact owns the truth if a search index disagrees.

## Check yourself

- Which invariant makes relational storage the safer default?
- When does a document aggregate remove a join without creating dangerous duplication?
- Why should search usually be a projection rather than the source of truth?
- What is the failure mode of giving two stores ownership of one fact?

---

[Course README](../../README.md) · [Scalable System Design & Distributed Architecture on LearnSome.tech](https://learnsome.tech/courses/systemdesign-course)
