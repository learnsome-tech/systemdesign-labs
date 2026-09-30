DAYS = 30
OBJECTIVE = 0.999                  # the monthly objective
MINUTES = DAYS * 24 * 60
budget = MINUTES * (1 - OBJECTIVE)
elapsed = 10                       # days into the month

print(f"objective {OBJECTIVE * 100:.1f}% -> {budget:.1f} budget minutes")
for observed in (0.0005, 0.002, 0.004):
    spent = MINUTES * (elapsed / DAYS) * observed
    burn = observed / (1 - OBJECTIVE)
    left = (budget - spent) / (MINUTES * observed / DAYS)
    tail = f"{left:4.1f} days left" if left > 0 else "budget gone"
    print(f"errors {observed * 100:.2f}%: spent {spent:5.1f} min, "
          f"burn {burn:4.1f}x, {tail}")
