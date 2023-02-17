def line(x, z):
    global a
    y = 0
    if x < k:
        if z.count(mas[x]) == 1:
            a.append(z.index(mas[x]) + 1)
            if len(a) == 1:
                ostov[0][a[-1] - 1] = 1
            else:
                ostov[a[-2] - 1][a[-1] - 1] = 1
            if column(x + 1, z.index(mas[x])) == 1:
                return column(x + 1, z.index(mas[x]))
            else:
                if len(a) == 1:
                    ostov[0][a[-1] - 1] = 0
                else:
                    ostov[a[-2] - 1][a[-1] - 1] = 0
                a.pop()
        elif z.count(mas[x]) == 0:
            return 0
        else:
            for i in range(f):
                if z[i] == mas[x] and (not a or a[-2] - 1 != i):
                    if not a:
                        if ostov[m.index(z)][i] == 0:
                            a.append(i + 1)
                            ostov[m.index(z)][i] = 1
                            if column(x + 1, i) == 1:
                                return column(x + 1, i)
                            else:
                                ostov[m.index(z)][i] = 0
                                a.pop()
                    else:
                        if ostov[a[-1] - 1][i] == 0:
                            a.append(i + 1)
                            ostov[m.index(z)][i] = 1
                            if column(x + 1, i) == 1:
                                return column(x + 1, i)
                            else:
                                ostov[a[-1] - 1][i] = 0
                                a.pop()
        if y == 0:
            return 0
    elif x == k:
        if len(a) == k:
            print()
            print('end: ', *a)
            print('-------------')
        return 1


def column(x, h):
    global a
    y = 0
    if x < k:
        for j in range(f):
            if m[j][h] == mas[x] and (not a or (len(a) == 1 and j != 0) or (len(a) > 1 and a[-2] - 1 != j)):
                a.append(j+1)
                ostov[j][h] = 1
                if line(x+1, m[j]) == 1:
                    return line(x+1, m[j]) == 1
                else:
                    ostov[j][h] = 0
                    a.pop()
        if y == 0:
            return 0
    elif x == k:
        if len(a) == k:
            print()
            print('done: ', *a)
            print('-------------')
        return 1


def igra(x):
    line(x, m[0])


n = int(input())

for l in range(n):
    a = []
    k = int(input())
    mas = input().split()
    f = int(input())
    m = []
    ostov = [[0 for j in range(f)] for i in range(f)]
    for i in range(f):
        r = input().split()
        m.append(r)
    print()

    igra(0)

    for i in ostov:
        for j in range(len(i)):
            print(i[j], end=' ')
        print()
    print()
