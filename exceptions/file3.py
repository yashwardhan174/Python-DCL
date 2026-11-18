#Case 3: If in Except block exception name is wrong then also it will throw an error

print("start")
print(1)
print(2)
print(3)

try:
    print(8/0) #risky line of code which may raise an exception
    
except ZeroDivisionError: #except blovk refers to handling code
# except TypeError: #if we give wrong exception name , it will throw error
# except ValueError: #wrong Error provided
    print("Exception Handled")

print(5)
print("end")