# Scalable System Design & Distributed Architecture — lesson m01l03 — Back Of The Envelope Estimation: Traffic And Throughput
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m01l03
# © LearnSome.tech
DAU = 20_000_000
READS_A_USER = 30
WRITES_A_USER = 2
PEAK_FACTOR = 3
A_DAY = 86_400
PER_SERVER = 2_000

reads = DAU * READS_A_USER / A_DAY
writes = DAU * WRITES_A_USER / A_DAY
print(f"mean read qps    {reads:9.0f}")
print(f"mean write qps   {writes:9.0f}")
print(f"peak read qps    {reads * PEAK_FACTOR:9.0f}")
print(f"peak write qps   {writes * PEAK_FACTOR:9.0f}")
print(f"read write ratio {READS_A_USER / WRITES_A_USER:9.0f} to one")
need = reads * PEAK_FACTOR / PER_SERVER
print(f"servers at peak  {need:9.1f} -> {int(need) + 1} with none spare")
