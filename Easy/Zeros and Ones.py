# zeros
#
# The zeros tool returns a new array with a given shape and type filled with 's.
#
# import numpy
#
# print numpy.zeros((1,2))                    #Default type is float
# #Output : [[ 0.  0.]]
#
# print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
# #Output : [[0 0]]
# ones
#
# The ones tool returns a new array with a given shape and type filled with 's.
#
# import numpy
#
# print numpy.ones((1,2))                    #Default type is float
# #Output : [[ 1.  1.]]
#
# print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
# #Output : [[1 1]]

####################################################################################
import numpy as np

sayilar = tuple(map(int, input().split()))
print(np.zeros(sayilar, dtype=np.int))
print(np.ones(sayilar, dtype=np.int))