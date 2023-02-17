import sys

sys.stdin = open('25-B.txt', 'r')

amount = int(input())

suma = 0
m = []
m2 = []
st = ''

for i in range(amount):
    s = input()
    if s[::-1] == s:
        m.append(s)
    else:
        m2.append(s)
print(1)
for i in range(len(m2)):
    for j in range(i + 1, len(m2)):
        if m2[i] == m2[j][::-1] and m2[i] != 'X':
            st += m2[i] + m2[j]
            m2[i] = 'X'
            m2[j] = 'X'
            break
print(2)
for i in range(len(m)):
    for j in range(i + 1, len(m)):
        if m[i] == m[j] and m[i] != 'X':
            st += m[i] + m[j]
            m[i] = 'X'
            m[j] = 'X'
            break
print(3)
ma = 0

for x in m:
    if x != 'X' and ma < int(x):
        ma = int(x)
print(4)
print(sum(map(int, [x for x in st])) + sum(map(int, [x for x in ma])))
