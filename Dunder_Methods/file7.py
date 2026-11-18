# __eq__(self.other)

class Employee:
    def __init__(self,eid,ename,dept):
        self.eid = eid
        self.ename = ename
        self.dept = dept

    def __eq__(self,other):
        if isinstance(other,Employee):
            return self.eid == other.eid
        return False

# e1 = Employee(234 , "Charan" , "Deployment")#This wioll return false
e1 = Employee(444 , "Charan" , "Deployment")#This will return true
e2 = Employee(444 , "Zeus" , "Security")
print(e1==e2) # internally it looks like print(e1.__eq__(e2))
print(e1==98)

# print(isinstance(e1,Employee)) 


