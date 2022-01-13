# >>> from itertools import combinations
# >>> 
# >>> print list(combinations('12345',2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
# >>> 
# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,4))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

#############################################################

from itertools import combinations

s,n = input().split()
s = s.upper()
s = sorted(s)

for i in range(1, int(n)+1):
    for j in combinations(s, i):
        print("".join(j))