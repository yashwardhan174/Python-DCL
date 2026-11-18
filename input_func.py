#it is a pre defined function in  python which is used to take input from user (via keyboard)
#-> whatever a user enters is always accepted/received in the foprm of string

# number  =int(input("Enter any integer"))
# #without int input will be considered as string , so using int we will be able to perform oprations.
# print(number+10)

# height = float(input("Enter Your Height"))

# print(height+3)

# ques = bool(input("Are you Indian?"))
# print(ques)

# eval("string Expression ")
# NOTE : It can automatically decide the datatype and perform typecasting
a = 10
b = 20
l = [30,40,50]
t = ()
d = {}
# result = eval("a+b+len(l)")
# result = eval("t")
# result = eval("d")
result = eval(input("Are you Indian"))
print(result)
print(type(result))



 