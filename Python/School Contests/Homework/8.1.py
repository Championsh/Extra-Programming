s = 'левий'
k = 0
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    a = x1 + x2 + x3 + x4 + x5
                    if (a.count('л') == 1 and a.count('е') == 1 and a.count('в') == 1 and a.count('и') == 1
                            and a.count('й') == 1 and a[0] != 'й' and 'еи' not in a):
                        k += 1
print(k)
