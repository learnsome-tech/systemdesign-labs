# m06l02-02 · Size the opening minute before choosing anything

**Lesson:** [Worked Design One: Scaling The Ticket Booking System](https://learnsome.tech/learn/systemdesign-course/m06l02) (lesson 6.2, module 6: Worked Designs End To End) · Pro  
**Check:** Graded

## Goal

You can size the opening minute of a ticket sale, choose admission control as the design rather than an add on, partition by event while admitting the hot shard it creates, and say exactly what the waiting room costs the people standing in it.

In the lesson: Estimation again, and again before any component is chosen. Three numbers you can defend: the seats on sale, the crowd that wants them, and the commit rate the guarded transaction actually sustains on the leader. That last one is measured, not hoped for, because the version check and the row lock both cost something. Then print the gap between demand and capacity. Half a million buyers want fifty thousand seats, so ten people want every seat, and that part is fine. The part that is not fine is the next line: the leader can serve eighteen thousand purchases in the opening minute, and the overload factor is the design brief. Roughly twenty eight times more people arrive at the door than the door can admit in that minute.

## Files

- [`starter/opening.py`](starter/opening.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-02/starter`
2. Read `opening.py` the way the lesson builds it:
   - Lines 1–3: three numbers you can defend
   - Lines 4–11: print the gap
3. Notes from the lesson:
   - Line 3: measured on the leader with the guard in place, not a hope
4. Run it: `python3 opening.py`.
5. Check it from the repository root: `./check m06l02-02`.

## Expected output

```text
buyers at sale open         500,000
seats available              50,000
buyers per seat                  10
commit capacity                 300 a second
served in the minute         18,000
overload at the door             28 times
seconds to sell the room        167
```

## How to check

`./check m06l02-02` copies `starter/` into a scratch directory and runs `python3 opening.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
