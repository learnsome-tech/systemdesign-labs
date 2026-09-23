# Scalable System Design & Distributed Architecture — lesson m03l04 — The Difference Between A Queue And A Log
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l04
# © LearnSome.tech
LOG = [f"r{n}" for n in range(1, 11)]
inbox, taken = list(LOG), {"A": [], "B": []}
while inbox:
    for c in ("A", "B"):
        if inbox:
            taken[c].append(inbox.pop(0))
print("queue A took ", " ".join(taken["A"]))
print("queue B took ", " ".join(taken["B"]))
print("queue left   ", inbox, "-> nothing left to replay")
offset = {"A": 0, "B": 0, "C": 0}
for c in ("A", "B"):
    read = LOG[offset[c]:]
    offset[c] += len(read)
    print(f"log   {c} read  {len(read)} records, offset {offset[c]}")
replay = LOG[offset["C"]:]
print("log   C joins late, replays", len(replay), "records from offset 0")
print("log   retains ", " ".join(LOG))
