#case 5: when an exception is occured in except block instead of try block then it returns abnormal flow

print("start")
print(1)
print(2)
print(3)

# try:
#     print("8") 
    
# except ZeroDivisionError: 
#     print(10/0) #it wont give any error now  becoz no exception is handled in try block so this block wont execute

try:
    print(3/0)

except ZeroDivisionError:
    print(10/0) #This will throw an error because in try gblock there is an exception occured so this except block will execute and face another exception

print(5)
print("end")