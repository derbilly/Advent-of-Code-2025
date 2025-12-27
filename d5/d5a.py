import sys

freshies = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    limits = [int(x) for x in line.split('-')]
    freshies.append((limits[0], limits[1]))

num_fresh_ingredients = 0
while True:
    line = sys.stdin.readline()
    if not line:
        break
    line = line.strip()
    ingredient = int(line)
    for start, stop in freshies:
        if (ingredient >= start) and (ingredient <= stop):
            num_fresh_ingredients += 1
            break
possible_ingredients = 0

# clear conflicts
n = 0
while n < len(freshies):
    a1, a2 = freshies[n]
    for b1, b2 in freshies[n+1:]:
        if b1 <= a1 and b2 >= a1:
            a1 = b2 + 1
        elif b1 <= a2 and b2 >= a2:
            a2 = b1 - 1
        elif b1 > a1 and b2 < a2:
            freshies.append((b2 + 1, a2))
            a2 = b1 - 1
    freshies[n] = (a1, a2)
    n += 1

for a1, a2 in freshies:
    possible_ingredients += max(a2 - a1 + 1, 0)

print(f"{num_fresh_ingredients} fresh ingredients.")
print(f"{possible_ingredients} possible ingredients.")

