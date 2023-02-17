def vosm(a):
    va = ''
    while a > 0:
        va = str(a % 8) + va
        a //= 8
    return va


# ans = 882

kol = 0
for i in range(512, 4096):
    s = vosm(i)
    k = 0
    so = s
    if s == s[::-1]:
        k = 2
    else:
        for j in range(len(s) - 1):
            if s[j] == s[j + 1] and s.count(s[j]) == 2 and s[j] != 'x':
                k += 1
                s = s[:j] + 'x' + s[j + 1:]
    if k == 1:
        kol += 1
print(kol)
