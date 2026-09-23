# Scalable System Design & Distributed Architecture — lesson m05l02 — Observability As A Design Input
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m05l02
# © LearnSome.tech
client --> gateway --> service A --> queue --> worker --> service B
           rid=7fa2      rid=7fa2     rid=7fa2   rid=7fa2   rid=7fa2
           budget 800ms  left 780ms   left 640ms          left 210ms
