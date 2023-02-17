import tqdm

for x in tqdm.tqdm(range(6, 100)):
    k = 0
    a = 3 * x + 23
    b = 3 * x - 17
    while a != b:
        if a < 10 and b < 10:
            k += 1
            break
        else:
            if a > b:
                a -= b
            else:
                b -= a
    if a == 10 and k == 0:
        print(x)

# Забыл сделать анализ зацикливания, из-за этого все пошло наперекосяк ;(
