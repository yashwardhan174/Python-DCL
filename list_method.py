l1 = []

#1) ref.append(object)

l1.append(10)
print(l1)
l1.append(20)
l1.append(30)

print(l1)

#2) ref.insert(index,object)

l1.insert(1,40)
print(l1)

#3) ref.extend(collection)

l2=[11,22,33]
l3=[44,55,66]

l2.extend(l3)
print(l2)

#4) ref.pop()

l4 = [100,200,600,300,400,500,600]
rem_elem  = l4.pop(3)
print(rem_elem)
print(l4)

#5) ref.remove(object)
#it removes the 1st occuring objext from the list
l4.remove(600)
print(l4)

#6) ref.clear()
l4.clear()
print(l4)

#7) ref.reverse()
l5 = [10,13,65,54,14,87,54 , 13,54,34]
l5.reverse()
print(l5)

#8) ref.sort()
l5.sort()
print(l5)

#9) ref.index(obj)

ind = l5.index(13)
print(ind)

#10) ref.count(object)

cnt = l5.count(54)
print(cnt)

