#__hash__(self)

class Citizen:
    def __init__(self,adharnum,state):
        self.adharnum = adharnum
        self.state = state

    def __hash__(self):
        return self.adharnum


c1 = Citizen(691515699687 , "Madhya Pradesh") #initialization
c2 = Citizen(152133513512 , "Madhya Pradesh") #initialization
print(hash(c1)) #calling hashfunction c1.__hash__() this is internal call
print(hash(c2))