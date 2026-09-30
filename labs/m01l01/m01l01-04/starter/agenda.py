TOTAL = 45
plan = [
    ("requirements and scope", 5),
    ("estimation", 5),
    ("api and data model", 8),
    ("high level design", 12),
    ("one deep dive", 10),
    ("failure modes", 5),
]
spent = 0
for step, minutes in plan:
    spent += minutes
    print(f"{spent:>3} min in | {step} | {minutes} min")
print("unspent:", TOTAL - spent, "min")
