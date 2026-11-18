#It is used top compare the memory locatron of object
# is , is not : is checks if poinitng to same meomry , is not checks if not poiintig to same moemory

a = 5
b = 5
print(b is a)
l1 = [10,20,30]
l2 = [10,20,30]
print(l1 is l2) # false : because list are created in 2 seperate memories 