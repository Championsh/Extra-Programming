def deli(n):
    m = [[], 0]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                m[0].append(i)
            else:
                m[0].append(i)
                m[0].append(n // i)
    if len(m[0]) < 2:
        f = 0
    else:
        f = max(m[0]) - min(m[0])
    if f % 23 == 9:
        s = [f, 1]
    else:
        s = [f, 0]
    return s


a = 350000
f = []
k = 0
while k < 6:
    m = deli(a)
    if m[1] == 1:
        s = [a, m[0]]
        f.append(s)
        k += 1
    a += 1
print(*f)
