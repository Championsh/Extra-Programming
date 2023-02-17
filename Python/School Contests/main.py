s1 = "0111110111111100"
s2 = "011011111100011?"
s3 = "0010101011010111"
r1 = 10452
r2 = 10322
r3 = 23948
r4 = 28663
x = int(s1, 2)
for i in range(16):
    for t in range(2):
        s3 = s3[:i] + str(t) + s3[i + 1:]
        z = int(s3, 2)
        for j in range(2):
            s2 = s2[:15] + str(j)
            y = int(s2, 2)
            a1 = z & x
            a2 = x ^ (z << 1)
            a3 = x & (y << 1)
            a4 = y | (z >> 2)
            if (a1 == r1) & (a2 == r2) & (a3 == r3) & (a4 == r4):
                print(s3)
                print(i)
'''
z & x
x ^ (z << 1)
x & (y << 1)
y | (z >> 2)
'''
