from abc import ABC , abstractmethod

class SuccessfulPerson(ABC):
    @abstractmethod
    def earn_money(self):
        pass

class Field(SuccessfulPerson):
    def earn_money(self):
        print("BusineesMan are Successfull Person")

s = Field()
s.earn_money()
