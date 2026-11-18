class Student:
    Institue = "DCL" #class varible 1
    course = "Python" #class Variable 2

Student.classRoom = "Online" #CV3 outside the Class
Student.yop = 2026 #CV4 Outside the class

# print(Student.__dict__)
print(Student.Institue) #accessing the CV outside the class
print(Student.course) #accessing the CV outside the class
print("---------------")

s1 = Student() #instance created with ref var s1
s1.name = "Yash" #IV 1
s1.college = "SVVV" #IV2

print(s1.__dict__)
s1.college = "Shree Vaishanv Vidyapeeth Vishwavidyalay" #Modifying IV using obj ref
print(s1.__dict__)
print(s1.name) #access the IV using obj ref
