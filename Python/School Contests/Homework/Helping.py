n = 1
s = 2
m = []
while s <= 2025 * (n + 1):
    n += 1
    s += n*(3*n-1)
    m.append(n)
print(m[-2])
