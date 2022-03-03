# (a). Using shape to get array dimensions
#
# import numpy
#
# my__1D_array = numpy.array([1, 2, 3, 4, 5])
# print my_1D_array.shape     #(5,) -> 1 row and 5 columns
#
# my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
# print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns
# (b). Using shape to change array dimensions
#
# import numpy
#
# change_array = numpy.array([1,2,3,4,5,6])
# change_array.shape = (3, 2)
# print change_array
#
# #Output
# [[1 2]
# [3 4]
# [5 6]]
# reshape
#
# The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.
#
# import numpy
#
# my_array = numpy.array([1,2,3,4,5,6])
# print numpy.reshape(my_array,(3,2))
#
# #Output
# [[1 2]
# [3 4]
# [5 6]]

####################################################################################
import numpy as np

arr = np.array([input().split()], int)
print(np.reshape(arr, (3, 3)))