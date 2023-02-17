s = input()
while '  ' in s:
    s = s.replace('  ', ' ')
n = len(s.split())
print(n)
