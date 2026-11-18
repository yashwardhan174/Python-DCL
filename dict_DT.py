#It is a Predefined Class in Python

emp_dict = {} #syntax to define empty dictionary

print(type(emp_dict))

print("-----------------------")

d = dict()
print(d)
print(type(d))
print(len(d))

print("--------------------------")

d2 = {1:10 , 2.2:20.4 , 3j:300j}
print(d2)

print("-------------------------")

d3 = {2:20 , 2:30 , 2:40} #if keys are same only last value will be considered
print(d3)

d4 = {2:20 , 3:20 , 4:20}
print(d4)

print(d4[2]) #syntax to access value of Dictionary -> ref[key]

#Syntax to update the value of a key -> ref[key] = newVal
d4[2] = 34
print(d4)

