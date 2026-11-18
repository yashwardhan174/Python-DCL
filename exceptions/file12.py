

def divide(a,b):
    print(a/b)

divide(10,2)
divide(20,2)
try:
    divide(30,0)
except ZeroDivisionError:
    print("Exception Handled")

print("end")
