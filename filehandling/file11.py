#Load
import pickle
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name}->{self.salary}"

with open("filehandling/emp.pkl","w+b") as f:
    e = Employee("Raju",9820000)
    pickle.dump(e,f)
    f.seek(0)
    eo = pickle.load(f)
    print(eo)