'''
Packing : Multiple Values are Grouped in Single Var
1) Explicit 
2) Implicit
'''

p = 10,20,30,40,50
print(p)
print(type(p))

friends = "Yash" , "Akshat" , "Rohan" , "Chindi"
print(friends)
print(type(friends))



'''
Unpacing - Extracting the values from sequence and assignning them into individual var

Rules : 
1)if n values in a collection then n var are needed unless * is used for leftover

2)extended iterable unpacking - when we dont know how many values to unpack , we use * var in LHS which collects thr remaining value sinto a list format
-Only one starred var should be used during unpacking assignm,ent
-we can use starred var in left or center or right
'''
l=[10,20,30,40,50,60,70]
# *a,b,c = l
# a,*b,c = l
# a,b,*c = l
a,b,*c = "yash"
print(a,b,c)