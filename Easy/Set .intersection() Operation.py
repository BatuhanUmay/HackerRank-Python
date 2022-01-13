# >>> s = set("Hacker")
# >>> print s.intersection("Rank")
# set(['a', 'k'])

# >>> print s.intersection(set(['R', 'a', 'n', 'k']))
# set(['a', 'k'])

# >>> print s.intersection(['R', 'a', 'n', 'k'])
# set(['a', 'k'])

# >>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
# set([])

# >>> print s.intersection({"Rank":1})
# set([])

# >>> s & set("Rank")
# set(['a', 'k'])

#############################################################

a , b = input(), set(input().split())
c , d = input(), set(input().split())

print(len(b & d))
