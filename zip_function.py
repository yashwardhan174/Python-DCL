l1 = [2,4,6,8]
l2 = [20,40,60,80]

zip_obj = (zip(l1,l2))
# print(next(zip_obj))
# print(next(zip_obj))
# print(next(zip_obj))
# print(next(zip_obj))

print(list(zip_obj))

#if l1= [1,2,3,4,5,6,7,7,8] and l2=[2,3,4,5] it will pair based on smaller iterable here it is l2 with 4 elem

l1 = ["Yash" , "Akshat"  , "Barik" , "Sarthak"]
l2 = [88,78,56 , 8]

zip_obj = zip(l1,l2)
# print(list(zip_obj))

#using zip in dict comprehensio
 

# d1 = {k:v for k,v in zip_obj}
# print(d1)

d1 = {k : ("Pass" if v >35 else "FAIL") for k,v in zip_obj}
print(d1)
