import math


def log2():
    n = float(input())
    print(math.log2(n))


def shen():
    amount = int(input())
    s = 0
    m = []
    I = 0
    for i in range(amount):
        n = int(input())
        m.append(n)
        s += n
    for x in m:
        f = x / s
        I -= f * math.log2(f)
    return I


def dv():
    n = int(input())
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    print(s)


dv()
