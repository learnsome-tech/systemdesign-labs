raw = [
    ("c-71", 1, 100, "are we still on"),
    ("c-82", 2, 98, "yes, seven"),
    ("c-71", 1, 104, "are we still on"),
    ("c-93", 3, 102, "bringing the deck"),
    ("c-82", 2, 99, "yes, seven"),
]
print("ordered by wall clock:")
for cid, seq, ts, text in sorted(raw, key=lambda r: r[2]):
    print(f"  {ts}  {text}")
seen = {}
for cid, seq, ts, text in raw:
    seen.setdefault(cid, (seq, text))
print("ordered by conversation sequence:")
for seq, text in sorted(seen.values()):
    print(f"  {seq}  {text}")
