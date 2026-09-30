# m06l02-04 · Three doors, one crowd, and the numbers each produces

**Lesson:** [Worked Design One: Scaling The Ticket Booking System](https://learnsome.tech/learn/systemdesign-course/m06l02) (lesson 6.2, module 6: Worked Designs End To End) · Pro  
**Check:** Graded

## Goal

You can size the opening minute of a ticket sale, choose admission control as the design rather than an add on, partition by event while admitting the hot shard it creates, and say exactly what the waiting room costs the people standing in it.

In the lesson: Now price the three doors against the same crowd. The model is a crowd that decays over three minutes, a fixed commit capacity, and one deliberate piece of realism: when attempts exceed capacity, contention makes it slower, so effective throughput falls instead of flattening. Print one row a door. Read the first row and then the last. With the door open, contention peaks at six hundred and sixty seven times capacity, the effective commit rate collapses, and the sale never finishes, so thirteen thousand seats sell and over a million people get an error. Both controlled doors sell the whole house. The bounded queue caps the wait near a minute and turns more people away. The waiting room turns away fewer and makes the ones it keeps wait twenty two minutes.

## Files

- [`starter/admission.py`](starter/admission.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-04/starter`
2. Read `admission.py` the way the lesson builds it:
   - Lines 1–3: a crowd that decays
   - Lines 4–18: contention makes it slower
   - Lines 19–22: print one row a door
3. Notes from the lesson:
   - Line 14: overload collapse: attempts above capacity reduce the commit rate
4. Run it: `python3 admission.py`.
5. Check it from the repository root: `./check m06l02-04`.

## Expected output

```text
plan             sold         lost   wait  contention
open door      13,537    1,140,966     0s        667x
bounded queue  50,000    1,080,803    65s          1x
waiting room   50,000      700,803  1332s          1x
```

## How to check

`./check m06l02-04` copies `starter/` into a scratch directory and runs `python3 admission.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
