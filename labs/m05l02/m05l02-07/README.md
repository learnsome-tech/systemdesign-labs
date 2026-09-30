# m05l02-07 · The error budget, and the burn rate that spends it

**Lesson:** [Observability As A Design Input](https://learnsome.tech/learn/systemdesign-course/m05l02) (lesson 5.2, module 5: Architecture And Operations) · Pro  
**Check:** Graded

## Goal

You can decide at design time what a system must emit, choose labels that respect cardinality, record latency as a histogram rather than a mean, and turn a service level objective into an error budget with a burn rate.

In the lesson: An indicator is a number you measure, such as the fraction of requests that succeeded. An objective is the line you promise to stay above. And the distance between that line and perfection is the error budget: failure you are allowed to spend. So turn the objective into minutes, which is the unit everybody understands, then run three scenarios, each ten days into the month. The first burns at half the permitted rate and has fifty days of budget left, more than the month contains, so it can afford to ship faster and take more risk. The second is burning twice as fast and runs dry in five days. The third spent the entire month by the tenth. That is what makes reliability a decision rather than a virtue: the arithmetic, not anybody's feelings, says stop shipping features and go and fix it.

## Files

- [`starter/budget.py`](starter/budget.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-07/starter`
2. Read `budget.py` the way the lesson builds it:
   - Lines 1–5: turn the objective into minutes
   - Lines 6–14: run three scenarios
3. Notes from the lesson:
   - Line 4: the allowance: minutes of failure you are permitted this month
   - Line 10: burn rate is observed failure divided by permitted failure
4. Run it: `python3 budget.py`.
5. Check it from the repository root: `./check m05l02-07`.

## Expected output

```text
objective 99.9% -> 43.2 budget minutes
errors 0.05%: spent   7.2 min, burn  0.5x, 50.0 days left
errors 0.20%: spent  28.8 min, burn  2.0x,  5.0 days left
errors 0.40%: spent  57.6 min, burn  4.0x, budget gone
```

## How to check

`./check m05l02-07` copies `starter/` into a scratch directory and runs `python3 budget.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
