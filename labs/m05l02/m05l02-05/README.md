# m05l02-05 · What an average hides, in one sample

**Lesson:** [Observability As A Design Input](https://learnsome.tech/learn/systemdesign-course/m05l02) (lesson 5.2, module 5: Architecture And Operations) · Pro  
**Check:** Graded

## Goal

You can decide at design time what a system must emit, choose labels that respect cardinality, record latency as a histogram rather than a mean, and turn a service level objective into an error budget with a burn rate.

In the lesson: Here is a sample with the shape real latency has: most requests on a healthy path, and three in every hundred that hit a retry, a cold cache or a collection pause. Sort it, add a helper that picks a percentile, then print five numbers. The mean is about seventy two milliseconds. The median is forty. The ninety fifth percentile is fifty nine, the ninety ninth is nearly fourteen hundred, and the worst is close to two seconds. Now look at the last line. Only three percent of requests are slower than the mean, so the mean describes almost nobody. It is the median with a slice of the tail sprinkled over everyone. It also cannot be averaged across services, which is why you keep buckets and compute percentiles from them.

## Files

- [`starter/percentiles.py`](starter/percentiles.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-05/starter`
2. Read `percentiles.py` the way the lesson builds it:
   - Lines 1–9: a sample with the shape real latency has
   - Lines 10–12: a helper that picks a percentile
   - Lines 13–21: print five numbers
3. Notes from the lesson:
   - Line 5: three in a hundred take the slow path: an ordinary, healthy service
   - Line 15: the fraction above the mean is the whole argument
4. Run it: `python3 percentiles.py`.
5. Check it from the repository root: `./check m05l02-05`.

## Expected output

```text
mean       71.9 ms
median     40.5 ms
p95        59.2 ms
p99      1388.0 ms
max      1998.1 ms
only 3.1% of requests are slower than the mean
```

## How to check

`./check m05l02-05` copies `starter/` into a scratch directory and runs `python3 percentiles.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
