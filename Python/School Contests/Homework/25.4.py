def deli(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


a, b = 245690, 245756
b += 1
f = []
k = 0
for i in range(a, b):
    if deli(i) == 1:
        s = [k, i]
        f.append(s)
    k += 1
print(*f)
