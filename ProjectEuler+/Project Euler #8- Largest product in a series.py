def compute(num, k):
    res = max(productKdigit(num[i: i + k]) for i in range(len(num) - k + 1))
    return res


def productKdigit(s):
    pro = 1
    for i in s:
        pro *= int(i)
    return pro


t = int(input().strip())
for i in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()

    print(compute(num, k))

##############################################################################

# from operator import mul
# import sys
# from functools import reduce
#
# t = int(input().strip())
# for a0 in range(t):
#     n, k = input().strip().split(' ')
#     n, k = [int(n), int(k)]
#     num = input().strip()
#     numList = [int(x) for x in str(num)]
#     prod = []
#     for i in range(0, len(numList) - k):
#         prod.append(reduce(mul, numList[i:i + k]))
#     print(max(prod))
