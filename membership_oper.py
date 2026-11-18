#It is used to check if an element is prewsent in a sequence / collection
# in , not in

l = [11,22,33,44]
print(11 in l) #True
print(11 not in l) # false
print(10 not in l) #True

l1 = (11,22,33,44)
print(11 not in l1)

l1 = {1:11,2:22,3:33,4:44}
print(11 not in l1) #true because 11 in not a key , it is a value
print(11 in l1.values())

l2 = "Brian Lara"
print("e" in l2) #false
print("rai" in l2) #false
print("ri" in l2) #true
