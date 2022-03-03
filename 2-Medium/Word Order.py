n = int(input())
d = {}

for i in range(n):
    s = input()
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1

print(len(d))

for i in d:
    print(d[i], end=" ")

####################################################################################

# from collections import Counter, OrderedDict
# class OrderedCounter(Counter, OrderedDict):
#     pass
# d = OrderedCounter(input() for _ in range(int(input())))
# print(len(d))
# print(*d.values())

####################################################################################

# from collections import OrderedDict
# #define empty ordered dictionary, which counts occurences
# dict = OrderedDict()
#
# for i in range(int(input())):
#     #If input not in the dictionary, then add it
#     #else increment the counter
#     key = input()
#     if not key in dict.keys():
#         dict.update({key : 1})
#         continue
#     dict[key] += 1
#
# print(len(dict.keys()))
# print(*dict.values())
