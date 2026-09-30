SEATS = 50_000
WINDOW = 120            # most of the house goes in the first two minutes
MAPS_PER_BUY = 30       # seat maps rendered for every purchase
HOLD = 300              # seconds a checkout may hold a seat

buys = SEATS / WINDOW
print(f"seats on sale             {SEATS:>10,}")
print(f"purchases a second        {buys:>10,.0f}")
print(f"seat map reads a second   {buys * MAPS_PER_BUY:>10,.0f}")
print(f"rows held at once         {buys * HOLD:>10,.0f}")
print(f"daily mean, same show     {SEATS / 86400:>10,.2f}")
print(f"spike over mean           {buys / (SEATS / 86400):>10,.0f} times")
