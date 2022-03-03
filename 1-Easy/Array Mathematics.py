# import numpy
#
# a = numpy.array([1,2,3,4], float)
# b = numpy.array([5,6,7,8], float)
#
# print a + b                     #[  6.   8.  10.  12.]
# print numpy.add(a, b)           #[  6.   8.  10.  12.]
#
# print a - b                     #[-4. -4. -4. -4.]
# print numpy.subtract(a, b)      #[-4. -4. -4. -4.]
#
# print a * b                     #[  5.  12.  21.  32.]
# print numpy.multiply(a, b)      #[  5.  12.  21.  32.]
#
# print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
# print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]
#
# print a % b                     #[ 1.  2.  3.  4.]
# print numpy.mod(a, b)           #[ 1.  2.  3.  4.]
#
# print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
# print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]

####################################################################################

# import numpy as np
#
# n, m = map(int, input().split())
# a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
# print(a + b, a - b, a * b, a // b, a % b, a ** b, sep='\n')

####################################################################################

import numpy as np

n, m = map(int, input().split())
a, b = (np.array([list(map(int, input().split())) for _ in range(n)]) for _ in range(2))
print(a + b, a - b, a * b, a // b, a % b, a ** b, sep='\n')