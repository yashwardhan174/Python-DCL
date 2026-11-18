#Super() function
from typing_extensions import override

class Athlete:
    def pushups(self):
        print("Warmup Pushups 10")

class Wrestler(Athlete): 
    @override
    def pushups(self):
        super().pushups() 
        print("50 Diamond Pushups") 

w = Wrestler()
w.pushups()