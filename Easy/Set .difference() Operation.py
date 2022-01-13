# >>> s = set("Hacker")
# >>> print s.difference("Rank")
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(set(['R', 'a', 'n', 'k']))
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(['R', 'a', 'n', 'k'])
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'r', 'e', 'H', 'k'])

# >>> print s.difference({"Rank":1})
# set(['a', 'c', 'e', 'H', 'k', 'r'])

# >>> s - set("Rank")
# set(['H', 'c', 'r', 'e']
    
#############################################################

# a,b = int(input()), set(input().split())
# c,d = int(input()), set(input().split())

# print(len(b-d))

#############################################################

a,b = [set(input().split()) for _ in range(4)][1::2]
print(len(a.difference(b)))

# Think of the whole input:

# n1 = input()
# a = set(input().split())
# n2 = input()
# b = set(input().split())

# n1, a, n2, b = [set(input().split()) for i in range(4)]

# a, b = [set(input().split() for i in range(4)][1::2]

