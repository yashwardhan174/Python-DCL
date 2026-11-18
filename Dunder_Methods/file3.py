class Employee(object):
    def __init__(self,name,id,dept):
        self.name = name
        self.id = id
        self.dept = dept

    def __str__(self):
        return f"{self.name}->{self.id}->{self.dept}"

e1 = Employee("Yash",101,"IT")
e2 = Employee("Akshat",102,"IT")

print(e1)
print(str(e1))
print(e2)