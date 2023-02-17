import sys

sys.stdin = open('25-A.txt', 'r')

amount = int(input())

su = 0
minrch1, minrch2 = 1000000, 1000000
minrnch1, minrnch2 = 1000000, 1000000
kch, knch = 0, 0
for raz in range(amount):
    m = []
    s = input().split()
    for x in s:
        m.append(int(x))
    su += min(m)
    if min(m) % 2 == 0:
        kch += 1
    else:
        knch += 1

    if min(m) % 2 != max(m) % 2:
        if min(m) % 2 == 0:
            if max(m) - min(m) < minrch1:
                minrch2 = minrch1
                minrch1 = max(m) - min(m)
            elif max(m) - min(m) < minrch2:
                minrch2 = max(m) - min(m)
        else:
            if max(m) - min(m) < minrnch1:
                minrnch2 = minrnch1
                minrnch1 = max(m) - min(m)
            elif max(m) - min(m) < minrnch2:
                minrnch2 = max(m) - min(m)
print(su, kch, knch)
print(minrch1, minrch2, minrnch1, minrnch2)
