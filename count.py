input = "aassdddfffgg"
count = {}

for char in input:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for char in sorted(count):
    print(f"{char.upper()}= {count[char]}")
