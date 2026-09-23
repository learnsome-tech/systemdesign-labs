# Scalable System Design & Distributed Architecture — lesson m03l01 — Caching Strategies And Topology
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m03l01
# © LearnSome.tech
CACHE_MS, ORIGIN_MS = 1.0, 40.0
PEAK_READS = 20833
print("hit%   mean ms   origin qps   vs 99% hit")
best = PEAK_READS // 100
for hit in (99, 95, 90, 80, 50):
    miss = 100 - hit
    mean = (hit * CACHE_MS + miss * ORIGIN_MS) / 100
    qps = PEAK_READS * miss // 100
    print(f"{hit:>3}   {mean:7.2f}   {qps:>10}   {qps / best:6.1f}x")
print("origin must be sized for the miss rate, not the hit rate")
