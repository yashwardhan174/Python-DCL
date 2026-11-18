#2) Protected : Any var or method using "single leading underscore"

class Student:
    def __init__(self , roll,name,fees):
        self.roll = roll     #public IV
        self.name = name     #public IV
        self._fees = fees    #protected IV

    def _pay_fees(self): #protected instance method
        print(f"{self.name} Paid {self._fees} to the college") #access protected IV inside

class EngineeringStudent(Student):
    def quarterlyInsallment(self): #public IM
        self._pay_fees() #accessing the protected instance menthod from the child class

es1 = EngineeringStudent(11330 , "yash" , 140000)
es1.quarterlyInsallment() #accesing public method