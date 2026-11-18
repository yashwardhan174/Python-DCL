#Explicit Type Casting
b = False
i = 49
f = 3.1
c = 5+1j

#1) bool to int 
b_i = int(b)
print(b_i)

#2) int to float
i_f = float(i)
print(i_f)

#3) int to boool
i_b = bool(i)
print(i_b)

#4) float to bool
f_b = bool(f)
print(f_b)

#5) complex to float
c_f = float(c)
print(c_f) #This is not possible

print(bool(c))