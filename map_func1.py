#map func
#syntax : map(func , iterable)
#it will return a map object which is a iterator
#It is used for transforming logic



#this is similar code as of last code of lambda_func1.py file

ref = map(lambda num:num**2 , [10,20,30,40])
print(list(ref))

#OR

print(list(map(lambda num:num**2 , [10,20,30,40])))
print(list(map(lambda num:num//5 , [10,20,30,40])))