#filter function
# filter(fucntion , iterable)
# function should return either True or False 


#normal user defined func
# def is_even(n):
#     return n%2==0

def transform(fun , col):
    nl = []
    for i in col:
        if fun(i):
            nl.append(i)
    return nl

l = [11,22,33,44,55]

# print(transform(is_even , l))

print("--------------------")
#lambda

print(transform(lambda n:n%2==0 , l))

#filter function - same code above created using filter
print("--------------------")
fo = filter(lambda n:n%2==0 , [11,22,33,44,55])
print(fo) #it will return filter object

print(list(filter(lambda n:n%2==0 , [11,22,33,44,55])))
print(list(filter(lambda n:n%5==0 , [11,22,33,44,55])))
print(list(filter(lambda n:n>30 and n<50 , [11,22,33,44,55])))