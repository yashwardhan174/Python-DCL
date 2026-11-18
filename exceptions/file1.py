#Case 1 : Default

print("start")
print(1)
print(2)
print(3)

try:
    print(8/0) #risky line of code which may raise an exception
    
except ZeroDivisionError: #except blovk refers to handling code
    print("Exception Handled")

print(5)
print("end")