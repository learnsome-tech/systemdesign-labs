# m06l03-06 · Same five arrivals, ordered two different ways

**Lesson:** [Worked Design Two: A Global Chat System](https://learnsome.tech/learn/systemdesign-course/m06l03) (lesson 6.3, module 6: Worked Designs End To End) · Pro  
**Check:** Graded

## Goal

You can design a chat system from written requirements and a connection estimate, route a message through a gateway registry to a partitioned store, order a conversation with a per conversation sequence instead of a clock, and make a client resend harmless with an idempotency key.

In the lesson: Five arrivals with two resends, and the clocks disagree, which is the ordinary case rather than a contrived one. First sort them by the clock the sender stamped. The answer arrives before the question, it is followed by a second copy of itself, and the question then shows up twice at the bottom, because a resend carried a later stamp. No reader would accept that transcript. Now take the identical input and do two things: key them by the client identifier, so a resend collapses into the message it repeats, and sort by the conversation sequence the store assigned. The second block is what a person should see: three messages, in the order they were accepted, each appearing once. The input never changed. Only the sort key and the deduplication did.

## Files

- [`starter/ordering.py`](starter/ordering.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-06/starter`
2. Read `ordering.py` the way the lesson builds it:
   - Lines 1–7: five arrivals with two resends
   - Lines 8–10: sort them by the clock
   - Lines 11–16: key them by the client identifier
3. Run it: `python3 ordering.py`.
4. Check it from the repository root: `./check m06l03-06`.

## Expected output

```text
ordered by wall clock:
  98  yes, seven
  99  yes, seven
  100  are we still on
  102  bringing the deck
  104  are we still on
ordered by conversation sequence:
  1  are we still on
  2  yes, seven
  3  bringing the deck
```

## How to check

`./check m06l03-06` copies `starter/` into a scratch directory and runs `python3 ordering.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
