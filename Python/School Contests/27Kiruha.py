# import sys
#
# sys.stdin = open('27.txt', 'r')

amount = int(input())

m = []

for chislo in range(amount):
    n = int(input())
    m.append(n)

t = [0 for i in range(73)]
a = [0 for i in range(73)]

sum = 0
ama = 0

for i in range(amount):
    t1 = [0 for h in range(73)]
    f = m[i] % 73
    for j in range(73):
        if t[j] != 0:
            t1[(j + f) % 73] = t[j] + m[i]
            a[(j + f) % 73] = a[j] + 1
    if m[i] > t1[f]:
        t1[f] = m[i]
        a[f] = 1
    for j in range(73):
        t[j] = t1[j]
    if t1[0] > sum:
        sum = t1[0]
        ama = a[0]
    elif t1[0] == sum and a[0] < ama:
        ama = a[0]
print(ama)
