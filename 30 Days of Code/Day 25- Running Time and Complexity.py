n = int(input())

for i in range(n):
    prime = True
    num = int(input())

    if num == 1:
        print("Not prime")
    else:
        for j in range(2, int(num**(1/2)) + 1):
            if num % j == 0:
                prime = False
                break

        print("Prime" if prime else "Not prime")

####################################################################################

# for _ in range(int(input())):
#     num = int(input())
#     if(num == 1):
#         print("Not prime")
#     else:
#         if(num % 2 == 0 and num > 2):
#             print("Not prime")
#         else:
#             for i in range(3, int(num**(1/2))+1, 2):
#                 if num % i == 0:
#                     print("Not prime")
#                     break
#             else:
#                 print("Prime")






