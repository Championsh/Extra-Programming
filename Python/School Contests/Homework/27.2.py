import sys

sys.stdin = open('24.txt', 'r')

n = int(input())
m1 = [0 for i in range(80)]
m2 = [0 for i in range(80)]
k = 0
for i in range(n):
    n = int(input())
    if n > 50:
        m2[n % 80] += 1
    else:
        m1[n % 80] += 1
for i in range(len(m2)):
    if 40 > i > 0:
        k += m1[(80 - i) % 80] * m2[i] + m2[80-i] * m2[i]
    elif i == 40 or i == 0:
        k += (m2[i] - 1) * m2[i] // 2 + m1[i] * m2[i]
    elif i > 40:
        k += m1[(80 - i) % 80] * m2[i]
print(k)
