import sys
from collections import Counter

sys.stdin = open('24.txt', 'r')

jmin = 100000001
ami = 1000000001

for amount in range(1000):
    s = input()
    if s.count('N') < jmin:
        jmin = s.count('N')
        smin = s

a = dict(Counter(smin))
vmax = 0

for k, v in dict(a).items():
    if v > vmax:
        vmax = v
        kmax = k
    if v == vmax:
        if ord(k) > ord(kmax):
            kmax = k
print(kmax)


