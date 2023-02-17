def dv(ma, a):
    if len(ma) > 1:
        f = len(ma) // 2
        if ma[f] == a:
            return 1
        elif ma[f] < a:
            return dv(ma[f:], a)
        else:
            return dv(ma[:f], a)
    else:
        if a == ma[0]:
            return 1
        else:
            return 0


import sys

sys.stdin = open('24.txt', 'r')

amount = int(input())

m = []

for i in range(amount):
    a = int(input())
    m.append(a)
m.sort()
