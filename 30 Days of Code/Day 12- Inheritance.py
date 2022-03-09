class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, score):
        super(Student, self).__init__(firstName, lastName, idNumber)
        # Person.__init__(self, firstName, lastName, idNumber)
        # super().__init__(firstName, lastName, idNumber)
        self.score = score

    def calculate(self):
        result = sum(self.score) / (len(self.score))

        if result >= 90:
            return "O"
        elif result >= 80:
            return "E"
        elif result >= 70:
            return "A"
        elif result >= 55:
            return "P"
        elif result >= 40:
            return "D"
        else:
            return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())