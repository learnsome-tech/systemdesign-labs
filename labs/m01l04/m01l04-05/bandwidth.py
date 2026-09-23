# Scalable System Design & Distributed Architecture — lesson m01l04 — Back Of The Envelope Estimation: Storage And Bandwidth
# https://learnsome.tech/courses/systemdesign-course/watch?lesson=m01l04
# © LearnSome.tech
PEAK_READ_QPS = 20_833
RESPONSE_BYTES = 4_000
IMAGE_SHARE = 0.1
IMAGE_BYTES = 250_000
BITS = 8
GIGA = 1000 ** 3

json_bps = PEAK_READ_QPS * RESPONSE_BYTES * BITS
image_bps = PEAK_READ_QPS * IMAGE_SHARE * IMAGE_BYTES * BITS
print(f"json egress   {json_bps / GIGA:7.2f} gigabit a second")
print(f"image egress  {image_bps / GIGA:7.2f} gigabit a second")
print(f"total         {(json_bps + image_bps) / GIGA:7.2f} gigabit a second")
cached = image_bps * 0.05
print(f"images at 95 percent cache hit {cached / GIGA:6.2f} gigabit a second")
