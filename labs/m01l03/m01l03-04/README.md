# m01l03-04 · From users to queries a second, and then to servers

**Lesson:** [Back Of The Envelope Estimation: Traffic And Throughput](https://learnsome.tech/learn/systemdesign-course/m01l03) (lesson 1.3, module 1: Foundations And Estimation) · Free  
**Check:** Graded

## Goal

You can turn a user count into mean and peak queries a second, apply a peak factor and a read to write ratio, convert throughput into a server count, and state every assumption you used out loud.

In the lesson: Here it is as a program, because an estimate you can re-run when an assumption changes is worth ten estimates on a whiteboard. The assumptions at the top are all named and all challengeable: twenty million daily actives, thirty reads and two writes each, and a peak factor of three times the mean. Then the mean rates, the peak rates, and the ratio between reads and writes. Finally divide by what one server can take, which is the number you should measure rather than guess. Read the results. Seven thousand reads a second on average, twenty one thousand at peak, and eleven servers with nothing spare, which is another way of saying eleven servers is the wrong answer.

## Files

- [`starter/traffic.py`](starter/traffic.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-04/starter`
2. Read `traffic.py` the way the lesson builds it:
   - Lines 1–6: the assumptions at the top
   - Lines 7–14: mean rates
   - Lines 15–16: divide by what one server can take
3. Notes from the lesson:
   - Line 4: peak factor: the busy hour, not the busy second
   - Line 6: the only input here you should measure rather than guess
4. Run it: `python3 traffic.py`.
5. Check it from the repository root: `./check m01l03-04`.

## Expected output

```text
mean read qps         6944
mean write qps         463
peak read qps        20833
peak write qps        1389
read write ratio        15 to one
servers at peak       10.4 -> 11 with none spare
```

## How to check

`./check m01l03-04` copies `starter/` into a scratch directory and runs `python3 traffic.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
