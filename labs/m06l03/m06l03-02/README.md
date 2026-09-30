# m06l03-02 · Estimate connections, then everything follows

**Lesson:** [Worked Design Two: A Global Chat System](https://learnsome.tech/learn/systemdesign-course/m06l03) (lesson 6.3, module 6: Worked Designs End To End) · Pro  
**Check:** Graded

## Goal

You can design a chat system from written requirements and a connection estimate, route a message through a gateway registry to a partitioned store, order a conversation with a per conversation sequence instead of a clock, and make a client resend harmless with an idempotency key.

In the lesson: Estimation first, as always, and this one has four numbers, and only the last one is unusual. Take two hundred million daily actives, forty messages each, a tenth of them holding a socket at the peak, and what one pod can terminate. The message rate comes out near ninety two thousand a second, tripled at the peak, which is a large but unremarkable service. Then look at the sockets: twenty million of them, needing over three hundred gateway pods just to hold the file descriptors. And the ratio at the bottom is the point. There are roughly two hundred and sixteen open connections for every message per second. This system is not busy, it is occupied, and that changes what you pay for and what fails first.

## Files

- [`starter/connections.py`](starter/connections.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-02/starter`
2. Read `connections.py` the way the lesson builds it:
   - Lines 1–4: four numbers, and only the last one is unusual
   - Lines 5–13: the ratio at the bottom
3. Notes from the lesson:
   - Line 4: sockets a pod holds: file descriptors and memory, not CPU
4. Run it: `python3 connections.py`.
5. Check it from the repository root: `./check m06l03-02`.

## Expected output

```text
messages a day           8,000,000,000
messages a second               92,592
peak, three times mean         277,776
sockets at the peak         20,000,000
gateway pods needed                333
sockets per message              216.0
```

## How to check

`./check m06l03-02` copies `starter/` into a scratch directory and runs `python3 connections.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
