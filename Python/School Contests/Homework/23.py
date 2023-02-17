a = 5
b = 102
c = 43
m = []
for i in range(b+1):
    m.append(0)
m[b] = 1
for i in range(b, c-1, -1):
    m[i-8] += m[i]
    m[i//2] += m[i]
for i in range(b, c, -1):
    m[i] = 0
for i in range(c, a-1, -1):
    m[i - 8] += m[i]
    m[i // 2] += m[i]
print(m[a])
