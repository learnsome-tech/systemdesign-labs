# Scalable System Design & Distributed Architecture — lesson m05l02 — Observability As A Design Input
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m05l02
# © LearnSome.tech
import random
rng = random.Random(7)
sample = []
for _ in range(10000):
    if rng.random() < 0.97:
        sample.append(rng.uniform(20, 60))      # the healthy path
    else:
        sample.append(rng.uniform(300, 2000))   # retry or cold cache
sample.sort()

def at(p):
    return sample[int(len(sample) * p / 100) - 1]

mean = sum(sample) / len(sample)
over = sum(1 for x in sample if x > mean) / len(sample) * 100
print(f"mean    {mean:7.1f} ms")
print(f"median  {at(50):7.1f} ms")
print(f"p95     {at(95):7.1f} ms")
print(f"p99     {at(99):7.1f} ms")
print(f"max     {at(100):7.1f} ms")
print(f"only {over:.1f}% of requests are slower than the mean")
