a, b = 1016, 7937
b += 1
m = [0, 0]
for i in range(a, b):
    if (i % 3 == 0) and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        if i > m[1]:
            m[1] = i
        m[0] += 1
print(*m)
