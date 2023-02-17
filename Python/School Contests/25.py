import sys

sys.stdin = open('25-B.txt', 'r')

amount = int(input())

m = []
for i in range(amount):
    s = int(input())
    m.append(s)

m.sort()

smin = 10000000001

k = 0
for x in range(amount):
    if k > 0:
        break
    else:
        for i in range(amount):
            if k > 0:
                break
            else:
                for j in range(amount):
                    if k > 0:
                        break
                    else:
                        s = m[x] + m[i] + m[j]
                        if (x != i and x != j and i != j) and (s % 3 == 0) and (s < smin):
                            smin = s
                            print(m[x], m[i], m[j])
                            k += 1
print(smin)
