# Scalable System Design & Distributed Architecture — lesson m06l02 — Worked Design One: Scaling The Ticket Booking System
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m06l02
# © LearnSome.tech
SEATS = 50_000
BUYERS = 500_000        # people who want one of them
CAP = 300               # purchase transactions a second the leader commits

print(f"buyers at sale open      {BUYERS:>10,}")
print(f"seats available          {SEATS:>10,}")
print(f"buyers per seat          {BUYERS / SEATS:>10,.0f}")
print(f"commit capacity          {CAP:>10,} a second")
print(f"served in the minute     {CAP * 60:>10,}")
print(f"overload at the door     {BUYERS / (CAP * 60):>10,.0f} times")
print(f"seconds to sell the room {SEATS / CAP:>10,.0f}")
