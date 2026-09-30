# m01l01-04 · Time is the real constraint: spend it on purpose

**Lesson:** [What A Design Is For, And How To Run A Design Discussion](https://learnsome.tech/learn/systemdesign-course/m01l01) (lesson 1.1, module 1: Foundations And Estimation) · Free  
**Check:** Graded

## Goal

You can explain what a system design is actually for, run a forty five minute design discussion in the right order, and record a decision together with the option you rejected and the cost you accepted.

In the lesson: A design discussion is bounded by something very unromantic: time. Take forty five minutes as the budget. Here is the plan itself, as a list of steps and the minutes each one is worth. Then add them up. Look at the running total. Requirements and estimation together take ten minutes, a fifth of everything, and that feels wrong to most people the first time. It is not wrong. Those ten minutes are what make the next thirty five possible. Notice also that the deep dive gets more time than the high level design. A design is judged on one part you took seriously, not on six parts you named. And nothing is unspent, because a design discussion that finishes early has not finished.

## Files

- [`starter/agenda.py`](starter/agenda.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-04/starter`
2. Read `agenda.py` the way the lesson builds it:
   - Lines 1–9: the plan itself
   - Lines 10–14: add them up
3. Notes from the lesson:
   - Line 1: a whiteboard session, or an interview: the same budget
4. Run it: `python3 agenda.py`.
5. Check it from the repository root: `./check m01l01-04`.

## Expected output

```text
  5 min in | requirements and scope | 5 min
 10 min in | estimation | 5 min
 18 min in | api and data model | 8 min
 30 min in | high level design | 12 min
 40 min in | one deep dive | 10 min
 45 min in | failure modes | 5 min
unspent: 0 min
```

## How to check

`./check m01l01-04` copies `starter/` into a scratch directory and runs `python3 agenda.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
