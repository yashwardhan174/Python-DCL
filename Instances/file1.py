class MarkerPen : #this is the user defined class
    'This class is for Pen Object'
    pass

class Mobile: #user defined class
    pass

pen1 = MarkerPen() #MarkerPen() is a instance and pen1 is instance reference
mob1 = Mobile()

print(MarkerPen.__dict__) #class dictionary with metadata
print(pen1.__dict__) #empty instance dictionary

print(Mobile.__dict__)
print(mob1.__dict__)