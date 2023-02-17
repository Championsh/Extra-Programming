def ma(a, b):
    a -= b
    k = '1' * b + '0' * a
    y = '0' * a + '1' * b
    m.append(y)
    x = int(k, 2)
    y = int(y, 2)
    for i in range(y + 1, x):
        f = bin(i)[2:]
        if f.count('1') == b:
            m.append(f.rjust(a + b, '0'))
    m.append(k)
    print(*m, sep='\n')


a, b = map(int, input().split())
m = []
ma(a, b)
