from abc import ABC , abstractmethod

class Payment_API(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod    
    def pay(self,amount):
        pass