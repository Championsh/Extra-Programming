def dv(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s


for n in range(100):
    h = 2*n
    a = dv(h)
    for i in range(2):
        s = 0
        for x in a:
            s += int(x)
        a += str(s % 2)
    h = 2 ** (len(a) - 1)
    f = 0
    for i in range(len(a)):
        f += int(a[i]) * h
        h //= 2
    if f > 249:
        print(n)
