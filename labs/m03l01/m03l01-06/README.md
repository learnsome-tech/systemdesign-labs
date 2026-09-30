# m03l01-06 · The cold cache spike nobody provisions for

**Lesson:** [Caching Strategies And Topology](https://learnsome.tech/learn/systemdesign-course/m03l01) (lesson 3.1, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Graded

## Goal

You can place a cache at the right layer, choose a read and write strategy while naming what it costs, and size the origin for the miss rate instead of the hit ratio.

In the lesson: Now the number that ruins deploy days. Start with an empty cache, six hundred distinct keys, and four hundred reads a tick. Fill the cache as the misses arrive, and print the hit ratio each tick next to the reads that reach the origin. Look at the first tick: barely a quarter served from cache, and nearly three hundred reads pushed at an origin that, once warm, sees fifteen. That is a nineteen times spike, and it arrives at the exact moment you restart every process at once. Nothing here is broken. This is a cache behaving correctly. The planning mistake is to size the origin for the warm state, and then be surprised that a rolling restart, an eviction storm or a flushed cache is indistinguishable from a traffic flood.

## Files

- [`starter/warm.py`](starter/warm.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-06/starter`
2. Read `warm.py` the way the lesson builds it:
   - Lines 1–5: start with an empty cache
   - Lines 6–18: print the hit ratio each tick
3. Notes from the lesson:
   - Line 3: six hundred distinct keys, four hundred reads in every tick
4. Run it: `python3 warm.py`.
5. Check it from the repository root: `./check m03l01-06`.

## Expected output

```text
tick  hits  misses  hit%   origin qps
   1   106     294   26%         294
   2   256     144   64%         144
   3   320      80   80%          80
   4   366      34   91%          34
   5   377      23   94%          23
   6   385      15   96%          15
cold peak 294 against warm 15: 19 times
```

## How to check

`./check m03l01-06` copies `starter/` into a scratch directory and runs `python3 warm.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
