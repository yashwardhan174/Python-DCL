#Encapsulation

class Student:
    def __init__(self,name):
        self.name = name #public IV
        self.__marks = 0 #private IV

    def get_marks(self): #public getter method
        return self.__marks #returning private data

    def set_marks(self , newMarks): #public setter method
        #validation logic
        if newMarks > 0 and newMarks <=100:
            self.__marks = newMarks #updation logic
        else:
            print("Invalid marks")


s1 = Student("Yash")
print(s1.get_marks())

s1.set_marks(78)
print(s1.get_marks())
s1.set_marks(-78)
print(s1.get_marks())