# m06l01-06 · The race, run twice: unguarded, then versioned

**Lesson:** [Worked Design One: Ticket Booking, Correctness First](https://learnsome.tech/learn/systemdesign-course/m06l01) (lesson 6.1, module 6: Worked Designs End To End) · Pro  
**Check:** Graded

## Goal

You can design a ticket booking system that sells each seat exactly once, starting from written requirements and a spike estimate rather than a diagram, choosing relational storage for the multi row transaction, and guarding the seat row with either a row lock or a version column.

In the lesson: Let us make the race real instead of described. This simulation gives twelve buyers three seats and a seeded generator, and it models concurrency the honest way: every buyer reads before any buyer writes, which is what happens when requests land inside the same few milliseconds. First run it with no guard at all. Twelve buyers see a free seat, twelve buyers write, and the oversold count is nine, which is nine people arriving at a venue that has nowhere to put them. Then run the same interleaving with the version check in place. Three seats sell, the oversold column is zero, and nine transactions are rejected and have to retry. That retry is the price, and it is the right price, because a retry costs a round trip and a refund costs a customer.

## Files

- [`starter/oversell.py`](starter/oversell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-06/starter`
2. Read `oversell.py` the way the lesson builds it:
   - Lines 1–9: a seeded generator
   - Lines 10–18: every buyer reads before any buyer writes
   - Lines 19–22: run it with no guard at all
3. Notes from the lesson:
   - Line 12: the version check: write only if nobody moved the row since
4. Run it: `python3 oversell.py`.
5. Check it from the repository root: `./check m06l01-06`.

## Expected output

```text
no protection: sold 12 oversold  9 retried  0
version check: sold  3 oversold  0 retried  9
```

## How to check

`./check m06l01-06` copies `starter/` into a scratch directory and runs `python3 oversell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
