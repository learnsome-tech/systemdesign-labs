# m04l04-02 · The breaker changes the shape of failure

**Lesson:** [Circuit Breakers](https://learnsome.tech/learn/systemdesign-course/m04l04) (lesson 4.4, module 4: Resilience And Traffic Management) · Pro  
**Check:** Graded

## Goal

You can use a circuit breaker to stop repeated work against a failing dependency, choose a safe probe policy, and explain the degraded behavior it exposes.

In the lesson: Run a small breaker with three failures required to trip. Read the calls first: the dependency receives the work and the breaker counts errors. Once it opens, read the fast fail lines. The caller stops waiting, and the dependency stops receiving doomed work. This example ends before the cool down probe, because the important difference is already visible: an open breaker changes a slow remote failure into a local, predictable response. In a real system the half open probe must be bounded so recovery testing cannot become another flood.

## Files

- [`starter/breaker.py`](starter/breaker.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-02/starter`
2. Read `breaker.py` the way the lesson builds it:
   - Lines 1–3: three failures required
   - Lines 4–14: once it opens
3. Run it: `python3 breaker.py`.
4. Check it from the repository root: `./check m04l04-02`.

## Expected output

```text
call error
call error
call error
fast fail
fast fail
fast fail
fast fail
```

## How to check

`./check m04l04-02` copies `starter/` into a scratch directory and runs `python3 breaker.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
