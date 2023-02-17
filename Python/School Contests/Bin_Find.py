import sys
import tqdm

sys.stdin = open('24.txt', 'r')


def bin(m, sr):
    if sr > m[-1] or sr < m[0]:
        return 0
    else:
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


amount = int(input())

m = []
m2 = []

for i in range(amount):
    s = int(input())
    if s % 2 == 0:
        m.append(s)
    else:
        m2.append(s)

m.sort()
m2.sort()

amax = 0
k = 0

for i in tqdm.tqdm(range(len(m2))):
    for j in range(i + 1, len(m2)):
        a = (m2[i] + m2[j]) // 2
        h = 0
        if a % 2 == 0 and bin(m, a) == 1:
            h += 1
        elif a % 2 != 0 and bin(m2, a) == 1:
            h += 1
        if h == 1:
            k += 1
            if a > amax:
                amax = a
print(k)
print(amax)
