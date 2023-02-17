# import tqdm
#
#
# def pr(x):
#     global f
#     kn = 0
#     for i in range(1, int(x ** 0.5) + 1):
#         if kn > 5:
#             return 0
#         else:
#             if x % i == 0:
#                 if i % 2 != 0:
#                     kn += 1
#                 if x % (x // i) == 0 and (x // i) % 2 != 0 and i != (x // i):
#                     kn += 1
#     if kn == 5:
#         return 1
#
#
# d = []
# for i in range(3, int(50000000 ** 0.25) + 1, 2):
#     if i ** 4 <= 50000000:
#         d.append(i ** 4)
#
# for n in d:
#     if 45000000 <= n <= 50000000:
#         if pr(n) == 1:
#             print(n)
#     else:
#         f = 0
#         while (2 ** f) * n <= 50000000:
#             h = (2 ** f) * n
#             if 45000000 <= h <= 50000000:
#                 if pr(h) == 1:
#                     print(h)
#                 break
#             else:
#                 f += 1

def p(a):
    k = 0
    for i in range(1, int(a**0.5) + 1):
        if k < 3:
            if a % i == 0:
                if i*i != a:
                    k += 2
                else:
                    k += 1
        else:
            return 0
    if k == 2:
        return 1
    else:
        return 0


m = []
j = []

for i in range(1, int(16238 ** 0.25) + 1):
    if p(i) == 1:
        m.append(i)

for x in m:
    if 11275 <= x**4 <= 16329:
        f = 0
        while f <= 4:
            j.append(x**f)
            f += 1
print(*j)
