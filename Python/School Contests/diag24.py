import sys
import tqdm

sys.stdin = open('25-A.txt', 'r')


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
m1 = []
m2 = []
k = 0

for i in range(amount):
    a = int(input())
    if a % 2 != 0:
        m1.append(a)
    else:
        m2.append(a)
m1.sort()
m2.sort()

for x in tqdm.tqdm(m1):
    for y in m2:
        n = x + y
        if n % 2 != 0:
            if bin(m1, n) == 1:
                k += 1
                m.append(n)
        elif bin(m2, n) == 1:
            k += 1
            m.append(n)
m.sort()
print(k, m[-1])
# Возможно, ошибка в том, что не отсортировал массив с суммами в конце -_-
