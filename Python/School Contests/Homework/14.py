def sem(n):
    s = ''
    while n > 0:
        s = str(n % 7) + s
        n //= 7
    return s


def vosm(n):
    s = ''
    while n > 0:
        s = str(n % 8) + s
        n //= 8
    return s


def shest(n):
    s = ''
    while n > 0:
        if n % 16 < 10:
            s = str(n % 16) + s
        elif n % 16 == 10:
            s = 'A' + s
        elif n % 16 == 11:
            s = 'B' + s
        elif n % 16 == 12:
            s = 'C' + s
        elif n % 16 == 13:
            s = 'D' + s
        elif n % 16 == 14:
            s = 'E' + s
        elif n % 16 == 15:
            s = 'F' + s
        n //= 16
    return s


def dv(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s


for x in range(401):
    n = 343 ** 5 + 7 ** 3 - 1 - x
    a = sem(n)
    if a.count('6') == 12:
        print(a)
        print(x)
