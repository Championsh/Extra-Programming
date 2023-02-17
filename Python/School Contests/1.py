def po(a):
    kp = 0
    for i in range(2, int(a ** 0.5) + 1):
        if kp > 3:
            return 0
        else:
            if a % i == 0:
                if pr(i) == 1:
                    kp += 1
                if i * i != a and pr(a // i) == 1:
                    kp += 1
    if kp == 3:
        return 1
    else:
        return 0


def pr(n):
    k = 2
    for j in range(2, int(n ** 0.5) + 1):
        if k > 2:
            return 0
        else:
            if n % j == 0:
                if j * j == n:
                    k += 1
                else:
                    k += 2
    if k == 2:
        return 1
    else:
        return 0


a, b = 50001, 90000
b += 1
s = 0
m = []
for j in range(a, b):
    if po(j) == 1:
        s += 1
        m.append(j)
print(s)
print(m[0])
