import random
rng = random.Random(7)
KEYS, PER_TICK = 600, 400
cache, first = set(), 0
print("tick  hits  misses  hit%   origin qps")
for tick in range(1, 7):
    hits = 0
    for _ in range(PER_TICK):
        key = rng.randrange(KEYS)
        if key in cache:
            hits += 1
        else:
            cache.add(key)
    miss = PER_TICK - hits
    first = first or miss
    pct = hits * 100 // PER_TICK
    print(f"{tick:>4} {hits:>5} {miss:>7} {pct:>4}% {miss:>11}")
print(f"cold peak {first} against warm {miss}: {first // miss} times")
