import sys

sys.stdin = open('25-B.txt', 'r')

amount = int(input())

m = {}
m2 = {}
m3 = []
su = 0
ma = '0'

for x in range(amount):
    s = input()
    if s == s[::-1]:
        if s not in m:
            m[s] = 1
        else:
            m[s] += 1
    else:
        if s not in m2:
            m2[s] = 1
        else:
            m2[s] += 1

for a in m:
    su += sum(map(int, [z for z in a])) * (m[a] // 2) * 2
    m[a] %= 2
    if m[a] == 1 and ma < a:
        ma = a

for a in m2:
    j = a[::-1]
    if j in m2 and j not in m3:
        m3.append(a)
        m3.append(j)
        if m2[j] > m2[a]:
            su += sum(map(int, [z for z in a])) * m2[a] * 2
            m2[a] = 0
            m2[j] -= m2[a]
        elif m2[j] <= m2[a]:
            su += sum(map(int, [z for z in a])) * m2[j] * 2
            m2[j] = 0
            m2[a] -= m2[j]

print(su + sum(map(int, [z for z in ma])))
