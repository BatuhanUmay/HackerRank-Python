N = int(input())

for i in range(N):
    text = input()
    try:
        if text == "0":
                print("False")
        if float(text):
            print("True")

    except Exception as e:
        print("False")
        
#############################################################
        
# import re
# for _ in range(input()):
# 	print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))        

#############################################################

# def is_float(txt):
#     try:
#         float(txt)
#         return True
#     except ValueError:
#         return False

# n = int(input())
# lines = [input().strip() for _ in range(n)]
# for l in lines:
#     if(l=='0'): print(False)
#     else:
#         print(is_float(l))    