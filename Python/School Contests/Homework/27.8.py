# import sys
#
# sys.stdin = open('24.txt', 'r')

amount = int(input())

m1 = []
m2 = []
m3 = []
m4 = []

for i in range(amount):
    n = int(input())
    if n % 17 == 0:
        if n % 2 == 0:
            m1.append(n)
        else:
            m2.append(n)
    elif n % 2 == 0:
        m3.append(n)
    else:
        m4.append(n)
m1.sort(reverse=True)
m2.sort(reverse=True)
m3.sort(reverse=True)
m4.sort(reverse=True)
print(m1)
print(m2)
print(m3)
print(m4)
