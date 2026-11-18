'''Range is a class and it was implemented in python 3rd version 
whenver we call range() we are creating a range object 
it is an immutable sequence type(like tuple , string)

syntax:
range(stop)
range(start,stop)
range(start,stop,step)

'''
r = range(1,11,1)
print(r)

print(list(r))
print(tuple(r))
print(set(r))

print("-----------------")
s = range(1,14,3)
print(list(s))

print("----------")

s = range(13,0,-3)
print(list(s))