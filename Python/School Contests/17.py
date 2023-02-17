import tqdm

def podh(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


def podh2(n):
    k = 0
    for x in p:
        if n % x == 0:
            k += 1
    if k == 3:
        return 1
    else:
        return 0


p = []
for i in range(2, 90001):
    if podh(i) == 1:
        p.append(i)

amount = 0
f = 0
for x in tqdm.tqdm(range(50001, 90001)):
    if podh2(x) == 1:
        f += 1
        if f == 1:
            print(x)
        amount += 1

print(amount)
