import random
SEATS = ["A1", "A2", "A3"]

def sale(guard):
    rng = random.Random(7)
    ver = {s: 0 for s in SEATS}
    owner = {s: None for s in SEATS}
    picks = [(b, rng.choice(SEATS)) for b in range(12)]
    seen = {b: ver[s] for b, s in picks}
    sold = retry = 0
    for b, s in picks:
        if guard and ver[s] != seen[b]:
            retry += 1
            continue
        ver[s], owner[s] = seen[b] + 1, b
        sold += 1
    taken = sum(1 for s in SEATS if owner[s] is not None)
    return sold, sold - taken, retry
for g in (False, True):
    sold, over, retry = sale(g)
    tag = "version check" if g else "no protection"
    print(f"{tag:>13}: sold {sold:>2} oversold {over:>2} retried {retry:>2}")
