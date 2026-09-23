# Scalable System Design & Distributed Architecture — lesson m04l01 — Load Balancing And The Failure Modes It Introduces
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m04l01
# © LearnSome.tech
import random
rng = random.Random(7)
JOBS = [50 if rng.random() < 0.04 else 1 for _ in range(400)]
PAIRS = [rng.sample(range(4), 2) for _ in JOBS]

def sim(pick):
    load, waits, peak = [0] * 4, [], 0
    for t, work in enumerate(JOBS):
        load = [max(0, x - 1) for x in load]
        b = pick(t, load)
        waits.append(load[b])
        load[b] += work
        peak = max(peak, load[b])
    return sum(waits) / len(waits), max(waits), peak

PLANS = [("round robin", lambda t, L: t % 4),
         ("least conns", lambda t, L: L.index(min(L))),
         ("two choices", lambda t, L: min(PAIRS[t], key=lambda i: L[i]))]
for name, pick in PLANS:
    mean, worst, peak = sim(pick)
    print(f"{name:<11} mean wait {mean:6.1f}  worst {worst:4d}  peak {peak:4d}")
