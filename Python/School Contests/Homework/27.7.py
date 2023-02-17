# import sys
#
# sys.stdin = open('24.txt', 'r')

amount = int(input())

su = 0
m1 = [0 for i in range(4)]

for para in range(amount):
    m2 = [0 for i in range(4)]
    s = input().split()
    m = [int(s[0]), int(s[1])]
    m.sort()
    su += m[1]
    r = m[1] - m[0]
    for i in range(1, 4):
        m2[(i + r % 4) % 4] = m1[i] + r
    m2[r % 4] = r
    for i in range(1, 4):
        if m1[i] == 0:
            m1[i] = m2[i]
        elif m1[i] > m2[i] != 0:
            m1[i] = m2[i]
print(su)
print(m1)
print()
if su % 4 == 0:
    print(su - min(m1[1], m1[2], m1[3]))
else:
    print(su)
