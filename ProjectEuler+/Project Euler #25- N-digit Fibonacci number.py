n = 24000

arr = [1, 1] + [0] * (n - 2)

for i in range(2, n):
    arr[i] = arr[i - 1] + arr[i - 2]

vals = {}

for i in range(len(arr)):
    if len(str(arr[i])) not in vals.keys():
        vals[len(str(arr[i]))] = i + 1

for _ in range(int(input())):
    digit = int(input())
    print(vals[digit])

###########################################################################
# from math import log10, ceil, sqrt
#
# phi = (1 + sqrt(5)) / 2  # phi is the golden ratio
# t = int(input())
# for a0 in range(t):
#     d = int(input())
#     term = ceil((log10(5) / 2 + d - 1) / log10(phi))
#     print(term)
