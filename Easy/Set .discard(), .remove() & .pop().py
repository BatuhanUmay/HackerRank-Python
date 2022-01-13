# >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> s.remove(5)
# >>> print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# >>> print s.remove(4)
# None
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# >>> s.remove(0)
# KeyError: 0

#############################################################

# >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> s.discard(5)
# >>> print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# >>> print s.discard(4)
# None
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# >>> s.discard(0)
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])

#############################################################

# >>> s = set([1])
# >>> print s.pop()
# 1
# >>> print s
# set([])
# >>> print s.pop()
# KeyError: pop from an empty set

#############################################################

n = int(input())
s = set(map(int, input().split()))

m= int(input())

for i in range(m):
    secim = input()
    
    if secim == "pop":
        s.pop()
    
    if secim[:-2] == "remove":
        s.remove(int(secim[-1]))

    if secim[:-2] == "discard":
        s.discard(int(secim[-1]))

print(sum(s))

#############################################################

# n = int(input())
# s = set(map(int, input().split())) 
# for i in range(int(input())):
#     eval('s.{0}({1})'.format(*input().split()+['']))

# print(sum(s))

#############################################################

# n = int(input())
# s = set(map(int, input().split()))
# m = int(input())
# for  i in range(m):
#     attr, *kw = input().split()
#     if kw:
#         getattr(s,attr)(*(map(int, *kw)))
#     else:
#         getattr(s,attr)()
# print(sum(s))