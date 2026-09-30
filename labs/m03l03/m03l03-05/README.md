# m03l03-05 · A healthy queue: bursty, never empty, always bounded

**Lesson:** [Queues, Events And Asynchronous Work](https://learnsome.tech/learn/systemdesign-course/m03l03) (lesson 3.3, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Graded

## Goal

You can decide what belongs on the request path and what belongs behind a queue, name the parts of a queue and what each one protects, and use Little's law to tell a buffering queue apart from a failing one.

In the lesson: Simulate it rather than argue about it. Arrivals with bursts: most ticks bring ten to seventeen items, and about one tick in eight brings forty five, which is what real traffic looks like. Drain a fixed number every tick, twenty two here, and print the depth and the age of the oldest item every third tick. The bursts are plainly visible in the depth column, climbing to thirty six, and then the depth comes back down to zero because the drain rate is genuinely above the mean arrival rate. The worst wait in the whole run is a single tick. That is what a healthy queue looks like: not empty, but bounded, returning to the floor between bursts. This queue is buying you the capacity you would otherwise have had to provision for a peak.

## Files

- [`starter/queue.py`](starter/queue.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-05/starter`
2. Read `queue.py` the way the lesson builds it:
   - Lines 1–7: arrivals with bursts
   - Lines 8–15: drain a fixed number every tick
3. Notes from the lesson:
   - Line 7: about one tick in eight is a burst of forty five arrivals
4. Run it: `python3 queue.py`.
5. Check it from the repository root: `./check m03l03-05`.

## Expected output

```text
tick  arrived  depth  oldest age
   3       45     23           0
   6       45     30           0
   9       45     36           0
  12       16      9           0
  15       12     12           0
  18       45     23           0
  21       13      0           0
  24       17      0           0
worst depth 36, worst age 1: bounded
```

## How to check

`./check m03l03-05` copies `starter/` into a scratch directory and runs `python3 queue.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
