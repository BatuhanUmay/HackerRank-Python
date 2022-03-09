import math
import os
import random
import re
import sys

if __name__ == '__main__':

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    res = []
    for i in range(4):
        for j in range(4):
            s = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            res.append(s)

    print(max(res))
