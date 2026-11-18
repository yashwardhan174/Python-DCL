'''
It is a named reusable block of code which performs a specific task

Types : Predefined : Alr exisiting in Python (input() , print() ,len()...)
2> User Defined : Func. created by user based on requirements

syntax: 

def func_name(param1 , param2 ,......param n):  ->Fucntion Declaration
    #function
    ..
    ..
    ..
    body

    return val

func_name(arg1 , arg2 ,.....arg n) -> Function calling / invocation

NOTE : No. of Parameteres and no of arguments should match

4 different of implementing a fucntion :

1) Func without param & without return
2) Func without param & with return
3) Func with param & without return
4) Func with param & with return

'''
#1 fucn without param & without return

def wish(): #func declaration
    print("Good Bye") #fucn body

def work():
    print("Hardwork")

work()
wish()       #func call
wish()
print(wish)       #if we print func name , it will only give func address

#NOTE : only when fucntrion is called explicitly then only fucn body will be executed 

def menu():
    print("1.Dosa")
    print("2.Idli")
    print("3.Vada")

menu()