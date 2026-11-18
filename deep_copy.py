#Deep Copy


import copy #step 1 
l1 = [10,20,30,[40,50]]
l2 = copy.deepcopy(l1) #deep Copy

l1[2] = 11
print("l1 will be affected",l1)
print("l2 will not be affected",l2) 

l2[3][0] = 41
print("l2 will be affected",l2)
print("l1 will not be affected",l1) 