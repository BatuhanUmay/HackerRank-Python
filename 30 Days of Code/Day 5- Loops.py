import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    for i in range(1,11):
        print(n, "x", i, "=", n*i)
        # print("{} x {} = {}".format(n, i, (n * i)))
####################################################################################
# print("\n".join("%d x %d = %d"%(n, i, n*i) for i in range(1,11)))
####################################################################################
# print( *['%d x %d = %d'%(n, i, n*i) for i in range(1, 11)], sep="\n" )
