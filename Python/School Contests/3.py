import sys
import tqdm

sys.stdin = open('24.txt', 'r')


def bin(m, sr):
    if len(m) > 1:
        a = len(m) // 2
        if sr == m[a]:
            return 1
        elif sr > m[a]:
            return bin(m[a:], sr)
        else:
            return bin(m[:a], sr)
    else:
        if m[0] != sr:
            return 0
        else:
            return 1


amount = int(input())

m = []
k = 0

for i in range(amount):
    a = int(input())
    m.append(a)
for i in tqdm.tqdm(range(len(m) - 2)):
    for j in range(i + 1, len(m) - 1):
        a = m[i] + m[j]
        p = sorted(m[j+1:])
        if bin(p, a) == 1:
            k += 1
print(k)
