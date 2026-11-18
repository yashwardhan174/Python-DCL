#2) __str__(self)

class Pen(object):
    def __str__(self):
        return "Custom Message"

p1 = Pen()
print(p1) #internally p.__str__() method call

p2 = Pen()
print(p2)

#accessing instance var inside instace methods

class Student(object):
    def __init__(self , name , roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"{self.name}->{self.roll}"


s1 = Student("Yashwardhan",11330)
s2 = Student("Akshat", 11296)
s3 = Student("Vasu",11329)

print(s1)
print(s2)
print(s3)