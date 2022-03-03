# floor
# The tool floor returns the floor of the input element-wise.
# The floor of  is the largest integer  where .
#
# import numpy
#
# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# ceil
# The tool ceil returns the ceiling of the input element-wise.
# The ceiling of  is the smallest integer  where .
#
# import numpy
#
# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# rint
# The rint tool rounds to the nearest integer of input element-wise.
#
# import numpy
#
# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

####################################################################################
import numpy as np

np.set_printoptions(sign=" ")

sayilar = np.array(input().split(), float)

print(np.floor(sayilar))
print(np.ceil(sayilar))
print(np.rint(sayilar))

####################################################################################

# import numpy as np
#
# arr = np.array(input().split(), float)
# print(str(np.floor(arr)).replace('.', '. ').replace('[', '[ ').replace('. ]', '.]'),
#       str(np.ceil(arr)).replace('.', '. ').replace('[', '[ ').replace('. ]', '.]'),
#       str(np.rint(arr)).replace('.', '. ').replace('[', '[ ').replace('. ]', '.]'), sep="\n")
####################################################################################

# import numpy as np
#
# a = np.array(input().split(), float)
# print(*(f(a) for f in [np.floor, np.ceil, np.rint]), sep='\n')