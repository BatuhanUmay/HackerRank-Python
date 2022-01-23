# import numpy

# array_1 = numpy.array([1,2,3])
# array_2 = numpy.array([4,5,6])
# array_3 = numpy.array([7,8,9])

# print numpy.concatenate((array_1, array_2, array_3))    

# #Output
# [1 2 3 4 5 6 7 8 9]

# import numpy

# array_1 = numpy.array([[1,2,3],[0,0,0]])
# array_2 = numpy.array([[0,0,0],[7,8,9]])

# print numpy.concatenate((array_1, array_2), axis = 1)   

# #Output
# [[1 2 3 0 0 0]
#  [0 0 0 7 8 9]]   

####################################################

import numpy as np
n, m, p = map(int,input().split())
arr1 = np.array([input().split() for _ in range(n)],int)
arr2 = np.array([input().split() for _ in range(m)],int)
print(np.concatenate((arr1, arr2), axis = 0))

####################################################

# #No concatenate!
# import numpy as np
# n, m, p = map(int, input().strip().split())
# arr = np.array(input().strip().split(), int)
# for i in range(1, n + m):
#     arr = np.vstack((arr, np.array(input().strip().split(), int)))
# print(arr)

####################################################

# import numpy as np
# n,m,p=map(int,input().split())
# lis=[]
# for i in range(n+m):
#     inp=input().split()
#     lis.append(inp)
# print(np.array(lis,int))