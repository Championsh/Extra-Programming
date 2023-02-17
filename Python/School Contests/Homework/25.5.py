def deli(n):
    k = 2
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                k += 1
            else:
                k += 2
    return k


def sort(n):
    return n[0]


a, b = 84052, 84130
b += 1
f = []
for i in range(a, b):
    k = deli(i)
    s = [k, i]
    f.append(s)
f = sorted(f, key=sort)
print(f[-1])
