#Duck Typing

class Zomato:
    def deliver(self):
        print("Zomato Delivery")

class Swiggy:
    def deliver(self):
        print("Swiggy Delivery")

class UberEats:
    def deliver(self):
        print("UberEats Delivery")  

class Porter:
    def transport(self):
        print("Porter Transports")  

def process(partner):
    if hasattr(partner,"deliver"): #ensures safe duck typing
        partner.deliver()

z = Zomato()
s = Swiggy()
u = UberEats()
p = Porter()

l = [z,s,u,p]

for i in l:
    process(i)

print(hasattr(p,"deliver"))