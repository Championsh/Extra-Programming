# import sys
#
# sys.stdin = open('24.txt', 'r')

amount = int(input())

a = [0 for i in range(11)]

su = 0
for stroka in range(amount):
    a1 = [0 for i in range(11)]
    a2 = [0 for i in range(11)]
    s = input().split()
    m = [int(s[0]), int(s[1]), int(s[2])]
    m.sort()
    su += m[0]
    minr1 = m[1] - m[0]
    minr2 = m[2] - m[0]

    for i in range(len(a)):
        if a[i] != 0:
            a1[(i + minr1 % 11) % 11] = a[i] + minr1
    a1[minr1 % 11] = minr1

    for i in range(len(a)):
        if a[i] != 0:
            a2[(i + minr2 % 11) % 11] = a[i] + minr2
    a2[minr2 % 11] = minr2

    for i in range(1, len(a)):
        if a1[i] == 0:
            a1[i] = a2[i]
        elif a1[i] > a2[i] != 0:
            a1[i] = a2[i]

    for i in range(1, len(a)):
        if a[i] == 0:
            a[i] = a1[i]
        elif a[i] > a1[i] != 0:
            a[i] = a1[i]
print(su + a[(11 - su % 11) % 11])
print(su)
print(a)
