import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())

    if N % 2 == 1:
        print("Weird")
    else:
        if N in range(2, 6):
            print("Not Weird")

        elif N in range(6, 21):
            print("Weird")

        elif N > 20:
            print("Not Weird")
####################################################################################
# if n % 2 == 0 and (n < 6 or n > 20):
#     print("Not Weird")
# print("Weird")
####################################################################################
# print((lambda n: 'Weird' if n % 2 or 5 < n < 21 else 'Not Weird')(int(input())))
