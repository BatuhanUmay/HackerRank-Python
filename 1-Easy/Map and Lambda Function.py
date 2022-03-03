# The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables.
# Let's say you are given a list of names, and you have to print a list that contains the length of each name.

# >> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
# [4, 3, 3]  
# Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.

# >> sum = lambda a, b, c: a + b + c
# >> sum(1, 2, 3)
# 6

#############################################################
# cube = lambda x : x**3

# def fibonacci(limit):
#     s1 = 0
#     s2 = 1
#     liste = []
    
#     if limit != 1 and limit != 0:
#         liste = [s1,s2]
#         while limit-2 > 0: 
#             s3 = s2 + s1
#             liste.append(s3)    
#             s1 = s2
#             s2 = s3
            
#             limit -= 1
            
#     elif limit == 1:
#         liste.append(s1)
        
#     return liste

# print(list(map(cube, fibonacci(int(input())))))

#############################################################

cube = lambda x : pow(x,3)

def fibonacci(n):
    liste = [0,1]
    
    for i in range(2,n):
        liste.append(liste[i-1] + liste[i-2])

    return liste[:n]
    
n = int(input())
print(list(map(cube, fibonacci(n))))
