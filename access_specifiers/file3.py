#Private

class Politician:
    def __init__(self,name,party,funds):
        self.name = name #public IV
        self.party = party #public IV
        self.__funds = funds #private IV

    def __multiply_money(self): #private IM
        print("Politician enter into real estate and Dumping yards")

    def file_ITR(self): #public IM
        print(self.__funds) #accesing private IV inside public IM
        self.__multiply_money() #access priavte IM inside public IM

p = Politician("Nagraj","BJP",1235655)
# print(p.__funds) #cant access Private IV outside the class Directly
# p.__multiply_money() #cant access Private IM outside the class Directly

p.file_ITR() #accessing the Public IM