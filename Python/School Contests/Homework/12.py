a = '1'*45 + '2'*45
while '111' in a:
    a = a.replace('111', '2', 1)
    a = a.replace('222', '1', 1)
print(a)
