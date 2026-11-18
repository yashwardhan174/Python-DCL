#case4 : If multiple lines are in try block and exception is handled in 1st line of try block , then remaining lines of try block wont be executed and they will be ignored

print("start")
print(1)
print(2)
print(3)

try:
    print(8/0) #risky line of code which may raise an exception
    print("Line 10")
    print("Line 11")
    print(2/0)
    
except ZeroDivisionError: #except blovk refers to handling code
    print("Exception Handled")

print(5)
print("end")