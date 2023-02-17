# import sys
#
# sys.stdin = open('24.txt', 'r')

amount = int(input())

m1 = []
m2 = []

for speed in range(amount):
    s = input()
    z = s[0]
    n = int(s[1:])
    if z == '+':
        m1.append(n)
    else:
        m2.append(n)
m1.sort()
m2.sort()
if len(m2) > 0:
    print(-1*m2[-1] * m1[-1])
else:
    print(m1[0] * m1[1])
