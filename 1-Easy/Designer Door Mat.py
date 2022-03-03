# n = int(input())
# x = int(input())

# m = 3 * n
# orta = int(n/2)
# isaret = 1
# yeniM = 0

# yeniM2 = 0
# isaret2 = 0

# if (n % 2 == 1 and n * 3 == x):    
#     for i in range(0,n):       
#         if (i == 0 or i == n-1):
#             print(".|.".center(m,"-"))
#             isaret += 2

#         elif (i < orta):            
#             if (i == orta-1):
#                 print((isaret * ".|.").center(m,"-"))
#                 continue
            
#             yeniM = int(m - isaret*3)
#             print((isaret * ".|.").center(m,"-"))
#             yeniM -= 3
#             isaret += 2

#         elif (i > orta):
            
#             print((isaret2 * ".|.").center(m,"-"))                          
#             yeniM2 += 3
#             isaret2 -= 2
            
#         else:
#             print("WELCOME".center(m,"-"))
#             yeniM2 = yeniM
#             isaret2 = isaret    

#############################################################

n, m = map(int,input().split())
sekil = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(sekil + ['WELCOME'.center(m, '-')] + sekil[::-1]))


