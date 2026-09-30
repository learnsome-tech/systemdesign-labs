# m01l05-06 · Fan out turns a good tail into a bad experience

**Lesson:** [Latency Numbers Every Engineer Should Know](https://learnsome.tech/learn/systemdesign-course/m01l05) (lesson 1.5, module 1: Foundations And Estimation) · Free  
**Check:** Graded

## Goal

You can recite the latency numbers that matter, compose a request budget from them, explain why the speed of light sets a floor no engineering removes, and show how fan out turns a good tail latency into a bad user experience.

In the lesson: Now the result that surprises people. Suppose a service is slow on one call in a hundred. That is an excellent service. But a request that fans out to many services is only fast if every one of them was fast, so compute the chance that every call is fast, and subtract it from one. Run it for four fan out widths. The last line is the lesson: at a hundred parallel calls, nearly two thirds of your requests touch the slow tail, from components that are individually excellent. Tail latency does not average out across a fan out. It accumulates. This single fact is why wide fan out designs need hedged requests, or a deadline that returns a partial answer, rather than better components.

## Files

- [`starter/tail.py`](starter/tail.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-06/starter`
2. Read `tail.py` the way the lesson builds it:
   - Lines 1–4: the chance that every call is fast
   - Lines 5–8: four fan out widths
3. Notes from the lesson:
   - Line 1: one call in a hundred is slow: an excellent service
4. Run it: `python3 tail.py`.
5. Check it from the repository root: `./check m01l05-06`.

## Expected output

```text
   1 calls in one request ->   1.0 percent are slow
   5 calls in one request ->   4.9 percent are slow
  20 calls in one request ->  18.2 percent are slow
 100 calls in one request ->  63.4 percent are slow
```

## How to check

`./check m01l05-06` copies `starter/` into a scratch directory and runs `python3 tail.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
