# m04l01-04 · Round robin is fine until service times vary

**Lesson:** [Load Balancing And The Failure Modes It Introduces](https://learnsome.tech/learn/systemdesign-course/m04l01) (lesson 4.1, module 4: Resilience And Traffic Management) · Pro  
**Check:** Graded

## Goal

You can choose a balancing algorithm and a health check policy on evidence, say what layer four and layer seven each can see, and name the failure modes the balancer itself adds to the system.

In the lesson: Four backends, four hundred requests, and a heavy tail: one arrival in twenty five costs fifty times what the others cost. Generate the stream once so that every algorithm is handed identical work. The simulator ticks, drains one unit from each backend, then records what each request waited before it started. Now dispatch it three ways. Round robin takes its turn whatever the backend is already carrying, so it posts a mean wait of twenty eight and a worst case of a hundred and fifty one. Least connections keeps the mean under three. Two random choices needs no shared state and lands between them. Read the peak depth column: identical work, identical arrival times, and one algorithm builds queues five times deeper than another.

## Files

- [`starter/balance.py`](starter/balance.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-04/starter`
2. Read `balance.py` the way the lesson builds it:
   - Lines 1–4: Generate the stream once
   - Lines 5–14: records what each request waited
   - Lines 15–21: dispatch it three ways
3. Notes from the lesson:
   - Line 3: one request in twenty five costs fifty times the others
   - Line 16: takes its turn whatever the backend is already carrying
4. Run it: `python3 balance.py`.
5. Check it from the repository root: `./check m04l01-04`.

## Expected output

```text
round robin mean wait   28.0  worst  151  peak  155
least conns mean wait    2.6  worst   22  peak   63
two choices mean wait    9.3  worst   55  peak  100
```

## How to check

`./check m04l01-04` copies `starter/` into a scratch directory and runs `python3 balance.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
