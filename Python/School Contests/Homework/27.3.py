# import sys
import math
#
# sys.stdin = open('24.txt', 'r')

amount = int(input())

m = [0 for i in range(12)]

k = 0

for chislo in range(amount):
    a = int(input())
    m[a % 12] += 1

for i in range(len(m)):
    for j in range(len(m)):
        for f in range(len(m)):

