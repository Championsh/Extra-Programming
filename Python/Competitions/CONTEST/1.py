n = int(input())
m = int(input())
n -= 1
n %= 7
n += m
n %= 7
if n == 0:
    n += 7
print(n)
