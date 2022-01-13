# import numpy

# a = numpy.array([1,2,3,4,5])
# print(a[1])        #2

# b = numpy.array([1,2,3,4,5],float)
# print(b[1])          #2.0

#############################################################

import numpy

def arrays(arr):
    dizi = numpy.array([i for i in arr[::-1]], float)
    return dizi

    # return(numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


