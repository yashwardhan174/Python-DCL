class Money:
    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return Money(self.value + other.value)

    def __str__(self):
        return f"{self.value}"

    def __sub__(self,other):
        return Money(self.value - other.value)

    def __mul__(self,other):
        return Money(self.value * other.value)

m1 = Money(100)
m2 = Money(500)
m3 = Money(200)

print(m1+m2+m3)
print(m1-m2-m3)
print(m1*m2*m3)
