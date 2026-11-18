'''
1> General Copy :Assigning one variable to another
- changes made in one var will be reflected in another
2> Shallow Copy
3> Deep Copy
'''
#General COpy

# l1 = [10,20,30,[40,50]]

# l2 = l1 #this is a general copy

# l1[2] = 41 #modifieng outer list
# print("l1",l1)
# print("l2",l2)

# l2[3][0] = 11 #modifing inner list
# print("l2",l2)
# print("l1",l1)

#Shallow Copy

import copy #step 1 
l1 = [10,20,30,[40,50]]
l2 = copy.copy(l1) #shallow Copy

l1[2] = 11
print(l1)
print(l2) #30 wont be changed to 11 because of shallow copy

l2[3][0] = 41
print("l2",l2)
print("l1",l1) #inner list change will be reflected in l1 also 