class Person:
    def __init__(self,name,age,gender,nationality):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality

class Citizen(Person):
    def __init__(self ,name,age,gender,nationality,citizenid):
        super().__init__(name,age,gender,nationality)
        self.citizenid = citizenid

class Refugee(Person):
    def __init__(self,name,age,gender,nationality,refugeeid):
        super().__init__(name,age,gender,nationality)
        self.refugeeid = refugeeid

c = Citizen("yash",22,"Male","Indian",9687)
print(c.__dict__)

r = Refugee("Chindi",23,"Hijda","Indian",6969)
print(r.__dict__)     