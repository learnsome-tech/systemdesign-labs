# Scalable System Design & Distributed Architecture — lesson m03l02 — Cache Invalidation And The Three Hard Cases
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l02
# © LearnSome.tech
import random
rng = random.Random(7)
TTL, TICKS = 8, 32
herd = [4 + rng.randrange(9) for _ in range(TICKS)]

def origin_calls(single_flight):
    calls, fresh_until = 0, 0
    for tick, waiting in enumerate(herd):
        if tick >= fresh_until:
            calls += 1 if single_flight else waiting
            fresh_until = tick + TTL
    return calls

print("requesters per tick:", " ".join(str(n) for n in herd[:12]), "...")
naive = origin_calls(False)
guarded = origin_calls(True)
print(f"origin calls, no single flight: {naive}")
print(f"origin calls, single flight:    {guarded}")
print(f"the herd multiplied one miss by {naive // guarded}")
