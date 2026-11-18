'''
Looping means repeting a set of instruction multiple times until a condition is satisfied
-> looping is used to traverse elements of collection

Why do we need loops
1) To avoid code duplication / repetetion
2) automates repetetive tasks
3) loops are used to work with collective(list , tuple,string etc)

Types of Loops: 
1) for : for is a keyword in python
- for loop is used when we know in advance , how many times to loop
- works very well with range() and collections
-syntax : for var in sequence:
            #for loop body
        in is a keyword
2) while
3) nested for
'''

l = [10,20,30,40,50,60,70,80,90,100]

# for i in l:
#     print(i) #accesing list items directly

# for i in range(1,12):
#     print(i)

for i in range(1,10,2):
    print(l[i])