# m01l02-04 · An availability target is a downtime budget

**Lesson:** [Requirements: The Constraints That Shape The System](https://learnsome.tech/learn/systemdesign-course/m01l02) (lesson 1.2, module 1: Foundations And Estimation) · Free  
**Check:** Graded

## Goal

You can separate functional requirements from the non-functional constraints that actually shape a system, turn an availability target into a monthly downtime budget, and show why availability multiplies along a chain of hard dependencies.

In the lesson: An availability percentage means nothing until you turn it into minutes, so let us do that. The allowance is the minutes in a month times the fraction you are permitted to be down. Run it for four common targets. Now look at the numbers. Ninety nine percent is over seven hours a month, which no serious product can wear. Ninety nine point nine is forty three minutes, which is one bad deployment. Ninety nine point nine nine is four minutes, and four minutes a month is less time than a human takes to read an alert, so that number is a promise about automation, not about people. Then the last two lines multiply five independent services, each at ninety nine point nine, in series.

## Files

- [`starter/availability.py`](starter/availability.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-04/starter`
2. Read `availability.py` the way the lesson builds it:
   - Lines 1–4: the allowance
   - Lines 5–7: four common targets
   - Lines 8–11: in series
3. Notes from the lesson:
   - Line 9: five hard dependencies, each one good on its own
4. Run it: `python3 availability.py`.
5. Check it from the repository root: `./check m01l02-04`.

## Expected output

```text
 99.0 percent ->   432.0 min a month
 99.9 percent ->    43.2 min a month
99.95 percent ->    21.6 min a month
99.99 percent ->     4.3 min a month
five services at 99.9 in series -> 99.50 percent
which allows 216 min a month
```

## How to check

`./check m01l02-04` copies `starter/` into a scratch directory and runs `python3 availability.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
