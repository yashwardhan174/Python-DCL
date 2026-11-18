#__repr__(self)
class Laptop:
    def __init__(self,brand,cost):
        self.brand = brand
        self.cost = cost

    def __repr__(self): #overriding __repr__
        return f"{self.brand}-> {self.cost}"


l1 = Laptop("Dell",68000)
l2 = Laptop("Asus",168000)
l3 = Laptop("HP",48000)
print(l1) #1) when __str__ is absent and __repr__ present and print instance
print("-----------")
print(repr(l1)) #2) l1.__repr__() works similarly
laptop_list = [l1,l2,l3]
print(laptop_list) #3) print container collections