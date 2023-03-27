class Student:

    def __init__(self):
        self._name = ""
        self._rollNumber = ""

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getRollNumber(self):
        return self._rollNumber

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber

s = Student()
s.setName("Kishan")
s.setRollNumber("1111")
print(s.getName()) 
print(s.getRollNumber()) 
