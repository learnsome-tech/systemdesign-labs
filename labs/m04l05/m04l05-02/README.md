# m04l05-02 · A shedder keeps the useful work alive

**Lesson:** [Backpressure And Load Shedding](https://learnsome.tech/learn/systemdesign-course/m04l05) (lesson 4.5, module 4: Resilience And Traffic Management) · Pro  
**Check:** Graded

## Goal

You can bound work in flight, shed low value load before queues exhaust resources, and explain why admission control is kinder than late timeouts.

In the lesson: Set a small capacity and feed the shedder a mixed stream. The first four requests are admitted until the limit is full. The next payment is queued because it is valuable and may wait. The next browse request is shed because it is lower value and can be refreshed later. Read the difference between queued and shed. Admission control makes the policy visible before resources are exhausted. In a real implementation, the active count falls when work completes, and the queue itself has a bound and a timeout.

## Files

- [`starter/shed.py`](starter/shed.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-02/starter`
2. Read `shed.py` the way the lesson builds it:
   - Lines 1–4: small capacity
   - Lines 5–12: next browse request is shed
3. Run it: `python3 shed.py`.
4. Check it from the repository root: `./check m04l05-02`.

## Expected output

```text
pay admitted 1
browse admitted 2
browse admitted 3
export admitted 4
pay queued
browse shed
```

## How to check

`./check m04l05-02` copies `starter/` into a scratch directory and runs `python3 shed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
