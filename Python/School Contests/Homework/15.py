p = []
q = []
for i in range(10, 40):
    p.append(i)
for i in range(23, 59):
    q.append(i)

for a in range(50):
    k = 0
    for x in range(1000):
        if (x not in p) or (x not in q) or (x in q and x == a):
            k += 1
    if k == 1000:
        print(a)
