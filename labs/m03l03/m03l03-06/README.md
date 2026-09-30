# m03l03-06 · Change one constant and the queue stops being a buffer

**Lesson:** [Queues, Events And Asynchronous Work](https://learnsome.tech/learn/systemdesign-course/m03l03) (lesson 3.3, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Graded

## Goal

You can decide what belongs on the request path and what belongs behind a queue, name the parts of a queue and what each one protects, and use Little's law to tell a buffering queue apart from a failing one.

In the lesson: Now change one constant. The consumer drains fifteen a tick against the same arrivals, whose mean is close to seventeen. Nothing else in the program moves. Read the depth column: thirty, fifty eight, eighty five, and on upward past a hundred and twenty, while the age of the oldest item climbs from zero ticks to seven. There is no equilibrium in this picture, and there is no queue size that creates one, because the deficit is two items a tick for as long as the load lasts. Little's law finishes the story: at a depth of a hundred and twenty six draining at fifteen, anything arriving now waits more than eight ticks. Nothing failed here. A queue faithfully converted a shortage of consumers into a growing delay, and it will keep doing that.

## Files

- [`starter/queue.py`](starter/queue.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-06/starter`
2. Read `queue.py` the way the lesson builds it:
   - Lines 1–3: change one constant
   - Lines 4–15: nothing else in the program moves
3. Notes from the lesson:
   - Line 3: fifteen drained a tick against a mean arrival near seventeen
4. Run it: `python3 queue.py`.
5. Check it from the repository root: `./check m03l03-06`.

## Expected output

```text
tick  arrived  depth  oldest age
   3       45     30           0
   6       45     58           1
   9       45     85           3
  12       16     79           3
  15       12    103           5
  18       45    129           5
  21       13    121           7
  24       17    126           6
worst depth 129, worst age 7: still rising
```

## How to check

`./check m03l03-06` copies `starter/` into a scratch directory and runs `python3 queue.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
