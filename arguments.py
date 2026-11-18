#3) Variable length arguments


def collect(*args): #this is packing
    print(args)

collect()

def collect(a,b,c): #params must be eqal to no. of elements in collection
    print(a)
    print(b)
    print(c)

l = [10,20,30]

collect(*l) #Unpacking

#Packing and Unpacking in same Fucntion
def collect(*args):
    print(args)

l = [1,2,3,4]
collect(*l)