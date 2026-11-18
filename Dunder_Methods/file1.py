#1) __new__(class_name)

class Pen:
    pass

# p=Pen()
# print(p)

p = Pen.__new__(Pen) #1) True Constructor
Pen.__init__(p) #2) Initialiser executes
print(p)

print("-----------------------")
class Student:
    pass

s = Student.__new__(Student)
Student.__init__(s)
print(s)
