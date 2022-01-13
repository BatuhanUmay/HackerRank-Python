# Code 01

# >>> from collections import namedtuple
# >>> Point = namedtuple('Point','x,y')
# >>> pt1 = Point(1,2)
# >>> pt2 = Point(3,4)
# >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# >>> print dot_product
# 11
# Code 02

# >>> from collections import namedtuple
# >>> Car = namedtuple('Car','Price Mileage Colour Class')
# >>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# >>> print xyz
# Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
# >>> print xyz.Class
# Y

#############################################################

# from collections import namedtuple

# Point = namedtuple("Point","x,y")
# pt1 = Point(1,2)
# pt2 = Point(3,4)
# r = (pt1.x * pt2.x) + (pt1.y * pt2.y)
# print(r)

# Car = namedtuple("Car","Price Mileage Colour Class")
# d = Car(Price = 100, Mileage = 1, Colour = 'Mavi', Class = 'A')
# print(d)
# print(d.Colour)

#############################################################

from collections import namedtuple

n = int(input())
basliklar = input().split()

ort = 0

for i in range(n):
    
    Student = namedtuple("Student",basliklar)
    
    ID,MARKS,NAME,CLASS = input().split()
    std = Student(ID,MARKS,NAME,CLASS)
    
    ort += int(std.MARKS)
    
print("{:.2f}".format(ort/n))
