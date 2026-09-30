# m05l03-06 · A capacity plan you can defend

**Lesson:** [Capacity Planning As A Design Input](https://learnsome.tech/learn/systemdesign-course/m05l03) (lesson 5.3, module 5: Architecture And Operations) · Pro  
**Check:** Graded

## Goal

You can explain why a queueing system is never run near saturation, size pools with Little's law, plan for peak plus the loss of one failure domain, and say what autoscaling cannot do for you.

In the lesson: Now the plan itself. The five inputs are peak queries a second, the capacity of one node measured by a load test, the utilisation you are willing to design for, the number of zones, and a monthly growth rate. Work out the node count twice. Once for throughput alone, at sixty percent of each node, which asks for sixty seven nodes. Then again for the loss of a zone, where the two survivors must carry the whole peak, so divide by the zones minus one and round up: thirty four per zone, a hundred and two in total. Print the plan. In normal operation those nodes sit at thirty nine percent, which looks wasteful to a spreadsheet and is in fact the premium you pay for surviving a bad afternoon. With a zone gone you are at fifty nine percent, still inside target, and growth gives you six months.

## Files

- [`starter/plan.py`](starter/plan.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-06/starter`
2. Read `plan.py` the way the lesson builds it:
   - Lines 1–6: the five inputs
   - Lines 7–15: work out the node count twice
   - Lines 16–21: print the plan
3. Notes from the lesson:
   - Line 4: per node capacity comes from a load test, never from a wish
   - Line 9: two zones must carry the whole peak, so divide by zones minus one
4. Run it: `python3 plan.py`.
5. Check it from the repository root: `./check m05l03-06`.

## Expected output

```text
throughput alone     67 nodes
one zone down       102 nodes, 34 per zone
normal utilisation   39.2%
with a zone lost     58.8%
headroom            6 months at 7% growth
```

## How to check

`./check m05l03-06` copies `starter/` into a scratch directory and runs `python3 plan.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/systemdesign-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
