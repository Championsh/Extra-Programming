m = [[] for i in range(10)]
m[0] = [1]

for i in range(1, 10):
    for x in m[i-1]:
        m[i].append(2 * x)
        m[i].append(2 * x + 1)
print(len(m[-1]))
# Массив был на 1 позицию меньше, чем нужно 0_O
