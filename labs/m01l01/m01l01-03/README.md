# m01l01-03 · The shape of the discussion

**Lesson:** [What A Design Is For, And How To Run A Design Discussion](https://learnsome.tech/learn/systemdesign-course/m01l01) (lesson 1.1, module 1: Foundations And Estimation) · Free  
**Check:** Read along

## Goal

You can explain what a system design is actually for, run a forty five minute design discussion in the right order, and record a decision together with the option you rejected and the cost you accepted.

In the lesson: Here is the shape of the conversation. Requirements, then estimation, then the data model, then a high level design, then one deep dive into the riskiest part, then failure modes. And the arrow at the bottom matters as much as the ones along the top, because this is a loop. An estimate that comes out ten times larger than you expected sends you back to the requirements to ask whether the feature is really meant to serve that many people. A failure mode you cannot live with sends you back to the data model. Going backwards is the design working, not the design failing. What you must not do is skip forwards, because a component chosen before an estimate is a guess wearing a diagram.

## Files

- [`starter/the-shape-of-the-discussion.txt`](starter/the-shape-of-the-discussion.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-shape-of-the-discussion.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
