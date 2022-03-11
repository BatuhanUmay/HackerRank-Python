import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    numberSwaps = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                numberSwaps += 1
                a[j], a[j+1] = a[j+1], a[j]

        if numberSwaps == 0:
            break

    print("Array is sorted in {} swaps.".format(numberSwaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
