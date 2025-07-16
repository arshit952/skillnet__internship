bottle=int(input("Enter the no of bottle"))
bottle_per_day=int(input("Enter the no of bottle"))
day=1
drank_bottle=0
while bottle>0:
    if bottle>=bottle_per_day:
        drank_bottle=drank_bottle+bottle_per_day
    else:
        drank_bottle=bottle + drank_bottle
    bottle=bottle-drank_bottle
    if bottle<=bottle/2:
        print("half bottles left")

    print(f"Day {day}: Drank {drank_bottle} bottle {bottle} left.")
    day += 1
print("refill bottle")