#Pickleing
import pickle

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name}->{self.salary}"

with open("filehandling/emp.pkl","w+b") as f:
    e = Employee("Raju",9820000)
    bin_data = pickle.dumps(e)
    f.write(bin_data)


#Unpickeling

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name}->{self.salary}"

with open("filehandling/emp.pkl","w+b") as f:
    e = Employee("Raju",9820000)
    bin_data = pickle.dumps(e)
    f.write(bin_data)
    f.seek(0)
    data = f.read()
    eo = pickle.loads(data)
    print(eo)