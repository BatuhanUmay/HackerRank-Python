import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    dict = {}

    for i in sorted(s):
        dict[i] = dict.get(i, 0) + 1

    dictSort = sorted(dict, key=dict.get, reverse=True)

    for key in dictSort[:3]:
        print(key, dict[key])

# aabbbccde

####################################################################################

# from collections import Counter, OrderedDict
#
# class OrderedCounter(Counter, OrderedDict):
#     pass
#
# [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]

####################################################################################

# from collections import Counter
#
# chars = Counter(input()).items()
#
# for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
#     print(char, n)
