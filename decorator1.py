def decorator(fun): #outerFunction
    def wrapper(): #inside the wrapper actual decorator logic exists
        #below three lines are actual decorator logic
        print("Take Gift Paper")
        fun() #it is gift()
        print("Put Label on Gift")
    return wrapper


def gift(): #fucntion to be decorated
    print("Smiling Buddha SELECTED as gift")


gift = decorator(gift) #assign var name same as func to be decorated
gift() #wrapper() is called