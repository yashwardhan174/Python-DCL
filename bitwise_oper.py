#It is used to perform opewrations on the binary digits(bits) of number
a = 12
#1) bitwise AND op(&) :It compares two bits and returns 1 when both bits are 1
print(12 & 5)
#2) bitwise OR op(|) : It compares 2 bits and returns 1 if atleast 1 bit is 1
print(12 | 5)
#3) bitwise XOR op(^) : It comapres 2 bits and returns 1 if both bits are opposite
print(12^5)
#4) bitwise NOT op(~) : It inverts the bits ~intvalue
print(~a)
#5) bitwise leftshift op(<<) : It shifts the bits to the left side by the no of positions given
#6) bitwise rightshift op(>>) : Shifts the bits to the right side by the no of positions given 
print(a<<2)