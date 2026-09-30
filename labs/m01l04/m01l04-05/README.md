# m01l04-05 · Bandwidth: the bill nobody estimates

**Lesson:** [Back Of The Envelope Estimation: Storage And Bandwidth](https://learnsome.tech/learn/systemdesign-course/m01l04) (lesson 1.4, module 1: Foundations And Estimation) · Free  
**Check:** Graded

## Goal

You can estimate stored bytes from a row size, a write rate and a retention window, apply index and replication multipliers, size shards from the result, and convert read traffic into egress bandwidth.

In the lesson: Bandwidth is the estimate people skip, and it is often the largest line on the bill. Take the same peak read rate we computed earlier. A structured response of four kilobytes, and one request in ten that also asks for a quarter megabyte image. Multiply by eight to get bits, then add the two together. The arithmetic is brutal: the structured responses cost you under a gigabit a second, and the images cost six times more than everything else combined. That single comparison is why a content delivery network is not an optimisation, it is part of the design. The last line puts images behind an edge cache with a ninety five percent hit rate, and your origin bandwidth falls by a factor of twenty.

## Files

- [`starter/bandwidth.py`](starter/bandwidth.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-05/starter`
2. Read `bandwidth.py` the way the lesson builds it:
   - Lines 1–6: the same peak read rate
   - Lines 7–12: add the two together
   - Lines 13–14: a content delivery network
3. Notes from the lesson:
   - Line 3: one request in ten asks for an image
4. Run it: `python3 bandwidth.py`.
5. Check it from the repository root: `./check m01l04-05`.

## Expected output

```text
json egress      0.67 gigabit a second
image egress     4.17 gigabit a second
total            4.83 gigabit a second
images at 95 percent cache hit   0.21 gigabit a second
```

## How to check

`./check m01l04-05` copies `starter/` into a scratch directory and runs `python3 bandwidth.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
