#1) Public : Normally decalred in a class 

class Employee:
    def __init__(self,name,eid,dept):
        self.name = name #3public Instance Var (IV)
        self.eid = eid
        self.dept = dept

    def display(self): #public Instance Method(IM)
        print(self.name , self.dept , self.eid) #access public IV inside the class


e = Employee("yash",21,"management") #instance
print(e.name) #access public IV outside the class
e.display() #access public IM outside the class

    