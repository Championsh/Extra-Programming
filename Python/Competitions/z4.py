def sort(f):
    return f % 10


n = int(input())
m = []
s = input().split()
for a in s:
    m.append(int(a))
m.sort(key=sort)
print(m)
