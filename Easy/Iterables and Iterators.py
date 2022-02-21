from itertools import combinations

N = int(input())
letters = input().split()
K = int(input())

combi = combinations("".join(letters), K)

total, selectedLetter = 0, 0

for i in combi:
    total += 1
    if 'a' in i:
        selectedLetter += 1

print(round(selectedLetter / total, 3))

####################################################################################

# from itertools import combinations
#
# N = int(input())
# L = input().split()
# K = int(input())
#
# C = list(combinations(L, K))
# F = filter(lambda c: 'a' in c, C)
# print("{0:.3}".format(len(list(F)) / len(C)))

####################################################################################
# from itertools import combinations
#
# _, s, n = input(), input().split(), int(input())
# t = list(combinations(s, n))
# f = [i for i in t if 'a' in i]
# print(len(f) / len(t))
