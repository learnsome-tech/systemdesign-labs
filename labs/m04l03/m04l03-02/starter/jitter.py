import random
rng = random.Random(7)
for attempt in range(1, 5):
    base = min(8.0, 0.5 * 2 ** (attempt - 1))
    waits = [rng.random() * base for _ in range(3)]
    print(attempt, base, [round(x, 2) for x in waits])
