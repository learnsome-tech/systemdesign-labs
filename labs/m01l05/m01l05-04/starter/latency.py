BUDGET_MS = 200
hops = [
    ("load balancer", 1),
    ("app server work", 20),
    ("cache read", 1),
    ("database read", 8),
    ("cross region call", 80),
]
spent = 0
for name, ms in hops:
    spent += ms
    print(f"{name:<18} {ms:>3} ms | running total {spent:>3} ms")
print(f"budget {BUDGET_MS} ms, headroom left {BUDGET_MS - spent} ms")
