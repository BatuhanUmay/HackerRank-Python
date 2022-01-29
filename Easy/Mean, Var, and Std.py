# mean
#
# The mean tool computes the arithmetic mean along the specified axis.
#
# import numpy
#
# my_array = numpy.array([ [1, 2], [3, 4] ])
#
# print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
# print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
# print numpy.mean(my_array, axis = None)     #Output : 2.5
# print numpy.mean(my_array)                  #Output : 2.5
# By default, the axis is None. Therefore, it computes the mean of the flattened array.
#
# var
#
# The var tool computes the arithmetic variance along the specified axis.
#
# import numpy
#
# my_array = numpy.array([ [1, 2], [3, 4] ])
#
# print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
# print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
# print numpy.var(my_array, axis = None)      #Output : 1.25
# print numpy.var(my_array)                   #Output : 1.25
# By default, the axis is None. Therefore, it computes the variance of the flattened array.
#
# std
#
# The std tool computes the arithmetic standard deviation along the specified axis.
#
# import numpy
#
# my_array = numpy.array([ [1, 2], [3, 4] ])
#
# print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
# print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
# print numpy.std(my_array, axis = None)      #Output : 1.11803398875
# print numpy.std(my_array)                   #Output : 1.11803398875

####################################################################################
import numpy as np

n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
# print(np.std(arr, axis = None))
print(round(np.std(arr, axis = None), 11))