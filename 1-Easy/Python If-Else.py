import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    if n >= 1 and n <= 100:
        if (n % 2 == 1):
            print("Weird")

        if (n % 2 == 0 and n > 2 and n <= 5):
            print("Not Weird")

        if (n % 2 == 0 and n > 6 and n <= 20):
            print("Weird")

        if (n % 2 == 0 and n > 20):
            print("Not Weird")


# n = int(input())
# if n % 2 == 0:
#     if n in range(2,6):
#         print("Not Weird")

#     elif n in range(6,21):
#         print("Weird")

#     elif n > 20:
#         print("Not Weird")
# else:
#     print("Weird")
