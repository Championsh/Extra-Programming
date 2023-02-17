o = int(input())
s = input().split()
m = []
for x in s:
    m.append(x)
m1 = m[:(len(m) // 2)]
m2 = m[(len(m) // 2):]
m1 = m1[::-1]
m2 = m2[::-1]
for i in range(len(m)//2):
    m[i] = m1[i]
for j in range(len(m)//2):
    m[j+len(m)//2] = m2[j]
print(*m)
