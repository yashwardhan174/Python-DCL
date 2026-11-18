#2nd way to iterate is through for loop

t = (11,22,33,44)

#1) creation of iterator object
itr_obj = iter(t)

print(list(itr_obj)) #explicit type casting is 3rd way to iterate

# print(next(itr_obj))
# print(next(itr_obj))
# print(next(itr_obj))
# print(next(itr_obj))

# for i in itr_obj: #now for loop wont run becuase itr_obj is exhausted earlier 
#     print(i)

print("----------------------")

# print(next(itr_obj)) it wont work becuase all the iterables are exhausted and no elem is left so it will throw stopIteration