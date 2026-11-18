class Student:
    
    def __init__(self , name , roll , marks):
        self.name = name #IV1
        self.rollNum = roll   #IV2
        self.marks = marks    #IV1

s1 = Student("Yash" , "11330" , "98") #C0nstructor Call #if n param in constructor , use n-1 while calling constructor : s1 is obj reference 
print(s1.__dict__)

s2 = Student("Akshat" , "11296" , "95")
print(s2.__dict__)

print("-----------------------")

class Actress:
    gender = "Female"
    nationality = "Indian"
    def __init__(self , name , age ,boobs):
        self.name = name
        self.age = age
        self.boobs = boobs

a1 = Actress("Aishwarya Rai" , 42 , 38 ) 
print(a1.__dict__) 

a2 = Actress("Kirti Sanon" , 32 , 30)
print(a2.__dict__)

a3 = Actress("Jhanvi Kapoor" , 26 , 36)
print(a3.__dict__)