class Employees:
    compamnyName = "TCS"
    companyOrigin = "India"

print(Employees.compamnyName)
print(Employees.companyOrigin)

e1 = Employees()
e1.location = "Indore"
e1.shift = "9am-5pm"
print(e1.__dict__)

e2 = Employees()
e2.location = "Pune"
e2.shift = "10pm-6am"
print(e2.__dict__)