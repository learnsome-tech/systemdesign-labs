# m01l04-03 · Rate, retention, indexes, replicas, shards

**Lesson:** [Back Of The Envelope Estimation: Storage And Bandwidth](https://learnsome.tech/learn/systemdesign-course/m01l04) (lesson 1.4, module 1: Foundations And Estimation) · Free  
**Check:** Graded

## Goal

You can estimate stored bytes from a row size, a write rate and a retention window, apply index and replication multipliers, size shards from the result, and convert read traffic into egress bandwidth.

In the lesson: Now the whole calculation, with every multiplier named rather than hidden. Forty million writes a day at four hundred bytes, kept for a year, with an index factor of one point three and three copies for durability. It prints four numbers: raw a day, raw a year, the same with indexes, and then the real figure on disk. Two multipliers deserve attention. Indexes are storage too, and they are the most commonly forgotten line in any estimate. And three copies is a durability decision, not a capacity one, so it multiplies your bill without serving a single extra request. Finally, spread across shards. Look at the last three lines, because that is the line that decides whether one machine can hold this.

## Files

- [`starter/storage.py`](starter/storage.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-03/starter`
2. Read `storage.py` the way the lesson builds it:
   - Lines 1–6: every multiplier named
   - Lines 7–14: four numbers
   - Lines 15–16: spread across shards
3. Notes from the lesson:
   - Line 3: indexes are storage too, and they are rarely budgeted
   - Line 4: three copies is durability, not capacity
4. Run it: `python3 storage.py`.
5. Check it from the repository root: `./check m01l04-03`.

## Expected output

```text
raw a day           16.0 GB
raw a year        5840.0 GB
with indexes      7592.0 GB
times 3 copies   22776.0 GB
  4 shards ->   5694.0 GB each
  8 shards ->   2847.0 GB each
 16 shards ->   1423.5 GB each
```

## How to check

`./check m01l04-03` copies `starter/` into a scratch directory and runs `python3 storage.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
