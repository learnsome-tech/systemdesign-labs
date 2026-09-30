WORK_MS = 40.0     # the real work, identical either way
IN_PROC = 0.0001   # a function call, at memory speed
HOP = 0.5          # one datacentre round trip
AVAIL = 0.999      # availability of one deployable

def price(calls, cost, parts):
    return WORK_MS + calls * cost, AVAIL ** parts

priced = []
for name, calls, cost, parts in (("monolith", 4, IN_PROC, 1),
                                 ("four services", 4, HOP, 4)):
    ms, up = price(calls, cost, parts)
    priced.append((ms, up))
    print(f"{name:<14} {ms:6.2f} ms   {up * 100:7.4f}% up   "
          f"{(1 - up) * 43200:6.1f} min down a month")

(m1, u1), (m2, u2) = priced
print(f"latency cost:  {(m2 / m1 - 1) * 100:.1f}% slower")
print(f"downtime cost: {(1 - u2) / (1 - u1):.1f} times more minutes")
