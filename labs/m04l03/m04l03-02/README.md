# m04l03-02 · Jitter separates the retry wave

**Lesson:** [Retries, Backoff And Jitter](https://learnsome.tech/learn/systemdesign-course/m04l03) (lesson 4.3, module 4: Resilience And Traffic Management) · Pro  
**Check:** Graded

## Goal

You can retry only safe failures, apply bounded exponential backoff with jitter, and show why synchronized retries become a second outage.

In the lesson: Start with a seeded generator so the demonstration repeats. For each attempt, double the base delay until a cap, then draw three waits uniformly below that base. Read the retry wave. Without jitter, three callers that failed together sleep together and wake together, producing another burst against the dependency. With jitter, the same work is spread across the interval. Full jitter is a simple default. The cap and the retry budget are the parts that stop a long outage from turning into a slow stream of self inflicted traffic.

## Files

- [`starter/jitter.py`](starter/jitter.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-02/starter`
2. Read `jitter.py` the way the lesson builds it:
   - Lines 1–3: seeded generator
   - Lines 4–6: three waits
3. Run it: `python3 jitter.py`.
4. Check it from the repository root: `./check m04l03-02`.

## Expected output

```text
1 0.5 [0.16, 0.08, 0.33]
2 1.0 [0.07, 0.54, 0.37]
3 2.0 [0.12, 1.01, 0.07]
4 4.0 [1.73, 0.28, 0.36]
```

## How to check

`./check m04l03-02` copies `starter/` into a scratch directory and runs `python3 jitter.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
