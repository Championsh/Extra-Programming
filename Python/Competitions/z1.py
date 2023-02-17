n = int(input())
t = []
for i in range(n+1):
    t.append([0, 0])
t[1] = [9, 45]
for i in range(2, n+1):
    if (i-1) % 2 != 0:
        t2 = 5
    else:
        t2 = 15
    t2 += t[i-1][1] + 45
    t1 = t[i-1][0] + t2 // 60
    t2 %= 60
    t[i] = [t1, t2]
print(*t[-1])
