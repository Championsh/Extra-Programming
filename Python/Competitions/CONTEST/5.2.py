from itertools import product

a, b = map(int, input().split())
print(*(''.join(f) for f in product('01', repeat=a) if f.count('1') == b), sep='\n')
