import sys
import math

sys.stdin = open('25.txt', 'r')

n = int(input())

m1 = [99999] * 10

sma = 0
smi = 0

for i in range(n):

    s = input()
    a = list(map(int, s.split()))
    sma += max(a)
    smi += min(a)
    r = abs(a[0] - a[1])
    m2 = [99999] * 10

    for z in m1:
        if z + r < m2[(z + r) % 10]:
            m2[(z + r) % 10] = z + r
    if m1[r % 10] > r:
        m1[r % 10] = r
        m2[r % 10] = r
    for j in range(10):
        if m1[j] > m2[j]:
            m1[j] = m2[j]

if sma % 10 == smi % 10:
    print(smi)
else:
    smi += m1[(sma - smi) % 10]
    print(smi)
