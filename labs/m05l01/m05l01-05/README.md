# m05l01-05 · Price the split instead of arguing about it

**Lesson:** [Monolith Versus Services: The Honest Trade Offs](https://learnsome.tech/learn/systemdesign-course/m05l01) (lesson 5.1, module 5: Architecture And Operations) · Pro  
**Check:** Graded

## Goal

You can argue the monolith and services decision from data ownership and team boundaries rather than fashion, price a split in latency and availability, and recognise a distributed monolith before you ship one.

In the lesson: Let us price a split rather than have opinions about one. Here are the four numbers this rests on: the real work the operation does, an in process call, which is a memory reference, a datacentre round trip taken from the latency list in module one, and the availability of a single deployable. Then one function that prices a plan: add the call costs to the work, and compose availability by raising one deployable's uptime to the number of independent parts. Run both plans, the monolith and the same chain split four ways. Now the numbers make the trade visible. Two milliseconds more, which is five percent and nobody will feel it. But four times the downtime, because four things that are each up ninety nine point nine percent of the time are only up ninety nine point six percent together.

## Files

- [`starter/split.py`](starter/split.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-05/starter`
2. Read `split.py` the way the lesson builds it:
   - Lines 1–4: the four numbers this rests on
   - Lines 5–7: one function that prices a plan
   - Lines 8–19: run both plans
3. Notes from the lesson:
   - Line 2: an in process call is a memory reference: a ten thousandth of a millisecond
   - Line 3: a datacentre round trip, from the latency list in module one
4. Run it: `python3 split.py`.
5. Check it from the repository root: `./check m05l01-05`.

## Expected output

```text
monolith        40.00 ms   99.9000% up     43.2 min down a month
four services   42.00 ms   99.6006% up    172.5 min down a month
latency cost:  5.0% slower
downtime cost: 4.0 times more minutes
```

## How to check

`./check m05l01-05` copies `starter/` into a scratch directory and runs `python3 split.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
