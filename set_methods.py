s1 = set()

#1) ref.add(object)

s1.add(10)
print(s1)
s1.add(20)
print(s1)

#2) ref.update(collection) : It copies and adds the element of collection into the set

s2 = {11,12,13}
s3 = {21,22,23}
s2.update(s3)
print(s2)

#3) ref.pop() : It removes and returns  a random element from a set
rem = s2.pop()
print(rem)
print(s2)

#4) ref.remove(object) : It removes the specified Object from that set
#s2.remove(111) : if elelment is not present(111) then a key error is shown
s2.remove(11)
print(s2)

#5) ref.discard(object) : It removes the specified object from the set
#if object is not present then no error is thrown

s2.discard(130)
print(s2)

#6)ref.clear() : It clears all the set elements at once

s2.clear()
print(s2)

#7) ref.issubset(set) : It checks if one set element are present in another set

s4 = {10,20,30}
s5 = {20,30,10,40}

print(s4.issubset(s5))

#8) ref.issuperset(set) : It checks if one set contains all elem of another set & returns a Boolean 

print(s5.issuperset(s4))


#9) ref.isdisjoint(set) : It returns False , if there is any common any elemnt btw sets

print(s4.isdisjoint(s5))

#10) set1.union(set2) : It returns a new set which contain the unique elements of both sets in random order

s6 = {11,22,33}
s7 = {33,44,55}

print(s6.union(s7))

#11) set1.intersection(set2) : It will return new set with only common elem of both sets

print(s6.intersection(s7))

#12) set1.difference(set2) : It returns a new set that contains elements present in the first set but not present in second set

print(s6.difference(s7))

#13) set1.symmetric_difference(set2) : It returns the new set that contains Uncommon elements of both the sets

unc = s6.symmetric_difference(s7)
print(unc)