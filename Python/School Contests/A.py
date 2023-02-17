def igra(p, q, k):
    a = [0] * (p + 1)
    a[1] = 1
    for i in range(2, q + 1):
        if i % k == 0:
            a[i] = a[i - 1] + a[i // k]
        else:
            a[i] = a[i - 1]
    for i in range(q):
        a[i] = 0
    for i in range(q + 1, p + 1):
        if i % k == 0:
            a[i] = a[i - 1] + a[i // k]
        else:
            a[i] = a[i - 1]

    print(a[p])


n = int(input())
m = []

for l in range(n):
    mas = []
    p, q, k = map(int, input().split())
    mas.append(p)
    mas.append(q)
    mas.append(k)
    m.append(mas)

for x in m:
    igra(x[0], x[1], x[2])