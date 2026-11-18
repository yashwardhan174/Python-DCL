# def decorator(fun): #(HIGHER ORDER FUNCTION) Outer function -- STEP 2
#     def wrapper(flavour ,bakeryname): #inner fucntion -- STEP 3
#         #decorator Logic -- STEP 4
#         print("Take a Cake Box")
#         fun(flavour, bakeryname) #bake_cake() is used -- MANDATORY
#         print("Write Happy Birthday On cake")
#         print("Place that cake in the box")
#     return wrapper #STEP 5

# def bake_cake(flavour , bakeryname): #func to be decorated -- STEP 1
#     print(f"{flavour} Choclate cake is selected from {bakeryname}")

# bake_cake = decorator(bake_cake) #assign decorator in same var name as func to be decorated -- STEP 6
# bake_cake("Black Forest", "Perfect Bakery") #FINAL STEP

#---------------------------------------------------------------------------------------------
#With Multiple Arguments

def decorator(fun): #(HIGHER ORDER FUNCTION) Outer function -- STEP 2
    def wrapper(*args , **kwargs): #inner fucntion -- STEP 3
        #decorator Logic -- STEP 4
        print("Take a  Box")
        fun(*args , **kwargs) #bake_cake() is used -- MANDATORY
        print("Write Happy Birthday On cake")
        print("Place that cake in the box")
    return wrapper #STEP 5

def bake_cake(*args , **kwargs): #func to be decorated -- STEP 1
    print(" Choclate cake is selected ",args,kwargs)

bake_cake = decorator(bake_cake) #assign decorator in same var name as func to be decorated -- STEP 6
bake_cake("maida" , "egg" , "sugar" , "bakingsoda" , "milk" , cream="Amul" , Flavour="Velvet",cost="500") #FINAL STEP

print("----------------------")

@decorator
def pizza_toppings(*args,**kwargs):
    print("selected a Pizza",args,kwargs)

# pizza_toppings=decorator(pizza_toppings)
pizza_toppings("maida" , "sauce" , "cheese" , category ="veg" , crust="Double")