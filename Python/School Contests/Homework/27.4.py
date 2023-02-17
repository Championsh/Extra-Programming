# import sys
#
# sys.stdin = open('24.txt', 'r')

amount = int(input())

m = []
m2 = []
su = 0

for i in range(amount):
    a = int(input())
    m.append(a)

for i in range(2):
    m2.append(0)

for i in range(amount - 5):
    if m[i] % 13 == 0:
        m2[0] += 1
    else:
        m2[1] += 1

    if m[i + 5] % 13 == 0:
        su += sum([m2[j] for j in range(len(m2))])
    else:
        su += m2[0]
print(su)
