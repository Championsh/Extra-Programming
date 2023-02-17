from collections import Counter

o = int(input())
s = input()
if s == s[::-1]:
    print(s)
else:
    a = dict(Counter(s))
    k = 0
    m1 = []
    j = []
    for x in a:
        if a[x] % 2 != 0:
            if a[x] > 1:
                for i in range(a[x] // 2):
                    m1.append(x)
            k += 1
            j.append(x)
        else:
            for i in range(a[x] // 2):
                m1.append(x)
    s = ''
    if k >= 1:
        j.sort()
        f = j[0]
        m1.sort()
        m3 = sorted(m1, reverse=True)
        for x in m1:
            s += x
        s += f
        for x in m3:
            s += x
    else:
        m1.sort()
        m2 = sorted(m1, reverse=True)
        for x in m1:
            s += x
        for x in m2:
            s += x
    print(s)
