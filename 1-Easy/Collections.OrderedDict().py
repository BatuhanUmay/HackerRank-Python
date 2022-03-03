# >>> from collections import OrderedDict
# >>> 
# >>> ordinary_dictionary = {}
# >>> ordinary_dictionary['a'] = 1
# >>> ordinary_dictionary['b'] = 2
# >>> ordinary_dictionary['c'] = 3
# >>> ordinary_dictionary['d'] = 4
# >>> ordinary_dictionary['e'] = 5
# >>> 
# >>> print ordinary_dictionary
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# >>> 
# >>> ordered_dictionary = OrderedDict()
# >>> ordered_dictionary['a'] = 1
# >>> ordered_dictionary['b'] = 2
# >>> ordered_dictionary['c'] = 3
# >>> ordered_dictionary['d'] = 4
# >>> ordered_dictionary['e'] = 5
# >>> 
# >>> print ordered_dictionary
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

#############################################################

# from collections import OrderedDict

# n = int(input())
# ordered_dict = OrderedDict()

# for i in range(n):
#     item_name , space, net_price = map(str,input().rpartition(" "))
#     net_price = int(net_price)
    
#     if item_name in ordered_dict:
#         ordered_dict[item_name] += net_price
#         continue
    
#     ordered_dict[item_name] = net_price
    
# for i,j in ordered_dict.items():
#     print(i,j)

#############################################################

from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    # d[item] = d.get(item,0) + int(quantity)
    #yada
    d[item] = int(quantity) + d[item] if item in d else int(quantity)
    
for item, quantity in d.items():
    print(item, quantity)

# B if A else C does a conditional evaluation: 
# if A evaluates to truth, then the value of the
# expression is B, else it evaluates to C.
