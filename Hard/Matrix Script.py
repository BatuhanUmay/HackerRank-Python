import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

text = [line[i] for i in range(m) for line in matrix]
text = ''.join(text)

pattern = r'([A-Za-z0-9])[!@#$%&\s]+(?=[A-Za-z0-9])'
text = re.sub(pattern, r'\1 ', text)
print(text)

"""
First: ([A-Za-z0-9]), the "()" capture the match as a group (useful to reuse the match later) and [A-Za-z0-9] means any character alphanumeric.
Second: [!@#$%&\s]+ means match any symbol between square braces (the \s refers to any spacing character) one or more times.
Third: match any alphanumeric character but not consume strings. This means, when the pattern match the position for nexts matches do not take this into account.
"""
####################################################################################

# import re
#
# n, m = map(int, input().split())
# a, b = [], ""
# for _ in range(n):
#     a.append(input())
#
# for z in zip(*a):
#     b += "".join(z)
#
# print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))

####################################################################################

# first_multiple_input = input().rstrip().split()
# n = int(first_multiple_input[0])
# m = int(first_multiple_input[1])
# matrix = []
#
# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)
# s = ''
# for c in range(m):
#     for r in range(n):
#         s += matrix[r][c]
#
# na = ''  # non-alpha gathered for start (tasecase 4) and end(#7
# s2 = ''  # answer is cooked here!
# nys = ''  # not-yet-started flag '' v/s ' '
# for x in s:
#     while x.isalpha():  # Neo wants to avoid i_f statement - why?
#         while (len(na) > 0):  # Neo wants to avoid i_f statement - why?
#             s2 += nys
#             while nys == '':
#                 nys = ' '
#                 s2 += na
#             na = ''
#         s2 += x
#         x = ''
#         nys = ' '
#     na += x
# s2 += na
# print(s2)
