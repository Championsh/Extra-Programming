a, b = 200000000, 400000000
b += 1
g = []
for n in range(2, 30, 2):
    for m in range(1, 30, 2):
        f = 2 ** n * 3 ** m
        if a <= f < b:
            g.append(f)
g.sort()
print(g)
