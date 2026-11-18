#Case 2 : Exception should occur only inside try block otherwise it will throw an error

print("start")
print(1)
print(2)
print(3)
# print(4/0) This will throw error and code execution will be stopped

try:
    print(8/0) #risky line of code which may raise an exception
    
except ZeroDivisionError: #except blovk refers to handling code
    print("Exception Handled")

print(5)
print("end")