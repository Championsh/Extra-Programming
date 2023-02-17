# import sys
#
# sys.stdin = open('24.txt', 'r')

amount = int(input())

su1, su2, su3 = 0, 0, 0
minr1, minr2, minr3 = 10**4, 10**4, 10**4

for troiki in range(amount):
    a, b, c = map(int, input().split())
    m = [a, b, c]
    m.sort()
    a, b, c = m[0], m[1], m[2]
    su3 += a
    su1 += b
    su2 += c
    if a % 2 != b % 2 and minr1 > b - a:
        minr1 = b - a
    if a % 2 != c % 2 and minr2 > c - a:
        minr2 = c - a
    if b % 2 != c % 2 and minr3 > c - b:
        minr3 = c - b

if (su1 % 2 == su2 % 2 != 0 and minr3 < 10**4) or (su1 % 2 == su2 % 2 == 0):
    print(su3)
else:
    print('Another')
    print(su1, su2, su3)
    print(minr1, minr2, minr3)
