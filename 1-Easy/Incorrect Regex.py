import re

for i in range(int(input())):
    bool = True
    
    try:
        regex = re.compile(input())

    except re.error:
        bool = False

    print(bool)

#############################################################

# import re

# def isvalidregex(regex):
#     try: re.compile(regex)
#     except re.error: return False
#     return True

# for i in range(int(input())):
#     print(isvalidregex(input()))

