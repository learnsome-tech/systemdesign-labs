# m01l05-04 · Composing a request budget out of hops

**Lesson:** [Latency Numbers Every Engineer Should Know](https://learnsome.tech/learn/systemdesign-course/m01l05) (lesson 1.5, module 1: Foundations And Estimation) · Free  
**Check:** Graded

## Goal

You can recite the latency numbers that matter, compose a request budget from them, explain why the speed of light sets a floor no engineering removes, and show how fan out turns a good tail latency into a bad user experience.

In the lesson: A latency budget is a subtraction, not a hope. Take two hundred milliseconds as the promise to the user, list the hops a request makes, and accumulate them. Watch the running total climb. The load balancer, the application work, the cache read and the database read come to thirty milliseconds between them. Then one single hop to another region costs eighty, which is more than everything else put together. Ninety milliseconds of headroom sounds comfortable, and it is not, because every number here is a typical case and your promise was about the tail. This is the most useful thing a budget does: it shows you which hop to attack, and it is almost never the one people are optimising.

## Files

- [`starter/latency.py`](starter/latency.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-04/starter`
2. Read `latency.py` the way the lesson builds it:
   - Lines 1–8: list the hops
   - Lines 9–13: accumulate
3. Notes from the lesson:
   - Line 7: one hop costs more than everything else put together
4. Run it: `python3 latency.py`.
5. Check it from the repository root: `./check m01l05-04`.

## Expected output

```text
load balancer        1 ms | running total   1 ms
app server work     20 ms | running total  21 ms
cache read           1 ms | running total  22 ms
database read        8 ms | running total  30 ms
cross region call   80 ms | running total 110 ms
budget 200 ms, headroom left 90 ms
```

## How to check

`./check m01l05-04` copies `starter/` into a scratch directory and runs `python3 latency.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
