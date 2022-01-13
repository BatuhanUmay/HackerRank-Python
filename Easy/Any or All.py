# any()
# This expression returns True if any element of the iterable is true.
# If the iterable is empty, it will return False.

# Code

# >>> any([1>0,1==0,1<0])
# True
# >>> any([1<0,2<1,3<2])
# False
# all()
# This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.

# Code

# >>> all(['a'<'b','b'<'c'])
# True
# >>> all(['a'<'b','c'<'b'])
# False

#############################################################

N,n = int(input()), input().split()
print( all( [ int(i) > 0 for i in n] ) and any( [ j == j[::-1] for j in n] ))

