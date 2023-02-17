# import sys
#
# sys.stdin = open('24.txt', 'r')

amount = int(input())

m = [['0' for j in range(10**5)] for i in range(21)]


for para in range(amount):
    s = input().split()
    a, b = int(s[0]), int(s[1])
    m[a-40][b] = '1'
for j in range(20, 0, -1):
    f = m[j]
    k = ''.join(f).find('1001')
    if k != -1:
        print(j+40, k+1)
        break
