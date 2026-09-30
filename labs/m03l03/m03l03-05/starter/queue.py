import random
rng = random.Random(7)
CONSUMER_RATE, TICKS = 22, 24
queue, worst_depth, worst_age = [], 0, 0
print("tick  arrived  depth  oldest age")
for tick in range(1, TICKS + 1):
    arrived = 45 if rng.random() < 0.12 else 10 + rng.randrange(8)
    queue.extend([tick] * arrived)
    del queue[:CONSUMER_RATE]
    age = tick - queue[0] if queue else 0
    worst_depth = max(worst_depth, len(queue))
    worst_age = max(worst_age, age)
    if tick % 3 == 0:
        print(f"{tick:>4} {arrived:>8} {len(queue):>6} {age:>11}")
print(f"worst depth {worst_depth}, worst age {worst_age}: bounded")
