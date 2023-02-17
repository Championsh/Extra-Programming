import sys

sys.stdin = open('24.txt', 'r')

amount = int(input())

m = []
m2 = []
su = 0

for i in range(amount):
    a = int(input())
    m.append(a)

for i in range(4):
    m2.append(0)

for i in range(amount - 7):
    if m[i] % 14 == 0:
        m2[0] += 1
    elif m[i] % 2 == 0:
        m2[1] += 1
    elif m[i] % 7 == 0:
        m2[2] += 1
    else:
        m2[3] += 1

    if m[i + 7] % 14 == 0:
        su += sum([m2[j] for j in range(1, len(m2))])
    elif m[i + 7] % 2 == 0:
        su += m2[2] + m2[0]
    elif m[i + 7] % 7 == 0:
        su += m2[1] + m2[0]
    else:
        su += m2[0]
print(su)
