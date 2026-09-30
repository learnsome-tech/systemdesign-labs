# m03l02-03 · The stampede, and what single flight is worth

**Lesson:** [Cache Invalidation And The Three Hard Cases](https://learnsome.tech/learn/systemdesign-course/m03l02) (lesson 3.2, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Graded

## Goal

You can tell expiry apart from invalidation, recognise the stampede, the stale read after write and the mass expiry in a running system, and apply single flight, versioned keys and jittered time to live to each.

In the lesson: Here is the stampede in twenty lines. Build a herd of requesters, between four and twelve of them arriving in every tick, against one hot key with a time to live of eight ticks. Then write one function with a switch: when the key is not fresh, either every waiting requester goes to the origin, or exactly one goes and the rest wait for its answer. Compare the two counts. Without single flight the origin takes thirty calls to serve four genuine misses. With it, four. The multiplier is the size of the herd, and the herd here peaks at twelve where in production it is twelve thousand, and an origin cannot tell that apart from an attack. The guard is a lock per key, plus a stale value served while one worker refreshes.

## Files

- [`starter/stampede.py`](starter/stampede.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-03/starter`
2. Read `stampede.py` the way the lesson builds it:
   - Lines 1–4: build a herd of requesters
   - Lines 5–12: one function with a switch
   - Lines 13–19: compare the two counts
3. Notes from the lesson:
   - Line 3: one hot key with a time to live of eight ticks
4. Run it: `python3 stampede.py`.
5. Check it from the repository root: `./check m03l02-03`.

## Expected output

```text
requesters per tick: 9 6 10 4 5 12 5 9 4 12 7 4 ...
origin calls, no single flight: 30
origin calls, single flight:    4
the herd multiplied one miss by 7
```

## How to check

`./check m03l02-03` copies `starter/` into a scratch directory and runs `python3 stampede.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
