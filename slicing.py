#extracting a part/portion of a sequence datatype

#syntax sequence[startindex : stopindex : step]

l = [10,20,30,40,50,60,70]
print(l[0:3:1]) #[10,20,30]
print(l[2:5:1]) #[30,40,50]
print(l[1:6:2]) #[20,40,60]
print(l[5:0:-2]) #[60,40,20]
print(l[::-1])

cid = "22100BTCSFBI11330"
print(cid[9:12:1])