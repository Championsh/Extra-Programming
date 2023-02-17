def sort(n):
    return n[0]


a, b = 10 ** 8, 3 * 10 ** 8
b += 1
f = []
for i in range(a, b):
    m = 0
    n = 0
    k = i
    while i % 2 == 0:
        i //= 2
        m += 1
    while i % 7 == 0:
        i //= 7
        n += 1
    if m % 2 != 0 and n % 2 == 0 and i == 1:
        s = [k, m + n]
        f.append(s)
print(*sorted(f, key=sort))
