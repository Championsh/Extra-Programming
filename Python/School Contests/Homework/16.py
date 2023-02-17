from collections import Counter

f = []
for i in range(1000):
    f.append(0)
f[1] = 1
for i in range(2, 27):
    if i % 2 == 0:
        f[i] = i + f[i-1]
    else:
        f[i] = 2*f[i-2]
a = dict(Counter(f))
print(f[26])
