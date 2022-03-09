class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = abs(min(a) - max(a))

    # def computeDifference(self):
    #     self.maximumDifference = abs(max(self.__elements) - min(self.__elements))

    # maximumDifference = None
    #
    # def computeDifference(self):
    #     minVal = min(self.__elements)
    #     maxVal = max(self.__elements)
    #
    #     Difference.maximumDifference = abs(minVal - maxVal)


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
