#1/2 doğruluk payı

# if __name__ == '__main__':
#     N = int(input())
    
#     liste = []
#     i = 0
    
#     while i < N:
#         secim = input()

#         if secim == "print":
#             print(liste)
        
#         elif secim[:6] == "append":
#             liste.append(int(secim[-1]))
        
#         elif secim[:6] == "insert":
#             secim = secim.split(" ")
#             liste.insert(int(secim[1]), int(secim[2])) 
        
#         elif secim[:6] == "remove":
#             liste.remove(int(secim[-1]))
        
#         elif secim == "sort":
#             liste.sort()
        
#         elif secim == "pop":
#             liste.pop()
        
#         elif secim == "reverse":
#             liste = liste[::-1]
            
#         else:
#             pass
        
#         i+= 1 
    
#############################################################

    
if __name__ == '__main__':
    N = int(input())

    liste = []
    
    for i in range(N):
        x = input().strip().split(" ")
        
        if x[0] == "print":
            print(liste)

        if x[0] == "append":
            liste.append(int(x[1]))
        
        if x[0] == "insert":
            liste.insert(int(x[1]), int(x[2]))
        
        if x[0] == "remove":
            liste.remove(int(x[1]))

        if x[0] == "sort":
            liste.sort()
    
        if x[0] == "pop":
            liste.pop()
    
        if x[0] == "reverse":
            liste.reverse()
    
    