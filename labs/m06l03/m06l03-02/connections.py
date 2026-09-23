# Scalable System Design & Distributed Architecture — lesson m06l03 — Worked Design Two: A Global Chat System
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m06l03
# © LearnSome.tech
DAU = 200_000_000
PER_USER = 40           # messages a day each active user sends
CONNECTED = 0.10        # share of them holding a socket at the peak
PER_NODE = 60_000       # sockets one gateway pod terminates

msgs = DAU * PER_USER
sockets = int(DAU * CONNECTED)
print(f"messages a day          {msgs:>14,}")
print(f"messages a second       {msgs // 86400:>14,}")
print(f"peak, three times mean  {msgs // 86400 * 3:>14,}")
print(f"sockets at the peak     {sockets:>14,}")
print(f"gateway pods needed     {sockets // PER_NODE:>14,}")
print(f"sockets per message     {sockets / (msgs / 86400):>14,.1f}")
