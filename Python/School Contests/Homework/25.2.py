def deli(n):
    m = [0, 0]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                m[0] += i
            else:
                m[0] += i
                m[0] += n // i
    if m[0] % 13 == 0 and m[0] != 0:
        m[1] = 1
    return m


def sort_pr(n):
    return n[0]


a = 350300
f = []
k = 0
while k < 6:
    m = deli(a)
    if m[1] == 1:
        s = [a, m[0]//13]
        f.append(s)
        k += 1
    a += 1
print(*sorted(f, key=sort_pr))
