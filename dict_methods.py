d1 = {1:10 , 2:20 , 3:30}

#1) ref.get(key) : It returns the key value pair if present , else None
print(d1.get(2))

#2) ref.setdefault(key,value) : If the key is not present , it adds the key with the given value

v = d1.setdefault(4 , 400)
print(v)

g=  d1.setdefault(2) #if key is already present then value is returned
print(g)

#3) ref.update(dict) : It copies and adds the items of 1 dict into another dict
d2 = {7:70 , 8:80 , 9:90}
d1.update(d2)
print(d1)

#4) ref.pop(key) : It returns the value and remove that specified item
ret_val = d1.pop(1)
print(ret_val)
print(d1)
print("------------------")

#5) ref.popitem() : It will remove the last item from the dictionary

item = d1.popitem()
print(item)
print(d1)

#6) ref.clear()
d1.clear()
print(d1)

#7) ref.keys() : It displays / returns all the keys of dictionary
print(d2.keys())

#8) ref.values() : It displays/returns all the values of dictionary
print(d2.values())

#9) ref.items() : It displays/returns the items in tuple form (key,value)
print("--------------------")
print(d2.items())

#10) ref.fromkeys(collection of keys, optionalValue) : It creates a dictionary with each key having that optional value 

print("-------------d3-------------")

d3 = {}
newDict = d3.fromkeys( [1,2,3])
print(newDict)  #if optional value is not given then value will be none



