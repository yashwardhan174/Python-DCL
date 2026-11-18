#User Defined Exception 

class InvalidAgeException(Exception): #user defined exception class
    pass

class Student:
    def __init__(self,name):
        self.name=name
        self.age = 0

    def set_age(self,actualage):
        if actualage < 0:
            raise InvalidAgeException("Age cannot be negative")
        else:
            self.age = actualage

s = Student("Yash")
try:
    s.set_age(-22)
except InvalidAgeException as e:
    print(e , "Handled")

print("End")