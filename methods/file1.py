class Student:
    school = "SICA" #CV1
    principal = "SL. Gorya" #CV2
    fees = 45000             #CV3

    @classmethod
    def increase_fees(cls): #class method
        cls.fees+=50000 #modifying class var
        # print(cls.fees) #access class var inside class method

    @classmethod
    def display_school(cls):
        print(cls.school)


Student.increase_fees() #access / call the class merthod
Student.increase_fees() #each time we call this , fees will be increased by 50000
print(Student.fees)

Student.display_school()

