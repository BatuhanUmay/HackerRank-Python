# inner
#
# The inner tool returns the inner product of two arrays.
#
# import numpy
#
# A = numpy.array([0, 1])
# B = numpy.array([3, 4])
#
# print numpy.inner(A, B)     #Output : 4
# outer
#
# The outer tool returns the outer product of two arrays.
#
# import numpy
#
# A = numpy.array([0, 1])
# B = numpy.array([3, 4])
#
# print numpy.outer(A, B)     #Output : [[0 0]
#                             #          [3 4]]
####################################################################################
import numpy as np

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

print(np.inner(A, B))
print(np.outer(A, B))

####################################################################################

# A,B = [np.array([input().split()],int) for _ in range(2)]
# print(np.inner(A,B)[0][0],np.outer(A,B),sep="\n")