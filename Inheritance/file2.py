#multi-level inheritance

class Vehicle:
    def move(self):
        print("Every Vehicle Will Move")

class Bike(Vehicle):
    def ride(self):
        print("We Ride A Bike")

class ElectricBike(Bike):
    def charge(self):
        print("We Charge Electric Bike")

v1 = ElectricBike()

v1.charge() #accessing IM 
v1.ride() #accesing parent method with child obj ref
v1.move() #accessing grandparent method with grandchild obj ref
print(ElectricBike.__mro__)
