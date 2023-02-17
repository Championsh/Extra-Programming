a = '01111112222222222222222222222222222222233'

print(a)

while a.find('01') != -1 or a.find('02') != -1 or a.find('03') != -1:
    a = a.replace('01', '2302')
    a = a.replace('02', '10')
    a = a.replace('03', '201')

print(a)

print(f'1 = {a.count(str(1))}')

print(f'2 = {a.count(str(2))}')

print(f'3 = {a.count(str(3))}')
