#syntax 1

l = [2,3,4,5]

new_dict = {i : i**2 for i in l}
print(new_dict)

l2 = ["tom" , "Jerry" , "kid" , "cat"]

nd = {i : len(i) for i in l2}
print(nd)

#syntax 2

nd = {i:i**2 for i in l if i%2==0}
print(nd)

nd = {i:i.upper() for i in l2 if len(i)>4}
print(nd)

#syntax 3

nd = {i: (i**2 if i%2==0 else i**3) for i in l}
print(nd)

d = {54:45 , 20:80 , 50:5 , 9:99}

nd = {k:("Pass" if v > 33 else "False") for k,v in d.items()}
print(nd)