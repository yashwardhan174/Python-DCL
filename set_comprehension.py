#syntax 1

s = {13,23,33,43}
ns = {i+5 for i in s}
print(ns)

#syntax 2

s = {11,21,24,27,34,39}

ns = {i for i in s if i%2==0}
print(ns)

#syntax 3

s = {2,3,4,5,6,7}

ns = {i**2 if i%2==0 else i**3 for i in s}
print(ns)