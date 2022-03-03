if __name__ == '__main__':
    # n = int(input())
    # arr = map(int, input().split())
    # arr = list(arr)
    # A = []
    # kume = set(arr)
    # for i in kume:
    #     A.append(i)
        
    # A.sort()
    # print(A[len(A)-2])
    
    
    #alt
    
    # i = int(input())
    # liste = list(map(int, input().strip().split()))[:i]
    # z = max(liste)
    
    # while max(liste) == z:
    #     liste.remove(max(liste))
        
    # print(max(liste))
    
    
    #alt2
    
    n = int(input())
    nums = map(int, input().split())
    print(sorted(list(set(nums)))[-2])
    