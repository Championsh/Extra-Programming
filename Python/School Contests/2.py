import sys
import tqdm


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


sys.stdin = open('24.txt', 'r')

amount = int(input())

m = []

for i in range(amount):
    a = int(input())
    m.append(a)

k = 0

for i in tqdm.tqdm(range(amount - 2)):
    for j in range(i + 1, amount - 1):
        m2 = sorted(m[j + 1:])
        if bin(m2, i + j) == 1:
            k += 1
print(k)
