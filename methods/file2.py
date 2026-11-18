class Employee:
    def __init__(self ,name, company , salary):
        self.name = name
        self.company = company
        self.salary = salary

    def display_details(self): #instance method
        print(self.name,self.company ,self.salary) #access IV inside IM using self param

    def deduct_salary(self,amount):
        self.salary-=amount

e1 = Employee("Yash" , "Google" , 15000000) #instances
e2 = Employee("Rohan" , "Amazon" , 120000)

e1.display_details()
e2.display_details() 


e1.deduct_salary(200)
print(e2.salary)

