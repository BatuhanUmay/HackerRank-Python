# https://developers.google.com/edu/python/regular-expressions
# https://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-13--regular-expression-matching

for i in range(int(input())):
    no  = input()
    if(len(no)==10 and no[0] in ['9', '8', '7'] and no.isnumeric()):
        print("YES")
    else:
        print("NO")

#############################################################

# import re
# N=input()
# for i in range(N):

#     if re.match(r'[789]\d{9}$',input()):   
#         print('YES')
#     else:  
#         print('NO')

#############################################################

# import re
# [print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]

#############################################################

# import re
# checkPhoneNumber = ["YES" if re.match("^[789]{1}\d{9}$", input()) else "NO" for _ in range(int(input()))]
# print("\n".join(checkPhoneNumber))
