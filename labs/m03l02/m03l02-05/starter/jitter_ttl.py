import random
KEYS, TTL, TICKS = 12, 10, 40

def refills(jitter):
    rng = random.Random(11)
    per_tick = [0] * TICKS
    for _ in range(KEYS):
        tick = 0
        while True:
            tick += TTL + (rng.randrange(9) if jitter else 0)
            if tick >= TICKS:
                break
            per_tick[tick] += 1
    return per_tick

for label, jitter in (("flat ttl", False), ("jittered", True)):
    load = refills(jitter)
    busy = [t for t, n in enumerate(load) if n]
    print(f"{label}  peak {max(load):>2} in a tick, {len(busy):>2} busy ticks")
print("same keys, same total work, spread instead of stacked")
