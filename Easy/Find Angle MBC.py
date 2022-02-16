import math

ab = int(int(input()))
bc = int(int(input()))

# print(str(int(round(math.degrees(math.atan2(ab, bc)))))+'°')
degree = chr(176)
print(str(int(round(math.degrees(math.atan2(ab, bc))))) + degree)

#######################################################################

# import math
#
# AB, BC = int(input()), int(input())
# hype = math.hypot(AB, BC)  # to calculate hypotenuse
# res = round(math.degrees(math.acos(BC / hype)))  # to calculate required angle
# degree = chr(176)  # for DEGREE symbol
# print(res, degree, sep='')
