from abc import ABC , abstractmethod

#the below class as a whole till pass is an contract
class Shape(ABC): #it is an abstarct class
    @abstractmethod
    def calc_area(self):
        pass

class Rectangle(Shape):
    def calc_area(self):
        print("length * breadth")


class Square(Shape):
    def calc_area(self):
        print("Side * Side")

s = Square()
s.calc_area()

r = Rectangle()
r.calc_area()