'This is Custom Constructor'

class Student :
    def __init__(self):
        # print(self)
        self.name = "Yash" #this is a Instance Variable 

s1 = Student() #obj creation /Instantiation = constructor execution
# print(s1) #it has the same address as of self in class
print(s1.name)
print("---------------")
s2 = Student() #obj creation / Constructor Call
print(s2.name)
print("----------------")
s3 = Student() #obj creation
print(s3.name)


