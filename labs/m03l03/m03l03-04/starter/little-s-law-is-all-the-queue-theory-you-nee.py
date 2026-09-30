L = lambda x W      depth  = arrivals per second x seconds waited
W = L / lambda      wait   = depth / drain rate

1,200 deep, drained at 50/s  ->  24 s behind, right now
same queue, 100 deep         ->  2 s behind

the depth is a latency reading, not a storage reading
