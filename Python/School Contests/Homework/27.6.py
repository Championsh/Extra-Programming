# import sys
#
# sys.stdin = open('24.txt', 'r')

amount = int(input())

m1 = []
m2 = []
m3 = []
m4 = []

for i in range(amount):
    n = int(input())
    if n % 5 == 0:
        if n % 2 == 0:
            m1.append(n)
        else:
            m2.append(n)
    elif n % 2 == 0:
        m3.append(n)
    else:
        m4.append(n)
m1.sort(reverse=True)
m2.sort(reverse=True)
m3.sort(reverse=True)
m4.sort(reverse=True)
a, b, c, d = 0, 0, 0, 0
if len(m1) > 0:
    a = m1[0]
if len(m2) > 0:
    b = m2[0]
if len(m3) > 0:
    c = m3[0]
if len(m4) > 0:
    d = m4[0]
print(max(a*d, b*c, a*b))
