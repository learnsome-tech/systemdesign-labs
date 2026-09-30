MINUTES_A_MONTH = 30 * 24 * 60

def allowed(percent):
    return MINUTES_A_MONTH * (1 - percent / 100)

for target in (99.0, 99.9, 99.95, 99.99):
    print(f"{target:>5} percent -> {allowed(target):7.1f} min a month")

series = 0.999 ** 5 * 100
print(f"five services at 99.9 in series -> {series:.2f} percent")
print(f"which allows {allowed(series):.0f} min a month")
