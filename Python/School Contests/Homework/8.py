from collections import Counter

def vosm(a):
    va = ''
    while a > 0:
        va = str(a % 8) + va
        a //= 8
    return va


def check(s):
    k = 0
    f = dict(Counter(s))
    j = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1] and s.count(s[i]) == 2:
            k += 1
            j = s[i]

    for x in f:
        if x != j and f[x] > 1:
            return 0
    if k == 1:
        return 1
    else:
        return 0


kol = 0
for n in range(512, 4096):
    s = vosm(n)
    if check(s) == 1:
        print(s)
        kol += 1
print(kol)
