from collections import Counter
s = input()
a = dict(Counter(s))
k = 0
m1 = []
for x in a:
    if a[x] % 2 != 0:
        k += 1
        j = x
    else:
        for i in range(a[x]//2):
            m1.append(x)
s = ''
if k > 1:
    print('-1')
elif k == 1:
    m1.sort()
    m3 = sorted(m1, reverse=True)
    for x in m1:
        s += x
    s += j
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
