class Student:
    def __init__(self,name):
        self.name = name #public IV
        self.__marks = 0 #private IV
        self.__fees  = 0

    @property
    def marks(self): #getter defines the property (marks)
        return self.__marks

    @property
    def fees(self):
        return self.__fees
    
    @marks.setter
    def marks(self,newMarks): #setter for that property (marks)
        if newMarks > 0 and newMarks < 101:
            self.__marks = newMarks
        else:
            print("Invalid Marks")

    @fees.setter
    def fees(self,newFees):
        if newFees > 0:
            self.__fees = newFees
        else:
            print("Invalid fees")

s = Student("Yashwardhan")
print(s.marks) #0   :- access like a variable , gette rmethod gets called

s.marks = 74 #initialize like a variable , setter method gets called
print(s.marks) #74

s.fees = 45000
print(s.fees)