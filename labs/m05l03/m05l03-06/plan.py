# Scalable System Design & Distributed Architecture — lesson m05l03 — Capacity Planning As A Design Input
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m05l03
# © LearnSome.tech
import math

PEAK = 48000       # queries a second at peak
PER_NODE = 1200    # measured by load test, never guessed
TARGET = 0.60      # the utilisation we design for
ZONES, GROWTH = 3, 0.07

serving = PEAK / (PER_NODE * TARGET)
per_zone = math.ceil(serving / (ZONES - 1))
total = per_zone * ZONES
capacity = total * PER_NODE * TARGET
degraded = PEAK / ((total - per_zone) * PER_NODE) * 100
load, months = PEAK, 0
while load * (1 + GROWTH) <= capacity:
    load, months = load * (1 + GROWTH), months + 1

print(f"throughput alone    {math.ceil(serving):3d} nodes")
print(f"one zone down       {total:3d} nodes, {per_zone} per zone")
print(f"normal utilisation  {PEAK / (total * PER_NODE) * 100:5.1f}%")
print(f"with a zone lost    {degraded:5.1f}%")
print(f"headroom            {months} months at 7% growth")
