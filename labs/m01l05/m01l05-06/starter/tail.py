SLOW = 0.01

def all_fast(calls):
    return (1 - SLOW) ** calls

for calls in (1, 5, 20, 100):
    slow = (1 - all_fast(calls)) * 100
    print(f"{calls:>4} calls in one request -> {slow:5.1f} percent are slow")
