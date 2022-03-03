from collections import Counter

# a = list(map(int, input().split()))

# print(Counter(a).items())

#############################################################

import collections

numShoes = int(input())
shoesNum = collections.Counter(map(int, input().split()))
numCustomer = int(input())

total = 0

for i in range(numCustomer):
    size,price = map(int, input().split())

    if shoesNum[size]:#Counter({44: 1, 40: 0, 41: 0})
        total += price
        shoesNum[size] -= 1

print(total)


"""
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

"""