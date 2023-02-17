def line(x, z, ostov):
    global a
    y = 0
    if x < k:
        if z.count(mas[x]) == 1:
            a.append(z.index(mas[x]) + 1)
            if len(a) == 1:
                ostov[0][a[-1] - 1] = 1
            else:
                ostov[a[-2] - 1][a[-1] - 1] = 1
            if column(x + 1, z.index(mas[x]), ostov) == 1:
                return column(x + 1, z.index(mas[x]), ostov)
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
                            ostov2 = create(ostov)
                            ostov2[m.index(z)][i] = 1
                            if column(x + 1, i, ostov2) == 1:
                                return column(x + 1, i, ostov2)
                            else:
                                a.pop()
                    else:
                        if ostov[a[-1] - 1][i] == 0:
                            a.append(i + 1)
                            ostov2 = create(ostov)
                            ostov2[m.index(z)][i] = 1
                            if column(x + 1, i, ostov2) == 1:
                                return column(x + 1, i, ostov2)
                            else:
                                ostov2 = []
                                a.pop()
        if y == 0:
            return 0
    elif x == k:
        if len(a) == k:
            print()
            print('ostov: ')
            for i in ostov:
                for j in range(len(i)):
                    print(i[j], end=' ')
                print()
            print()
            print('end: ', *a)
            print('-------------')
        return 1


def column(x, h, ostov):
    global a
    y = 0
    if x < k:
        for j in range(f):
            if m[j][h] == mas[x] and ((len(a) == 1 and j != 0) or (len(a) > 1 and a[-2] - 1 != j)):
                if ostov[j][h] == 0:
                    a.append(j + 1)
                    ostov2 = create(ostov)
                    ostov2[j][h] = 1
                    if line(x + 1, m[j], ostov2) == 1:
                        return line(x + 1, m[j], ostov2) == 1
                    else:
                        ostov2 = []
                        a.pop()
        if y == 0:
            return 0
    elif x == k:
        if len(a) == k:
            print()
            print('ostov: ')
            for i in ostov:
                for j in range(len(i)):
                    print(i[j], end=' ')
                print()
            print()
            print('done: ', *a)
            print('-------------')
        return 1


def igra(x):
    line(x, m[0], ostov)


def create(ostov):
    ostov2 = []
    for i in ostov:
        s = []
        for j in range(len(i)):
            s.append(i[j])
        ostov2.append(s)
    return ostov2


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

    print('********************************************************')
