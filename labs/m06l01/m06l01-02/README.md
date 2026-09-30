# m06l01-02 · Estimate the spike, because the mean is a lie here

**Lesson:** [Worked Design One: Ticket Booking, Correctness First](https://learnsome.tech/learn/systemdesign-course/m06l01) (lesson 6.1, module 6: Worked Designs End To End) · Pro  
**Check:** Graded

## Goal

You can design a ticket booking system that sells each seat exactly once, starting from written requirements and a spike estimate rather than a diagram, choosing relational storage for the multi row transaction, and guarding the seat row with either a row lock or a version column.

In the lesson: Now estimate, the way module one lesson three does it, and watch which number turns out to matter. The venue holds fifty thousand seats and the sale opens at a fixed minute, so the daily mean describes a system nobody is using. Write down the four constants, then divide the house by the window in which most of it really sells. Every purchase drags a pile of seat map reads behind it, and every checkout pins a row for minutes, so compute those as well. Then print the ratio at the end. And the last number is the design brief: the opening spike runs about seven hundred times the daily mean, so a system sized for the average is not slightly undersized, it is the wrong system.

## Files

- [`starter/spike.py`](starter/spike.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-02/starter`
2. Read `spike.py` the way the lesson builds it:
   - Lines 1–4: write down the four constants
   - Lines 5–12: print the ratio at the end
3. Notes from the lesson:
   - Line 2: the house empties in two minutes, not across a day
4. Run it: `python3 spike.py`.
5. Check it from the repository root: `./check m06l01-02`.

## Expected output

```text
seats on sale                 50,000
purchases a second               417
seat map reads a second       12,500
rows held at once            125,000
daily mean, same show           0.58
spike over mean                  720 times
```

## How to check

`./check m06l01-02` copies `starter/` into a scratch directory and runs `python3 spike.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
