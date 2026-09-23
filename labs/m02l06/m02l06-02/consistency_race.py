# Scalable System Design & Distributed Architecture — lesson m02l06 — Eventual Consistency And What It Costs A Product
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m02l06
# © LearnSome.tech
leader = {"cart": 3}
follower = {"cart": 2}
print("t0 leader", leader["cart"], "follower", follower["cart"])
leader["cart"] = 3
print("t1 write acknowledged", leader["cart"])
print("t1 refresh from follower", follower["cart"])
follower["cart"] = leader["cart"]
print("t2 after replication", follower["cart"])
print("safe route after write: leader")
