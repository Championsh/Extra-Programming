for a in range(100):
    k = 0
    for x in range(1, 501):
        if (x & 73 != 0 or x & 28 == 0 or x & a != 0) == 1:
            k += 1
    if k == 500:
        print(a)

# Не знал о битовых операциях в питоне, не стал тратить время на эту задачу, в конце не хватило времени-_-
