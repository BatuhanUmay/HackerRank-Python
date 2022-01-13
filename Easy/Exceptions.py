# >>> a = '1'
# >>> b = '0'
# >>> print int(a) / int(b)
# >>> ZeroDivisionError: integer division or modulo by zero


# >>> a = '1'
# >>> b = '#'
# >>> print int(a) / int(b)
# >>> ValueError: invalid literal for int() with base 10: '#'


# #Code
# try:
#     print 1/0
# except ZeroDivisionError as e:
#     print "Error Code:",e

#############################################################

# n = int(input())
# s = 0

# while s < n:
    
#     a,b = input().split()

#     try:
#         print(int(int(a)/int(b)))
#     except Exception as e:
#         print("Error Code:",e)
#     finally:
#         s += 1

#############################################################

for i in range(int(input())):
    try:
        a,b = map(int, input().split())
        print(a//b)
        
    except Exception as e:
        print("Error Cod:",e)
        
    # except (ZeroDivisionError,ValueError) as e:
    #     print("Error Code: ",e)    
    
    # except BaseException as err:
    #     print("Error Code:", err)