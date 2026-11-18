#Method Overriding
from typing_extensions import override

class Athlete:
    def pushups(self):
        print("Warmup Pushups 10")

class Wrestler(Athlete): #1.inheritance
    @override
    def pushups(self): #2.methodname and param same
        print("50 Diamond Pushups") #3.Method Implementation
        #Parent Method is Overriden by Child

w = Wrestler()
w.pushups()