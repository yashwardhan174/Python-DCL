# import keyword as k, math as m, random as r #in this everytime we need to use alias to call

# print(k.kwlist)
# print(m.sqrt(100))
# print(m.pow(2,5))
# print(r.randint(1,100)) #always returns a random int no. between given 2 numbers

#now we will access specific members from module

# from math import sqrt as s, pow as p, cbrt , factorial
# print(s(100))
# print(p(2,3))
# print(cbrt(1000))
# print(factorial(5))

#Impoprting Members from File2 in File1
from package2.file2 import rapper , birthday ,display as d,showcase as s

print(rapper)
print(birthday)
d()
s()