import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    print(max((bin(n)[2:]).split("0")).count("1"))

####################################################################################
# print(len(max(bin(int(input().strip()))[2:].split('0'))))
####################################################################################

# n = int(input())
#
# count = 0
# while n:
#     n &= n << 1
#     count += 1
#
# print(count)
