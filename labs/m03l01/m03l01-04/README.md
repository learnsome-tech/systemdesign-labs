# m03l01-04 · Latency slides, origin load falls off a cliff

**Lesson:** [Caching Strategies And Topology](https://learnsome.tech/learn/systemdesign-course/m03l01) (lesson 3.1, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Graded

## Goal

You can place a cache at the right layer, choose a read and write strategy while naming what it costs, and size the origin for the miss rate instead of the hit ratio.

In the lesson: Take the peak read rate we estimated in module one, twenty thousand eight hundred and thirty three reads a second, a cache that answers in a millisecond, and an origin that answers in forty. Set out the constants, then walk five hit ratios and compute two things for each: the mean latency a reader feels, and the queries a second that still arrive at the origin. Now read the two columns side by side, because they do not behave the same way at all. Latency slides gently from under one and a half milliseconds to twenty. Origin load does not slide. At ninety nine percent the origin takes two hundred reads a second, at ninety percent it takes two thousand, and the step from ninety five down to ninety doubles it. You size the origin for the miss rate.

## Files

- [`starter/cache_math.py`](starter/cache_math.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-04/starter`
2. Read `cache_math.py` the way the lesson builds it:
   - Lines 1–4: set out the constants
   - Lines 5–10: walk five hit ratios
3. Notes from the lesson:
   - Line 2: the peak read rate estimated in module one, reads a second
4. Run it: `python3 cache_math.py`.
5. Check it from the repository root: `./check m03l01-04`.

## Expected output

```text
hit%   mean ms   origin qps   vs 99% hit
 99      1.39          208      1.0x
 95      2.95         1041      5.0x
 90      4.90         2083     10.0x
 80      8.80         4166     20.0x
 50     20.50        10416     50.1x
origin must be sized for the miss rate, not the hit rate
```

## How to check

`./check m03l01-04` copies `starter/` into a scratch directory and runs `python3 cache_math.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
