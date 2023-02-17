import sys

sys.stdin = open('25-A.txt', 'r')

amount = int(input())

s1 = 0
s2 = 0
minr1, minr2, minr3 = 10 ** 6, 10 ** 6, 10 ** 6

for i in range(amount):
    a, b = map(int, input().split())
    if a % 2 != 0:
        mi = min(a, b)
        ma = max(a, b)
        s1 += ma
        s2 += mi
        f = ma + mi
        if ma % 2 != mi % 2:
            if ma % 2 != 0:
                if f < minr1:
                    minr1 = f
            elif f < minr2:
                minr2 = f
        elif ma % 2 != 0 and f < minr3:
            minr3 = f
if minr1 + minr3 < minr2 or minr2 + minr3 < minr1:
    print('Be careful!')
print(s1, s2, s1 + s2)
print(minr1, minr2, minr3)
# Ошибка в том, что minr2+minr3<minr1 =(
