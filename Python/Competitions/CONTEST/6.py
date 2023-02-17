def enter():
    s = input().split()
    if s[0] == 'g':
        print(m[int(s[1]) - 1])
    else:
        x = int(s[3])
        for f in range(int(s[1]) - 1, int(s[2])):
            m[f] = int(m[f]) + x


o = int(input())
m = input().split()
o = int(input())
for i in range(o):
    enter()

