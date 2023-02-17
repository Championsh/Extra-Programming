from collections import Counter


o = int(input())
s = input().split()
a = dict(Counter(s))
print(len(a))
