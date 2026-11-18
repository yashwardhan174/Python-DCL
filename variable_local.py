#local variable
def show():
    a=100
    print(a,"LV can be accessed inside the function")
    a=a+50
    print(a,"LV modification")
show()
#print(a,"LV can be accessed outside the function") : it is not possible as var is local var

def show(a):
    a = a+100
    print(a,"Modification of LV")

show(100)


