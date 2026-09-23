# Scalable System Design & Distributed Architecture — lesson m05l03 — Capacity Planning As A Design Input
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m05l03
# © LearnSome.tech
print("busy   response time versus an idle system")
for pct in (50, 60, 70, 80, 90, 95, 99):
    rho = pct / 100
    wait = 1 / (1 - rho)
    print(f"{pct:3d}%   {wait:6.1f}x   {'#' * min(40, round(wait))}")
print("the knee is real: ten points of load, ten times the wait")
