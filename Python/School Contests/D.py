def hIN(m):
    global mas, h
    for i in range(m):
        s = list(map(int, input().split()))
        if s[0] == 1 and s[1] == m:
            for j in range(m):
                mas[j][len(h)] = 1
            h.append(0)
        elif s[0] > 1 and sum((int(s[i]) for i in range(1, len(s)))) + s[0] - 1 == m:
            dot = []
            f = 0
            for j in range(1, len(s)):
                dot.append(f + s[j])
                f += s[j]
            for j in range(m):
                if j not in dot:
                    mas[j][len(h)] = 1
            h.append(0)
        else:
            s = s[1:]
            h.append(s)


def lIN(n):
    global mas, l
    for i in range(n):
        s = list(map(int, input().split()))
        if s[0] == 1 and s[1] == n:
            for j in range(n):
                mas[len(l)][j] = 1
            l.append(0)
        elif s[0] > 1 and sum((int(s[i]) for i in range(1, len(s)))) + s[0] - 1 == n:
            leng = sum((int(s[i]) for i in range(1, len(s))))
            leng += s[0] - 1
            if leng == n:
                dot = []
                f = 0
                for j in range(1, len(s)):
                    dot.append(f + s[j])
                    f += s[j]
                for j in range(n):
                    if j not in dot:
                        mas[j][len(l)] = 1
                l.append(0)
        else:
            s = s[1:]
            l.append(s)


amount = 1

for trying in range(amount):
    n, m = map(int, input().split())
    mas = [[0 for j in range(n)] for i in range(m)]
    h = []
    l = []
    lIN(n)
    hIN(m)
    for x in mas:
        print(*x)
    print()
