#reduce function 
#we use it when we need to have one value after performing some operations
#reduce(fucntion , iterator)
#function must have 2 arguments

#normal user defined func
# def add(n1,n2): #helper func
#     return n1+n2

def transform(fun , col):
    result = 0
    for i in col:
        result = fun(result,i)
    return result

l=[11,22,33,44,55]
print(transform(lambda n1,n2:n1+n2 , l))


#using Reduce Function
from functools import reduce
fo = reduce(lambda n1,n2:n1+n2 , [11,22,33,44,55])
print(fo)

#or
print(reduce(lambda n1,n2:n1+n2 , [11,22,33,44,55])) #165
print(reduce(lambda n1,n2:n1*n2 , [2,3,4,5,1]))


print("-----------------------")
#task

def square(n):
    return n**2

def trans(fun , col):
    nl = []
    for i in col:
        if i%2==0:
            result = fun(i)
            nl.append(result)
    return nl


l = [10,12,13,14,16,17,18]
print(trans(square , l))


flt_obj = filter(lambda n:n%2==0 , [10,12,13,14,16,17,18])
map_obj = map(lambda n:n**2 , flt_obj)
print(list(map_obj))

print("-------------------")
#one line approach

print(list(map(lambda a:a**2 , filter(lambda n:n%2==0 , l))))