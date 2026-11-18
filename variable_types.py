#Global Varibaler , Local Variable

a = 100
b = 800
def display():
    global a,b #It helps to modify global var inside a func
    print(a,"accessing global var inside function")
    a = a+50
    b=b+30
    print(b)
    print(a,"Modifying GV inside Function")


display()
print(a,"accessing global var outside function")
a=a+100 #modifing outside func
print(a , "Modified GV Outside Function")