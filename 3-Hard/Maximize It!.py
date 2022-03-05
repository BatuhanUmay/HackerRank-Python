from itertools import product

K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i ** 2 for i in x) % M, product(*N))
print(max(results))

"""
arr1 = [1, 2, 3]
arr2 = [5, 6, 7]
product(arr1, arr2)
[(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)] 
"""

####################################################################################

# k = list(map(int, input().split()))
# r = k[1]
# k = k[0]
#
# s = []
# for _ in range(k):
#     s.append(list(map(int, input().split()))[1:])
# global maxx
# maxx = 0
#
# def fun(l, i):
#     global maxx
#     if i < len(s):
#         for j in s[i]:
#             l.append(j)
#             fun(l, i + 1)
#             l.pop()
#     else:
#         tmp = sum([x * x for x in l]) % r
#         if tmp > maxx:
#             maxx = tmp
#
# fun([], 0)
# print(maxx)
