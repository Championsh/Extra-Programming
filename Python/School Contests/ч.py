import sys

sys.stdin = open('25-A.txt', 'r')

f = int(input())
m = []
su = 0

for i in range(f):
    a = int(input())
    m.append(a)

m.sort(reverse=True)

for i in range(len(m)):
    x = m[i]
    if x % 34 == 0:
        ch = x
        jch = i
        break

for i in range(len(m)):
    x = m[i]
    if x % 17 == 0 and x % 2 != 0:
        nch = x
        jnch = i
        break

for i in range(len(m)):
    x = m[i]
    if i != jch and x % 2 == 0:
        mch = x
        break

for i in range(len(m)):
    x = m[i]
    if i != jch and x % 2 != 0:
        mnch = x
        break

if mch + ch > mnch + nch:
    print(mch, ch)
else:
    print(mnch, nch)
