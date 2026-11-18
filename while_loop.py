'''
-While is a keyword in python
-it is used when we dont know how many times to loop(unknown iterations)
-it will run/execute until the condition becomes False
-syntax: 
#initialization
while conditon:
    while loop body
    #updation
'''

a = 1 #initializartion
while a<=5:
    # print("Hello")
    a = a+1 #updation

i = 13
while i >= 1:
    # print(i)
    i=i-3

l = [10,20,30,40,50,60,70,80,90,100]

i = 1
while i<=10:
    # print(l[i])
    i = i+2

for i in range(1,11,1):
    if i%4==0:
        break
    # print(i)

l = [23,42,11,56,32,-4,6,-6,7]

for i in l:
    if i<0:
        continue
    print(i)

for i in l:
    if i<0:
        break
    print(i)

d ={1:10 ,2:20,3:30,4:40}
for i in d.values():
    print(i)
    print("-----------------------------")

for i in range(1,11,1):
    if i==7:
        continue
    print(i)

print("-----------------")

for i in range(1,11,1):
    if i%4==0:
        continue
    print(i)