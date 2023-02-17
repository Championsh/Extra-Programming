n = int(input())
m = [[0 for j in range(n)] for i in range(n)]
print(m)
for task in range(3):
    s = input().split()
    if s[0] == 'ADD':
        m[int(s[1]) - 1][int(s[2]) - 1] += 1
        print(m[int(s[1]) - 1][int(s[2]) - 1])
    elif s[0] == 'GET':
        n = 0
        x1 = int(s[1]) - 1
        y1 = int(s[2]) - 1
        x2 = int(s[3]) - 1
        y2 = int(s[4]) - 1
        for i in range(abs(x2 - x1) + 1):
            for j in range(abs(y2 - y1) + 1):
                n += m[i + min(x1, x2)][j + min(y1, y2)]
        print(n)
