class Patient:
    def __init__(self,name,age):
        self.name = name #public IV
        self._age = age #protected IV
        self.__bp = None #privateIV

    def check_up(self): #public getter method
        return self.__bp

    def restore_bp(self,newbp): #public setter method
        if newbp <155 and newbp >77: #validation logic
            self.__bp = newbp #updation
        else:
            print("Sorry We cant restore bp")

p1 = Patient("Yash",22)

p1.restore_bp(87)
print(p1.check_up())