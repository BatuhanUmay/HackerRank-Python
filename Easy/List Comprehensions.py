if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # liste = []
    
    # for i in range(0,x+1):
    #     for j in range(0,y+1):
    #         for k in range(0,z+1):
    #             if ((i + j + k) != n):
    #                 liste.append([i,j,k])
    # print(liste)
    
    
    #altf
    
    print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n])
    
    