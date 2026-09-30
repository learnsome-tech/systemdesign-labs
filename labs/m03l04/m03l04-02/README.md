# m03l04-02 · The same ten records through both shapes

**Lesson:** [The Difference Between A Queue And A Log](https://learnsome.tech/learn/systemdesign-course/m03l04) (lesson 3.4, module 3: Caching, Queues And Asynchrony) · Pro  
**Check:** Graded

## Goal

You can say what a queue and a log each guarantee, choose between them from whether the message is a command or a fact, and explain why retention and consumer lag become design inputs once you pick a log.

In the lesson: One program, ten records, two shapes. First the queue: hand them to two competing consumers and every record goes to exactly one of them. Consumer A takes the odd numbered records, B takes the even ones, and between them they have seen everything once. Then the third line is the important one. The queue is empty and there is nothing left to replay, because those records were deleted as they were taken. Now give every consumer an offset of its own against a retained log. A reads all ten and B reads all ten. A third consumer that did not exist when the records were written joins late and replays from offset zero. Same ten facts, and two completely different sets of things you are permitted to do tomorrow.

## Files

- [`starter/shapes.py`](starter/shapes.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-02/starter`
2. Read `shapes.py` the way the lesson builds it:
   - Lines 1–9: hand them to two competing consumers
   - Lines 10–17: give every consumer an offset of its own
3. Notes from the lesson:
   - Line 9: the queue is empty: the records were deleted as they were taken
4. Run it: `python3 shapes.py`.
5. Check it from the repository root: `./check m03l04-02`.

## Expected output

```text
queue A took  r1 r3 r5 r7 r9
queue B took  r2 r4 r6 r8 r10
queue left    [] -> nothing left to replay
log   A read  10 records, offset 10
log   B read  10 records, offset 10
log   C joins late, replays 10 records from offset 0
log   retains  r1 r2 r3 r4 r5 r6 r7 r8 r9 r10
```

## How to check

`./check m03l04-02` copies `starter/` into a scratch directory and runs `python3 shapes.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
