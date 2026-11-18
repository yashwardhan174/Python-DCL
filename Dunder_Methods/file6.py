class Product:
    def __init__(self,prodID , name , cost):
        self.prodID = prodID
        self.name = name
        self.cost = cost

    def __hash__(self):
        return self.prodID


p1 = Product(101 , "Football" , 500)
p2 = Product(102 , "Dildo" , 5000)

print(hash(p1))
print(hash(p2))