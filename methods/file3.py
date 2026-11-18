class Restaurent:
    def __init__(self,name,location):
        self.name = name
        self.location = location

    def display_details(self):
        print(self.name , self.location)

    def modif_res(self):
        self.name = "Radisson"


r1 = Restaurent("Sayaji" , "Indore")
r2 = Restaurent("Marriot" , "Indore")

r1.display_details()
r2.display_details()

r1.modif_res()
print(r1.name)