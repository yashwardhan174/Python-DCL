
a = 100
def outer(): 
    b = 200 #b is LV (locval var) of outer Funciton / Enclosing Variable
    print("Accessing GV inside outer function",a)
    print(b)
    def inner(): 
        print("Accessing GV inside inner Fucntion",a)
        print(b)
    inner() 
    
outer()

print("------------------")


def outer():
    a = 100
    print(a)
    def inner():
        nonlocal a #it allows modification of Outer Func var inside Inner fucntion
        print("inner function")
        # a = a+50 #it is not possible , so we use nonlocal keyword
        a = a+50
        print(a)

    inner()
outer()

def counter():
    count = 0 #Enclosing Variable
    def increment():
        nonlocal count
        count=count+1
        print(count)

    increment()
    increment()
    increment()
counter()