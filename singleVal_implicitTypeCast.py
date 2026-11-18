#Implicit Type Casting 

b=False
i=49
f=3.1
c=5+1j

#1) bool -> int

b_i = b+i
print(b_i)
print(type(b_i))
print("-----------------")

#2) bool -> float
b_f = b+f
print(b_f)
print(type(b_f))
print("---------------")

#3) bool -> complex
b_c  = b+c
print(b_c)
print(type(b_c))
print("------------_------")

#4) int -> float
i_f = i+f
print(i_f)
print(type(i_f))
print("----------------")

#5) int -> complex
i_c = i+c
print(i_c)
print(type(i_c))
print("-----------")

#6) float -> complex
f_c = f+c
print(f_c)
print(type(f_c))