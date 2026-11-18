l = [10,20,30,40,50] #iterable

#creation of iterator Object
itr_obj = iter(l)
print(itr_obj) #this gives address of iterator object
#next(iterator_Obj)

ele1 = next(itr_obj)
print(ele1) #10
ele2 = next(itr_obj)
print(ele2)#20
print(next(itr_obj))#30
print(next(itr_obj))#40
print(next(itr_obj))#50
# print(next(itr_obj)) #Since no element is left in iterable it will thorw an stop iteration error
