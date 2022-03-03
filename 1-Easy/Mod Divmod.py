# >>> print divmod(177,10)
# (17, 7)

#############################################################

# a = int(input())
# b = int(input())
# print(a//b)
# print(a%b)
# print(divmod(a,b))

#############################################################

a,b = (int(input()) for i in range(2))
c,d = divmod(a,b)
print(c, d, (c,d), sep = "\n")

#############################################################

# a = divmod(int(input()), int(input()))
# print(*a, a, sep='\n')
