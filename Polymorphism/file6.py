#Constructor Chaining

class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

class SchoolStudent(Student):
    def __init__(self, name , roll , principal):
        super().__init__(name,roll)
        self.principal = principal

s = SchoolStudent("Yash",21,"Gorilla")
print(s.__dict__)