# N1:
# import sys
#
# sys.stdin = open('24.txt', 'r')
#
# s = input()
# a = 0
# ama = 0
# for i in range(len(s)-1):
#     if s[i] != s[i+1]:
#         a += 1
#     else:
#         if a > ama:
#             ama = a + 1
#         a = 0
# if a > ama:
#     ama = a + 1
# print(ama)

# N3:
# import sys
#
# sys.stdin = open('24.txt', 'r')
#
# s = input()
# print(s)
# a = 0
# ama = 0
# s = s.replace('РљРћРў', 'Х')
# for i in range(len(s) - 1):
#     if s[i] == 'Х' and s[i + 1] == s[i]:
#         a += 1
#     else:
#         if a > ama:
#             ama = a + 1
#         a = 0
# if a > ama:
#     ama = a + 1
# print(ama)


# N4
# import sys
#
# sys.stdin = open('24.txt', 'r')
#
# m = []
# for i in range(1000):
#     s = input()
#     m.append(s)
# k = 0
# for x in m:
#     for i in range(1,len(x)-1):
#         if x[i-1] == 'A' and x[i+1] == 'R':
#             k+=1
#             break
# print(k)

# N5
# import sys
#
# sys.stdin = open('24.txt', 'r')
#
# s = input()
# print(s.count('KOT'))

# N6:
# import sys
#
# sys.stdin = open('24.txt', 'r')
#
# s = input()
# a = 0
# ama = 0
# for i in range(len(s) - 1):
#     if s[i] == 'X' and s[i + 1] == s[i]:
#         a += 1
#     else:
#         if a > ama:
#             ama = a + 1
#         a = 0
# if a > ama:
#      ama = a + 1
# print(ama)
