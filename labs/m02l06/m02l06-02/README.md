# m02l06-02 · A read can lose a write without losing data

**Lesson:** [Eventual Consistency And What It Costs A Product](https://learnsome.tech/learn/systemdesign-course/m02l06) (lesson 2.6, module 2: Data, Storage And State) · Pro  
**Check:** Graded

## Goal

You can model an eventual consistency race, identify the product cost of stale state, and add read routing or reconciliation where the user cannot tolerate surprise.

In the lesson: Here is a tiny consistency race. Show the leader and follower with different cart counts. The write is acknowledged by the leader, then a refresh lands on the follower before replication. Read the refresh from the follower. The data was not lost, but the product tells the person that their cart went backwards. After replication the copies agree. The safe route after a write is to read from the leader for a short session window, or to wait until the follower has reached the write position. This is why consistency is a product behavior, not a database setting.

## Files

- [`starter/consistency_race.py`](starter/consistency_race.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l06/m02l06-02/starter`
2. Read `consistency_race.py` the way the lesson builds it:
   - Lines 1–3: show the leader and follower
   - Lines 4–9: refresh from the follower
3. Run it: `python3 consistency_race.py`.
4. Check it from the repository root: `./check m02l06-02`.

## Expected output

```text
t0 leader 3 follower 2
t1 write acknowledged 3
t1 refresh from follower 2
t2 after replication 3
safe route after write: leader
```

## How to check

`./check m02l06-02` copies `starter/` into a scratch directory and runs `python3 consistency_race.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m02l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
