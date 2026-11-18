
def outer(): #outer function declaration
    print("Outer Function Call")
    def inner(): #inner func declarartion
        print("Inner Function Body")

    inner() #inner function caLL
    

outer() #outer fucntion call
# inner() :it is not possible because inner() was created inside the outer fucntion
