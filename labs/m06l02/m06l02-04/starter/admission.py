CAP, SEATS = 300, 50_000
crowd = [200_000 // (t + 1) for t in range(180)]
PLANS = (("open door", 0), ("bounded queue", 20_000), ("waiting room", 400_000))
def sim(room):
    q = sold = lost = wait = 0
    for new in crowd:
        offered = new
        if room:
            drop = max(0, new - (room - q))
            lost += drop
            q += new - drop
            offered = min(q, CAP)
            q -= offered
        eff = CAP if offered <= CAP else max(CAP // 4, CAP * CAP // offered)
        done = min(eff, offered, SEATS - sold)
        sold, lost = sold + done, lost + (0 if room else offered - done)
        wait = max(wait, q // CAP)
    return sold, lost, wait, 1 if room else max(crowd) / CAP
print(f"{'plan':<14}{'sold':>7}{'lost':>13}{'wait':>7}{'contention':>12}")
for name, room in PLANS:
    a, b, c, d = sim(room)
    print(f"{name:<14}{a:>7,}{b:>13,}{c:>6}s{d:>11.0f}x")
