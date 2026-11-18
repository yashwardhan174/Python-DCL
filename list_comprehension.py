
#syntax 1
l = [13,23,33,43]
nl = [i+5 for i in l]
print(nl)

nl = [i**2 for i in l]
print(nl)

l = ['Tarun' , 'Parth' ,'Zen','Yash']

nl = [i.upper() for i in l]
print(nl)


#syntax 2

l2 = [11,21,24,34,39]

# nl = [i for i in l2 if i%2==0]
nl = [i**2 for i in l2 if i%2==0]
print(nl)

l = ['Tarun' , 'Parth' ,'Zen','Yash']

nl = [i.upper() for i in l if len(i) > 4]
print(nl)

#syntax 3

l3 = [2,3,4,5,6,7]

nl = [i**2 if i%2==0 else i**3 for i in l3]
print(nl)
