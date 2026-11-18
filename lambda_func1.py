#Lambda func is a small ,anonymous func 
#- No func name , it uses lambda keyword
#- No return keyword is used 
#-Only one expression can be given

# def add(a,b): This is a normal user defined function 
#     return a+b

# sum = add(5,4)
# print(sum)

#instead of using normal user defined function we will perform same operations using lambda function

#1st Approach - Assign it to a var then call it 
var = lambda a,b : a+b #assigning it to a variable
print(var(11,22)) #after assigning call that variable

var1 = lambda a,b,c : a*b*c
print(var1(3,4,2))

print("--------------")
#2nd Approach - Directly Call without assigning it to a var

print((lambda a,b : a+b) (11,22)) #lambda directly calling

print((lambda a,b,c : a*b*c)(2,3,4))

print("------------------------")


def square(num):  #callback / helper func
    return num**2

def transform(fun , coln): #higher order func
    new_l = []
    for ele in coln:
        # result = ele**2
        result = fun(ele) #using fun will call the square func and use it for sqauring
        new_l.append(result)
    return new_l
l = [10,20,30,40]

print(transform(square , l))  #[100,400,900,1600]

#Now doing this same thing with lambda function

def transform(fun ,col):
    new_l = []
    for i in col:
        result = fun(i)
        new_l.append(result)
    return new_l

l = [10,20,30,40]

print(transform(lambda num : num**2 , l )) #square
print(transform(lambda num : num**3 , l )) #cube
print(transform(lambda num : num+50 , l )) #increase elem by 50