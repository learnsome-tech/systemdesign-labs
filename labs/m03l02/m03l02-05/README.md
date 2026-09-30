# m03l02-05 · Mass expiry, and what jitter costs you

**Lesson:** [Cache Invalidation And The Three Hard Cases](https://learnsome.tech/learn/systemdesign-course/m03l02) (lesson 3.2, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Graded

## Goal

You can tell expiry apart from invalidation, recognise the stampede, the stale read after write and the mass expiry in a running system, and apply single flight, versioned keys and jittered time to live to each.

In the lesson: Mass expiry is the least clever of the three and much the most common. Warm twelve keys together, which is what every bulk load and every deploy does, give them all the same time to live, and refill them as they expire. Then run the same keys twice, once flat and once jittered. With a flat time to live all twelve refills land in the same tick, three separate times across the run, because keys born together die together. Add a random jitter of up to eight ticks and the identical total work spreads over nineteen busy ticks, with the peak in one tick down to three. The origin sees a quarter of the burst. All jitter costs you is the ability to say precisely when a key expires, which was never a guarantee worth having.

## Files

- [`starter/jitter_ttl.py`](starter/jitter_ttl.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-05/starter`
2. Read `jitter_ttl.py` the way the lesson builds it:
   - Lines 1–14: refill them as they expire
   - Lines 15–20: run the same keys twice
3. Notes from the lesson:
   - Line 10: the jitter: a base time to live plus a random tail
4. Run it: `python3 jitter_ttl.py`.
5. Check it from the repository root: `./check m03l02-05`.

## Expected output

```text
flat ttl  peak 12 in a tick,  3 busy ticks
jittered  peak  3 in a tick, 19 busy ticks
same keys, same total work, spread instead of stacked
```

## How to check

`./check m03l02-05` copies `starter/` into a scratch directory and runs `python3 jitter_ttl.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
