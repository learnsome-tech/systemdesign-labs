# m05l03-02 · The knee: why you never run a queue hot

**Lesson:** [Capacity Planning As A Design Input](https://learnsome.tech/learn/systemdesign-course/m05l03) (lesson 5.3, module 5: Architecture And Operations) · Pro  
**Check:** Graded

## Goal

You can explain why a queueing system is never run near saturation, size pools with Little's law, plan for peak plus the loss of one failure domain, and say what autoscaling cannot do for you.

In the lesson: Here is the whole argument for headroom in one formula. For a single server with arrivals that are not politely spaced out, response time relative to an idle system is one over one minus the load. That is it. Sweep the utilisation from a half up to nearly full and watch the bars. At half busy you wait twice as long as on an empty machine, which is fine. At eighty percent, five times. At ninety, ten times. At ninety nine percent, a hundred times. Read the gap between eighty and ninety: ten points of extra load doubled the wait, and the last nine points multiplied it by ten. That is the knee, and one sentence at the bottom names it. A target of high utilisation is a decision to have bad latency.

## Files

- [`starter/knee.py`](starter/knee.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-02/starter`
2. Read `knee.py` the way the lesson builds it:
   - Lines 1–5: sweep the utilisation
   - Lines 6: one sentence at the bottom
3. Notes from the lesson:
   - Line 4: the standard single server queue: response time is one over one minus load
4. Run it: `python3 knee.py`.
5. Check it from the repository root: `./check m05l03-02`.

## Expected output

```text
busy   response time versus an idle system
 50%      2.0x   ##
 60%      2.5x   ##
 70%      3.3x   ###
 80%      5.0x   #####
 90%     10.0x   ##########
 95%     20.0x   ####################
 99%    100.0x   ########################################
the knee is real: ten points of load, ten times the wait
```

## How to check

`./check m05l03-02` copies `starter/` into a scratch directory and runs `python3 knee.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
