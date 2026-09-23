# Scalable System Design & Distributed Architecture — lesson m04l05 — Backpressure And Load Shedding
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m04l05
# © LearnSome.tech
capacity = 4
arrivals = ["pay", "browse", "browse", "export", "pay", "browse"]
active = 0
for name in arrivals:
    if active == capacity and name in {"browse", "export"}:
        print(name, "shed")
        continue
    if active == capacity:
        print(name, "queued")
        continue
    active += 1
    print(name, "admitted", active)
