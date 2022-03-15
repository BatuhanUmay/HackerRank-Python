import math
import functools


def gcd(x, y):
    return math.gcd(x, y)


def lcm(x, y):
    return (x * y) // gcd(x, y)


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    liste = range(1, n + 1)
    print(functools.reduce(lcm, liste))
    del liste

#############################################################################################
# from math import gcd
# from functools import reduce
#
# for _ in range(int(input())):
#     N = int(input())
#     print(reduce(lambda x, y: x * y // gcd(x, y), range(1, N + 1)))
