# from itertools import groupby
# print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

####################################################################################

# [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
# [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D

from itertools import groupby

for char, howMany in groupby(input()):
    print(tuple([len(list(howMany)), int(char)]), end = " ")
    # print(tuple([len(list(howMany)), str(char)]), end= " ")