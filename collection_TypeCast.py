#List to Others
l = [10,20,30]

print(tuple(l))
print(set(l))
print(str(l))
# print(dict(l)) it is not possible
print("-----------------")
#Tuple to Others
t = (3,4,5)
print(list(t))
print(set(t))
print(str(t))
# print(dict(t)) Not Possible
print("-----------------")

#Set to others

s = {11,22,33,44}
print(list(s))
print(tuple(s))
print(str(s))
# print(dict(s))Not possible
print("-----------------")

st = "python"
print(list(st))
print(tuple(st))
print(set(st))
# print(dict(st))
print("-----------------")


d = {1:10 , 2:20 , 3:30}
print(list(d))
print(tuple(d))
print(set(d))
print(str(d))

#if you convert dict to other collections only keys will be taken into consideration Only String is Exception it can convert dict to str with keys and values

print("-----------------")

print(str(10))
print(str(10.1))
print(str(True))
print(str(5+1j))

print("----------------")

s = "1"
i = int(s)
print(i)