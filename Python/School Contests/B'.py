def create(ostov):
    ostov2 = []
    for i in ostov:
        s=[]
        for j in range(len(i)):
            s.append(i[j])
        ostov2.append(s)
    return ostov2


f = int(input())
ostov = [[0 for j in range(f)] for i in range(f)]
print('ostov: ')
for i in ostov:
    for j in range(len(i)):
        print(i[j], end=' ')
    print()
print()
ostov2=create(ostov)
print('ostov2: ')
for i in ostov2:
    for j in range(len(i)):
        print(i[j], end=' ')
    print()
print()
