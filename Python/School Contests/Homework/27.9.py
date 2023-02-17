# import sys
from collections import Counter
#
# sys.stdin = open('24.txt', 'r')

amount = int(input())

su = 1000000
m = [[] for i in range(9)]
a = []
g = []

for i in range(amount):
    n = int(input())
    m[n % 9].append(n)
for i in range(9):
    m[i].sort()
for z in range(9):
    for x in range(9):
        for c in range(9):
            for v in range(9):
                if (z + x + c + v) % 9 == 0:
                    a1 = [z, x, c, v]
                    a2 = {}
                    a3 = dict(Counter(a1))
                    a0 = list(a3.keys())
                    a0.sort()
                    for f in a0:
                        a2[f] = dict(Counter(a1))[f]
                    if len(m[z]) != 0 and len(m[x]) != 0 and len(m[c]) != 0 and len(m[v]) != 0:
                        if a2 not in g:
                            a.append(a1)
                            g.append(a2)
print(*a)
print(*m)
